import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read('D:\gitprojects\genai-app\config.ini')
    return config
