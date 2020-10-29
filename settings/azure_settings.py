import os
import logging
import json
import redis
import yaml
import simplejson
from configuration import BUCKET_NAME, FLAG
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.servicebus import Message, QueueClient
import datetime

LOGGER = logging.getLogger("einvoice_app_pull")

class RedisConfig:

    @staticmethod
    def get_cache_dump(key):
        # pylint: disable-msg=W0703
        # pylint: disable-msg=W0613
        '''
        Summery Line.
            Here we are read client configuration from s3 bucket
        Parameters:
            key(str) : redis key
        Return:
            cache(dict): returning cache 
        '''
        cache = {}
        try:
            client = redis.Redis(host=os.environ['redis_url'],\
                port=int(os.environ['redis_port']), db=0,\
                ssl=True,
                password=os.environ['redis_password'])            
            return  client.get(key)            
        except Exception as error:
            LOGGER.error(str(error), exc_info=True)
        return cache
    
    @staticmethod
    def get_cache(key):
        # pylint: disable-msg=W0703
        # pylint: disable-msg=W0613
        '''
        Summery Line.
            Here we are read client configuration from s3 bucket
        Parameters:
            key(str) : redis key
        Return:
            cache(dict): returning cache 
        '''
        # cache = {}
        try:
            client = redis.Redis(host=os.environ['redis_url'],\
                port=int(os.environ['redis_port']), db=0,\
                ssl=True,
                password=os.environ['redis_password'])
            get_key_value = json.loads(client.get(key)) if client.get(key) else client.get(key)
            print(get_key_value)
            logging.info(get_key_value)
            if get_key_value==None:
                return {}
            else:   
                return {key:get_key_value}
        except Exception as error:
            LOGGER.error(str(error), exc_info=True)
        return {}

    @staticmethod
    def set_cache(key,value):
        # pylint: disable-msg=W0703
        # pylint: disable-msg=W0613
        '''
        Summery Line.
            Here we are set value into redis cache
        Parameters:
            key(str) : redis key        
        '''        
        try:
            client = redis.Redis(host=os.environ['redis_url'],\
                port=int(os.environ['redis_port']), db=0,\
                ssl=True,
                password=os.environ['redis_password'])
            client.set(key, value)
            logging.info(f"Setting Redis Case for Key -> {key} to Value -> {value}")
        except Exception as error:
            LOGGER.error(str(error), exc_info=True)

    @staticmethod
    def get_all_cache(customer_id):
        # pylint: disable-msg=W0703
        # pylint: disable-msg=W0613
        '''
        Summery Line.
            Here we are set value into redis cache
        Parameters:
            key(str) : redis key        
        '''        
        try:
            client = redis.Redis(host=os.environ['redis_url'],\
                port=int(os.environ['redis_port']), db=0,\
                ssl=True,
                password=os.environ['redis_password'])
            key_values={}
            all_keys = client.keys('*')
            #List of keys to fetch
            all_keys = [customer_id+"_etl_ewb_config",\
            customer_id+"_etl_gstin_config",\
            customer_id+"_etl_gstin_status",\
            customer_id+"_etl_master_config",\
            customer_id+"_gstin_credentials",\
            customer_id+"_validation_rules",\
            customer_id+"_etl_irn_config"]
            # values = client.mget(all_keys)
            for key in all_keys:
                key_values[key]=json.loads(client.get(key)) if client.get(key) else client.get(key)
        except Exception as error:
            LOGGER.error(str(error), exc_info=True)
        return key_values

    @staticmethod
    def delete_all_cache():
        # pylint: disable-msg=W0703
        # pylint: disable-msg=W0613
        '''
        Summery Line.
            Here we are delete all data from redis
        Parameters:
            key(str) : redis key        
        '''        
        try:
            client = redis.Redis(host=os.environ['redis_url'],\
                port=int(os.environ['redis_port']), db=0,\
                ssl=True,
                password=os.environ['redis_password'])
            client.flushall()
        except Exception as error:
            LOGGER.error(str(error), exc_info=True)

    @staticmethod
    def delete_cache(key):
        # pylint: disable-msg=W0703
        # pylint: disable-msg=W0613
        '''
        Summery Line.
            Here we are delete all data from redis
        Parameters:
            key(str) : redis key        
        '''        
        try:
            client = redis.Redis(host=os.environ['redis_url'],\
                port=int(os.environ['redis_port']), db=0,\
                ssl=True,
                password=os.environ['redis_password'])
            client.delete(key)
        except Exception as error:
            LOGGER.error(str(error), exc_info=True)

    @staticmethod
    def get_host_port():
        HOST = os.environ['redis_url']
        PORT = os.environ['redis_port']
        return HOST, PORT
   
class BucketConfig:
    '''
    Summery Line.
        All s3 related work are here
    '''
    def __str__(self):
        '''
        Summery Line.
            S3Read object Representation
        '''
        return "S3Read object"

    #Reading the config file from s3 bucket
    @staticmethod
    def read_config_file_from_bucket(default_config_path, json_load=True, bucket_name=None):
        # pylint: disable-msg=W0703
        # pylint: disable-msg=W0613
        '''
        Summery Line.
            #Reading the config file from s3 bucket
        Parameters:
            bucket_name: The s3 bucket
            default_config_path: The configuration file path
        Return:
            file_dict(dict): The config file is read from s3 bucket
        '''
        file_dict = {}
        try:
            # Azure blob storage client
            container_client =  BlobServiceClient.from_connection_string(\
                os.environ.get("AzureWebJobsStorage"))            
            bucket = BUCKET_NAME if not bucket_name else bucket_name
            blob_client = container_client.get_blob_client(container=bucket,\
                blob=default_config_path)
            s3_clientdata = blob_client.download_blob().readall()
            file_dict = json.loads(s3_clientdata) if json_load else s3_clientdata

            return 
        except Exception as error:
            LOGGER.error("EXCEPTION OCCURED %s", str(error), exc_info=True)
        return file_dict

    @staticmethod
    def delete_file(bucket_name, key):
        container_client =  BlobServiceClient.from_connection_string(\
            os.environ.get("AzureWebJobsStorage"))

        blob_client = container_client.get_blob_client(container=bucket_name, blob=key)
        # Deleting the json file from s3 bucket
        blob_client.delete_blob()

    @staticmethod
    def upload_file(bucket_name, key, data):
        container_client =  BlobServiceClient.from_connection_string(\
            os.environ.get("AzureWebJobsStorage"))

        blob_client = container_client.get_blob_client(container=bucket_name, blob=key)
        with open(data, "rb") as data:
            blob_client.upload_blob(data,overwrite=True) 
        # container_client.upload_client()

    @staticmethod
    def upload_data(bucket_name, key, data):
        container_client =  BlobServiceClient.from_connection_string(\
            os.environ.get("AzureWebJobsStorage"))

        blob_client = container_client.get_blob_client(container=bucket_name, blob=key)
        blob_client.upload_blob(data,overwrite=True) 
        container_client.upload_client()

class ReadYmlConfig:

    def read_yml_s3(f_path):
        '''
        Summery Line.
            reading properties file from s3 bucket
        Parameters:
            f_path: file path
        Return:
            properties(dict): Properties configuration 
        '''
        container_client =  BlobServiceClient.from_connection_string(\
            os.environ.get("AzureWebJobsStorage"))

        blob_client = container_client.get_blob_client(container=BUCKET_NAME, blob=f_path)
        s3_clientdata = blob_client.download_blob().readall()

        proptes = yaml.safe_load(s3_clientdata)        
        return proptes

class SQSConfig:

    @staticmethod
    def send_sqs(sqs_message, sqs_url):
        try:
            # email_sqs_url ==> queue connection string in azure
            # sqs_url = os.environ.get("email_sqs_url")
            queue_client = QueueClient.from_connection_string(\
                sqs_url)            
            queue_message = Message(json.dumps(sqs_message))
            queue_client.send(queue_message)

        except Exception as error:
            LOGGER.error(f"SQS Exception -> {error}", exc_info=True)

class Serialization:

    @staticmethod
    def read_event(req):
        try:
            event = {}
            event["body"] = json.dumps(req.get_json())
            event["headers"] = req.headers

        except Exception as error:
            LOGGER.error(f"Event Exception -> {error}", exc_info=True)
            logging.info(f"Event Exception -> {error}")
        finally:
            return event
            
class Response:

    @staticmethod
    def send_response(status_code, body):
        try:
            response = {}
            response["body"] = simplejson.dumps(body, default=myconverter)
            response["statusCode"] = status_code
            response["headers"] = {'Content-Type': 'application/json'}
        except Exception as error:
            LOGGER.error(f"Event Exception -> {error}", exc_info=True)
        finally:
            return simplejson.dumps(response)


def myconverter(data):
    # pylint: disable-msg=R1705
    # pylint: disable-msg=R1710
    '''
    converting datetime and date object to str
    '''
    if isinstance(data, datetime.datetime):
        return data.__str__()
    elif isinstance(data, datetime.date):
        return data.__str__()