from getRawdata.rawdata import Rawdata
import contentutil

# ========================================================
'''
■=== 與新聞有關事件的rawdata

cupoy 熱門新聞 - https://www.cupoy.com/newsfeed/topstory

資料源
    在網頁埋GA事件(微觀)

    包含function
        在熱門新聞，點擊新聞事件 - getReadNewsRawdata
        在熱門新聞，使用者行為事件 - getNewsUserEngageRawdata
        專家/意見領袖發文事件 - getPostNewsRawdata

'''
# ========================================================
class AllRawData(Rawdata):

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
    ■=== 獲得 getViewRawdata 的 rawdata

    @param 
    @return
    '''
    # ----------------
    def getViewRawdata(self):

        #獲得登入資訊
        analytics = self.initialize_analyticsreporting_from_p12()

        #查詢參數
        VIEW_ID = contentutil.GA_ID #GA資料編號，此為"所有網站資料"
        start_date = self.start_date
        end_date = self.end_date
        metrics = ['ga:uniqueEvents']
        dimensions = ['ga:date','ga:eventCategory','ga:eventAction','ga:eventLabel']
        filters = 'ga:hostname=@m.cupoy.com,ga:hostname=@www.cupoy.com;ga:eventCategory=@View'

        #獲得查詢資料(未清理)
        queryResponse = self.get_report(analytics,VIEW_ID,start_date,end_date,metrics,dimensions,filters)

        for report in queryResponse.get('reports', []): #only 1 report

            #得到  data 的 value (dict)
            rawdata = report.get('data', {})

        return rawdata
    
    # ----------------
    '''
    ■=== 獲得 getNewsRawdata 的 rawdata

    @param 
    @return
    '''
    # ----------------
    def getNewsRawdata(self):

        #獲得登入資訊
        analytics = self.initialize_analyticsreporting_from_p12()

        #查詢參數
        VIEW_ID = contentutil.GA_ID #GA資料編號，此為"所有網站資料"
        start_date = self.start_date
        end_date = self.end_date
        metrics = ['ga:uniqueEvents']
        dimensions = ['ga:date','ga:eventCategory','ga:eventAction','ga:eventLabel']
        filters = 'ga:hostname=@m.cupoy.com,ga:hostname=@www.cupoy.com;ga:eventCategory=@News'

        #獲得查詢資料(未清理)
        queryResponse = self.get_report(analytics,VIEW_ID,start_date,end_date,metrics,dimensions,filters)

        for report in queryResponse.get('reports', []): #only 1 report

            #得到  data 的 value (dict)
            rawdata = report.get('data', {})

        return rawdata
    
     # ----------------
    '''
    ■=== 獲得 getInfluencerRawdata 的 rawdata

    @param 
    @return
    '''
    # ----------------
    def getInfluencerRawdata(self):

        #獲得登入資訊
        analytics = self.initialize_analyticsreporting_from_p12()

        #查詢參數
        VIEW_ID = contentutil.GA_ID #GA資料編號，此為"所有網站資料"
        start_date = self.start_date
        end_date = self.end_date
        metrics = ['ga:uniqueEvents']
        dimensions = ['ga:date','ga:eventCategory','ga:eventAction','ga:eventLabel']
        filters = 'ga:hostname=@m.cupoy.com,ga:hostname=@www.cupoy.com;ga:eventCategory=@Influencer'

        #獲得查詢資料(未清理)
        queryResponse = self.get_report(analytics,VIEW_ID,start_date,end_date,metrics,dimensions,filters)

        for report in queryResponse.get('reports', []): #only 1 report

            #得到  data 的 value (dict)
            rawdata = report.get('data', {})

        return rawdata
    
    
    # ----------------
    '''
    ■=== 獲得 getkwAssistRawdata 的 rawdata

    @param 
    @return
    '''
    # ----------------
    def getkwAssistRawdata(self):

        #獲得登入資訊
        analytics = self.initialize_analyticsreporting_from_p12()

        #查詢參數
        VIEW_ID = contentutil.GA_ID #GA資料編號，此為"所有網站資料"
        start_date = self.start_date
        end_date = self.end_date
        metrics = ['ga:uniqueEvents']
        dimensions = ['ga:date','ga:eventCategory','ga:eventAction','ga:eventLabel']
        filters = 'ga:hostname=@m.cupoy.com,ga:hostname=@www.cupoy.com;ga:eventCategory=@kwAssist'

        #獲得查詢資料(未清理)
        queryResponse = self.get_report(analytics,VIEW_ID,start_date,end_date,metrics,dimensions,filters)

        for report in queryResponse.get('reports', []): #only 1 report

            #得到  data 的 value (dict)
            rawdata = report.get('data', {})

        return rawdata
    
     # ----------------
    '''
    ■=== 獲得 getCumatrixRawdata 的 rawdata

    @param 
    @return
    '''
    # ----------------
    def getCumatrixRawdata(self):

        #獲得登入資訊
        analytics = self.initialize_analyticsreporting_from_p12()

        #查詢參數
        VIEW_ID = contentutil.GA_ID #GA資料編號，此為"所有網站資料"
        start_date = self.start_date
        end_date = self.end_date
        metrics = ['ga:uniqueEvents']
        dimensions = ['ga:date','ga:eventCategory','ga:eventAction','ga:eventLabel']
        filters = 'ga:hostname=@m.cupoy.com,ga:hostname=@www.cupoy.com;ga:eventCategory=@Cumatrix'

        #獲得查詢資料(未清理)
        queryResponse = self.get_report(analytics,VIEW_ID,start_date,end_date,metrics,dimensions,filters)

        for report in queryResponse.get('reports', []): #only 1 report

            #得到  data 的 value (dict)
            rawdata = report.get('data', {})

        return rawdata
    
     # ----------------
    '''
    ■=== 獲得 getMerberRawdata 的 rawdata

    @param 
    @return
    '''
    # ----------------
    def getMerberRawdata(self):

        #獲得登入資訊
        analytics = self.initialize_analyticsreporting_from_p12()

        #查詢參數
        VIEW_ID = contentutil.GA_ID #GA資料編號，此為"所有網站資料"
        start_date = self.start_date
        end_date = self.end_date
        metrics = ['ga:uniqueEvents']
        dimensions = ['ga:date','ga:eventCategory','ga:eventAction','ga:eventLabel']
        filters = 'ga:hostname=@m.cupoy.com,ga:hostname=@www.cupoy.com;ga:eventCategory=@Member;'

        #獲得查詢資料(未清理)
        queryResponse = self.get_report(analytics,VIEW_ID,start_date,end_date,metrics,dimensions,filters)

        for report in queryResponse.get('reports', []): #only 1 report

            #得到  data 的 value (dict)
            rawdata = report.get('data', {})

        return rawdata
    
    
     # ----------------
    '''
    ■=== 獲得 getAi100Rawdata 的 rawdata

    @param 
    @return
    '''
    # ----------------
    def getAi100Rawdata(self):

        #獲得登入資訊
        analytics = self.initialize_analyticsreporting_from_p12()

        #查詢參數
        VIEW_ID = contentutil.GA_ID #GA資料編號，此為"所有網站資料"
        start_date = self.start_date
        end_date = self.end_date
        metrics = ['ga:uniqueEvents']
        dimensions = ['ga:date','ga:eventCategory','ga:eventAction','ga:eventLabel']
        filters = 'ga:hostname=@www.ai100.cupoy.com,ga:eventCategory=@AI100'

        #獲得查詢資料(未清理)
        queryResponse = self.get_report(analytics,VIEW_ID,start_date,end_date,metrics,dimensions,filters)

        for report in queryResponse.get('reports', []): #only 1 report

            #得到  data 的 value (dict)
            rawdata = report.get('data', {})

        return rawdata

    

if __name__ == '__main__':

    pass