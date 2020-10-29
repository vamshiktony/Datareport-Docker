'''
create response strucure message
'''
import datetime


def response_dict(msg, response_code, key, count=None, next_offset=None):
    '''
    create response structure
    params - msg: Status Message
    params - response_code: Response Code
    params - key: return data
    '''
    response_message = {}
    response_message["status"] = response_code
    response_message["message"] = msg
    response_message["system time"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    response_message["data"] = key
    if count != None:
        response_message["count"] = str(count)
    if next_offset != None:
        response_message["next_offset"] = next_offset
    return response_message
