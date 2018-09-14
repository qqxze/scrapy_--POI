import random
import re

import pandas as pd

def getReadList():
    data = pd.read_csv("I:/roadNet/data/FV/citycode.csv")
    return list(data.Code)
def getStarUrls():
    url_search = "https://restapi.amap.com/v3/place/text?key=b8***62c1ae2b07318c90acaceab84720&keywords=&types=110201|110202|110203|110204|110208&city={0}&children=1&offset=20&page=1&extensions=base"
    listCity = getReadList()  # 读取要爬取的城市列表
    starUrls=[]
    for c in listCity:
        starUrls.append(url_search.format(c))
    return starUrls

def getStationName():
    data = pd.read_csv("I:/roadNet/data/FV/station.csv")
    return list(data.name)
def getStationStarts():
    url_search = "https://restapi.amap.com/v3/place/text?key=b82d***18c90acaceab84720&keywords={0}&types=收费站&city=&children=1&offset=20&page=1&extensions=base"
    listSation= getStationName()  # 读取要爬取的城市列表
    starUrls = []
    for c in listSation:
        reg = re.compile(r'(.*)?(东|北|南|西|站|入|出|出京|进京|外)$')
        match = reg.match(c)
        if match:

            starUrls.append(url_search.format(match.group(1)))
        else:
            starUrls.append(url_search.format(c))
    return starUrls

def getNewURL(url):
    key_list = ['4322ae2**221a7618726474d9042', 'a6e19141b27**28852fda107']
    reg = re.compile(r'.*((key=)(.+?)(\&)).*')
    match = reg.match(url)
    index = random.randint(0, len(key_list) - 1)
    url_new = str(url).replace(match.group(1), match.group(2) + str(key_list[index])+"&")

    reg_page = re.compile(r'.*(page=(\d+)).*')
    match_page = reg_page.match(url)
    flag = True
    if (match_page.group(2) == 1):
        flag = False
    return url_new,flag

if __name__ == '__main__':
    print(len(getStationStarts()))
    for i in getStationStarts():
        print(i)


