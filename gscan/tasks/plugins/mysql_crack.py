#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pymysql
import threadpool


class Plugin:
  def __init__(self, ip):
    self.ip = ip
    self.port = 3306
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
    self.result = ''

  def _mysql_crack(self, dict):
    username = dict.split(':')[0]
    password = dict.split(':')[1]
    try:
      pymysql.connect(host=self.ip, user=username, passwd=password, port=self.port)
      return 2
    except:
      pass

  def _scan_start(self, dict):
    status = self._mysql_crack(dict)
    if status == 2:
      print('mysql weak pass %s' % dict)
      self.result = 'mysql weak pass %s' % dict

  def run(self):
    pool = threadpool.ThreadPool(20)
    reqs = threadpool.makeRequests(self._scan_start, self.dicts)
    [pool.putRequest(req) for req in reqs]
    pool.wait()
    pool.dismissWorkers(20, do_join=True)
    return self.result


if __name__ == '__main__':
  Plugin('127.0.0.1').run()


