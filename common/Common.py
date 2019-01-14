#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/11
'''
公共模板
'''
import time,os,sys
Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Dir)
import configparser
import random
import hashlib,hmac
import binascii
from common import ConfPath


'''====================================================================================================='''
#区分大小写configparser模块重写
class myconf(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr
'''====================================================================================================='''

'''1.参数及必要凭证准备'''
conf = myconf()
conf.read(ConfPath.confpath)

AccessKey = conf.items('AccessKey')
AccessKey_ = {}
for i in AccessKey:
    AccessKey_[list(i)[0]] = list(i)[1]
SecretId = AccessKey_['SecretId']
SecretKey = AccessKey_['SecretKey']

uri = conf.items('URI')
uri = uri[0][1]

paramDict = {
    "Timestamp":int (time.time()),
    "Nonce":random.randint(65535,999999999),
    "Version":"2017-03-12",
    "SecretId":SecretId
}

f = conf.items('ParamDict')
ParamDict = {}
for i in f:
    ParamDict[list(i)[0]] = (list(i)[1])
paramDict.update(ParamDict)

'''2.生成签名串'''
'''2.1参数排序'''
tempList = []
tempDict = {}
for eveKey,eveValue in paramDict.items():
    tempLowerData = eveKey.lower()
    tempList.append(tempLowerData)
    tempDict[tempLowerData] = eveKey
tempList.sort()

'''2.2参数拼接'''
resultList = []
for eveData in tempList:
    tempStr = str(tempDict[eveData]) + "=" + str(paramDict[tempDict[eveData]])
    resultList.append(tempStr)
sourceStr = "&".join(resultList)

'''2.3拼接出需要签名的原文字符串'''
requestStr = "%s%s%s%s%s"%("GET",uri,"/","?",sourceStr)

'''2.4生成签名串'''
if sys.version_info[0] > 2 :
    signStr = requestStr.encode("utf-8")
    SecretKey = SecretKey.encode("utf-8")


digestmod = hashlib.sha1

hased = hmac.new(SecretKey,signStr,digestmod)

base64Data = binascii.b2a_base64(hased.digest())[:-1]

'''3.签名串URL编码'''

if sys.version_info[0] > 2 :
    base64Data = base64Data.decode()

import urllib.parse
base64Data = urllib.parse.quote(base64Data)

'''4.请求URL拼接'''
url = 'https://' + uri + '/' + '?' + sourceStr + '&Signature=' + base64Data
print(url)


if __name__ == '__main__':
    print(paramDict)
    pass
    # import urllib.request
    # print(urllib.request.urlopen(url).read().decode("utf-8"))

    # import json
    # try:
    #     for eveData in json.loads(urllib.request.urlopen(url).read().decode("utf-8"))["Response"]["RegionSet"]:
    #         print(eveData)
    # except:
    #         pass
