import urllib
import urllib2
import re
from datetime import datetime

def mainProcess():
	html = getHTML()
	storeHTML(html,"html")
	# print html
	sectionlist = parseHTML(html)
	print sectionlist
	# storeHTML(sectionlist[0],"txt")

	infolist = getSubInfo(sectionlist[0])
	resInfoList=[]
	for item in infolist:
		resItem = str(item).replace('\n','').replace(' ','')
		resInfoList.append(resItem)
		# storeHTML(resItem,"txt")

	result = getFinalRes(resInfoList)

	storeList(result,"result")

	return 'success'

def getHTML():
	url = "http://www.ishadowsocks.com/"
	headers = { #Grab disguised as a browser
	    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36'
	    }
	req = urllib2.Request(url,headers=headers)
	page = "";

	#record current time
	ft = file("log.tmp","w")
	curtime = str(datetime.now())
	ft.write(curtime+'\n')
	ft.close()

	try:
	    page = urllib2.urlopen(req)
	    html = page.read()
	    return html
	except:
	    print "getHtml: "+url+" error"

def storeHTML(html,suffix):
	curtime = datetime.now()

	tmpHTMLFileName = str(curtime)[0:-3]+"."+suffix
	tmpHTMLFileName = tmpHTMLFileName.replace(':','.')
	tmpHTMLFileName = tmpHTMLFileName.replace('-','_')
	print tmpHTMLFileName

	#record that time page..
	ft = file(str(tmpHTMLFileName),"w")
	ft.write(html)
	ft.close()

def parseHTML(html):
	print html
	regexSection = r'<section\ id="free">(.+?)</section>'
	# regexSection = r'''<section\ id="free">\n\t<div\ class="container">\n\t\t<div\ class="row">\n\t\t\t<div\ class="col-lg-12\ text-center">\n\t\t\t\t<h3>(.+?)</h3>\n\t\t\t\t<hr\ class="star-primary">\n\t\t\t</div>\n\t\t</div>\n\t\t<div\ class="row">\n\t\t\t<div\ class="col-lg-4\ text-center">\n\t\t\t\t(<h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4><h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4>)\n\t\t\t</div>\n\t<div\ class="col-lg-4\ text-center">\n\t\t\t\t(<h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4><h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4>)\n\t\t\t</div>\n\t\t\t<div\ class="col-lg-4\ text-center">\n\t\t\t\t(<h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4><h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4>\n\t\t\t\t<h4>(.+?)</h4>)\n\t\t\t</div>\n\t\t</div>\n\t</div></section>'''
	# sectionre = re.compile(regexSection)
	sectionlist = re.findall(regexSection,html,re.S)
	return sectionlist

def getSubInfo(html):
	regexInfo = r'''<div class="col-lg-4 text-center">(.+?)</div>'''
	infolist = re.findall(regexInfo,html,re.S)
	print infolist
	return infolist

def getFinalRes(resItemList):
	print resItemList
	regexFinalInfo = r'<h4>(.+?)</h4>'
	reFinalInfo = re.compile(regexFinalInfo)
	result=[]
	for item in resItemList:
		item = item.replace('<fontcolor="green">','').replace('<fontcolor="red">','').replace('</font>','')
		resu = reFinalInfo.findall(item)
		for it in resu:
			result.append(it)
	print result
	return result

def storeList(list,suffix):
	curtime = datetime.now()

	tmpHTMLFileName = str(curtime)[0:-3]+"."+suffix
	tmpHTMLFileName = tmpHTMLFileName.replace(':','.')
	tmpHTMLFileName = tmpHTMLFileName.replace('-','_')
	print tmpHTMLFileName

	#record that time page..
	ft = file(str(tmpHTMLFileName),"w")
	i=0
	for item in list:
		ft.write(item+'\n')
		i+=1
		if i%6==0:
			ft.write('\n')
	ft.close()

html = mainProcess()
