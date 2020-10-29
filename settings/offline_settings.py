import os
import logging
import json
import redis
import boto3
import simplejson
# import yaml
from configuration import BUCKET_NAME, FLAG
import datetime

LOGGER = logging.getLogger("einvoice_app_pull")

class RedisConfig:

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
        return {}
    
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
        return cache

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
        return None

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
        return None
        
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
        return None

    @staticmethod
    def get_host_port():
        HOST = os.environ.get('redis_url','')
        PORT = os.environ.get('redis_port','0')
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
            s3_object = boto3.client(
                service_name='s3',
                endpoint_url= os.environ.get("s3_localstack_endpoint", "http://localhost:4566")
                )
            bucket = BUCKET_NAME if not bucket_name else bucket_name
            s3_clientobj = s3_object.get_object(Bucket=bucket, Key=default_config_path)
            s3_clientdata = s3_clientobj['Body'].read().decode('utf-8')
            file_dict = json.loads(s3_clientdata) if json_load else s3_clientdata
        except Exception as error:
            LOGGER.error("EXCEPTION OCCURED %s", str(error), exc_info=True)
        return file_dict

    @staticmethod
    def delete_file(bucket_name, key):
        s3_client = boto3.client(
            service_name='s3',
            endpoint_url= os.environ.get("s3_localstack_endpoint", "http://localhost:4566")
        )
        # Deleting the json file from s3 bucket
        s3_client.delete_object(Bucket=bucket_name, Key=key)

    @staticmethod
    def upload_file(bucket_name, key, filename):
        s3 = boto3.client(
            service_name='s3',
            endpoint_url= os.environ.get("s3_localstack_endpoint", "http://localhost:4566")
        )
        s3.upload_file(filename, bucket_name, key)
        # with open(filename, "rb") as data:
        #     s3.Object(bucket_name, key).put(
        #         Body = (bytes(data.encode('UTF-8')))
        #     )
        # s3.Object(bucket_name, key).put(
        #     Body = (bytes(data.encode('UTF-8')))
        # )
        
class SQSConfig:

    @staticmethod
    def send_sqs(sqs_message, sqs_url):
        try:
            client = boto3.client('sqs', region_name='ap-south-1')
            # sqs_url = os.environ['email_sqs_url']
            response = client.send_message(\
                QueueUrl=sqs_url,\
                MessageBody=json.dumps(sqs_message))
        except Exception as error:
            LOGGER.error(f"SQS Exception -> {error}", exc_info=True)

class Serialization:

    @staticmethod
    def read_event(req):
        try:
            event = {}
            event["body"] = json.dumps(req.stream.read())
            event["headers"] = req.headers
            # event = req            
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
        except Exception as error:
            LOGGER.error(f"Event Exception -> {error}", exc_info=True)
        finally:
            return response


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