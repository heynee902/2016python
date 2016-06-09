# -*- coding: utf-8 -*-
from xml.etree import ElementTree
from http.client import HTTPConnection

import sys
import urllib
import time
import http.client

import GUI
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

loopFlag = 1
xmlFD = -1
##global
conn = None
regKey = 'bb48880c629b0289e1b1fea9d38c09a5'

# 박스오피스 OpenAPI 접속 정보 information
server = "kobis.or.kr"
url = "/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=4fcb6abebdbbbd59800be590e10cdc23"
url2 = "/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml?key=4fcb6abebdbbbd59800be590e10cdc23"
itemElements = None
itemElements1 = None #영화상세정보
itemElements2 = None
itemElements3 = None
itemElements4 = None
itemElements5 = None

#####영화코드 저장 리스트
movieTop10 = []
movieTop10d = dict()

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
#--------------------파싱함수-------------------------------------


#--------------------데이터 골라내는함수-------------------------------------
def extractBookData(strXml, listWidget_box, listWidget_audi, listWidget_sales, listWidget_info): 
	global itemElements    

	tree = ElementTree.fromstring(strXml)
	itemElements = tree.getiterator("dailyBoxOffice")  # return list type
	movieTop10.clear()

	listWidget_box.clear()	#검색할때마다 초기화할려고
	listWidget_audi.clear()
	listWidget_sales.clear()

	for item in itemElements:
		rank = item.find("rank")
		strTitle = item.find("movieNm")
		movieCd = item.find("movieCd").text     #movieCd를 찾아서 movieCd에넣어줌
		audiAcc = item.find("audiAcc")
		salesAcc = item.find("salesAcc")
		movieTop10.append(movieCd)      #리스트에 넣는다

		listWidget_box.addItem(str(rank.text)  + str("위 : ") + str(strTitle.text))
		listWidget_audi.addItem(str(audiAcc.text) + str("명"))
		listWidget_sales.addItem(str(salesAcc.text) + str("원"))

	for x in range(10): #사전에 리스트 넣어주기
		movieTop10d[x+1] = movieTop10[x]
		print("\n-----------------------------------------\n")
	for k,v in movieTop10d.items():
		print(k,"위 Code : ",v)     #시험 출력

#extractBookData1~5()는 영화상세정보 따로 파싱해야되서 나눴음 ㅠ
def extractBookData1(strXml, listWidget_info):
	global itemElements1

	tree = ElementTree.fromstring(strXml)
	itemElements1 = tree.getiterator("movieInfo")  # return list type

	for item in itemElements1:
		strTitle = item.find("movieNm")
		date = item.find("openDt")
		runtime = item.find("showTm")

		listWidget_info.addItem(str("영화 제목 : ") + str(strTitle.text))
		listWidget_info.addItem(str("개봉 날짜 : ") + str(date.text))
		listWidget_info.addItem(str("상영 시간 : ") + str(runtime.text) + str("분"))

def extractBookData2(strXml, listWidget_info):
	global itemElements2
	tree = ElementTree.fromstring(strXml)
	itemElements2 = tree.getiterator("nation")

	for item in itemElements2:
		nation = item.find("nationNm")
		listWidget_info.addItem(str("국적 : ") + str(nation.text))



def extractBookData3(strXml, listWidget_info):
	global itemElements3
	tree = ElementTree.fromstring(strXml)
	itemElements3 = tree.getiterator("genre")

	for item in itemElements3:
		genres = item.find("genreNm")
		listWidget_info.addItem(str("장르 : ") + str(genres.text))

def extractBookData4(strXml, listWidget_info):
	global itemElements4
	tree = ElementTree.fromstring(strXml)
	itemElements4 = tree.getiterator("director")

	for item in itemElements4:
		director = item.find("peopleNm")
		listWidget_info.addItem(str("감독 : ") + str(director.text))

def extractBookData5(strXml, listWidget_info):
	global itemElements5

	tree = ElementTree.fromstring(strXml)
	itemElements5 = tree.getiterator("actor")
	
	for item in itemElements5:
		actor = item.find("peopleNm")
		listWidget_info.addItem(str("배우 : ") + str(actor.text))
#--------------------데이터 골라내는함수-------------------------------------


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
		self.listWidget_box.clicked.connect(self.BtnClicked) 
	
	def BtnClicked(self): #클릭 받아서 넣는 곳
		sender = self.sender()
		###########################################
		# 탭을 클릭할 경우와 갱신 버튼을 누를경우 currentIndex가 정상적으로 작동하지 않는다.
		# 그걸 방지하기 위해 indexBox를 만들어 미리 오류처리를 여기서 해결한다.
		indexBox = ""
		try:
			indexBox = sender.currentIndex()
		except:
			indexBox = 0
		###########################################

		if sender.objectName() == "pushButton_Search":	#검색버튼 눌렸을 때
			itemElements = parsingData(server,url,self.lineEdit_date.text()) #파싱함수에서 데이터 받아온다
			print(itemElements)
			extractBookData(itemElements, self.listWidget_box, self.listWidget_audi, self.listWidget_sales, self.listWidget_info)
			pass
		
		if sender.objectName() == "listWidget_box": #박스오피스 리스트 내 클릭
			self.listWidget_info.clear()
			#itemElements1~5 영화상세정보 데이터 받아오기
			itemElements1 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			itemElements2 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			itemElements3 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			itemElements4 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			itemElements5 = parsingData2(server,url2,movieTop10[self.listWidget_box.currentRow()])  #파싱함수에서 데이터 받아온다
			
			extractBookData1(itemElements1, self.listWidget_info)
			extractBookData2(itemElements2, self.listWidget_info)
			extractBookData3(itemElements3, self.listWidget_info)
			extractBookData4(itemElements4, self.listWidget_info)
			extractBookData5(itemElements5, self.listWidget_info)
			pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
