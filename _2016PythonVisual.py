# -*- coding: utf-8 -*-
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

import sys
import urllib
import time

import sys
from PyQt5 import QtWidgets

import urllib
import http.client


loopFlag = 1
xmlFD = -1
BooksDoc = None

##global
conn = None
regKey = 'bb48880c629b0289e1b1fea9d38c09a5'
# 박스오피스 OpenAPI 접속 정보 information
server = "kobis.or.kr"
itemElements = None


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    button = QtWidgets.QPushButton("Hello world")
    window.setCentralWidget(button)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()


#### Menu  implementation
def printMenu():
	print("\nWelcome! BoxOffice Movie Manager Program (xml version)") 
	print("========Menu==========")
	print("Quit program: q")
	print("print movie list: p")
	print("sEarch Daily BoxOffice list: e")
	print("Search movieCd: c")
	print("==================")
	
def userURIBuilder(server,**user):  #**은 사전형식으로 반환?해주는
	str = "http://" + server + "/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml" + "?"
	for key in user.keys():
		str += key + "=" + user[key] + "&"
	return str


def connectOpenAPIServer():
	global conn, server
	conn = HTTPConnection(server)

def API(server, url):
    conn = http.client.HTTPConnection(server)
    conn.request("GET",url)
    req = conn.getresponse()
    req.status
    req.reason
    return req.read().decode('utf-8')


def getBookDataFromISBN(date):
	global server, regKey, conn, req
	if conn == None :
		connectOpenAPIServer()
	uri = userURIBuilder(server, key=regKey, targetDt=date)
	conn.request("GET", uri)

	req = conn.getresponse()
	print (req.status)
	if int(req.status) == 200 :
		print("BoxOffice data downloading complete!")
		extractBookData(req.read())
	else:
		print("OpenAPI request has been failed!! please retry")
		return None


def extractBookData(strXml):
	global itemElements
	tree = ElementTree.fromstring(strXml)
	itemElements = tree.getiterator("dailyBoxOffice")  # return list type
	for item in itemElements:
		date = item.find("rank")
		strTitle = item.find("movieNm")
		if len(strTitle.text) > 0 :
			print(date.text,"위 : ", strTitle.text)


def launcherFunction(menu):
	global BooksDoc  
	global itemElements

	if menu == 'e':
		date = str(input ('조회할 날짜 입력(yyyymmdd):'))
		getBookDataFromISBN(date)
	  #  printBookList(SearchBookTitle(keyword))
#    elif menu == 'p':
#        print(itemElements)
	elif menu == 'c':
		keyword = str(input ('input keyword to search :'))
		printBookList(SearchBookTitle(keyword)) 
	else:
		print ("error : unknow menu key")

 
def PrintBookList(tags):
	global BooksDoc
#    if not checkDocument():
 #      return None
    
	booklist = BooksDoc.childNodes
	book = booklist[0].childNodes
	for item in book:
		if item.nodeName == "dailyBoxOffice":
			subitems = item.childNodes
			for atom in subitems:
			   if atom.nodeName in tags:
				   print("title=",atom.firstChild.nodeValue)
               
               
def SearchBookTitle(keyword):
	global BooksDoc
	retlist = []
#    if not checkDocument():
 #       return None
    
	try:
		tree = ElementTree.fromstring(str(BooksDoc.toxml()))
	except Exception:
		print ("Element Tree parsing Error : maybe the xml document is not corrected.")
		return None

	itemElements = tree.getiterator("movieNm")  # return list type
	for item in itemElements:
		strTitle = item.find("movieNm")
		if (strTitle.text.find(keyword) >=0 ):
			retlist.append((item.attrib["movieCd"], strTitle.text))

	return retlist


               
def printBookList(retlist):
	for res in retlist:
		print (res)
    
    
		"""
def checkDocument():
	global BooksDoc
	if BooksDoc == None:
		print("Error : Document is empty")
		return False
	return True
    
		"""
    
    
##### run #####
while(loopFlag > 0):
	printMenu()
	menuKey = str(input ('select menu :'))
	launcherFunction(menuKey)
else:
	print ("Thank you! Good Bye")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.setWindowIcon(QIcon('./Img/main_icon.png'))
    form.show()
    sys.exit(app.exec_())
