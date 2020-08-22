from urllib.request import urlopen

from bs4 import BeautifulSoup
import json

# try:
from getDatalists.encryption import AESCBC
# except ModuleNotFoundError:
# 	from encryption import AESCBC

from datetime import datetime
import pytz

from urllib.parse import quote
import string

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# ----------------
'''
■=== 接收 url 獲得對應的 InfoData(datadict)，後再經過 getXXXXInfo() 篩選出所需的值

@param 
@return
'''
# ----------------
def getInfoData(url):

	try:
		#使用 urlopen 去開啟網址，獲得回傳的 response
		response = urlopen(url)

	except urllib.error.HTTPError:
		print("pass url : {}".format(url))

		#出現錯誤，先以空值取代
		return None

	#接著使用bs4去解析，得到bs4的object
	bs4_object = BeautifulSoup(response,features="html.parser")

	#將bs4的object轉為dict
	#參考 - https://stackoverflow.com/questions/19915010/python-beautiful-soup-how-to-json-decode-to-dict
	datadict = json.loads(str(bs4_object))

	return datadict

# ----------------
''' 
■=== AES 加密，用在 getAnswerInfo 與 getMemberInfo

加密前 答案ID
	Ilinke25567226 + YYYY-MM-DD(當天日期) + /answerid

加密前 會員ID
	Ilinke25567226 + YYYY-MM-DD(當天日期) + /mrscid

@param 
@return
'''
# ----------------
def AEStransform(itemid):

	#調整時區為 Taipei，並獲得執行當下的日期
	#參考 http://hant.ask.helplib.com/timezone/post_12256705
	utcmoment_naive = datetime.utcnow()
	utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
	localFormat ="%Y-%m-%d"
	tz = "Asia/Taipei"
	localDatetime = utcmoment.astimezone(pytz.timezone(tz))
	today = localDatetime.strftime(localFormat)

	#加密用的參數
	ilinkid = "Ilinke25567226"

	#新增加密用的物件
	aes = AESCBC()

	#將三個參數(ilinkid,當天日期],answerid/mrscid)組合起來
	before_encrypt_data = "{}{}/{}".format(ilinkid,today,itemid)

	#得到加密後結果
	after_encrypt_data = aes.encrypt(before_encrypt_data)

	return after_encrypt_data

# ----------------
''' 
■=== 傳入新聞大分類ID，獲得新聞大分類標題

@param 
@return
'''
# ----------------
def getNewsBucketGrpTitles(bucketgrpids):

	#當前大分類清單
	bucketgrptitle_dict = {}
	bucketgrptitle_dict["tech_tw"] = "科技"
	bucketgrptitle_dict["business_tw"] = "商業"
	bucketgrptitle_dict["life_tw"] = "生活"
	bucketgrptitle_dict["Game_tw"] = "遊戲"
	bucketgrptitle_dict["Sports_tw"] = "運動"
	bucketgrptitle_dict["design_tw"] = "設計"
	bucketgrptitle_dict["Reading_tw"] = "閱讀"
	bucketgrptitle_dict["3CExpert_tw"] = "3C達人"
	bucketgrptitle_dict["GamePlayer_tw"] = "御宅學園"
	bucketgrptitle_dict["Babyhome_tw"] = "親子家庭"
	bucketgrptitle_dict["Hipster_tw"] = "文青聚落"
	bucketgrptitle_dict["Fitness_tw"] = "健身瘦身"
	bucketgrptitle_dict["WhiteCollar_tw"] = "職場白領"
	bucketgrptitle_dict["InternationalFinance_tw"] = "國際財經"
	bucketgrptitle_dict["Hedonism_tw"] = "享樂女性"
	bucketgrptitle_dict["CityTour_tw"] = "城市食旅"


	bucketgrptitles = []

	for bucketgrpid in bucketgrpids:

		bucketgrptitle = bucketgrptitle_dict[bucketgrpid]

		bucketgrptitles.append(bucketgrptitle)

	return bucketgrptitles

# ========================================================
'''
■=== CupoyAPI以url形式，向後台取得資料，並得到reponse(回傳值)

包含function
	獲得新聞後台資訊 - getNewsInfo

	獲得問題後台資訊 - getQuestionInfo

	獲得答案後台資訊 - getAnswerInfo

	獲得書籍課程後台資訊 - getCumatrixInfo

	獲得書籍課程內容後台資訊 - getCumatrixItemInfo

	獲得每日精選後台資訊 - getHeadlineItemInfo

	獲得會員後台資訊 - getMemberInfo

'''
# ========================================================
class CupoyAPI():

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
	■=== 獲得新聞資訊，包含newstitle(新聞標題)、bucketgrpids(新聞大分類)、bucketids(新聞小分類)、influencerids(意見領袖ID)

	@param 
	@return
	'''
	# ----------------
	def getNewsInfo(self):

		#組合出調用api的url
		#queryUrl = "https://www.cupoy.com/MixNewsAction.do?op=getItem&itemid={}".format(self.newsid)
		queryUrl = "https://www.prerelease.cupoy.com/MixNewsAction.do?op=getItem&itemid={}".format(self.newsid)

		newsInfoData = getInfoData(queryUrl) #dict

		#TypeError: 'NoneType' object is not subscriptable
		if newsInfoData == None:
			return None


		newsInfo = {}

		try:
			newsid = newsInfoData["itemuid"]
		except KeyError:
			return None

		#獲得新聞的標題
		newsInfoData["title"]=newsInfoData["title"].replace("\n", "")
		newsInfo["newstitle"] = newsInfoData["title"]

		#獲得新聞的大分類
		try:
			newsInfo["bucketgrpids"] = newsInfoData["bucketgrpids"]
		except KeyError:
			newsInfo["bucketgrpids"] = ["empty"]

		#獲得新聞的大分類標題
		if newsInfo["bucketgrpids"] == ["empty"]:
			newsInfo["bucketgrptitles"] = ["空的"]

		else:
			newsInfo["bucketgrptitles"] = getNewsBucketGrpTitles(newsInfo["bucketgrpids"])

		#獲得新聞的小分類
		try:
			newsInfo["bucketids"] = newsInfoData["bucketids"]
		except KeyError:
			newsInfo["bucketids"] = ["empty"]	

		#獲得新聞的url，用於查詢意見領袖id
		newsurl = newsInfoData["linkurl"]

		#組合出調用api的url
		url = "https://www.cupoy.com/MixNewsAction.do?op=getSonarLog&itemid={}&linkurl={}&len=20".format(self.newsid,newsurl)
		
		#對包含中文字的網址做修正
		#https://blog.csdn.net/sijiaqi11/article/details/78449770
		url = quote(url,safe=string.printable)


		influencerData = getInfoData(url)

		try:
			#獲得意見領袖的資訊
			influencers = influencerData["influMap"]

			#擷取意見領袖的id
			influencerids = list(influencers.keys())

		except TypeError:
			influencerids = ["empty"]

		newsInfo["influencerids"] = influencerids

		return newsInfo

	# ----------------
	'''
	■=== 獲得問題資訊，包含qtitle(問題標題)、qtags(問題標籤)

	@param
	@return
	'''
	# ----------------
	def getQuestionInfo(self):

		#組合出調用api的url
		#queryUrl = "https://www.cupoy.com/KAsstQAAction.do?op=getQuestionContent&qid={}".format(self.qid)
		queryUrl = "https://www.prerelease.cupoy.com/KAsstQAAction.do?op=getQuestionContent&qid={}".format(self.qid)

		questionInfoData = getInfoData(queryUrl)

		#TypeError: 'NoneType' object is not subscriptable
		if questionInfoData == None:
			return None

		questionInfo = {}

		try:
			qid = questionInfoData["qid"]
			#獲得問題的標題
			questionInfo["qtitle"] = questionInfoData["title"]

		# 若沒有則回傳 None
		except KeyError:
			print("pass")
			return None

		#獲得問題的標籤
		try:
			questionInfo["qtags"] = questionInfoData["tags"]
		except KeyError:
			questionInfo["qtags"] = ["empty"]

		return questionInfo

	# ----------------
	'''
	■=== 獲得(知識特助中)答案資訊，包含answermrscid(回答者ID/新增答案者ID)

	@param 
	@return
	'''
	# ----------------
	def getAnswerInfo(self):

		token = AEStransform(self.answerid)

		#組合出調用api的url
		queryUrl = "https://www.prerelease.cupoy.com/GAAction.do?op=getKwAssistAnswerContent&token={}".format(token)

		# queryUrl = "https://www.cupoy.com/GAAction.do?op=getKwAssistAnswerContent&token={}".format(token)

		answerInfoData = getInfoData(queryUrl)

		#TypeError: 'NoneType' object is not subscriptable
		if answerInfoData == None:
			return None

		answerInfo = {}

		try:
			#獲得答案id
			answerid = answerInfoData["answerid"]

		# 若沒有則回傳 None
		except KeyError:
			return None

		answerInfo["answermrscid"] = answerInfoData["mrscid"]

		return answerInfo

	# ----------------
	'''
	■=== 獲得書籍課程資訊，包含posterid(策展人id)、cumatrixtitle(書籍課程標題)、cumatrixtags(書籍課程標籤)、groupids & cumatrixgrpids(書籍課程分類)

	@param 
	@return
	'''
	# ----------------
	def getCumatrixInfo(self):

		#組合出調用api的url
		#queryUrl = "https://www.cupoy.com/CumatrixAction.do?op=getCumatrix&cumatrixid={}".format(self.cumatrixid)
		queryUrl = "https://www.prerelease.cupoy.com/CumatrixAction.do?op=getCumatrix&cumatrixid={}".format(self.cumatrixid)

		cumatrixInfoData = getInfoData(queryUrl)

		#TypeError: 'NoneType' object is not subscriptable
		if cumatrixInfoData == None:
			return None

		cumatrixInfo = {}

		try:
			#獲得書籍課程策展人id
			cumatrixInfo["posterid"] = cumatrixInfoData["mrscid"]

		# 若沒有則回傳 None
		except KeyError:
			return None

		#獲得書籍課程的標題
		cumatrixInfoData["name"]=cumatrixInfoData["name"].replace("\n", "")
		cumatrixInfo["cumatrixtitle"] = cumatrixInfoData["name"]

		#獲得書籍課程的訂閱數
		cumatrixInfo["accSubscribeNum"] = cumatrixInfoData["followSize"]

		#獲得書籍課程的標籤
		try:
			cumatrixInfo["cumatrixtags"] = cumatrixInfoData["tags"]
		except KeyError:
			cumatrixInfo["cumatrixtags"] = ["empty"]

		if cumatrixInfo["cumatrixtags"] == []:
			cumatrixInfo["cumatrixtags"] = ["empty"]

		#獲得書籍課程的分類
		try:
			groupids = cumatrixInfoData["groupids"]
		except KeyError:
			groupids = []

		try:
			bucketids = cumatrixInfoData["bucketids"]
		except KeyError:
			bucketids = []

		cumatrixInfo["cumatrixgrpids"] = groupids + bucketids

		if cumatrixInfo["cumatrixgrpids"] == []:
			cumatrixInfo["cumatrixgrpids"] = ["empty"]

		return cumatrixInfo

	# ----------------
	'''
	■=== 獲得書籍課程內容資訊，包含cumatrixitemtitle(書籍課程內容標題)

	@param 
	@return
	'''
	# ----------------
	def getCumatrixItemInfo(self):

		cumatrixInfo = self.getCumatrixInfo()

		#沒有書籍課程資料則回傳None
		if cumatrixInfo == None:
			return None

		#組合出調用api的url
		#queryUrl = "https://www.cupoy.com/CumatrixItemAction.do?op=getCumatrixItem&cumatrixid={}&itemid={}".format(self.cumatrixid,self.cumatrixitemid)
		queryUrl = "https://www.prerelease.cupoy.com/CumatrixItemAction.do?op=getCumatrixItem&cumatrixid={}&itemid={}".format(self.cumatrixid,self.cumatrixitemid)

		cumatrixItemInfoData = getInfoData(queryUrl)

		cumatrixItemInfo = {}

		try:
			itemuid = cumatrixItemInfoData["itemuid"]

		# 若沒有則回傳 None
		except KeyError:
			return None

		#獲得書籍課程內容標題
		cumatrixItemInfoData["title"]=cumatrixItemInfoData["title"].replace("\n", "")
		cumatrixItemInfo["cumatrixitemtitle"] = cumatrixItemInfoData["title"]

		#去掉 \t 避免匯出的 csv 欄位出錯
		cumatrixItemInfo["cumatrixitemtitle"] = cumatrixItemInfo["cumatrixitemtitle"].replace("\t"," ")

		cumatrixItemInfo = dict(list(cumatrixInfo.items())+list(cumatrixItemInfo.items()))

		return cumatrixItemInfo

	# ----------------
	'''
	■=== 獲得(知識特助中)每日精選新聞資訊，包含headlineitemtitle(每日精選新聞標題)

	@param 
	@return
	'''
	# ----------------
	def getHeadlineItemInfo(self):

		#組合出調用api的url
		#queryUrl = "https://www.cupoy.com/KAsstHeadlineAction.do?op=getHeadlineItemInfo&itemuid={}".format(self.headlineitemid)
		queryUrl = "https://www.prerelease.cupoy.com/KAsstHeadlineAction.do?op=getHeadlineItemInfo&itemuid={}".format(self.headlineitemid)

		headlineItemInfoData = getInfoData(queryUrl)

		#TypeError: 'NoneType' object is not subscriptable
		if headlineItemInfoData == None:
			return None


		headlineItemInfo = {}

		try:
			itemuid = headlineItemInfoData["itemuid"]

		# 若沒有則回傳 None
		except KeyError:
			return None

		headlineItemInfoData["title"]=headlineItemInfoData["title"].replace("\n", "")
		headlineItemInfo["headlineitemtitle"] = headlineItemInfoData["title"]

		return headlineItemInfo

	# ----------------
	'''
	■=== 獲得會員資訊，包含membername(會員名稱)

	@param 
	@return
	'''
	# ----------------
	def getMemberInfo(self):

		token = AEStransform(self.mrscid)

		#組合出調用api的url
		queryUrl = "https://www.prerelease.cupoy.com/GAAction.do?op=getMemberInfo&token={}".format(token)
		
		memberInfoData = getInfoData(queryUrl)

		#TypeError: 'NoneType' object is not subscriptable
		if memberInfoData == None:
			return None

		memberInfo = {}

		try:
			memberInfo["mrscid"] = memberInfoData["mrscid"]

		# 若沒有則回傳 None
		except KeyError:

			print("mrscid-{} doesn't exist".format(self.mrscid))

			return None

		#獲得會員名稱
		memberInfo["mrsname"] = memberInfoData["membername"]

		#獲得會員email
		memberInfo["email"] = memberInfoData["email"]

		return memberInfo

	# ----------------
	'''
	■=== 獲得發文資訊，包含title(文章標題)

		發文功能不限分享新聞，故內容主要接收title為主

	@param 
	@return
	'''
	# ----------------
	def getPostNewsInfo(self):

		#組合出調用api的url
		queryUrl = "https://www.prerelease.cupoy.com/InfluencerAction.do?op=getItemContent&influid={}&itemid={}".format(self.mrscid,self.itemid)

		# queryUrl = "https://www.cupoy.com/InfluencerAction.do?op=getItemContent&influid={}&itemid={}".format(self.mrscid,self.itemid)

		postNewsInfoData = getInfoData(queryUrl)

		#TypeError: 'NoneType' object is not subscriptable
		if postNewsInfoData == None:
			return None

		postNewsInfo = {}

		try:
			influencerid = postNewsInfoData["influencerid"]

		# 若沒有則回傳 None
		except KeyError:
			return None

		try:
			#獲得發文title
			postNewsInfoData["title"]=postNewsInfoData["title"].replace("\n", "")
			postNewsInfo["title"] = postNewsInfoData["title"]
		except KeyError:
			postNewsInfo["title"] = "empty"


		return postNewsInfo

	# ----------------
	'''
	■=== 取得特助資訊，包含subscribersize(訂閱數)

	@param 
	@return
	'''
	# ----------------
	def getKwAssistInfo(self):

		#組合出調用api的url
		#queryUrl = "https://www.cupoy.com/KwAssistAction.do?op=getKwAssistInfo&assistid={}".format(self.assistid)
		queryUrl = "https://www.prerelease.cupoy.com/KwAssistAction.do?op=getKwAssistInfo&assistid={}".format(self.assistid)
		
		kwAssistInfoData = getInfoData(queryUrl)

		#TypeError: 'NoneType' object is not subscriptable
		if kwAssistInfoData == None:
			return None

		kwAssistInfo = {}

		try:
			assistid = kwAssistInfoData["assistid"]

		# 若沒有則回傳 None
		except KeyError:
			return None

		#獲得subscribersize(特助訂閱數)
		kwAssistInfo["subscribersize"] = kwAssistInfoData["subscribersize"]

		return kwAssistInfo

if __name__ == '__main__':

	# newsInfoData = CupoyAPI()

	# newsInfoData.newsid = "68747470733A2F2F7777772E65766572796461796865616C74682E636F6D2E74772F61727469636C652F31373130313F6662636C69643D497741523037335977704D4156516431384D337575763145527034504E49396B39356C72496D346B3547393957344B465531703144476E6D5771613349"

	# newsInfo = newsInfoData.getNewsInfo()

	# print("newsInfo - type : {}".format(type(newsInfo)))

	# print(newsInfo)


	# questionInfoData = CupoyAPI()

	# questionInfoData.qid = "0000016B78FAEB95000000156375706F795F72656C656173655155455354"

	# questionInfo = questionInfoData.getQuestionInfo()

	# print("questionInfo - type : {}".format(type(questionInfo)))

	# print(questionInfo)


	# cumatrixInfoData = CupoyAPI()

	# cumatrixInfoData.cumatrixid = "00000165AD08BC70000000026375706F795F70726572656C656173654355"

	# cumatrixInfo = cumatrixInfoData.getCumatrixInfo()

	# print("cumatrixInfo - type : {}".format(type(cumatrixInfo)))

	# print(cumatrixInfo)


	# cumatrixItemInfoData = CupoyAPI()

	# cumatrixItemInfoData.cumatrixid = "0000015B4CAE3332000000036375706F795F72656C656173654355"

	# cumatrixItemInfoData.cumatrixitemid = "0000015EDC37D4CD000000106375706F795F72656C656173654349"

	# cumatrixItemInfo = cumatrixItemInfoData.getCumatrixItemInfo()

	# print("cumatrixItemInfo - type : {}".format(type(cumatrixItemInfo)))

	# print(cumatrixItemInfo)


	# headlineItemInfoData = CupoyAPI()

	# headlineItemInfoData.headlineitemid = "0000016B75A06915000000106375706F795F70726572656C656173655F696F737276484541444C494E454954454D"

	# headlineItemInfo = headlineItemInfoData.getHeadlineItemInfo()

	# print("headlineItemInfo - type : {}".format(type(headlineItemInfo)))

	# print(headlineItemInfo)


	# answerInfoData = CupoyAPI()

	# answerInfoData.answerid = "0000016BBE0A41A0000000AE6375706F795F72656C65617365414E53"

	# answerInfo = answerInfoData.getAnswerInfo()

	# print("answerInfo - type : {}".format(type(answerInfo)))

	# print(answerInfo)


	# memberInfoData = CupoyAPI()

	# memberInfoData.mrscid = "C3411361"

	# memberInfo = memberInfoData.getMemberInfo()

	# print("memberInfo - type : {}".format(type(memberInfo)))

	# print(memberInfo)


	postNewsInfoData = CupoyAPI()

	postNewsInfoData.mrscid = "A4910200"

	postNewsInfoData.itemid = "0000016A339B0027000000016375706F795F72656C65617365494E455753"

	postNewsInfo = postNewsInfoData.getPostNewsInfo()

	print("postNewsInfo - type : {}".format(type(postNewsInfo)))

	print(postNewsInfo)