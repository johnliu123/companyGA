import json

from getDatalists.cupoyAPI import CupoyAPI
import time

import pymongo

# ========================================================
'''
■=== 與會員有關事件的rawdata

資料源
    在網頁埋GA事件(微觀)

    包含function
        在線換頁事件 - getMemberOnLineRawdata
        會員註冊事件 - getMemberNewRegisterRawdata

'''
# ========================================================
class Datalists():

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
    ■=== 將GA回傳值 row 轉為 (dimensions_values,metric_values) 的 tuple

    @param 
    @return
    '''
    # ----------------
    def getRowTuple(self,row):

        #取出 dimension 值
        dimensions_values = row.get('dimensions', []) #得到["Cumatrix", "createCumatrix", "(not set)", "20190424" ]

        #取出 values 值
        metric_values_list = row.get('metrics', []) #結果為[{'values': ['15.0', '7.5']}]
        metric_values_dict = metric_values_list[0] #結果為{'values': ['15.0', '7.5']}
        metric_values = metric_values_dict["values"] #['15.0', '7.5']

        return (dimensions_values,metric_values)


    # ----------------
    '''
    ■=== 將 eventLabel 從 string 轉換回 dict

    @param
    @return
    '''
    # ----------------
    def convertStringToDict(self,label_string):

        #去除 { } , :
        label_string = label_string.replace("{","").replace("}","").replace(",","").replace(":","")
        
        #以 " 切割
        label_list = label_string.split("\"")

        #去除重複的空值("") 留下 index 0 的空值
        label_data_list = []
        for label in label_list:
            if not label in label_data_list:
                label_data_list.append(label)

        #若 index 0 為空值 則移除
        if label_data_list[0] == "":
            label_data_list.remove("")

        #裝清理完的 label
        label_dict = {}

        index_number = len(label_data_list)/2
        for num in range(int(index_number)):
            label_dict[label_data_list[num*2]] = label_data_list[num*2+1]

        return label_dict

    # ----------------
    '''
    ■=== 將 YYYYMMDD 轉為 YYYY-MM-DD

    @param 
    @return
    '''
    # ----------------
    def getDateType(self,YYYYMMDD):

        YYYY = YYYYMMDD[:4]
        MM = YYYYMMDD[4:6]
        DD = YYYYMMDD[6:8]

        date = "{}-{}-{}".format(YYYY,MM,DD)

        return date

    # ----------------
    
    '''
    ■=== 將 YYYYMMDD 轉為 MM-DD

    @param 
    @return
    '''
    # ----------------
    def getDateType1(self,YYYYMMDD):

        #YYYY = YYYYMMDD[:4]
        MM = YYYYMMDD[4:6]
        DD = YYYYMMDD[6:8]

        date = "{}-{}".format(MM,DD)

        return date

    # ----------------
       
    # ----------------
    
    '''
    ■=== 取得當前 mrscid:mrsname 列表及 mrscid，回傳對應的 mrsname，若沒有則使用Cupoy API 調閱並新增

    @param 
    @return
    '''
    # ----------------
    def getMrsname(self,mrsname_dict,mrscid):

        #沒有mrscid(會員ID)的紀錄
        if mrscid == "empty":
            mrsname = "空的"

        #若mrsname_dict包含mrscid，則獲得對應的mrsname
        elif mrscid in mrsname_dict:
            mrsname = mrsname_dict[mrscid]

        #若mrsname_dict不包含mrscid，則調閱API取得mrsname，並將"mrscid":"mrsname"存入mrsname_dict
        else:
            memberInfoData = CupoyAPI()
            memberInfoData.mrscid = mrscid
            memberInfo = memberInfoData.getMemberInfo()

            if memberInfo == None:
                
                return None

            # data_dict 存入 API 取得的 mrsname
            mrsname = memberInfo["mrsname"]

            # "mrscid":"mrsname" 存入 mrsname_dict
            mrsname_dict[mrscid] = memberInfo["mrsname"]


        return mrsname


    # ----------------
    '''
    ■=== 將清理完成的資料儲存到mongo

    @param 
    @return
    '''
    # ----------------
    def send_datalists_to_mongo(self,db,collection):
        #設定連入的 mongo
        client = pymongo.MongoClient(host='127.0.0.1',port=27017)

        #設定 db
        mongo_db = client[db]

        #設定 collection
        mongo_collection = mongo_db[collection]

        result = mongo_collection.insert_many(self.datalists)

    # ----------------
    '''
    ■=== 將清理完成的資料輸出成json

    @param 
    @return
    '''
    # ----------------
    def save_to_json_file(self,rawdata):
        
        #dic 存成 json
        fiel_name = 'clear_{}.json'.format("test")
        with open(fiel_name, 'w') as fp:
            json.dump(rawdata, fp, indent=4, separators=(',', ':'))

    # ----------------
    '''
    ■=== 將清理完成的資料輸出成csv

    @param 
    @return
    '''
    # ----------------
    def save_to_csv(self,filepath,start_date):

        #添加週次
        filename = self.addWeekNumber(filepath,start_date)

        datalists = self.datalists
        column_name = self.columnName

        data_array = []

        #將dict資料轉為一筆csv的資料
        for data in datalists:
            datalist = []
            for column in column_name:
                try:
                    datalist.append(data[column])
                except KeyError:
                    datalist.append("")
            data_array.append(datalist)

        dataframe = pd.DataFrame(data_array, columns = column_name)

        csvname = '{}.csv'.format(filename)
               
        #輸出成 csv，選擇可與excel 相容的 'utf_8_sig'
        dataframe.to_csv(csvname,index=0, encoding='utf_8_sig')
        
       
        #去除重複欄位
        if "kwAssistDailyDownloadPdf" in csvname:
            df=pd.read_csv(csvname)
            df.drop_duplicates(subset=['mrscid','taskid','logdate'],keep='first',inplace=True)
            df.to_csv(csvname,index=0, encoding='utf_8_sig')
        else:
            pass
       
    # ----------------
    '''
    ■=== 替檔案名稱添加週數 ex [filename]_201901

    @param 
    @return
    '''
    # ----------------
    def addWeekNumber(self,filename,date=time.strftime("%Y-%m-%d", time.localtime())):

        datetime = time.strptime(date, '%Y-%m-%d')
        #獲得當前年份
        yearNumber = time.strftime("%Y", datetime)

        #獲得當前週次(00-53)
        weekNumber = time.strftime("%U", datetime)

        #由於 weekNumber 對應google日曆的週次少1，在此作處理
        trueWeekNumber = int(weekNumber) + 1

        
        newFilename = "{}_{}{:0>2}".format(filename,yearNumber,trueWeekNumber)

        return newFilename

if __name__ == '__main__':

    pass