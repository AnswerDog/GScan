#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import threadpool
import re
import logging

HTTP_REQUEST_DEFAULT_HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}
HTTP_REQUEST_DEFAULT_TIME_OUT = 20
CUSTOM_REQUEST_ARGS = {
		"headers": HTTP_REQUEST_DEFAULT_HEADERS,
		"timeout": HTTP_REQUEST_DEFAULT_TIME_OUT
}

class WeakfileScan:
	def __init__(self,taskid, target):
		self.taskid = taskid
		self.url = 'http://' + target
		self.file_list = self._init_files()
		self.result = []

	def _init_files(self):
		rule_file = '/var/GScan/gscan/tasks/weakfile/dict/common.txt'
		for url in open(rule_file, 'r'):
			if url.startswith('/'):
				yield url

	def _http_request(self, url, **kwargs):
		for key, value in CUSTOM_REQUEST_ARGS.items():
			if key not in kwargs:
				kwargs[key] = value
		while True:
			try:
				resp = requests.get(url, **kwargs)
				header = resp.headers
				if header['content-type'].find('text') >= 0 or header['content-type'].find('html') >= 0 or int(header['content-length']) <= 1048576:
					html_doc = self._decode_response_text(resp.content)
				else:
					html_doc = ''
				return resp.status_code, header, html_doc
			except Exception, e:
				return 0, {}, ''

	def _decode_response_text(self, rtxt, charset=None):
		if charset:
			try:
				return rtxt.decode(charset)
			except:
				pass
		encodings = ['UTF-8', 'GB2312', 'GBK', 'iso-8859-1', 'big5']
		for _ in encodings:
			try:
				return rtxt.decode(_)
			except:
				pass
		try:
			return rtxt.decode('ascii', 'ignore')
		except:
			pass
		raise Exception('Fail to decode response Text')

	def _scan_start(self, weakfile):
		path = weakfile.split()[0]
		p_severity = re.compile('{severity=(\d)}')
		p_tag = re.compile('{tag="([^"]+)"}')
		p_status = re.compile('{status=(\d{3})}')
		p_content_type = re.compile('{type="([^"]+)"}')
		p_content_type_no = re.compile('{type_no="([^"]+)"}')
		p_plugin = re.compile('{plugin="([^"]+)"}')

		_ = p_severity.search(weakfile)
		severity = int(_.group(1)) if _ else 3
		_ = p_tag.search(weakfile)
		tag = _.group(1) if _ else ''
		_ = p_status.search(weakfile)
		code = int(_.group(1)) if _ else 0
		_ = p_content_type.search(weakfile)
		content_type = _.group(1) if _ else ''
		_ = p_content_type_no.search(weakfile)
		content_type_no = _.group(1) if _ else ''
		_ = p_plugin.search(weakfile)
		plugin = _.group(1) if _ else ''
		try:
			status, header, html_doc = self._http_request(self.url + path)
			if status in [200, 301, 302, 303, 403]:
				if code and status != code:
					return
				if not tag or html_doc.find(tag) >= 0:
					if content_type and header['content-type'].find(content_type) < 0 or content_type_no and header['content-type'].find(content_type_no) >=0:
						return
					print self.url + path
					self.result.append({'taskid': self.taskid,'target': self.url,'file': self.url + path,'status': status,'plugin':plugin})
					#print severity,tag,status,content_type,content_type_no,plugin
		except Exception, e:
			#logging.error('[Exception in _http_request] %s' % e)
			pass
		

	def scan(self):
		pool = threadpool.ThreadPool(10)
		reqs = threadpool.makeRequests(self._scan_start, self.file_list)
		[pool.putRequest(req) for req in reqs]
		pool.wait()
		pool.dismissWorkers(30, do_join=True)
		if len(self.result) > 10:
			return []
		else:
			return self.result

if __name__ == '__main__':
	target = 'pec.swpu.edu.cn'
	print WeakfileScan(123,target).scan()	
