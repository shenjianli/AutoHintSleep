#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@software: PyCharm 
@file: ssq_lucky.py 
@time: 2021/12/22 下午9:52 
@description：判断双色球是否中奖
"""
from ticket.util import nums_pre


def __get_lucky_desc(luck_level):
    """
    根据幸运指数，返回描述信息
    :param luck_level:
    :return:
    """
    if luck_level == 1:
        luck_desc = "一等奖（财富自由）"
    elif luck_level == 2:
        luck_desc = "二等奖（安逸了）"
    elif luck_level == 3:
        luck_desc = "三等奖（单注：3000元）"
    elif luck_level == 4:
        luck_desc = "四等奖（单注：200元）"
    elif luck_level == 5:
        luck_desc = "五等奖（单注：10元）"
    elif luck_level == 6:
        luck_desc = "六等奖（单注：5元）"
    else:
        luck_desc = "未中奖"

    return luck_desc


def judge_ssq_lucky(red_nums_result, red_nums_buy, blue_num_result, blue_num_buy):
    """
    根据中奖号码及购买号码，返回对应的中奖信息
    :param red_nums_result:
    :param red_nums_buy:
    :param blue_num_result:
    :param blue_num_buy:
    :return:
    """
    # 红球预测的数目
    red_lucky_count = 0
    # 篮球预测的数目
    blue_lucky_count = 0

    # 数据预处理
    red_nums_buy = nums_pre(red_nums_buy)
    blue_num_buy = nums_pre(blue_num_buy)

    # 判断红球
    for red_result_item in red_nums_result:
        for red_buy_item in red_nums_buy:
            if red_result_item == red_buy_item:
                red_lucky_count += 1

    # 判断蓝球
    if blue_num_result == blue_num_buy:
        blue_lucky_count = 1

    # 据福彩双色球的中奖规则所写，包括了所有的红蓝组合以及相对应的中奖情况
    if red_lucky_count == 6 and blue_lucky_count == 1:
        luck_level = 1  # 一等奖（6+1）
    elif red_lucky_count == 6 and blue_lucky_count == 0:
        luck_level = 2  # 二等奖（6+0）
    elif red_lucky_count == 5 and blue_lucky_count == 1:
        luck_level = 3  # 三等奖（5+1)
    elif red_lucky_count == 5 and blue_lucky_count == 0:
        luck_level = 4  # 四等奖(5+0)
    elif red_lucky_count == 4 and blue_lucky_count == 1:
        luck_level = 4  # 四等奖(4+1)
    elif red_lucky_count == 4 and blue_lucky_count == 0:
        luck_level = 5  # 五等奖(4+0)
    elif red_lucky_count == 3 and blue_lucky_count == 1:
        luck_level = 5  # 五等奖(3+1)
    elif red_lucky_count == 0 and blue_lucky_count == 1:
        luck_level = 6  # 六等奖(0+1)
    elif red_lucky_count == 1 and blue_lucky_count == 1:
        luck_level = 6  # 六等奖(1+1)
    elif red_lucky_count == 2 and blue_lucky_count == 1:
        luck_level = 6  # 六等奖(2+1)
    else:
        luck_level = -1

    return __get_lucky_desc(luck_level),luck_level




