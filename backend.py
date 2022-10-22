#Part 1
def get_matches(listofdict,key,value):
    retdic=[]
    for dictionary in listofdict:
        for k in dictionary:
            if k==key and dictionary[k]==value:
                retdic.append(dictionary)
    return retdic

def list_descriptions(listofdict):
    accumulator=[]
    for dictionary in listofdict:
        tow_description=dictionary["tow_description"]
        if tow_description not in accumulator:
            accumulator.append(tow_description)
    return accumulator

def count_by_month(listofdict):
    monthcount=[]
    for i in range(12):
        monthcount.append(0)
    for dictionary in listofdict:
        tow_date=dictionary["tow_date"]
        month=int(tow_date[5]+tow_date[6])
        monthcount[month-1]=monthcount[month-1]+1
    return monthcount

def count_by_day(listofdict):
    daycount=[]
    for i in range(31):
        daycount.append(0)
    for dictionary in listofdict:
        tow_date=dictionary["tow_date"]
        day=int(tow_date[8]+tow_date[9])
        daycount[day-1]=daycount[day-1]+1
    return daycount