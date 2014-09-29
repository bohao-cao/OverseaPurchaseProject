__author__ = 'bohaocao'
from htmldom import htmldom
import urllib.request
import shutil
import os
import time

#this is the view all bag url
dom= htmldom.HtmlDom("http://www.coach.com/online/handbags/-handbags-us-us-62-en?t1Id=62&t2Id=62&t3Id=5000000000000018501&viewType=viewall&LOC=SN2").createDom()

#Get Category
#eg. Shoulder bags, Totes
cat = dom.find('.categoryDivider')
print(cat.len)
print(cat.text())


#Create dir to store pics
dirName = "CoachAllBagsPhotos"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    while not os.path.exists(dirName):
        time.sleep(1)

#Find all the div for bags
childrn = dom.find(".categoryGrid").children()
print(childrn.len)

for node in childrn:

    imgUrl = node.find(".product-image").children().first().attr("data-original")

    seqNo = node.children("a").attr("name")
    i = node.find(".productInfo\sto_lowercase")
    title = i.find(".prod-title").text()
    price = i.find(".prodListPrice").text()

    fileName = seqNo + "_" + title + ' ' + price + '.jpg'
    fileName = fileName.replace('/', '')
    response = urllib.request.urlopen(imgUrl)
    if not os.path.exists(os.path.join(dirName, fileName)):
        with open(os.path.join(dirName, fileName), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
