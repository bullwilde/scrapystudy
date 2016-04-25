import scrapy
from sinascrapy.items import SinaItem

class SinaSpider(scrapy.Spider):
	name = "sina"
	allowed_domains = ['sina.com.cn']
	start_urls = [
		"http://blog.sina.com.cn/s/blog_48486f0c0102w9t4.html"]
	
	def parse(self, response):
		item = SinaItem()    
		
		item['article'] = response.selector.xpath(
				'//div[@id="sina_keyword_ad_area2"]/descendant::text()').extract()
		if response.xpath('//div[@class="BNE_title"]'):
			item['title'] = response.xpath('//div[@id="articlebody"]/div/h1/text()').extract()
			item['timestamp'] = response.xpath(
				'//div[@id="articlebody"]/div/div/span[@id="pub_time"]/text()').extract()
		else:
			item['title'] = response.selector.xpath(
				'//div[@class="articalTitle"]/h2[@class="titName SG_txta"]/text()').extract()
			item['timestamp'] = response.selector.xpath(
					'//div[@class="articalTitle"]/span[@class="time SG_txtc"]/text()').extract()
		yield item

		if response.xpath('//div/span[@class="SG_txtb"]'):
			url = response.xpath(
				'//div[@class="articalfrontback SG_j_linedot1 clearfix"]//div[1]/a/@href').extract()[0]
			yield scrapy.Request(url, self.parse)
		
		elif response.xpath('//div/span[@class="BNE_txtC prev"]'):
			url = response.xpath('//div/span[@class="BNE_txtC prev"]/a/@href').extract()[0]
			yield scrapy.Request(url, self.parse)

