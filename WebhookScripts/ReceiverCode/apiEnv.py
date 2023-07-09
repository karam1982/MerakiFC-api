import os
from dotenv import load_dotenv

global filePath
global envFile

filePath = "apiEnv/apiParams.env"
envFile = os.path.abspath(filePath)

def envTest():
    if os.path.exists(filePath):
        load_dotenv(dotenv_path=envFile)
        print(".env File found!")
        print("Working environment parameters:")
        print("ORG ID = ", os.getenv("FCM_ORG_ID"))
        print("Webex API URL = ", os.getenv("WX_API_URL"))
    else:
        print("Working env not set.\nCheck file exists or in proper directory.\n\nTerminating.\n")
        exit()


def getMerakiAPIKey():
    if os.path.exists(envFile):
        load_dotenv(dotenv_path=envFile)
        apiKey = os.getenv("FCM_API_KEY")
        return apiKey
    else:
        print("Env file not found")
        exit()