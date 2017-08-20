#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于进行http请求，以及MD5加密，生成签名的工具类

import http.client
import urllib
import json
import hashlib
import struct
import time
import hmac

#OKCoin
def buildMySign(params,secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) +'&'
    data = sign+'secret_key='+secretKey
    return  hashlib.md5(data.encode("utf8")).hexdigest().upper()


#JUBI
def buildJSign(params,secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) + '&'
    sign = sign.rstrip('&')
    md5_key = hashlib.md5(secretKey.encode(encoding='utf-8')).hexdigest()
    key = md5_key.encode(encoding='utf-8')
    msg = sign.encode(encoding='utf-8')
    return hmac.new(key, msg,digestmod=hashlib.sha256).hexdigest()

#YUNBI
def buildYunbiSign(params, METHOD , URI_RESOURCE, secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) + '&'
    sign = METHOD+'|'+ URI_RESOURCE +'|'+sign.rstrip('&')
    #md5_key = hashlib.md5(secretKey.encode(encoding='utf-8')).hexdigest()
    key = secretKey.encode(encoding='utf-8')
    sign_encode = sign.encode(encoding='utf-8')
    return hmac.new(key,sign_encode,digestmod=hashlib.sha256).hexdigest()

#CHBTC
def buildCHBTCSign(self,params, secretKey):
    sha1_key = secretKey.encode(encoding='utf-8')
    sha1 = hashlib.sha1()
    sha1.update(sha1_key)
    SHA_secret = sha1.hexdigest()
    sign = ''
    for key in params.keys():
        sign += key + '=' + str(params[key]) + '&'
    sign = sign.rstrip('&')

    sign = sign.encode(encoding='utf-8')
    sha_secret = SHA_secret.encode(encoding='utf-8')
    return hmac.new(sha_secret,sign).hexdigest();


#https
def httpGet(url,resource,params=''):
    conn = http.client.HTTPSConnection(url, timeout=10)
    conn.request("GET",resource + '?' + params)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.dumps(json.loads(data), indent = 4)

#http
def httpGetNoSSL(url,resource,params=''):
    conn = http.client.HTTPConnection(url, timeout=10)
    conn.request("GET",resource + '?' + params)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.dumps(json.loads(data), indent = 4)


def httpPost(url,resource,params):
     headers = {
            "Content-type" : "application/x-www-form-urlencoded",
     }
     conn = http.client.HTTPSConnection(url, timeout=10)
     temp_params = urllib.parse.urlencode(params)
     conn.request("POST", resource, temp_params, headers)
     response = conn.getresponse()
     data = response.read().decode('utf-8')
     params.clear()
     conn.close()
     return json.dumps(json.loads(data), indent=4)




