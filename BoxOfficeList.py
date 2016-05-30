# -*- coding: utf-8 -*-
from xml.etree import ElementTree

from http.client import HTTPConnection
loopFlag = 1
xmlFD = -1

##global
conn = None
regKey = 'bb48880c629b0289e1b1fea9d38c09a5'
# 박스오피스 OpenAPI 접속 정보 information
server = "kobis.or.kr"
itemElements = None


######
movieTop10 = []
movieTop10d = dict()

def userURIBuilder(server,**user):  #**은 사전형식으로 반환?해주는
    str = "http://" + server + "/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)
    
    
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
        dictMovieData(req.read())
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
           print(date.text,"위 : ",strTitle.text)
           
def dictMovieData(strXml):
    global movieTop10, movieTop10d, itemElements    
    tree = ElementTree.fromstring(strXml)

    itemElements = tree.getiterator("dailyBoxOffice")  # return list type

    for item in itemElements:
        movieCd = item.find("movieCd").text     #movieCd를 찾아서 movieCd에넣어줌
        movieTop10.append(movieCd)      #리스트에 넣는다
    
    for x in range(10): #사전에 리스트 넣어주기
        movieTop10d[x+1] = movieTop10[x]
        
    for k,v in movieTop10d.items():
        print(k,". ",v)     #시험 출력


#### Menu  implementation
def printMenu():
    connectOpenAPIServer()
    print("\nWelcome! BoxOffice Movie Manager Program (xml version)") 
    print("========Menu==========")
    print("Quit program: q")
    print("print movie list: p")
    print("sEarch Daily BoxOffice list: e")
    print("Search movieCd: c")
    print("==================")
    
def launcherFunction(menu):
    global itemElements

    if menu == 'e':
        date = str(input ('조회할 날짜 입력(yyyymmdd):'))
        getBookDataFromISBN(date)
      #  printBookList(SearchBookTitle(keyword))
    elif menu == 'p':
        print(itemElements)
    elif menu == 'c':
        keyword = str(input ('input keyword to search :'))
        SearchBookTitle(keyword)
    elif menu == 'q':
        QuitBookMgr()
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
#    if not checkDocument():
 #       return None
    retlist = []
        
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    
    itemElements = tree.getiterator(keyword)  # return list type
    for item in itemElements:
        strTitle = item.find("movieNm").text
        if len(strTitle.text) > 0 :
           print(strTitle.text,": ",item.attrib["movieCd"].text)
    return retlist
    
    
                   
def printBookList(retlist):
    for res in retlist:
        print (res)
        
        
def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    
##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")