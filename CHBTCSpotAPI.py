#!/usr/bin/python
# -*- coding: utf-8 -*-
from HttpMD5Util import buildCHBTCSign,httpGet,httpGetNoSSL,httpPost
import time

class CHBtcSpot:

    def __init__(self, url, apikey, secretkey):
        self.__url = url
        self.__apikey= apikey
        self.__secretkey= secretkey


    def _get_tonce(self):
        return int(time.time()*1000)

    #行情
    def ticker(self, symbol = ''):
        TICKER_RESOURCE = "/data/v1/ticker"
        params =''
        if symbol:
           params = 'currency=%(symbol)s' %{'symbol':symbol}
        return httpGetNoSSL(self.__url, TICKER_RESOURCE, params)

    #深度曲线
    def depth(self,symbol = '', size = '' , merge = ''):
        DEPTH_RESOURCE = "/data/v1/depth"
        params=''
        if symbol:
            params = 'currency=%(symbol)s' %{'symbol':symbol}
            if size:
               params += '&size=%(size)s' %{'size': size}
            if merge:
               params += '&merge=%(merge)s' %{'merge':merge}
        return httpGetNoSSL(self.__url,DEPTH_RESOURCE,params)

    #获取 CHBTC 现货历史交易信息
    def trades(self,symbol = ''):
        TRADES_RESOURCE = "/data/v1/trades"
        params=''
        if symbol:
            params = 'currency=%(symbol)s' %{'symbol':symbol}
        return httpGetNoSSL(self.__url,TRADES_RESOURCE,params)

    #获取 Kline
    def kline(self, symbol = ''):
        KLINE_RESOURCE = "/data/v1/kline"
        params=''
        if symbol:
            params = 'currency=%(symbol)s' %{'symbol':symbol}
        return httpGetNoSSL(self.__url,KLINE_RESOURCE,params)


    #获取用户现货账户信息
    def userinfo(self):
        USERINFO_RESOURCE = "/api/getAccountInfo"
        #获取签名
        dic={}
        dic['method'] = 'getAccountInfo'
        dic['accesskey'] = self.__apikey
        dic['sign'] = buildCHBTCSign(self,dic,self.__secretkey)
        dic['reqTime'] = self._get_tonce()
        params = ''
        #拼接参数
        for key in dic.keys():
            params += key + '=' + str(dic[key]) + '&'
        params = params.rstrip('&')
        return httpGet(self.__url,USERINFO_RESOURCE,params)


    #现货交易
    def trade(self,symbol,tradeType,price='',amount=''):
        TRADE_RESOURCE = "/api/v1/trade.do"
        params = {
            'api_key':self.__apikey,
            'symbol':symbol,
            'type':tradeType
        }
        if price:
            params['price'] = price
        if amount:
            params['amount'] = amount

        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,TRADE_RESOURCE,params)

    #现货批量下单
    def batchTrade(self,symbol,tradeType,orders_data):
        BATCH_TRADE_RESOURCE = "/api/v1/batch_trade.do"
        params = {
            'api_key':self.__apikey,
            'symbol':symbol,
            'type':tradeType,
            'orders_data':orders_data
        }
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,BATCH_TRADE_RESOURCE,params)

    #现货取消订单
    def cancelOrder(self,symbol,orderId):
        CANCEL_ORDER_RESOURCE = "/api/v1/cancel_order.do"
        params = {
             'api_key':self.__apikey,
             'symbol':symbol,
             'order_id':orderId
        }
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,CANCEL_ORDER_RESOURCE,params)

    #现货订单信息查询
    def orderinfo(self,symbol,orderId):
         ORDER_INFO_RESOURCE = "/api/v1/order_info.do"
         params = {
             'api_key':self.__apikey,
             'symbol':symbol,
             'order_id':orderId
         }
         params['sign'] = buildMySign(params,self.__secretkey)
         return httpPost(self.__url,ORDER_INFO_RESOURCE,params)

    #现货批量订单信息查询
    def ordersinfo(self,symbol,orderId,tradeType):
         ORDERS_INFO_RESOURCE = "/api/v1/orders_info.do"
         params = {
             'api_key':self.__apikey,
             'symbol':symbol,
             'order_id':orderId,
             'type':tradeType
         }
         params['sign'] = buildMySign(params,self.__secretkey)
         return httpPost(self.__url,ORDERS_INFO_RESOURCE,params)

    #现货获得历史订单信息
    def orderHistory(self,symbol,status,currentPage,pageLength):
           ORDER_HISTORY_RESOURCE = "/api/v1/order_history.do"
           params = {
              'api_key':self.__apikey,
              'symbol':symbol,
              'status':status,
              'current_page':currentPage,
              'page_length':pageLength
           }
           params['sign'] = buildMySign(params,self.__secretkey)
           return httpPost(self.__url,ORDER_HISTORY_RESOURCE,params)

