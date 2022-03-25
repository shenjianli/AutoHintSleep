#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: 随机生成一注.py 
@time: 2021/10/20 下午9:57 
@description：随机生成一注双色球
"""

import random

from ticket.util import nums_pre


def gene_ssq(number):
    """
    随机产生几注双色球（6+1）
    :param number:
    :return:
    """
    result = []

    for item in range(number):
        reds = []

        # 产生6个红球
        while len(reds) < 6:
            # 从1-33中随机取一个数字
            temp_red_num = random.randint(1, 33)
            if temp_red_num not in reds:
                reds.append(temp_red_num)

        # 蓝球
        blue = random.randint(1, 16)

        # 红球排序
        reds.sort()

        # 数据预处理
        reds = nums_pre(reds)
        blue = nums_pre([blue])[0]

        result.append(' '.join(reds) + " + " + blue)
    return '\n'.join(result)


def gene_blue_random_ssq(reds, number):
    """
    红球固定，蓝球随机
    :param reds:
    :param number:
    :return:
    """
    result = []

    for item in range(number):
        # 蓝球
        blue = random.randint(1, 16)

        # 红球排序
        reds.sort()

        # 数据预处理
        reds = nums_pre(reds)
        blue = nums_pre([blue])[0]

        result.append(' '.join(reds) + " + " + blue)
    return '\n'.join(result)


def gene_red_random_ssq(blue, number):
    """
    蓝球固定，红球随机
    :param blue:
    :param number:
    :return:
    """
    result = []

    for item in range(number):
        reds = []

        # 产生6个红球
        while len(reds) < 6:
            # 从1-33中随机取一个数字
            temp_red_num = random.randint(1, 33)
            if temp_red_num not in reds:
                reds.append(temp_red_num)

        # 红球排序
        reds.sort()

        # 数据预处理
        reds = nums_pre(reds)
        blue = nums_pre([blue])[0]

        result.append(' '.join(reds) + " + " + blue)
    return '\n'.join(result)


print(gene_ssq(1))
