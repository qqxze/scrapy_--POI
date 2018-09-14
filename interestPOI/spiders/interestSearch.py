# -*- coding: utf-8 -*-
import scrapy
import json
import math
import re
import random
from tools import readCity
from interestPOI.items import InterestpoiItem
from urllib.parse import unquote

class InterestsearchSpider(scrapy.Spider):
    name = 'interestSearch'
    allowed_domains = ['restapi.amap.com']
    start_urls = readCity.getStarUrls()
    key_list = ['4322ae2635536221a7618726474d9042','a6e19141b2760bbcf3c4528852fda107']
    # start_urls=["https://restapi.amap.com/v3/place/text?key=b82d62c1ae2b07318c90acaceab84720&keywords=&types=110201|110202|110203|110204|110208&city=120000&children=1&offset=20&page=1&extensions=base"]
    headers = {
        "HOST": "restapi.amap.com",
        "Referer": "https://restapi.amap.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }



    def parse(self, response):
        detail_json = json.loads(response.text)
        sta = int(detail_json['status'])

        if (response.status != 200 or sta == 0):
            newURL,flag = readCity.getNewURL(response.url)
            if flag:

                yield scrapy.Request(url=newURL, callback=self.parse_detail)
            else:
                yield scrapy.Request(url=newURL, callback=self.parse)

        if (response.status == 200 and sta == 1):
            # detail_json = json.loads(response.text)
            count = detail_json['count']  # 返回数量
            if (count != 0):
                page = int(math.ceil(int(count) / 20))  # 应读取的页数

                yield  scrapy.Request(url=response.url, callback=self.parse_detail)
                if(page>1):
                    for i in range(2, page+1):
                        reg = re.compile(r'.*((page=)(\d+)).*')
                        match = reg.match(response.url)
                        next_url = str(response.url).replace(match.group(1), match.group(2) + str(i))
                        yield  scrapy.Request(url = next_url,callback = self.parse_detail)


    def parse_detail(self,response):
        detail_json = json.loads(response.text)
        if detail_json['status']==0:
            newURL, flag = readCity.getNewURL(response.url)
            if flag:
                yield scrapy.Request(url=newURL, callback=self.parse_detail)
            else:
                yield scrapy.Request(url=newURL, callback=self.parse)
        else:
            list_pois = detail_json['pois']
            reg = re.compile(r'.*(city=(\d+)).*')
            match = reg.match(response.url)
            for poi in list_pois:
                intersItem = InterestpoiItem()
                intersItem['code'] = match.group(2)
                intersItem['name'] = poi['name']
                intersItem['lon'] = poi['location'].split(",")[0]
                intersItem['lat'] = poi['location'].split(",")[1]
                yield intersItem

