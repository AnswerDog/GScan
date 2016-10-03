#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

HTTP_REQUEST_DEFAULT_HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Cookie':
        'Cookie: __utma=32101439.1264916047.1418201645.1421203474.1426559404.2;'
        ' __utmc=32101439; _gali=content-body; _ga=GA1.2.1264916047.1418201645; _gat=1'
}
HTTP_REQUEST_DEFAULT_TIME_OUT = 5
HTTP_REQUEST_DEFAULT_RETRY_TIMES = 3
CUSTOM_REQUEST_ARGS = {
		"headers": HTTP_REQUEST_DEFAULT_HEADERS,
		"timeout": HTTP_REQUEST_DEFAULT_TIME_OUT
}

def http_request(url, **kwargs):
	for key, value in CUSTOM_REQUEST_ARGS.items():
		if key not in kwargs:
			kwargs[key] = value
		requests_times = 0
	while True:
		try:
			resp = requests.get(url, **kwargs)
			return resp.status_code
		except Exception, e:
			requests_times += 1
			if requests_times >= HTTP_REQUEST_DEFAULT_RETRY_TIMES:
				return 0
