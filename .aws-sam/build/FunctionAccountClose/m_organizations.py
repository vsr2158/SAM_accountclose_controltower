import boto3


client = boto3.client('organizations')

def get_accountid_list():
    # List all accounts to cremap account id with account name
    paginator = client.get_paginator('list_accounts')
    page_iterator = paginator.paginate(MaxResults=10)

    accountid_list = []
    for page in page_iterator:
        #page is a dict, we are interested in the key 'Accounts'
        accountid_list_page = page['Accounts']
        #combine several pages (lists) to single list
        for a in accountid_list_page:
            accountid_list.append(a)

    return (accountid_list)

def get_accountid_for_accountname(account_name):
    accountid_list = get_accountid_list()
    for a in accountid_list:
        if a['Name'] == account_name:
            account_id = a['Id']
            return (account_id)

def close_account(account_id):
    response = client.close_account(
        AccountId=account_id
    )