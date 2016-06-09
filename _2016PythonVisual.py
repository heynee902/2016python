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

itemElements = None


#####영화코드 저장 리스트
movieTop10 = []
movieTop10d = dict()

def parsingData(server, url, targetDt):
		conn = http.client.HTTPConnection(server)
		conn.request("GET",url + "&targetDt=" + str(targetDt))
		req = conn.getresponse()
		req.status
		req.reason
		return req.read().decode('utf-8')


def extractBookData(strXml, listWidget_box,listWidget_audi, listWidget_sales):
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
				
			if len(strTitle.text) > 0 :
				listWidget_box.addItem(str(rank.text)  + str("위 : ") + str(strTitle.text))
				listWidget_audi.addItem(str(audiAcc.text) + str("명"))
				listWidget_sales.addItem(str(salesAcc.text) + str("원"))

		for x in range(10): #사전에 리스트 넣어주기
			movieTop10d[x+1] = movieTop10[x]
			print("\n-----------------------------------------\n")
		for k,v in movieTop10d.items():
			print(k,"위 Code : ",v)     #시험 출력


#def extractBookData_2(strXml, listWidget_info):
#    global itemElements

#    tree = ElementTree.fromstring(strXml)
#    itemElements = tree.getiterator("movieInfo")  # return list type
#    itemElements2 = tree.getiterator("nation")
#    itemElements3 = tree.getiterator("genre")
#    itemElements4 = tree.getiterator("director")
#    itemElements5 = tree.getiterator("actor")
    
#    for item in itemElements:
#        strTitle = item.find("movieNm")
#        date = item.find("openDt")
#        runtime = item.find("showTm")

#    for item in itemElements2:
#        nation = item.find("nationNm")
#    for item in itemElements3:
#        genres = item.find("genreNm")
#    for item in itemElements4:
#        director = item.find("peopleNm")
        
#    if len(strTitle.text) > 0 :          
#		listWidget_info.addItem(str("영화 제목 : ") + str(strTitle.text))
#		listWidget_info.addItem(str("개봉 날짜 : ") + str(date.text))
#		listWidget_info.addItem(str("상영 시간 : ") + str(runtime.text) + str("분"))
#		listWidget_info.addItem(str("국적 : ") + str(nation.text))
#		listWidget_info.addItem(str("장르 : ") + str(genres.text))
#		listWidget_info.addItem(str("감독 : ") + str(director.text))

#    for item in itemElements5:
#            actor = item.find("peopleNm")    
#            if len(strTitle.text) > 0 :  
#                listWidget_info.addItem(str("배우 : ") + str(actor.text))
        
          

class MainWindow(QDialog, GUI.Ui_Dialog):
	def closeEvent(self, event):
	    reply = QMessageBox.question(self, '박스오피스 영화정보 서비스   ', "정말 종료할까요?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
	    if reply == QMessageBox.Yes:
	        event.accept() 
	    else:
	        event.ignore()      
	

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.pushButton_Search.clicked.connect(self.BtnClicked)
		self.pushButton_Exit.clicked.connect(self.BtnClicked)
	

	def BtnClicked(self):
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

		if sender.objectName() == "pushButton_Search":
			itemElements = parsingData(server,url,self.lineEdit_date.text())
			print(itemElements)
			extractBookData(itemElements, self.listWidget_box, self.listWidget_audi, self.listWidget_sales)
			pass


	def closeEvent(self, event):
		reply = QMessageBox.question(self, '박스오피스 상세정보 서비스', "정말 종료할까요?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
		    event.accept() 
		else:
		    event.ignore()      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
