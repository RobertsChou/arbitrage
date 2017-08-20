#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于访问JUBI 现货REST API
from HttpMD5Util import buildMySign,buildJSign, httpGet,httpPost
import time

class JubiSpot:

    def __init__ (self,url,apikey,secretkey):
        self.__url = url
        self.__apikey = apikey
        self.__secretkey = secretkey

    #获取Jubi现货行情信息
    def ticker(self, symbol = ''):
        TICKER_RESOURCE = "/api/v1/ticker/"
        params=''
        if symbol:
            params = 'coin=%(symbol)s' % {'symbol':symbol}
        return httpGet(self.__url,TICKER_RESOURCE,params)

    #获取Jubi现货市场深度信息
    def depth(self,symbol = ''):
        DEPTH_RESOURCE = "/api/v1/depth/"
        params=''
        if symbol:
            params = 'coin=%(symbol)s' %{'symbol':symbol}
        return httpGet(self.__url,DEPTH_RESOURCE,params)

    #获取Jubi现货历史交易信息  最近100个交易信息
    def trades(self,symbol = ''):
        TRADES_RESOURCE = "/api/v1/orders/"
        params=''
        if symbol:
            params = 'coin=%(symbol)s' %{'symbol':symbol}
        return httpGet(self.__url,TRADES_RESOURCE,params)

    #获取用户现货账户信息
    def userinfo(self):
        USERINFO_RESOURCE = "/api/v1/balance/"
        params ={}
        params['key'] = self.__apikey
        params['nonce'] = int(time.time() *100)
        params['signature'] = buildJSign(params,self.__secretkey)
        return httpPost(self.__url,USERINFO_RESOURCE,params)

    #现货交易 下单
    def trade(self,symbol,tradeType,price='',amount=''):
        TRADE_RESOURCE = "/api/v1/trade_add/"
        params = {
            'key':self.__apikey,
            'coin':symbol,
            'type':tradeType
        }
        if price:
            params['price'] = price
        if amount:
            params['amount'] = amount

        params['nonce'] = int(time.time() *100)
        params['signature'] = buildJSign(params,self.__secretkey)
        return httpPost(self.__url,TRADE_RESOURCE,params)

    #现货批量下单

    #现货取消订单
    def cancelOrder(self,symbol,orderId):
        CANCEL_ORDER_RESOURCE = "/api/v1/trade_cancel/"
        params = {
             'key':self.__apikey,
             'coin':symbol,
             'id':orderId
        }
        params['nonce'] = int(time.time() *100)
        params['signature'] = buildJSign(params,self.__secretkey)
        return httpPost(self.__url,CANCEL_ORDER_RESOURCE,params)

    #现货订单信息查询
    def orderinfo(self,symbol,orderId):
         ORDER_INFO_RESOURCE = "/api/v1/trade_view/"
         params = {
             'key':self.__apikey,
             'coin':symbol,
             'id':orderId
         }
         params['nonce'] = int(time.time() *100)
         params['signature'] = buildJSign(params,self.__secretkey)
         return httpPost(self.__url,ORDER_INFO_RESOURCE,params)

    #现货批量订单信息查询  tradeType all:所有挂单  open:正在挂单
    def ordersinfo(self,symbol,tradeType, since=0):
         ORDERS_INFO_RESOURCE = "/api/v1/trade_list/"
         params = {
             'key':self.__apikey,
             'coin':symbol,
             'type':tradeType,
             'since':since
         }
         params['nonce'] = int(time.time() *100)
         params['signature'] = buildJSign(params,self.__secretkey)
         return httpPost(self.__url,ORDERS_INFO_RESOURCE,params)

    #现货获得历史订单信息

