import re
#
# url = 'restapi.amap.com/v3/place/text?key=您的key&keywords=北京&types=收费站&city=&children=1&offset=20&page=1&extensions=all'
# reg = re.compile(r'(.*)?(东|北|南|西)$')
# match = reg.match("北京")
# if match:
#     print("yes")
# else:
#     print("no")
# # print(match.group(2))
# # print(match.group(3))
#
# test = {"T":"北京收费站"}
# name0 = "北京北"
# reg = re.compile(r'(.*)?(东|北|南|西)$')
# match = reg.match("北京")
# name = match.group(1)
# print(test["T"][:len(name)])
# print(test["T"][:len(name)].__contains__(name))
url ="https://restapi.amap.com/v3/place/text?key=b82d62c1ae2b07318c90acaceab84720&keywords=%E8%8B%8F%E6%B5%99%E7%9C%81%E7%95%8C&types=%E6%94%B6%E8%B4%B9%E7%AB%99&city=&children=1&offset=20&page=1&extensions=base"
reg = re.compile(r'.*((key=)(.+?)(\&)).*')
match = reg.match(url)
print(match.group(1))
print(match.group(2))
print(match.group(3))