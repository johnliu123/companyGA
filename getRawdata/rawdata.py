from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import contentutil

# ========================================================
'''
■=== 
包含所有 XXXXRawdata 會共同使用的function

    initialize_analyticsreporting_from_p12 - 使用 .p12的金鑰 & .p12金鑰對應的email 登入 google analytic

    initialize_analyticsreporting_from_json - 使用 .json 登入 google analytic (目前沒在使用)

    get_report - 輸入登入資訊與查詢值，獲得未清理的response

'''
# ========================================================
class Rawdata():

    # ----------------
    '''
    ■=== 

    @param 
    @return
    '''
    # ----------------  
    def __init__(self):
        pass

    # ----------------
    '''
    ■=== 使用 .p12 keyfile 登入，.p12 有對應的 service_account_email & private_key_password

    @param 
    @return
    '''
    # ----------------
    def initialize_analyticsreporting_from_p12(self,private_key_password=None):

        #.p12金鑰的 email
        service_account_email = contentutil.GA_ACCOUNT_EMAIL
        
        #.p12金鑰的檔案路徑
        key_file_location = contentutil.GA_P12_KEY_FILE_PATH
        
        #固定參數
        scopes = ['https://www.googleapis.com/auth/analytics.readonly']

        #驗證.p12金鑰的函數
        credentials = ServiceAccountCredentials.from_p12_keyfile(service_account_email,
            key_file_location,private_key_password, scopes)

        # credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, scopes)
            

        # Build the service object.
        analytics = build('analyticsreporting', 'v4', credentials=credentials)

        return analytics

    # ----------------
    '''
    ■=== 使用 .json keyfile 登入

    目前使用 .p12 金鑰，沒有使用 .json 金鑰，要使用請將 "json_keyfile_path" 改為 .json 金鑰路徑

    @param 
    @return
    '''
    # ----------------
    def initialize_analyticsreporting_from_json(self):

        #.json金鑰的檔案路徑
        key_file_location = "json_keyfile_path"

        #固定參數
        scopes = ['https://www.googleapis.com/auth/analytics.readonly']

        #驗證.json金鑰的函數
        credentials = ServiceAccountCredentials.from_p12_keyfile(key_file_location, scopes)

        # Build the service object.
        analytics = build('analyticsreporting', 'v4', credentials=credentials)

        return analytics

    # ----------------
    '''
    ■=== 輸入查詢參數，獲得回傳值(未清理的資料)

    analytics - initialize_analyticsreporting_from_p12 獲得的登入資訊

    VIEW_ID - Google Analytics 資料檢視的 ID

    start_date - 查詢起始時間

    end_date - 查詢終止時間

    metrics - 查詢的指標

    dimensions - 查詢的分類

    filters - 根據 metrics & dimensions 的內容做篩選

    @param 
    @return
    '''
    # ----------------

    def get_report(self,analytics,VIEW_ID,start_date,end_date,metrics,dimensions,filters,dataIndex=''):

        #設定起始時間
        dateRanges_content = {} #dict
        dateRanges_content['startDate'] = start_date
        dateRanges_content['endDate'] = end_date

        #設定 metrics
        metrics_content = [] #list
        for metric in metrics:
            metric_column = {}
            metric_column['expression'] = metric
            metrics_content.append(metric_column)

        #設定 dimensions
        dimensions_content = [] #list
        for dimension in dimensions:
            dimensions_content.append({'name': dimension})

        #輸入查詢參數，獲得回傳值
        return analytics.reports().batchGet(
            body={'reportRequests': [
                    {
                        'viewId': VIEW_ID,
                        'dateRanges': [dateRanges_content],
                        'metrics': metrics_content,
                        'dimensions': dimensions_content,
                        'filtersExpression': filters,
                        'pageToken': dataIndex,
                        'pageSize': 100000
                        #'pageSize': 10000
                    }]
            }
        ).execute()


if __name__ == '__main__':

    pass