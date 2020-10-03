from storages.backends.azure_storage import AzureStorage
import os
class AzureMediaStorage(AzureStorage):
    account_name = os.environ.get('Azure_Account_Name', '')
    account_key = os.environ.get('Azure_Account_Key', '') 
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = os.environ.get('Azure_Account_Name', '')
    account_key = os.environ.get('Azure_Account_Key', '') 
    azure_container = 'static'
    expiration_secs = None