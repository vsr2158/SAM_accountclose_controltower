import json
import m_organizations
import os
import logging

LOG_LEVEL = os.getenv('LOG_LEVEL')
logging.getLogger().setLevel(LOG_LEVEL)

def lambda_handler(event, context):
    logging.info(f'EVENT : {event}')
    # Filter and act on the right event
    if event.get("detail").get("eventName") == "TerminateProvisionedProduct":
        # extract account_name from the event
        account_name = event.get("detail").get("requestParameters").get("provisionedProductName")
        logging.info(f'ACCOUNT NAME : {account_name}')
    else:
        return {
            'statusCode': 200,
            'Status': 'IGNORE',
            'exception_type': 'Null',
            'exception_message': 'Null'
        }

    # extract account id for given account_name
    account_id = m_organizations.get_accountid_for_accountname(account_name)
    logging.info(f'ACCOUNT ID : {account_id}')

    # close account
    try:
        response = m_organizations.close_account(account_id)
        return {
            'statusCode': 200,
            'Status': 'SUCCESS',
            'account_id': account_id,
            'account_name': account_name,
            'response': response,
            'exception_type': 'Null',
            'exception_message': 'Null'
        }

    except Exception as e:
        exception_type = e.__class__.__name__
        exception_message = str(e)
        logging.exception(f'{exception_type}: {exception_message}')
        return {
            'statusCode': 500,
            'Status': 'FAIL',
            'account_id': account_id,
            'account_name': account_name,
            'event': event,
            'exception_type': exception_type,
            'exception_message': exception_message
        }
