__author__ = 'julia.waldhagen'
from config import APIreal
from datetime import datetime
import requests




#url_site="http://api.sl.se/api2/typeahead.json?key={APIplats}&searchstring={search}"

#res=requests.get(url_site.format(APIplats=APIplats,search="Flemingsbergs"))

#print res.json()

siteid='7006'

url="http://api.sl.se/api2/realtimedepartures.json?key={APIreal}&siteid={siteid}&timewindow={timewindow}"

url=url.format(APIreal=APIreal,siteid=siteid,timewindow=15)



def get():
    #result
    res=requests.get(url)
    #json
    res=res.json()
    #trains
    res=res['ResponseData']['Trains']
    if len(res) >= 2:
        rad1=res[0]
        rad2=res[1]
        msg = rad1, rad2
    else:
        msg = "kaos"

    return msg

def sen(row):

    t1=row['TimeTabledDateTime']
    t2=row['ExpectedDateTime']
    d1=datetime.strptime(t1,"%Y-%m-%dT%H:%M:%S")
    d2=datetime.strptime(t2,"%Y-%m-%dT%H:%M:%S")
    tid =(d2-d1).seconds
    tid = tid/60
    return tid

def tabell(msg):
    row=[]
    for rader in msg:
        x=rader['TimeTabledDateTime']
        y=rader['DisplayTime']
        z=rader['Destination']
        w=rader['ExpectedDateTime']
        rad={}
        rad['TimeTabledDateTime']=rader['TimeTabledDateTime'].split('T')[1].rsplit(":",1)[0]
        rad['DisplayTime']=rader['DisplayTime']
        rad['Destination']=rader['Destination']
        rad['ExpectedDateTime']=rader['ExpectedDateTime'].split('T')[1]
        rad['Late']=sen(rader)      #seconds
        row.append(rad)
    return row

#msg=length_of_list(res.json()['ResponseData']['Trains'])



def busstops():
    msg=get()
    return tabell(msg)






