# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import csv


class InterestpoiPipeline(object):
    def process_item(self, item, spider):

        return item

class WriteCSV(object):
    def __init__(self):
        self.file = open('intersetPOIS.csv', 'w',newline='', encoding="utf-8")
        self.headers = ["code","name", "lon", "lat"]
        self.writer = csv.writer(self.file)
        self.writer.writerow(self.headers)
    def process_item (self, item, spider):
        self.writer.writerow([item['code'],item['name'],item['lon'],item['lat']])
        return item
    def spider_closed(self, spider):
        self.file.close()
class WithInterstPOIText(object):
    # def __init__(self):
    #     self.file = codecs.open('comment.txt', 'w', encoding="utf-8")
    def process_item (self, item, spider):
        self.file = codecs.open('intersetPOIS0.txt', 'a', encoding="utf-8")
        # print(item['comment'])
        self.file.write(item['code']+","+item['name']+","+str(item['lon'])+","+str(item['lat'])+"\r\n")
        return item
    def spider_closed(self, spider):
        self.file.close()
class WriteStationCSV(object):
    def __init__(self):
        self.file = open('stationPOIS.csv', 'w',newline='', encoding="utf-8")
        self.headers = ["name", "lon", "lat"]
        self.writer = csv.writer(self.file)
        self.writer.writerow(self.headers)
    def process_item (self, item, spider):
        self.writer.writerow([item['name_orien'],item['lon'],item['lat']])
        return item
    def spider_closed(self, spider):
        self.file.close()

class WithText(object):
    # def __init__(self):
    #     self.file = codecs.open('comment.txt', 'w', encoding="utf-8")
    def process_item (self, item, spider):
        self.file = codecs.open('stationPOIS0.txt', 'a', encoding="utf-8")
        # print(item['comment'])
        self.file.write(item['name_orien']+","+str(item['lon'])+","+str(item['lat'])+"\r\n")
        return item
    def spider_closed(self, spider):
        self.file.close()