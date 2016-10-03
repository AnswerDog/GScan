#!/usr/bin/env python

# -*- encoding: utf-8 -*-
#pip install pymongo==2.4
import pymongo

class Plugin:
  def __init__(self,ip):
    self.ip = ip

  def run(self):
    try:
      pymongo.Connection(self.ip, 27017)
      print 'mangodb vul exists'
      return 'mangodb vul exists'
    except:
      pass


if __name__ == '__main__':
    Plugin('123.56.85.22').run()
