#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import rsynclib

class Plugin:
	def __init__(self,ip,port=873):
		self.ip = ip
		self.port = port
	
	def run(self):
		try:
			rsynclib.rsync(self.ip,port=873,timeout=5).connect()
			print 'rsync vul exists'
			return 'rsync vul exists'
		except:
			pass

if __name__ == '__main__':
	print Plugin('42.62.104.116').run()
