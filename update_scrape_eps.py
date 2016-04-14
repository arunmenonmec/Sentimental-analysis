import urllib2
from bs4 import BeautifulSoup
from bs4.element import (
    CharsetMetaAttributeValue,
    Comment,
    ContentMetaAttributeValue,
    Doctype,
    SoupStrainer,
)
import MySQLdb
import re


symbols={'HDFC':'HDFC.NS','WIPRO':'WIPRO.NS','TITAN':'TITAN.NS','VOLTAS':'VOLTAS.NS','BIRLACORPN':'BIRLACORP.NS','SOUTHBANK':'SOUTHBANK.NS','SIEMENS':'SIEMENS.NS','RELIANCE':'RELIANCE.NS','HILTON':'HILTON.NS','CASTROL':'CASTROL.NS','MRF':'MRF.NS','MARUTI':'MARUTI.NS','APTECHT':'APTECHT.NS','BLUEDART':'BLUEDART.NS','IDBI':'IDBI.NS','ICICIBANK':'ICICIBANK.NS','GAIL':'GAIL.NS','BPCL':'BPCL.NS','BOSCHLTD':'BOSCHLTD.NS','ASIANPAINT':'ASIANPAINT.BO'}

url="http://in.finance.yahoo.com/q?s="

db = MySQLdb.connect("localhost","root","","users" )
cursor = db.cursor()

for k in symbols:
     tmp=symbols[k]
     u = urllib2.urlopen(url+tmp)
     soup = BeautifulSoup(u.read())
     universities=soup.findAll('tr')
     for eachuniversity in universities:
	     if eachuniversity.th!=None:
		     if eachuniversity.th.text=='EPS (ttm):':
			    temp1=float(re.sub(",","",eachuniversity.td.text))
			    print str(temp1)
			    sql = "UPDATE stockvalue SET eps = %f WHERE  nsecode = '%s'" % (temp1,k) 
			    cursor.execute(sql) 
			    db.commit()
				
db.close()
