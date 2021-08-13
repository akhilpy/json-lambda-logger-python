import json
import boto3
import os
import logging
from setup_logger import SetupLogging

args =["source", "api_id"] #optional

@SetupLogging(*args)
def lambda_handler(event, context, log_dict=None, logger=None):
    
    log_dict['api_id'] =event.get('requestContext')['requestId'] if event.get('requestContext') else None
    log_dict['source'] = context.function_name
    logger.info("success", extra=log_dict)
    
    try:
        a=10
        res =a/10
        logger.info("success", extra=log_dict)
        return_res=  {
        'statusCode': 200,
        'body': json.dumps('OK')
        }
    except Exception as e:
        logger.exception(str(e), extra=log_dict)
        return_res= {
                'statusCode': 409,
                'body': json.dumps('Exception:{}'.format(str(e)))
                }
        
    return return_res
        
    
