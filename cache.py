#Part 2
def read_csv_header(csv_r):
    list=[]
    header=next(csv_r)
    for i in header:
        list.append(i)
    return list

def read_data(csv_r,sl):
    listofdict=[]
    for row in csv_r:
      retdict={}
      for i in range(len(sl)):
          retdict[sl[i]]=row[i]
      listofdict.append(retdict)
    return listofdict

def write_csv_header(csv_w,dict):
    ret=[]
    for i in dict:
        csv_w.writerow(i)
        ret.append(i)
    return ret

def write_dictionaries_to_csv(csv_w,listofdict,listofkey):
    retlist=[]
    for dict in listofdict:
            firstcolumn=retlist.append(dict[listofkey[0]])
            secondcolumn=retlist.append(dict[listofkey[1]])
            csv_w.writerow([firstcolumn,secondcolumn])


#Part 3
import json
import urllib.request
def get_data(jsonurl):
    webPage=urllib.request.urlopen(jsonurl)
    content=webPage.read().decode()
    data=json.loads(content)
    return data

def minimize_dictionaries(dl,sl):
    newlist=[]
    for dict in dl:
        retdict = {}
        for i in range(len(sl)):
            retdict[sl[i]]=dict.get(sl[i])
        newlist.append(retdict)
    return newlist

import csv
def write_cache(dl,name):
    with open (name,"w") as file:
        writer=csv.writer(file)
        header=[]
        for key in dl[0]:
            header.append(key)
        writer.writerow(header)
        for dict in dl:
          retrow=[]
          for i in header:
              retrow.append(dict[i])
          writer.writerow(retrow)
          
import csv
def read_cache(name):
    with open (name) as file:
        reader=csv.reader(file)
        header=next(reader)
        retlist=[]
        for row in reader:
            retdict={}
            for i in range(len(header)):
                retdict[header[i]]=row[i]
            retlist.append(retdict)
    return retlist