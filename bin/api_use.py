#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/11
'''

'''
import sys,os
Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Dir)
from common import Common
import urllib.request
import json


def run():
    print("腾讯云API调用接口demo\n")
    ap = input(('*'*60 + "\n1.常规返回方法请输入1\n2.Json定制方法请输入2\n" + '*'*60 + "\n"))
    if ap == "1" or "":
        print(urllib.request.urlopen(Common.url).read().decode("utf-8"))
    elif ap == "2":
        try:
            for eveData in json.loads(urllib.request.urlopen(Common.url).read().decode("utf-8"))["Response"]["DiskSet"]:
                print(eveData)
        except:
            pass



if __name__ == '__main__':
    run()
