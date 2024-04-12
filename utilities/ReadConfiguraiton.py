from configparser import ConfigParser

def read_configuration(catagory,key):
    config=ConfigParser()
    config.read('D:\pytest_framework\cofigurations\config.ini')
   
    return config.get(catagory,key)