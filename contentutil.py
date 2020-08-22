import logging
 
# log 基礎設定
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    handlers = [logging.FileHandler('python.log', 'w', 'utf-8'),])

# Variable

MONGO_DBNAME = 'CupoyGoogleAnalytics'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = '27017'

GA_ID = '119454156' # GA資料編號，此為"所有網站資料"
GA_ACCOUNT_EMAIL = 'cupoy-analytics@cupoy-analytics-1273.iam.gserviceaccount.com'
GA_P12_KEY_FILE_PATH = './cupoy-analytics-project-key.p12'

# Method

def printlog(logstring):
    print(logstring) 
    logging.info(logstring)