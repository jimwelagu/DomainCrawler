import scrapy


class DomainSpider(scrapy.Spider):
	name = 'domains'
	
	start_urls = []
	
	
	def __init__(self, start_urls=None, target=None, *args, **kwargs):
		super(DomainSpider, self).__init__(*args, **kwargs)
		self.start_urls = ['{}'.format(start_urls)]
		self.target = '{}'.format(target)
	
			
	def parse(self, response):
		links = response.css('a::attr(href)').extract()
		
		for link in links:
			if self.target not in link:		
				continue
			else:					
				index = link.index(self.target)	
				index = index + len(self.target)	 	
				
				if index == len(link) or index+1 == len(link):	
					print('Link: {} <<<<<<<<<<'.format(link))
					
					with open('output.txt', 'a') as f:
						f.write('{}\n'.format(link))
						f.closed	
					
					yield response.follow(link, callback=self.parse)
	
	

