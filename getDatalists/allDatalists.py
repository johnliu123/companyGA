from getRawdata.allRawData import AllRawData

from getDatalists.datalists import Datalists

from getDatalists.cupoyAPI import CupoyAPI






# ========================================================
'''
■=== 與新聞有關事件的 datalists

資料源
	在網頁埋GA事件(微觀)

	包含function
		在線換頁事件 - getMemberOnLineRawdata
		會員註冊事件 - getMemberNewRegisterRawdata

'''
# ========================================================
class AllDatalists(Datalists):

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
	■=== 獲得新聞的使用者行為事件

	@param 
	@return
	'''
	# ----------------
	def getViewDatalists(self):

		
		self.datalists = []

		

		#get data list
		rows = self.rawdata.get('rows', [])

		datalists = []

		for row in rows:

			#裝要儲存的資料
			data_dict = {}

			(dimensions_list,metric_list) = self.getRowTuple(row)

			#日期與小時
			data_dict["logdate"] = self.getDateType(dimensions_list[0])
			#data_dict["loghour"] = dimensions_list[1]

			
			#eventCategory
			data_dict["category"] = dimensions_list[1]
			
			#eventAction
			data_dict["action"] = dimensions_list[2]

			

			#eventLabel
			label_dict = self.convertStringToDict(dimensions_list[3])
			
			if "timestamp" not in label_dict:
				data_dict["timestamp"]= None
			else:
				data_dict["timestamp"] = int(label_dict["timestamp"])
			

			#會員ID - 若沒有會員ID則透過錯誤處理，改為裝 emtpy
			try:
				data_dict["mrscid"] = label_dict["mrscid"]
			except KeyError:
				data_dict["mrscid"] = None

			#新聞ID
			if "nationid" not in label_dict:
				data_dict["nationid"]= None
			else:
				data_dict["nationid"] = label_dict["nationid"]
			
			if "bucketgrpid" not in label_dict:
				data_dict["bucketgrpid"]= None
			else:
				data_dict["bucketgrpid"] = label_dict["bucketgrpid"]
			
			if "assistid" not in label_dict:
				data_dict["assistid"]= None
			else:
				data_dict["assistid"] = label_dict["assistid"]
			
			
			
			#放入 array 中
			self.datalists.append(data_dict)
			

			
			"""
			newsInfoData = CupoyAPI()
			newsInfoData.newsid = data_dict["newsid"]
			newsInfo = newsInfoData.getNewsInfo()
			

			#如果用新聞ID調資料出問題，則跳過
			if newsInfo == None:
				continue
			

			data_dict = dict(list(data_dict.items())+list(newsInfo.items()))

			#data_dict = dict(list(data_dict.items()))
			
			
			#輸入 mrsname_dict 與 mrscid 會員ID 獲得會員名稱
			data_dict["mrsname"] = self.getMrsname(mrsname_dict,data_dict["mrscid"])

			#若會員名稱不存在，表示資料庫無此 mrscid 資訊，故跳過此筆資料
			if data_dict["mrsname"] == None:

				#continue
				data_dict["mrsname"]="空的"
			
			
			#data_dict = dict(list(data_dict.items()))
				
			#放入 array 中
			self.datalists.append(data_dict)
			"""
	
	# ----------------
	'''
	■=== 獲得新聞的使用者行為事件

	@param 
	@return
	'''
	# ----------------
	def getNewsDatalists(self):

		
		self.datalists = []

		

		#get data list
		rows = self.rawdata.get('rows', [])

		datalists = []

		for row in rows:

			#裝要儲存的資料
			data_dict = {}

			(dimensions_list,metric_list) = self.getRowTuple(row)

			#日期與小時
			data_dict["logdate"] = self.getDateType(dimensions_list[0])
			#data_dict["loghour"] = dimensions_list[1]

			
			#eventCategory
			data_dict["category"] = dimensions_list[1]
			
			#eventAction
			data_dict["action"] = dimensions_list[2]

			

			#eventLabel
			label_dict = self.convertStringToDict(dimensions_list[3])
			
			if "timestamp" not in label_dict:
				data_dict["timestamp"]= None
			else:
				data_dict["timestamp"] = int(label_dict["timestamp"])
			
			if "itemid" not in label_dict:
				data_dict["itemid"]= None
			else:
				data_dict["itemid"] = label_dict["itemid"]
			

			#會員ID - 若沒有會員ID則透過錯誤處理，改為裝 emtpy
			try:
				data_dict["mrscid"] = label_dict["mrscid"]
			except KeyError:
				data_dict["mrscid"] = None

			
			#新聞ID
			if "nationid" not in label_dict:
				data_dict["nationid"]= None
			else:
				data_dict["nationid"] = label_dict["nationid"]
			
			"""
			if "bucketgrpid" not in label_dict:
				data_dict["bucketgrpid"]= None
			else:
				data_dict["bucketgrpid"] = label_dict["bucketgrpid"]
			
			if "assistid" not in label_dict:
				data_dict["assistid"]= None
			else:
				data_dict["assistid"] = label_dict["assistid"]
			"""
			
			

			
			newsInfoData = CupoyAPI()
			newsInfoData.newsid = data_dict["itemid"]
			newsInfo = newsInfoData.getNewsInfo()

			#如果用新聞ID調資料出問題，則跳過
			if newsInfo == None:
				continue

			data_dict = dict(list(data_dict.items())+list(newsInfo.items()))

			"""
			#輸入 mrsname_dict 與 mrscid 會員ID 獲得會員名稱
			data_dict["mrsname"] = self.getMrsname(mrsname_dict,data_dict["mrscid"])

			#若會員名稱不存在，表示資料庫無此 mrscid 資訊，故跳過此筆資料
			if data_dict["mrsname"] == None:

				#continue
				data_dict["mrsname"]="空的"
			"""

			
				
			#放入 array 中
			self.datalists.append(data_dict)
            
    # ----------------
	'''
	■=== 獲得新聞的使用者行為事件

	@param 
	@return
	'''
	# ----------------
	def getinfluencerDatalists(self):

		
		self.datalists = []

		

		#get data list
		rows = self.rawdata.get('rows', [])

		datalists = []

		for row in rows:

			#裝要儲存的資料
			data_dict = {}

			(dimensions_list,metric_list) = self.getRowTuple(row)

			#日期與小時
			data_dict["logdate"] = self.getDateType(dimensions_list[0])
			#data_dict["loghour"] = dimensions_list[1]

			
			#eventCategory
			data_dict["category"] = dimensions_list[1]
			
			#eventAction
			data_dict["action"] = dimensions_list[2]

			

			#eventLabel
			label_dict = self.convertStringToDict(dimensions_list[3])
			
			if "timestamp" not in label_dict:
				data_dict["timestamp"]= None
			else:
				data_dict["timestamp"] = int(label_dict["timestamp"])
			
			if "itemid" not in label_dict:
				data_dict["itemid"]= None
			else:
				data_dict["itemid"] = label_dict["itemid"]
			

			#會員ID - 若沒有會員ID則透過錯誤處理，改為裝 emtpy
			try:
				data_dict["mrscid"] = label_dict["mrscid"]
			except KeyError:
				data_dict["mrscid"] = None

			
			#新聞ID
			if "nationid" not in label_dict:
				data_dict["nationid"]= None
			else:
				data_dict["nationid"] = label_dict["nationid"]
			
			"""
			if "bucketgrpid" not in label_dict:
				data_dict["bucketgrpid"]= None
			else:
				data_dict["bucketgrpid"] = label_dict["bucketgrpid"]
			
			if "assistid" not in label_dict:
				data_dict["assistid"]= None
			else:
				data_dict["assistid"] = label_dict["assistid"]
			"""
			
			

			
			newsInfoData = CupoyAPI()
			newsInfoData.newsid = data_dict["itemid"]
			newsInfo = newsInfoData.getNewsInfo()

			#如果用新聞ID調資料出問題，則跳過
			if newsInfo == None:
				continue

			data_dict = dict(list(data_dict.items())+list(newsInfo.items()))

			"""
			#輸入 mrsname_dict 與 mrscid 會員ID 獲得會員名稱
			data_dict["mrsname"] = self.getMrsname(mrsname_dict,data_dict["mrscid"])

			#若會員名稱不存在，表示資料庫無此 mrscid 資訊，故跳過此筆資料
			if data_dict["mrsname"] == None:

				#continue
				data_dict["mrsname"]="空的"
			"""

			
				
			#放入 array 中
			self.datalists.append(data_dict)
    
    
			
	
	# ----------------
	'''
	■=== 獲得新聞的使用者行為事件

	@param 
	@return
	'''
	# ----------------
	def getkwAssistDatalists(self):

		
		self.datalists = []

		

		#get data list
		rows = self.rawdata.get('rows', [])

		datalists = []

		for row in rows:

			#裝要儲存的資料
			data_dict = {}

			(dimensions_list,metric_list) = self.getRowTuple(row)

			#日期與小時
			data_dict["logdate"] = self.getDateType(dimensions_list[0])
			#data_dict["loghour"] = dimensions_list[1]

			
			#eventCategory
			data_dict["category"] = dimensions_list[1]
			
			#eventAction
			data_dict["action"] = dimensions_list[2]

			

			#eventLabel
			label_dict = self.convertStringToDict(dimensions_list[3])
			
			if "timestamp" not in label_dict:
				data_dict["timestamp"]= None
			else:
				data_dict["timestamp"] = int(label_dict["timestamp"])
			
			
					
			#會員ID - 若沒有會員ID則透過錯誤處理，改為裝 emtpy
			try:
				data_dict["mrscid"] = label_dict["mrscid"]
			except KeyError:
				data_dict["mrscid"] = None

			
			#新聞ID
			if "nationid" not in label_dict:
				data_dict["nationid"]= None
			else:
				data_dict["nationid"] = label_dict["nationid"]
				
			if "assistid" not in label_dict:
				data_dict["assistid"]= None
			else:
				data_dict["assistid"] = label_dict["assistid"]
			
			
			"""
			if "bucketgrpid" not in label_dict:
				data_dict["bucketgrpid"]= None
			else:
				data_dict["bucketgrpid"] = label_dict["bucketgrpid"]
			
			if "assistid" not in label_dict:
				data_dict["assistid"]= None
			else:
				data_dict["assistid"] = label_dict["assistid"]
			"""
			
			
			
			if "qid" not in label_dict:
				data_dict["qid"]= None
				
			else:
				data_dict["qid"] = label_dict["qid"]
				
				questionInfoData = CupoyAPI()

				questionInfoData.qid = data_dict["qid"]

				questionInfo = questionInfoData.getQuestionInfo()

				#去除不存在的問題
				if questionInfo == None:
					continue
	
				else:
					#合併用api獲得的資料
					data_dict = dict(list(data_dict.items())+list(questionInfo.items()))
					#放入 array 中
					#self.datalists.append(data_dict)
			
			
			if "itemid" not in label_dict:
				data_dict["itemid"]= None
				
			else:
				data_dict["itemid"] = label_dict["itemid"]
				newsInfoData = CupoyAPI()
				newsInfoData.newsid = data_dict["itemid"]
				newsInfo = newsInfoData.getNewsInfo()
	
				#如果用新聞ID調資料出問題，則跳過
				if newsInfo == None:
					continue
	
				data_dict = dict(list(data_dict.items())+list(newsInfo.items()))
				#放入 array 中
				#self.datalists.append(data_dict)
				
			
			
			if "cumatrixitemid" not in label_dict:
				data_dict["cumatrixitemid"]= None
			else:
				data_dict["cumatrixitemid"] = label_dict["cumatrixitemid"]
				
				cumatrixItemInfoData = CupoyAPI()

				cumatrixItemInfoData.cumatrixid = data_dict["cumatrixid"]
	
				cumatrixItemInfoData.cumatrixitemid = data_dict["cumatrixitemid"]
	
				cumatrixItemInfo = cumatrixItemInfoData.getCumatrixItemInfo()
	
				#書籍課程內容不存在，跳過
				if cumatrixItemInfo == None:
					continue
	
				else:
					data_dict = dict(list(data_dict.items())+list(cumatrixItemInfo.items()))
					#放入 array 中
					#self.datalists.append(data_dict)
			
			if "cumatrixid" not in label_dict:
				data_dict["cumatrixid"]= None
				
			else:
				
				data_dict["cumatrixid"] = label_dict["cumatrixid"]
				cumatrixItemInfoData = CupoyAPI()

				cumatrixItemInfoData.cumatrixid = data_dict["cumatrixid"]
	
				cumatrixItemInfoData.cumatrixitemid = data_dict["cumatrixitemid"]
	
				cumatrixItemInfo = cumatrixItemInfoData.getCumatrixItemInfo()
	
				#書籍課程內容不存在，跳過
				if cumatrixItemInfo == None:
					continue
	
				else:
					data_dict = dict(list(data_dict.items())+list(cumatrixItemInfo.items()))
					#放入 array 中
					#self.datalists.append(data_dict)
			
			
			
			
			if "headlineitemid" not in label_dict:
				
				data_dict["headlineitemid"]= None
				
			else:
				data_dict["headlineitemid"] = label_dict["headlineitemid"]
				
				headlineItemInfoData = CupoyAPI()

				headlineItemInfoData.headlineitemid = data_dict["headlineitemid"]
	
				headlineItemInfo = headlineItemInfoData.getHeadlineItemInfo()
	
				#去除不存在的問題
				if headlineItemInfo == None:
					continue
	
				else:
					data_dict = dict(list(data_dict.items())+list(headlineItemInfo.items()))
					#放入 array 中
					#self.datalists.append(data_dict)
			
						
				
			#放入 array 中
			self.datalists.append(data_dict)
	
	
	# ----------------
	'''
	■=== 獲得新聞的使用者行為事件

	@param 
	@return
	'''
	# ----------------
	def getCumatrixDatalists(self):

		
		self.datalists = []

		

		#get data list
		rows = self.rawdata.get('rows', [])

		datalists = []

		for row in rows:

			#裝要儲存的資料
			data_dict = {}

			(dimensions_list,metric_list) = self.getRowTuple(row)

			#日期與小時
			data_dict["logdate"] = self.getDateType(dimensions_list[0])
			#data_dict["loghour"] = dimensions_list[1]

			
			#eventCategory
			data_dict["category"] = dimensions_list[1]
			
			#eventAction
			data_dict["action"] = dimensions_list[2]

			

			#eventLabel
			label_dict = self.convertStringToDict(dimensions_list[3])
			
			if "timestamp" not in label_dict:
				data_dict["timestamp"]= None
			else:
				data_dict["timestamp"] = int(label_dict["timestamp"])
			

			#會員ID - 若沒有會員ID則透過錯誤處理，改為裝 emtpy
			try:
				data_dict["mrscid"] = label_dict["mrscid"]
			except KeyError:
				data_dict["mrscid"] = None
			
			
			if "cumatrixid"	 not in label_dict:
				continue
				#data_dict["cumatrixid"]= None
				#self.datalists.append(data_dict)
				
			elif "cumatrixitemid" not in label_dict:
				continue
				#data_dict["cumatrixitemid"]= None
				#self.datalists.append(data_dict)
			
			else:
				data_dict["cumatrixid"] = label_dict["cumatrixid"]
				data_dict["cumatrixitemid"] = label_dict["cumatrixitemid"]
				
				cumatrixItemInfoData = CupoyAPI()

				cumatrixItemInfoData.cumatrixid = data_dict["cumatrixid"]
	
				cumatrixItemInfoData.cumatrixitemid = data_dict["cumatrixitemid"]
	
				cumatrixItemInfo = cumatrixItemInfoData.getCumatrixItemInfo()
	
				#書籍課程內容不存在，跳過
				if cumatrixItemInfo == None:
					continue
	
				else:
					data_dict = dict(list(data_dict.items())+list(cumatrixItemInfo.items()))
					
					
				
				
				
			#放入 array 中
			self.datalists.append(data_dict)
	
	
	# ----------------
	'''
	■=== 獲得新聞的使用者行為事件

	@param 
	@return
	'''
	# ----------------
	def getMemberDatalists(self):

		
		self.datalists = []

		

		#get data list
		rows = self.rawdata.get('rows', [])

		datalists = []

		for row in rows:

			#裝要儲存的資料
			data_dict = {}

			(dimensions_list,metric_list) = self.getRowTuple(row)

			#日期與小時
			data_dict["logdate"] = self.getDateType(dimensions_list[0])
			#data_dict["loghour"] = dimensions_list[1]

			
			#eventCategory
			data_dict["category"] = dimensions_list[1]
			
			#eventAction
			data_dict["action"] = dimensions_list[2]

			

			#eventLabel
			label_dict = self.convertStringToDict(dimensions_list[3])
			
			if "timestamp" not in label_dict:
				data_dict["timestamp"]= None
			else:
				data_dict["timestamp"] = int(label_dict["timestamp"])
			

			if	"mrscid" in data_dict:
				
				data_dict["mrscid"] = data_dict["mrscid"]
				data_dict = dict(list(data_dict.items()))
				
				#以取不到後台api mrscid
				memberInfoData = CupoyAPI()
				memberInfoData.mrscid = data_dict["mrscid"]
				memberInfo = memberInfoData.getMemberInfo()
				data_dict = dict(list(data_dict.items())+list(memberInfo.items()))
				
								   
			elif "Mrscid" in data_dict:
				
				data_dict["mrscid"] = data_dict["Mrscid"]
				data_dict = dict(list(data_dict.items()))
				
			else:
				
				data_dict["mrscid"] = None
				data_dict = dict(list(data_dict.items()))
				
				
				memberInfoData = CupoyAPI()
				memberInfoData.mrscid = data_dict["mrscid"]
				memberInfo = memberInfoData.getMemberInfo()
				data_dict = dict(list(data_dict.items()))
				
		   

			#放入 array 中
			self.datalists.append(data_dict)
			
	# ----------------
	'''
	■=== 獲得新聞的使用者行為事件

	@param 
	@return
	'''
	# ----------------
	def getAi100Datalists(self):

		
		self.datalists = []

		

		#get data list
		rows = self.rawdata.get('rows', [])

		datalists = []

		for row in rows:

			#裝要儲存的資料
			data_dict = {}

			(dimensions_list,metric_list) = self.getRowTuple(row)

			#日期與小時
			data_dict["logdate"] = self.getDateType(dimensions_list[0])
			#data_dict["loghour"] = dimensions_list[1]

			
			#eventCategory
			data_dict["category"] = dimensions_list[1]
			
			#eventAction
			data_dict["action"] = dimensions_list[2]

			

			#eventLabel
			label_dict = self.convertStringToDict(dimensions_list[3])
			
			if "taskid" not in label_dict:
				data_dict["taskid"]= None
			else:
				data_dict["taskid"] = label_dict["taskid"]
			
			if "postid" not in label_dict:
				data_dict["postid"]= None
			else:
				data_dict["postid"] = label_dict["postid"]
			
			if "hwid" not in label_dict:
				data_dict["hwid"]= None
			else:
				data_dict["hwid"] = label_dict["hwid"]
								   

			#放入 array 中
			self.datalists.append(data_dict)
			
			


if __name__ == '__main__':

	pass

	