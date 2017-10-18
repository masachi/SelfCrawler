import random
import requests
import urllib2
import json


class ProxyMiddleWares(object):
    # ip_pool = []
    # with open('../file/proxies.txt', 'r') as f:
    #     for line in f.readlines():
    #         ip = 'https://' if line.split(' ')[6] == 'yes' else 'http://' + line.split(' ')[0] + ':' + line.split(' ')[1]
    #         ip_pool.append(ip)

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        ip = json.loads(urllib2.urlopen('http://gimmeproxy.com/api/getProxy?get=true&protocol=http&maxCheckPeriod=200').read())['curl']
        request.meta['proxy'] = ip
        print 'ip:' + ip
