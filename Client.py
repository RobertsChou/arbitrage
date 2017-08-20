#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from CHBTCSpotAPI import CHBtcSpot
from JubiSpotAPI import JubiSpot
from YunbiSpotAPI import YunbiSpot
from enum import Enum

#class Coin(Enum):
#    BTC_CNY = 'btc_cny'
#    LTC_CNY = 'ltc_cny'
#    ETH_CNY = 'eth_cny'


#初始化 OKCoin 参数
okcoin_apikey = 'ak'
okcoin_secretkey = 'sK'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn

#OKCoin现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,okcoin_apikey,okcoin_secretkey)



#初始化 YUNBI 参数
yunbi_apikey = 'ak'
yunbi_secretkey = 'sk'
yunbiRESTURL = 'www.yunbi.com'

yunbiSpot = YunbiSpot(yunbiRESTURL,yunbi_apikey,yunbi_secretkey)



#初始化 CHBTC 参数
chbtc_apikey = 'ak'
chbtc_secretkey = 'sk'
chbtc_market = 'api.chbtc.com'     #行情api
chbtc_trade = 'trade.chbtc.com'   #交易api

chbtcMarket = CHBtcSpot(chbtc_market, chbtc_apikey, chbtc_secretkey) #行情
chbtcTrade = CHBtcSpot(chbtc_trade, chbtc_apikey, chbtc_secretkey)   #交易



#初始化 JUBI 参数
jubi_apikey = 'ak'
jubi_apisecret = 'sk'
jubiRESTURL = 'www.jubi.com'

jubiSpot = JubiSpot(jubiRESTURL, jubi_apikey, jubi_apisecret)


##################### OKCOIN ##################

print (u' 现货行情 ')
#print (okcoinSpot.ticker('eth_cny')) # form okcoin 成交量是24小时数据

print (u' 现货深度 ')
#print (okcoinSpot.depth('eth_cny')) #asks:卖方深度 bids:买方深度

print (u' 现货历史交易信息 ')
#print (okcoinSpot.trades('eth_cny'))

print (u' 用户现货账户信息 ')
#print (okcoinSpot.userinfo())


##################### JUBI ######################

print (u' JUBI 现货行情 ')
#print (jubiSpot.ticker('eth'))

print (u'JUBI 现货深度')
#print (jubiSpot.depth('eth'))

print (u'JUBI 用户现货账户信息')
#print (jubiSpot.userinfo())


#################### YUNBI ######################

print (u' YUNBI 现货行情 ')
#print (yunbiSpot.ticker('ethcny'))

print (u' YUNBI 现货深度 ')
#print (yunbiSpot.depth('ethcny', 10))

print (u' YUNBI 用户现货账户信息 ')
#print (yunbiSpot.userinfo())


#################### CHBTC #######################

print (u' CHBTC 现货行情')
print (chbtcMarket.ticker('eth_cny'))

print (u' CHBTC 深度')
#print (chbtcMarket.depth('eth_cny', 3))

print (u' CHBTC 历史交易订单')
#print (chbtcMarket.trades('eth_cny'))

print (u' K line')
#print (chbtcMarket.kline('eth_cny'))

print (u' CHBTC 获取用户信息')
print (chbtcTrade.userinfo())


#print (u' 现货下单 ')
#print (okcoinSpot.trade('eth_cny','buy','0.1','0.2'))

#print (u' 现货批量下单 ')
#print (okcoinSpot.batchTrade('eth_cny','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))

#print (u' 现货取消订单 ')
#print (okcoinSpot.cancelOrder('eth_cny','18243073'))

#print (u' 现货订单信息查询 ')
#print (okcoinSpot.orderinfo('eth_cny','18243644'))

#print (u' 现货批量订单信息查询 ')
#print (okcoinSpot.ordersinfo('eth_cny','18243800,18243801,18243644','0'))

#print (u' 现货历史订单信息查询 ')
#print (okcoinSpot.orderHistory('eth_cny','0','1','2'))

