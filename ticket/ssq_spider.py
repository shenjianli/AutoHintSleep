#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@software: PyCharm 
@file: ssq_spider.py 
@time: 2021/11/6 上午11:18 
@description：双色球爬虫
"""

import re
import requests


# 公众号：煎蛋搞钱

class SSQ(object):

    def __init__(self):
        self.url = 'http://kaijiang.500.com/static/info/kaijiang/xml/ssq/list.xml'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    def get_last_ssq_lucky(self):
        # 发起请求
        reponse = requests.get(url=self.url, headers=self.headers)

        # 正则规则
        pattern = re.compile(r'<row.*?expect="(.*?)".*?opencode="(.*?)".*?opentime="(.*?)"')

        # 双色球数据
        ssq_raw_list = pattern.findall(reponse.text)

        results = []

        for item in ssq_raw_list:
            # 期数、数据、时间
            no, info, create_at = item
            # 6个红球、1个篮球
            red, blue = info.split("|")

            red_datas = red.split(",")

            results.append(
                [no, red_datas[0], red_datas[1], red_datas[2], red_datas[3], red_datas[4], red_datas[5], blue,
                 create_at]
            )

        # 最近的一期中奖号码
        last_lottery = results[0]

        return [last_lottery[1], last_lottery[2], last_lottery[3], last_lottery[4], last_lottery[5], last_lottery[6]], \
               last_lottery[7]