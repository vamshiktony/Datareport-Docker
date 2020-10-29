'''
all report api functions
'''
import os
import gc
import datetime
import time
import timeit
import json
import boto3
from importlib import import_module
import asyncio
from db_config import read_data_in_pandas
from key_validation import response_dict
from mis_function import date_format
from report_fields import IRN_DOC_REPORT_FIELDS,IRN_DOC_REPORT_HEADERS
import logging
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from zipfile import ZipFile, ZIP_DEFLATED
from memory_profiler import profile
LOGGER = logging.getLogger('report_api')
LOGGER.setLevel(logging.INFO)
app_settings = import_module(f"{os.environ.get('app_settings', 'settings.aws_settings')}")

# def create_zip(data, index, zipfilename):
def create_zip(df, start_date, index, zipfilename):
    """ Writing data to csv """    
    try:    
        path = get_path()
        #timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        filename =  f"{path}_IRN_Doc_Detail_{start_date}_{index + 1}.csv"
        # df = pd.DataFrame(data) if df == None else df
        with open(filename, 'w', encoding='utf8', newline='') as output_file:
            output_file.write(",".join(IRN_DOC_REPORT_HEADERS))
            output_file.write("\n")
            df.to_csv(output_file, header=False, index=False)
            
        LOGGER.info(f"...CSV Written {filename}...")
        zip_file_name = f"{path}{zipfilename}"
        with ZipFile(zip_file_name, 'a', ZIP_DEFLATED) as zipObj2:
            zipObj2.write(filename)
        LOGGER.info(f"...{filename} added to zip....")
        os.remove(filename)
        count = len(df)
        del df
        gc.collect()
        return count
    except Exception as ex:
        LOGGER.error(f"Exception in creating zip and exception is {ex}", exc_info=True)
        return -1

def get_path():
    path = os.environ.get('src_folder_path', "")
    APP_SET = os.environ.get("app_settings", "aws_settings")
    if APP_SET == "settings.azure_settings":
        path = os.environ.get("HOME","/home")
        path = path + "/"
    # return "/mnt/reports/"
    return path

def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3', 'ap-south-1')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration,
                                                    HttpMethod="GET")
    except Exception as e:
        logging.error(e)
        return None
    # The response contains the presigned URL
    return response

def send_report_to_sqs(email_sqs, bucket_name, key, email, 
                       report_name, from_date, to_date, user_login_id, 
                       message=None):
    """send report in sqs for email

    :param eamil_sqs: email sqs url
    :param bucket_name: bucket name where report store
    :param key: name of zip file
    :param key: email id fo user
    :return: Presigned URL as string. If error, returns None.
    """
    report_url, error = "", ""
    if message == None:
        report_url = create_presigned_url(bucket_name, key, expiration=86400)
    else:
        error = message
    
    message = {
        "ReportLink": report_url,
        "Error": error
    }
    data = {
        "ReportName": report_name,
        "FromDate": from_date,
        "ToDate": to_date,
        "UserLoginId": user_login_id,
        "message": message
    }
    email_template = {
        "template": "Download Data",
        #"template": "Testing",
        "message": "",
        "to": email,
        "irn_email_struct" : json.dumps(data)
    }
    app_settings.SQSConfig.send_sqs(email_template, email_sqs)

LastUDID = ""

def process_report_dataframe(item):
    UniqueId = f"{item.udid}:{item.load_id}"
    global LastUDID 
    if LastUDID != UniqueId:
        item.unique_document = "Y"
        LastUDID = UniqueId
    if item.nic_error_details:
        try:
            error_codes = [str(x["ErrorCode"]) for x in item.nic_error_details]
            error_codes = list(set(error_codes))
            nic_code = "-".join(error_codes)
            item.nic_code = nic_code
        except Exception as ex:
            LOGGER.error(item["nic_error_details"])
            LOGGER.error(f"Eroor in parseing nic error detail -> {ex}")
            item.nic_code = ""
    if item["itemcnt_mainhsn"]:
        Obj = json.loads(item.itemcnt_mainhsn)
        item.itemcnt = Obj.get("ItemCnt", "")
        item.mainhsncode = Obj.get("MainHsnCode", "")
    else:
        item.itemcnt = ""
        item.mainhsncode = ""
    return item

def process_report_data(data):
    LastUDID = ""
    for item in data:
        UniqueId = f"{item['udid']}:{item['load_id']}"
        if LastUDID != UniqueId:
            item["unique_document"] = "Y"
            LastUDID = UniqueId
        if item["nic_error_details"]:
            try:
                error_codes = [str(x["ErrorCode"]) for x in json.loads(item["nic_error_details"])]
                error_codes = list(set(error_codes))
                nic_code = "-".join(error_codes)
                item["nic_code"] = nic_code
            except Exception as ex:
                LOGGER.error(item["nic_error_details"])
                LOGGER.error(f"Eroor in parseing nic error detail -> {ex}")
                item["nic_code"] = ""
        if item["itemcnt_mainhsn"]:
            Obj = json.loads(json.loads(item["itemcnt_mainhsn"]))
            item["itemcnt"] = Obj.get("ItemCnt", "")
            item["mainhsncode"] = Obj.get("MainHsnCode", "")
        else:
            item["itemcnt"] = ""
            item["mainhsncode"] = ""
        del item["itemcnt_mainhsn"]
        del item["nic_error_details"]
    return data

def get_data(query, database):
    asyncio.set_event_loop(asyncio.new_event_loop())
    return asyncio.get_event_loop().run_until_complete(read_data_in_pandas(database, query))
    # return asyncio.get_event_loop().run_until_complete(async_execute_select(database, query))

def case_IrnDocDetails():
    UserLoginId = os.environ.get("UserLoginId")
    ReportName = os.environ.get("ReportName","") #"IRN Doc Details"
    UserGstin  = os.environ.get("UserGstin", "")
    Location = os.environ.get("Location", "")
    Bu = os.environ.get("Bu", "")
    Sbu = os.environ.get("Sbu", "")
    fromDate = os.environ.get("fromDate", "")
    toDate = os.environ.get("toDate", "")
    UserLoginEmail = os.environ.get("UserLoginEmail", "")
    database = json.loads(os.environ.get("database", "{}"))
    commonConditions = f"is_active = 'Y'"
    commonConditions += f"AND location_id IN ({Location}) " if Location else "location_id = 0 "    
    commonConditions += f"AND bu_id IN ({Bu}) " if Bu else "bu_id = 0 "
    commonConditions += f"AND sbu_id IN ({Sbu}) " if Sbu else "sbu_id = 0 "
    commonConditions += f"AND gstin_id IN ({UserGstin})"
    
    finalfromdate = date_format(fromDate, "%d/%m/%Y", "%Y-%m-%d %H:%M:%S")
    finaltodate = date_format(toDate, "%d/%m/%Y", "%Y-%m-%d %H:%M:%S")
    # fields = ",".join()
    response_code = 200
    msg = "Zip file created and Stored in S3"
    TOTAL_RECORDS_FOUND = 0
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    zipfilename = f"IRN_Doc_Detail_{now}.zip"
    file_counter = 0
    all_processed = True
    customer_id=os.environ.get("customer_id", "")   
    key = f"{customer_id}_etl_irn_config"
    # bucket_name = client_configuration[key]["bucket_name"] if key in client_configuration else client_configuration["bucket_name"]
    bucket_name = os.environ.get("bucket_name", "")
    # email_sqs_url = client_configuration[key]["email_sqs_url"] if key in client_configuration else client_configuration["email_sqs_url"]
    email_sqs_url = os.environ.get("email_sqs_url", "")

    try:
        start_date = datetime.datetime.strptime(fromDate,"%d/%m/%Y").date()
        to_date = datetime.datetime.strptime(toDate,"%d/%m/%Y").date()
        day_incr = datetime.timedelta(days=1)
        while start_date <= to_date:
            query = f"SELECT {IRN_DOC_REPORT_FIELDS} FROM demo.irn_master_details_cold where docdtls_dt::date = '{start_date}'"\
                    f" and {commonConditions}  ORDER BY load_id DESC, udid DESC "
            file_counter = 0
            OFFSET = 1
            LIMIT = 50000
            while True:
                main_query = f"{query} OFFSET {OFFSET} LIMIT {LIMIT}"
                start = timeit.default_timer()
                data = get_data(main_query, database)
                LOGGER.info(f"Time Taken for Query Execution -> {timeit.default_timer() - start}")
                TOTAL_RECORDS_FOUND += len(data)
                if len(data) == 0:
                    break
                else:
                    # data = process_report_dataframe(data)
                    global LastUDID
                    LastUDID = "" 
                    data = data.apply(process_report_dataframe, axis=1)
                    RECORD_FETCHED = len(data)
                    del data["itemcnt_mainhsn"]
                    del data["nic_error_details"]
                    start = timeit.default_timer()
                    temp = create_zip(data, start_date, file_counter, zipfilename)
                    del data
                    gc.collect()
                    LOGGER.info(f"Time Taken for Creating Csv and adding into zip -> {timeit.default_timer() - start}")
                    file_counter += 1
                    if temp == -1:
                        all_processed = False
                        break
                    elif RECORD_FETCHED < LIMIT:
                        break
                    else:
                        OFFSET = TOTAL_RECORDS_FOUND + 1
            if all_processed == False:
                break                
            start_date = start_date + day_incr
            
        if all_processed == False:
            response_code = 500
            msg = "Exception occured while creating zip file"
            send_report_to_sqs(email_sqs_url, bucket_name, key, UserLoginEmail, \
                ReportName, fromDate, toDate, UserLoginId, message=msg)
        elif TOTAL_RECORDS_FOUND == 0:
            response_code = 404
            msg = "No Records Found"
            send_report_to_sqs(email_sqs_url, bucket_name, key, UserLoginEmail, \
                ReportName, fromDate, toDate, UserLoginId, message=msg)
        else:
            LOGGER.info(f"Total Records processed {TOTAL_RECORDS_FOUND}")
            # Uploading file on s3 bucket
            zfname = zipfilename.split("/")[-1]
            key = f"reports/{zfname}"
            start = timeit.default_timer()
            app_settings.BucketConfig.upload_file(bucket_name, key, f"{get_path()}{zipfilename}")
            LOGGER.info(f"Time Taken for Uploading zip on s3 -> {timeit.default_timer() - start}")
            LOGGER.info("...ZIP uploaded to s3....")
            # Sending email for report
            start = timeit.default_timer()
            send_report_to_sqs(email_sqs_url, bucket_name, key, UserLoginEmail, \
                ReportName, fromDate, toDate, UserLoginId)
            LOGGER.info(f"Time Taken for Sending message in que -> {timeit.default_timer() - start}")
            LOGGER.info("...Send Zip pre signed link to email queue....")
            os.remove(f"{get_path()}{zipfilename}")
    except Exception as ex:
        response_code = 500
        msg = "Exception in generating IRN Doc Report"
        LOGGER.error(f"Exception in generating IRN Doc Report and error is {ex}", exc_info=True)
        send_report_to_sqs(email_sqs_url, bucket_name, key, UserLoginEmail, \
                ReportName, fromDate, toDate, UserLoginId, message="Exception in generating IRN Doc Report")
    return response_code, response_dict(msg, response_code, [])

# database = {"readonly_host": "irn-stg-db-cluster.cluster-chsjqt1rncee.ap-south-1.rds.amazonaws.com", \
#             "user": "pocmaster",
#             "port": "5432" ,
#             "password": "consider123", 
#             "database": "demo1_customer_QA"}
# os.environ["database"] = json.dumps(database)
# os.environ["UserLoginId"] = "ankit1"
# os.environ["UserGstin"] = "17,23,117,27,26,28,72,31,32,25,1,6,7,8,9,10,12,18,15,4,16,20,21,22,24,2,11,35,37,40,42,43,44,46,50,51,57,58,60,48,64,67,109,118,114,88,62,29,89,39,75,38,78,70,66,95,55,103,19,56,71,86,116,115,91,106,41,100,105,87,119,108,92,99,14,63,74,90,53,101,65,97,94,79,81,77,54,113,34,47,112,102,80,93,96,33,98,36,5,110,120,76,3,83,84,85,104,52,73,107,82"
# os.environ["Location"] = "38,45,85,48,49,55,8,11,12,13,14,19,22,26,27,28,29,30,31,33,39,35,25,37,1,40,43,44,46,47,2,32,56,57,59,61,62,63,64,65,69,70,71,72,73,74,66,76,5,67,78,81,82,86,0"
# os.environ["Bu"] = "48,53,96,58,56,55,0,65,64,83,9,92,72,13,29,26,25,24,23,22,21,16,15,14,12,1,61,36,35,37,27,38,39,40,42,49,46,33,47,50,52,51,54,5,2,44,67,66,69,71,74,79,78,81,82,84,76,86,89,91,90,97,70,75,59,95"
# os.environ["Sbu"] = "47,52,91,58,59,57,56,55,0,64,65,63,79,8,71,62,11,30,27,26,25,24,23,22,21,20,34,19,10,18,14,13,12,54,1,36,35,42,37,28,38,60,39,40,43,48,45,33,46,49,51,50,53,5,2,44,67,66,69,70,76,77,78,80,74,82,84,86,85,92,73,89"
# os.environ["fromDate"] = "08/10/2020"
# os.environ["toDate"] = "12/10/2020"
# os.environ["UserLoginEmail"] = "rakesh.com007@gmail.com,ashish@mobifly.in"
# os.environ["bucket_name"] = "qa-irn-stg-demo1-raw"
# os.environ["email_sqs_url"] = "https://sqs.ap-south-1.amazonaws.com/966297163257/qa-irn-email-demo1"