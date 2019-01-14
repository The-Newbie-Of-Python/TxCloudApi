#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/11
'''
项目所有的装饰器函数
'''
import time

#函数耗时
def timeSpend(func):
    def wrapper(*args, **kwargs):
        start_Time = time.time()
        func()
        end_Time = time.time()
        total_time = (end_Time - start_Time)*1000
        print("程序耗时%s毫秒"%total_time)
    return wrapper

@timeSpend
def main():
    for i in range(10*1000000):
        pass

if __name__ == "__main__":
    main()
