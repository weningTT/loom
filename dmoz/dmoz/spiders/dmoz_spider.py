import scrapy
#import middlewares
from scrapy.http import Request
from dmoz.items import DmozItem

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        #"http://www.ideacallin.com/wx.do"
        "http://www.gamersky.com/handbook/"
	]
    proxy_pool = [
        #"http://112.25.41.136:80"
	#"http://202.108.23.247:80"
        "http://120.195.207.14:80"
	#"http://120.195.193.223:80"
	#"http://119.254.97.160:21320"
	#"http://120.195.201.36:80"
	]

    def start_requests(self):
        requests = []
        for item in self.start_urls:
            print item
	    req = Request(url=item, headers={'Referer':None,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'})
            req.meta['proxy'] = self.proxy_pool[0]
	    requests.append(req)
	    
        return requests

    def parse(self, response):
	filename = "html_output/mulu.txt"
	with open(filename, 'w') as f:
	    for class_abc in response.xpath('//div[@class="ABC"]'):
		letter = class_abc.xpath('div/text()').extract()[0].encode('utf-8').strip()
		print class_abc.xpath('div/text()').extract()[0]
	        for class_li2 in class_abc.xpath('div[@class="ABClike"]/ul/li[@class="li2"]'):
		    title = class_li2.xpath('a/text()').extract()[0].encode('utf-8').strip()
		    link = class_li2.xpath('a/@href').extract()[0].encode('utf-8').strip()
		    line = ("%s\t%s\t%s\n") % (letter, title, link)
		    f.write(line)
	
	#filename = "html_output/a.out"
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
