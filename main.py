#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#初次尝试用python 程序化交易
#__author__ : Tyraan


import config
from Okcoin import OkcoinConfig,getTicker

from Okcoin.OkcoinSpotAPI import OKCoinSpot
from Okcoin.OkcoinFutureAPI import OKCoinFuture
#初始化apikey，secretkey,url
from config import apiKey,secretKey,OkCoinCN,OkcoinCOM


#现货api
spot = OKCoinSpot(OkCoinCN,apiKey,secretKey)

#期货api
future=OKCoinFuture(OkcoinCOM,apiKey,secretKey)


def getTickerInfo():
    cnurl = OkcoinConfig.okcoinCN
    comurl = OkcoinConfig.okcoin

    CNinfo = getTicker(cnurl)
    COMinfo = getTicker(comurl)



def