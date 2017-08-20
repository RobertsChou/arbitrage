#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于访问OKCOIN 现货REST API
from HttpMD5Util import buildYunbiSign,httpGet,httpPost
import time

class YunbiSpot:

    def __init__ (self,url,apikey,secretkey):
        self.__url = url
        self.__apikey = apikey
        self.__secretkey = secretkey


    #获取YUNBI 指定现货行情信息
    def ticker(self, symbol = ''):
        TICKER_RESOURCE = "/api/v2/tickers/"
        TICKER_RESOURCE += symbol
        if not symbol:
           TICKER_RESOURCE = "/api/v2/tickers.json"
        return httpGet(self.__url,TICKER_RESOURCE,'')


    #获取YUNBI现货市场深度信息
    def depth(self,symbol = '', limit = ''):
        DEPTH_RESOURCE = "/api/v2/depth.json"
        params=''
        if symbol:
            params = 'market=%(symbol)s' %{'symbol':symbol}
        if limit:
            params += '&limit=%(limit)s' %{'limit':limit}

        return httpGet(self.__url,DEPTH_RESOURCE,params)

    #获取YUNBI现货历史交易信息
    def trades(self,symbol = ''):
        TRADES_RESOURCE = "/api/v1/trades.do"
        params=''
        if symbol:
            params = 'symbol=%(symbol)s' %{'symbol':symbol}
        return httpGet(self.__url,TRADES_RESOURCE,params)

    #获取用户现货账户信息
    def userinfo(self):
        USERINFO_RESOURCE = "/api/v2/members/me.json"
        #获取签名
        dic ={}
        dic['tonce'] = time.time()*1000
        dic['access_key'] = self.__apikey
        dic['signature'] = buildYunbiSign(dic, "GET",USERINFO_RESOURCE, self.__secretkey)
        params = ''
        #拼接参数
        for key in dic.keys():
            params += key + '=' + str(dic[key]) + '&'
        params = params.rstrip('&')
        return httpGet(self.__url,USERINFO_RESOURCE,params)

    #获取用户现货账户信息
    def userinfoV2(self):
        USERINFO_RESOURCE = "/api/v2/members/me.json"
        params =''
        params = 'tonce=%(tonce)s' %{'tonce':time.time()*1000} + '&access_key=%(access_key)s' %{'access_key':self.__apikey}
        #signature = buildYunbiSign(params, self__secretkey)

        #params += '&signature=%(signature)'  %{'signature':signature}
        print (params)
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
















