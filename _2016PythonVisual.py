# -*- coding: utf-8 -*-
from xml.etree import ElementTree
from http.client import HTTPConnection
from urllib.request import urlopen

import sys
import urllib
import urllib.request
import string
import codecs
import time
import http.client

import GUI
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

loopFlag = 1
xmlFD = -1
##global
conn = None

# 박스오피스 OpenAPI 접속 정보 information
server = "kobis.or.kr"
server_p = "movie.naver.com"

url = "/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=4fcb6abebdbbbd59800be590e10cdc23"
url2 = "/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml?key=4fcb6abebdbbbd59800be590e10cdc23"
url_p = "/movie/search/result.nhn?section=all&ie=utf8&query="
itemElements = None
itemElements1 = None #영화상세정보
itemElements2 = None
itemElements3 = None
itemElements4 = None
itemElements5 = None
itemElements_p = None #영화포스터

#####영화코드 저장 리스트
movieTop10 = []

movieList = []

MovieData = []
BoxData = [0,]


def urlencode(string):
    # URL 인코딩
    return urllib.parse.quote(string)

#--------------------파싱함수-------------------------------------
def parsingData(server, url, targetDt):		#박스오피스 파싱함수
	conn = http.client.HTTPConnection(server)
	conn.request("GET",url + "&targetDt=" + str(targetDt))
	req = conn.getresponse()
	req.status
	req.reason
	return req.read().decode('utf-8')

def parsingData2(server, url2, movieCd):		#영화상세정보 파싱함수
	conn = http.client.HTTPConnection(server)
	conn.request("GET",url2 + "&movieCd=" + str(movieCd))
	req = conn.getresponse()
	req.status
	req.reason
	return req.read().decode('utf-8')

def parsingData_p(server_p, url_p, listWidget_box):		#영화포스터 파싱함수
	global movieList
	
	conn = http.client.HTTPConnection(server_p)
	conn.request("GET", url_p + urlencode(str(movieList[listWidget_box.currentRow()])))


	req = conn.getresponse()
	req.status
	req.reason
	data = ""
	data = req.read().decode("euc-kr") 
	
	p1 = data.find("<p class=\"result_thumb\">") + 26 # 현재 위치를 나타내 주는 글자의 위치를 구한다.

	data = data[p1:p1 + 1000] # 해당 글자 위치에서 1000글자를 data에 넣는다.
	p2 = data.find("width=")
	
	urldata = str( data[:p2].split())



	p1 = urldata.find("http://")  # 현재 위치를 나타내 주는 글자의 위치를 구한다.
	urldata = urldata[p1:p1 + 1000] # 해당 글자 위치에서 1000글자를 data에 넣는다.
	p2 = urldata.find("?type=f67\"")


	print(str(urldata[:p2].split()))

	return str(urldata[:p2].split())



#--------------------파싱함수-------------------------------------


#--------------------데이터 골라내는함수-------------------------------------
def extractMovieData(strXml, listWidget_box, listWidget_audi, listWidget_sales, listWidget_info): 
	global itemElements    

	tree = ElementTree.fromstring(strXml)
	itemElements = tree.getiterator("dailyBoxOffice")  # return list type
	movieTop10.clear()

	listWidget_box.clear()	#검색할때마다 초기화할려고
	listWidget_audi.clear()
	listWidget_sales.clear()
	movieList.clear()
	BoxData.clear()
	BoxData.append(0)
	
	for item in itemElements:
		rank = item.find("rank")
		strTitle = item.find("movieNm")
		movieCd = item.find("movieCd").text     #movieCd를 찾아서 movieCd에넣어줌
		audiAcc = item.find("audiAcc")
		salesAcc = item.find("salesAcc")
		movieTop10.append(movieCd)      #리스트에 넣는다
		movieList.append(str(strTitle.text)) #제목리스트

		listWidget_box.addItem(str(rank.text)  + str("위 : ") + str(strTitle.text))
		listWidget_audi.addItem(str(audiAcc.text) + str("명"))
		listWidget_sales.addItem(str(salesAcc.text) + str("원"))
		BoxData.append(rank.text + "위:" + strTitle.text)
		

#extractMovieData1~5()는 영화상세정보 따로 파싱해야되서 나눴음 ㅠ
def extractMovieData1(strXml, listWidget_info):
	global itemElements1

	tree = ElementTree.fromstring(strXml)
	itemElements1 = tree.getiterator("movieInfo")  # return list type

	MovieData.clear()

	for item in itemElements1:
		strTitle = item.find("movieNm")
		date = item.find("openDt")
		runtime = item.find("showTm")

		listWidget_info.addItem(str("영화 제목 : ") + str(strTitle.text))
		listWidget_info.addItem(str("개봉 날짜 : ") + str(date.text))
		listWidget_info.addItem(str("상영 시간 : ") + str(runtime.text) + str("분"))
		MovieData.append('영화 제목: ' + strTitle.text)
		MovieData.append('개봉 날짜: '+ date.text)
		MovieData.append('상영 시간: ' + runtime.text + '분')

def extractMovieData2(strXml, listWidget_info):
	global itemElements2
	tree = ElementTree.fromstring(strXml)
	itemElements2 = tree.getiterator("nation")

	for item in itemElements2:
		nation = item.find("nationNm")
		listWidget_info.addItem(str("국적 : ") + str(nation.text))
		MovieData.append('국적: ' + nation.text)

def extractMovieData3(strXml, listWidget_info):
	global itemElements3
	tree = ElementTree.fromstring(strXml)
	itemElements3 = tree.getiterator("genre")

	for item in itemElements3:
		genres = item.find("genreNm")
		listWidget_info.addItem(str("장르 : ") + str(genres.text))
		MovieData.append('장르: ' + genres.text)

def extractMovieData4(strXml, listWidget_info):
	global itemElements4
	tree = ElementTree.fromstring(strXml)
	itemElements4 = tree.getiterator("director")

	for item in itemElements4:
		director = item.find("peopleNm")
		listWidget_info.addItem(str("감독 : ") + str(director.text))
		MovieData.append('감독: ' + director.text)

def extractMovieData5(strXml, listWidget_info):
	global itemElements5

	tree = ElementTree.fromstring(strXml)
	itemElements5 = tree.getiterator("actor")
	
	for item in itemElements5:
		actor = item.find("peopleNm")
		listWidget_info.addItem(str("배우 : ") + str(actor.text))
		MovieData.append('배우: ' + actor.text)

def extractMovieData6(strXml, Label_poster):

	urldata = strXml.replace("\'", "")
	urldata = urldata.replace("[", "")
	urldata = urldata.replace("]", "")

	print(str(urldata))
	
	if str(urldata).find(".gif") >= 0:
		Label_poster.setText("포스터가 없습니다.")
		pass
	elif urldata != '':
		full_name =  str("poster") + ".jpg"
		urllib.request.urlretrieve(str(urldata), full_name)
		Label_poster.setPixmap(QPixmap("poster.jpg"))
		Label_poster.setScaledContents(True)

	MovieData.append('포스터URL: ' + str(urldata))

#--------------------데이터 골라내는함수-------------------------------------


#--------------------메일 보내는 함수----------------------------------------
def sendMail(senderAddr, passwd, recipientAddr, title, date, urldata):
	global host, port
	html = ""

	html = MakeHtmlDoc(date)

	import mysmtplib
	# MIMEMultipart의 MIME을 생성합니다.
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	#Message container를 생성합니다.
	msg = MIMEMultipart('alternative')
	#msgtext = listWidget_info

	#set message
	msg['Subject'] = title
	msg['From'] = senderAddr
	msg['To'] = recipientAddr

	msgPart = MIMEText('y', 'plain')
	moviePart = MIMEText(html, 'html', _charset = 'UTF-8')

	# 메세지에 생성한 MIME 문서를 첨부합니다.
	msg.attach(msgPart)
	msg.attach(moviePart)

	print ("connect smtp server ... ")
	s = mysmtplib.MySMTP(host,port)
	s.set_debuglevel(1)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(senderAddr, passwd)    # 로긴을 합니다. 
	s.sendmail(senderAddr , [recipientAddr], msg.as_string())
	s.close()

	print ("Mail sending complete!!!")



def MakeHtmlDoc(date):
    from xml.dom.minidom import getDOMImplementation
    impl = getDOMImplementation()
    
    newdoc = impl.createDocument(None, "html", None)  #DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    br = newdoc.createElement('br')
    body.appendChild(br)
    for boxitem in BoxData:
        if boxitem == 0:
            b = newdoc.createElement('b')
            dateText = newdoc.createTextNode("<날짜 " + date + " 의 박스오피스 순위>")
            b.appendChild(dateText)
            body.appendChild(b)
        else:
            b = newdoc.createElement('b')
            boxText = newdoc.createTextNode(boxitem)
            b.appendChild(boxText)
            body.appendChild(b)
        br = newdoc.createElement('br')
        body.appendChild(br)
    
    br = newdoc.createElement('br')
    body.appendChild(br)
    info = newdoc.createElement('info')
    infoText = newdoc.createTextNode("<영화 상세정보>")
    body.appendChild(infoText)
    br = newdoc.createElement('br')
    body.appendChild(br)
    for movieitem in MovieData:
        q = newdoc.createElement('q')
        titleText = newdoc.createTextNode(movieitem)
        body.appendChild(titleText)
        br = newdoc.createElement('br')
        body.appendChild(br)

    top_element.appendChild(body)

    return newdoc.toxml()

#--------------------메일 보내는 함수----------------------------------------




class MainWindow(QDialog, GUI.Ui_Dialog):
	def closeEvent(self, event):
		reply = QMessageBox.question(self, '    박스오피스 상세정보 서비스     ', "\n종료하시겠습니까?\n", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept() 
		else:
			event.ignore()      


	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.pushButton_Search.clicked.connect(self.BtnClicked)	#버튼 클릭되면 연결해라
		self.pushButton_Exit.clicked.connect(self.BtnClicked)
		self.pushButton.clicked.connect(self.BtnClicked)
		self.listWidget_box.clicked.connect(self.BtnClicked)

		self.label_post.setPixmap(QPixmap('post.png'))
		self.label_post.setScaledContents(True)
		self.label_box.setPixmap(QPixmap('box.jpg'))
		self.label_box.setScaledContents(True)
	
	def BtnClicked(self): #클릭 받아서 넣는 곳
		sender = self.sender()

		indexBox = ""
		try:
			indexBox = sender.currentIndex()
		except:
			indexBox = 0

		if sender.objectName() == "pushButton_Search":	#검색버튼 눌렸을 때
			itemElements = parsingData(server,url,self.lineEdit_date.text()) #파싱함수에서 데이터 받아온다
			print(itemElements)
			extractMovieData(itemElements, self.listWidget_box, self.listWidget_audi, self.listWidget_sales, self.listWidget_info)
			pass
		
		if sender.objectName() == "listWidget_box": #박스오피스 리스트 내 클릭
			self.listWidget_info.clear()
			self.Label_poster.clear()
			#itemElements1~5 영화상세정보 데이터 받아오기
			itemElements1 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			itemElements2 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			itemElements3 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			itemElements4 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			itemElements5 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			

			extractMovieData1(itemElements1, self.listWidget_info)
			extractMovieData2(itemElements2, self.listWidget_info)
			extractMovieData3(itemElements3, self.listWidget_info)
			extractMovieData4(itemElements4, self.listWidget_info)
			extractMovieData5(itemElements5, self.listWidget_info)
			itemElements_p = ""
			itemElements_p = parsingData_p(server_p, url_p, self.listWidget_box)
			extractMovieData6(itemElements_p, self.Label_poster)
			pass
		
		if sender.objectName() == "pushButton":    #메일보내기 버튼 눌렀을 때
			sendMail(self.lineEdit_mail_ID.text(), self.lineEdit_mail_PW.text(), self.lineEdit_mail_address.text(), self.lineEdit_mail_address_2.text(), self.lineEdit_date.text())
			pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


