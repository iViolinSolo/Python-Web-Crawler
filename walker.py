import urllib
import urllib2
import re

def mainProcess(userId):
	userIdTemp = userId.split('\n')
	userId = userIdTemp[0];

	# html = getHTML("http://www.amazon.com/gp/pdp/profile/"+userId)
	html = getHTML(userId)
	namelist = getName(html)

	infolist = getInfo(html)
	if(len(infolist) == 0):
		infolist = ['_']

	addrlist = getAddress(html)
	if(len(addrlist) == 0):
		addrlist = ['_']

	helpflist = ['_','_']
	helpflistTemp = getHelpfulness(html)
	for item in helpflistTemp:
		if(len(item) != 0):
			helpflist[0] = item[0]
			helpflist[1] = item[1]

	userIdlist = []
	userIdlist.append(userId)

	result = userIdlist + namelist + addrlist + infolist + helpflist
	return result

def getHTML(userId):
	url = "http://www.amazon.com/gp/pdp/profile/"+userId
	headers = { #Grab disguised as a browser
	    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
	    }
	req = urllib2.Request(url,headers=headers)
	page = "";
	#record current userId
	ft = file("breakpoint","w")
	ft.write(userId+'\n')
	ft.close()

	try:
	    page = urllib2.urlopen(req)
	    html = page.read()
	    return html
	except:
	    print "getHtml: "+url+" error"

# def getHtml(url):
# 	page = urllib.urlopen(url)
# 	html = page.read()
# 	return html

# html = getHtml("http://www.cnblogs.com/fnng/p/3576154.html")
# html = getHTML("http://www.amazon.com/gp/pdp/profile/A3NPHQVIY59Y0Y")

# # print html
# f = file("test.html","w")
# f.write(html)
# f.close()

def getName(html):
	# regex = r'<div\ class="profile-info">(.+)</div>'
	# regex = r'<span\ class="profile-display-name\ break-word">(.+?)</span>'
	regexName = r'<div\ class="a-row\ a-spacing-top-small\ profile-name-container"><span\ class="profile-display-name\ break-word">(.+?)\n</span></div>'

	namere = re.compile(regexName)
	namelist = re.findall(namere, html)
	return namelist

def getAddress(html):
	regexAddr = r'</span></div><span\ class="a-size-small\ a-color-secondary">(.+?)\n</span></div>'
	addrre = re.compile(regexAddr)
	addrlist = re.findall(addrre, html)
	return addrlist

def getInfo(html):
	regexInfo = r'<div\ class="a-row\ a-spacing-small"><span\ class="a-size-small\ a-color-secondary">(.+?)</span>\n</div>'

	infore = re.compile(regexInfo)
	infolist = re.findall(infore, html)
	return infolist

def getHelpfulness(html):
	regexHelpfulness = r'<div\ class="a-row\ a-spacing-small"><div\ class="a-row\ customer-helpfulness"><span\ class="a-size-large\ a-text-bold">(.+?)</span>\n<span\ class="a-size-base\ a-text-bold">helpful</span>\n</div><span\ class="a-size-small\ a-color-secondary">votes received on reviews</span>\n<div\ class="a-row"><span\ class="a-size-small\ a-color-secondary">(.+?)</span>\n</div></div>'
	helpfre = re.compile(regexHelpfulness)
	helpflist = re.findall(helpfre, html)
	return helpflist

# infolist = getInfo(r'<span class="profile-display-name break-word">Soo. noo</span><></span>')
# infolist = getInfo(r'''<div class="a-row a-spacing-top-small profile-name-container"><span class="profile-display-name break-word">S. Dorman
# </span></div>''')

# html = getHTML("http://www.amazon.com/gp/pdp/profile/A3NPHQVIY59Y0Y")
# infolist = getInfo(html)
# print infolist

# f = file("storage.dat","w")
# userIdList = ["A1RSDE90N6RSZF","A328S9RN3U5M68","A1I7QGUDP043DG","A1M5405JH9THP9","A3NPHQVIY59Y0Y"]





breakpointUserId = ""
breakpointpath = "breakpoint"
with open(breakpointpath) as fbp:
	for linebp in fbp:
		breakpointUserId = linebp
		break

print "last stop breakpoint: "+breakpointUserId
print "begin at that time"

breakpointUserId += ''
print "<begin>"+breakpointUserId+"</begin>"
canBegin = False
filepath = "newIDs"
userIdList=[]
i =0
with open(filepath) as f:
    for line in f:
		i = i+1
		if(canBegin == False):
			if(breakpointUserId == line):
				canBegin = True
				print "find.."+breakpointUserId
			else:
				canBegin = False
				# print str(i)+" "+line
		if(canBegin == True):
			userIdList.append(line)

fw = file("userInfo.data","a")
for item in userIdList:
	result = mainProcess(item)
	for resItem in result:
		fw.write(resItem+'  |  ')
	print result
	fw.write('\n')
fw.close()


# for item in infolist:
# 	print item

# # print html
#
# def getImg(html):
# 	regex = r'<img\ alt="(.+?)"\ src="(.+?\.jpg)">'
# 	# regex = r'<img\ alt=".+">'
# 	imgre = re.compile(regex)
# 	imglist = re.findall(imgre, html)
# 	return imglist
#
# # imglist = getImg(r'<img alt="This is ALT" src="This is SRC.jpg"> <img alt="this is ALT2" src="This is SRC.jpg"> <img alt="Epson WorkForce 645 Wireless All-in-One Color Inkjet Printer, Copier, Scanner, Fax, iOS/Tablet/Smartphone/AirPrint Compatible (C11CB86201)" src="https://images-na.ssl-images-amazon.com/images/I/51lDvmxHLtL._01_SR90,90_.jpg">')
# # imglist = getImg(r'<img alt3="This is alt"> <img alt="This is alt2"> <img alt3="this is alt3">')
#
#
# for item in imglist:
# 	print item[0], '----', item[1]
