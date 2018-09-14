# scrapy_--POI
基于scrapy框架爬取高德地图POI
#### 1.按照市级爬取景区数据
    获取全国市级code
#### 2.景区数据存在冗余
    只搜索以下级别的景物数据
		  110201
		  风景名胜
		  风景名胜
		  世界遗产
		  110202
		  风景名胜
		  风景名胜
		  国家级景点
		  110203
		  风景名胜
		  风景名胜
		  省级景点
		  110204
		  风景名胜
		  风景名胜
		  纪念馆
		  110208
		  风景名胜
		  风景名胜
		  海滩
  但是仍会有一些景区相近的，爬取完再进行处理吧
#### 3.申请高德地图key，按照官方网址教程很快就会申请下来。
#### 4.创建scrapy项目

- 在所创建的文件路径下，workon python环境

- scrapy startproject name

- cd spiders目录下，scrapy genspider spiderName 网址

- 设置item  数据格式

 - 在spiders的爬取主程序中 设置starURLS(list),写parse (返回startURLS的爬取结果)及 parse_detail函数

- pipline编写对item数据的处理及保存

