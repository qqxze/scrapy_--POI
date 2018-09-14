# -*- coding: utf-8 -*-
import json
import random
import re

import numpy as np
import math
import scrapy

from interestPOI.items import StaionPOIItem
from tools import readCity
from urllib.parse import unquote




class TollstationSpider(scrapy.Spider):
    name = 'tollStation'
    allowed_domains = ['restapi.amap.com']
    start_urls = readCity.getStationStarts()
    key_list = ['4322ae2635536221a7618726474d9042', 'a6e19141b2760bbcf3c4528852fda107']
    # start_urls=["https://restapi.amap.com/v3/place/text?key=b82d62c1ae2b07318c90acaceab84720&keywords=&types=收费站&city=120000&children=1&offset=20&page=1&extensions=base"]
    headers = {
        "HOST": "restapi.amap.com",
        "Referer": "https://restapi.amap.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }

    # def getNewUrl(self,response):
    #     # key_list = ['4322ae2635536221a7618726474d9042', 'a6e19141b2760bbcf3c4528852fda107']
    #     reg = re.compile(r'.*((key=)(.+?)(\&)).*')
    #     match = reg.match(response.url)
    #     index = random.randint(0, len(self.key_list) - 1)
    #     url_new = str(response.url).replace(match.group(1), match.group(2) + str(self.key_list[index]) + "&")
    #
    #     reg_page = re.compile(r'.*(page=(\d+)).*')
    #     match_page = reg_page.match(response.url)
    #
    #     if (match_page.group(2) == 1):
    #         yield scrapy.Request(url=url_new, callback=self.parse)
    #     else:
    #         yield scrapy.Request(url=url_new, callback=self.parse_detail)
    def parse(self, response):
        detail_json = json.loads(response.text)
        sta = int(detail_json['status'])
        cur_url = response.url
        if (response.status != 200 or sta == 0):
            # yield scrapy.Request(url=response.url, callback=self.getNewUrl)
            newURL,flag = readCity.getNewURL(cur_url)
            if flag:

                yield scrapy.Request(url=newURL, callback=self.parse_detail)
            else:
                yield scrapy.Request(url=newURL, callback=self.parse)

        elif (response.status == 200 and sta == 1):

            count = detail_json['count']  # 返回数量
            if(count!=0):
                page = int(math.ceil(int(count) / 20))  # 应读取的页数
                yield scrapy.Request(url=response.url, callback=self.parse_detail)
                if (page > 1):
                    for i in range(2, page + 1):
                        reg = re.compile(r'.*((page=)(\d+)).*')
                        match = reg.match(response.url)
                        next_url = str(response.url).replace(match.group(1), match.group(2) + str(i))
                        yield scrapy.Request(url=next_url, callback=self.parse_detail)

    def parse_detail(self,response):
        detail_json = json.loads(response.text)
        if detail_json['status'] == '0':
            # yield scrapy.Request(url=response.url, callback=self.getNewUrl)
            newURL,flag = readCity.getNewURL(response.url)
            if flag:
                yield scrapy.Request(url=newURL, callback=self.parse_detail)
            else:
                yield scrapy.Request(url=newURL, callback=self.parse)
        else:
            list_pois = detail_json['pois']
            reg = re.compile(r'.*((keywords=)(.+?)(\&)).*')
            match = reg.match(response.url)
            stationName = unquote(match.group(3), 'utf-8')
            print(stationName)
            stationItem = StaionPOIItem()
            stationItem['name_orien'] = stationName
            # reg = re.compile(r'(.*)?(东|北|南|西|站|入|出|出京|进京|外)$')
            # match = reg.match(stationName)
            # if match:
            #     name = match.group(1)
            # else:
            #     name = stationName
            # print(name)
            lon_list=[]
            lat_list=[]
            for poi in list_pois:
                if(poi['name'][:len(stationName)]==stationName):#如果匹配到的是
                    print(poi['name'])
                    lon_list.append( float(poi['location'].split(",")[0]))
                    lat_list.append(float(poi['location'].split(",")[1]))
            stationItem['lon'] = np.mean(lon_list)
            stationItem['lat'] = np.mean(lat_list)
            yield stationItem


