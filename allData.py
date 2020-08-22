from getDatalists.allDatalists import AllDatalists
from getRawdata.allRawData import AllRawData
import contentutil

class Alldata():
	
	def __init__(self):
			pass
	
	
	# ----------------
	'''
	■=== 輸出GA儲存的埋code新聞資料
	
	@param 
	@return
	'''
	# ----------------
	def outputData(self,start_date,end_date):
	
		allRawdata = AllRawData()
	
		#查詢時間區間
		allRawdata.start_date = start_date
		allRawdata.end_date = end_date
		
		viewRawdata = allRawdata.getViewRawdata()
		self.outputViewDb(viewRawdata,start_date)
		
		newsRawdata = allRawdata.getNewsRawdata()
		self.outputNewsDb(newsRawdata,start_date)
		
		influencerRawdata = allRawdata.getInfluencerRawdata()
		self.outputInfluencerDb(influencerRawdata,start_date)
		
		kwAssistRawdata = allRawdata.getkwAssistRawdata()
		self.outputKwAssistDb(kwAssistRawdata,start_date)
		
		cumatrixRawdata = allRawdata.getCumatrixRawdata()
		self.outputcumatrixDb(cumatrixRawdata,start_date)
		
		memberRawdata = allRawdata.getMerberRawdata()
		self.outputmemberDb(memberRawdata,start_date)
		
		ai100Rawdata = allRawdata.getAi100Rawdata()
		self.outputai100Db(ai100Rawdata,start_date)		
		
	
	
	# ----------------
	"""
	
	測試mongo連線
	
	"""
	def outputViewDb(self,viewRawdata,start_date):
	
		db = contentutil.MONGO_DBNAME
	
		collection = "GAViewLog"
		
		log_message = "===== Start Output ViewData to Mongo db : {} =====".format(db)
		contentutil.printlog(log_message)
	
		allDatalists = AllDatalists()
	
		allDatalists.rawdata = viewRawdata
	
		allDatalists.getViewDatalists()
	
		allDatalists.send_datalists_to_mongo(db,collection)
		
		
	def outputNewsDb(self,newsRawdata,start_date):
	
		db = contentutil.MONGO_DBNAME
	
		collection = "GANewsLog"
		
		log_message = "===== Start Output NewsData to Mongo db : {} =====".format(db)
		contentutil.printlog(log_message)
	
		allDatalists = AllDatalists()
	
		allDatalists.rawdata = newsRawdata
	
		allDatalists.getNewsDatalists()
	
		allDatalists.send_datalists_to_mongo(db,collection)
	
	
	def outputKwAssistDb(self,kwAssistRawdata,start_date):
	
		db = contentutil.MONGO_DBNAME
	
		collection = "GAKwAssistLog"
		
	
	
		log_message = "===== Start Output KwAssistData to Mongo db : {} =====".format(db)
		contentutil.printlog(log_message)
	
		allDatalists = AllDatalists()
	
		allDatalists.rawdata = kwAssistRawdata
	
		allDatalists.getkwAssistDatalists()
	
		allDatalists.send_datalists_to_mongo(db,collection)
	
	def outputInfluencerDb(self,influencerRawdata,start_date):
	
		db = contentutil.MONGO_DBNAME
	
		collection = "GAInfluencerLog"
	
		log_message = "===== Start Output InfluencerData to Mongo db : {} =====".format(db)
		contentutil.printlog(log_message)
	
		allDatalists = AllDatalists()
	
		allDatalists.rawdata = influencerRawdata
	
		allDatalists.getinfluencerDatalists()
	
		allDatalists.send_datalists_to_mongo(db,collection)
	
		
	def outputcumatrixDb(self,cumatrixRawdata,start_date):
	
		db = contentutil.MONGO_DBNAME
	
		collection = "GACumatrixLog"
		
		
	
		log_message = "===== Start Output CumatrixData to Mongo db : {} =====".format(db)
		contentutil.printlog(log_message)
	
		allDatalists = AllDatalists()
	
		allDatalists.rawdata = cumatrixRawdata
	
		allDatalists.getCumatrixDatalists()
	
		allDatalists.send_datalists_to_mongo(db,collection)
	
	def outputmemberDb(self,memberRawdata,start_date):
	
		db = contentutil.MONGO_DBNAME
	
		collection = "GAMemberLog"
		
		
	
		log_message = "===== Start Output MemberData to Mongo db : {} =====".format(db)
		contentutil.printlog(log_message)
	
		allDatalists = AllDatalists()
	
		allDatalists.rawdata = memberRawdata
	
		allDatalists.getMemberDatalists()
	
		allDatalists.send_datalists_to_mongo(db,collection)
	
	
	def outputai100Db(self,ai100Rawdata,start_date):
	
		db = contentutil.MONGO_DBNAME
	
		collection = "GAAI100Log"
		
		
	
		log_message = "===== Start Output Ai100Data to Mongo db : {} =====".format(db)
		contentutil.printlog(log_message)
	
		allDatalists = AllDatalists()
	
		allDatalists.rawdata = ai100Rawdata
	
		allDatalists.getAi100Datalists()
	
		allDatalists.send_datalists_to_mongo(db,collection)
		
		
		