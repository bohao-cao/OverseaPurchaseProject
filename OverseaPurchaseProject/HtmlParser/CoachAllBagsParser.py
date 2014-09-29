__author__ = 'bohaocao'
from htmldom import htmldom
import urllib.request
import shutil

dom= htmldom.HtmlDom("http://www.coach.com/online/handbags/-handbags-us-us-62-en?t1Id=62&t2Id=62&t3Id=5000000000000018501&viewType=viewall&LOC=SN2").createDom()

#Get Category
#eg. Shoulder bags, Totes
cat = dom.find('.categoryDivider')
#print(cat.text())

sib = cat.children()
x=sib.attributes(id)
print (x)



# f = dom.find("div#seq_1 > a")
# print('f=' + f.html())
#
# p = f.find(".product-image")
# imgUrl = p.children().first().attr("data-original")
#
# #print(p.html())
# print ('imgUrl=' + imgUrl)
#
#
# i = f.find(".productInfo\sto_lowercase")
# title = i.find(".prod-title").text()
# price = i.find(".prodListPrice").text()
#
# print ('title=' + title)
# print ('price=' + price)
#
# fileName = title + ' ' + price + '.jpg'
#
# with urllib.request.urlopen(imgUrl) as response, open(fileName, 'wb') as out_file:
#     shutil.copyfileobj(response, out_file)


#Save image with name and price