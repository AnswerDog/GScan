#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import redis

class Plugin:
    def __init__(self,ip):
        self.ip = ip

    def run(self):
        try:
            redisClient = redis.StrictRedis(host=self.ip)
            redisClient.set('test_redis', 'Hello Python')
            print 'Redis unauthorized access vul exists'
            return 'Redis unauthorized access vul exists'
        except:
            pass

if __name__ == '__main__':
    Plugin('127.0.0.1').run()
