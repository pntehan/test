from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time
import os
import urllib.request
from progress.bar import Bar

#网页地址
url1 = 'https://www.google.com.sg/search?q='
url2 = '&source=lnms&tbm=isch'
#下载目录
path = 'E:/Downlord/Google/'

class google(object):
	"""docstring for google"""
	def __init__(self, keyword):
		self.url = url1 + keyword + url2
		self.path = path + keyword

	#连接网页，获取图片地址，返回一个列表
	def Get_imgList(self):
		print('打开游览器...')
		driver = webdriver.Chrome()
		print('连接网址...')
		print(self.url)
		try:
			driver.get(url)
		except:
			print('未知错误...')
			exit(0)
		print('获取源码...')
		source = driver.page_source
		print('分析源码...')
		soup = BeautifulSoup(source, 'html.parser')
		print('获取图片地址...')
		imglist = soup.findAll('img', {'class': 'rg_ic rg_i'})
		return imglist

	#初始化下载目录
	def init_path(self):
		if not os.path.exists(self.path):
			os.makedirs(self.path)

	#下载图片
	def DownLordImage(self, img):
		bar = Bar('正在下载图片', max=len(img), fill='#', suffix='%(percent)d%%')
		history = []
		x = 0
		for i in img:
			try:
				if i['src'] not in history:
					target = '{}/{}.jpg'.format(self.path, x)
					urllib.request.urlretrieve(i['src'], target)
					x += 1
			except KeyError:
				print('Error!')
				continue
			bar.next()
		bar.finish()
		
if __name__ == '__main__':
	new = google('斋藤飞鸟')
	img = new.Get_imgList()
	new.init_path()
	#print(img)
	new.DownLordImage(img)
	print('下载完成!')


