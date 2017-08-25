from subprocess import call 
from domain_spider import DomainSpider
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os.path

def delete_duplicates(target):
	target_rem = '{}/'.format(target)
        
	#Replace all 'target.com/' with 'target.com'       
	with open('output.txt', 'r') as f:	
		links = f.read()
		links = links.replace(target_rem, target)
		f.closed
	#After replacing, Write to the file	
	with open('output.txt', 'w') as f:	
		f.write(links)
		f.closed
	#Extract links to a set	
	with open('output.txt', 'r') as f:	 
		links = f.readlines()
		links_set = set(links)
		f.closed
	#Write to output.txt
	with open('output.txt', 'w') as f:	
		for link in links_set:
			f.write(link)

def highlight_history():
	with open('output.txt', 'r') as f:
		links = f.readlines()
		f.closed

	if os.path.isfile('temp.txt'):
		with open('temp.txt', 'r') as f:
			temp = f.readlines()
			f.closed

		with open('output.txt', 'w') as f: 
			for link in links:
				if link not in temp:
					addedlink = '[++] {}'.format(link)	
					links[links.index(link)] = addedlink
		
			links_set = set(links)	
		
			for link in links_set:
				f.write(link)
		
			f.closed

		with open('output.txt', 'r') as f:
			links = f.read()
			links = links.replace('[++] ', '')
			f.closed
		with open('temp.txt', 'w') as f:
			f.write(links)
			f.closed 				
		
								 
	else:
		with open('output.txt', 'r') as f:
			links = f.read()
			f.closed
		with open('temp.txt', 'a') as f:
			f.write(links)
			f.closed

def remove_highlights():
	with open('output.txt', 'r') as f:
                links = f.read()
                links = links.replace('[++] ', '')
                f.closed
        #After replacing, Write to the file     
        with open('output.txt', 'w') as f:
                f.write(links)
                f.closed
def main():
	print('~~~~~~~~~ WEBCRAWLER ~~~~~~~~~~')

        starting = raw_input("Starting Url: ")
        target = raw_input('Target Domain: ')
	down_delay = int(input('Download Delay [Default: 0]: '))

        #Sets settings of the crawler. Currently only supports 'DOWNLOAD_DELAY'
	process = CrawlerProcess({
			'DOWNLOAD_DELAY': '{}'.format(down_delay)})

	#Starts the crawler with the set attributes
        process.crawl(DomainSpider, start_urls='{}'.format(starting), target='{}'.format(target))
        process.start()
	
	remove_highlights()
	delete_duplicates(target)
	       
	#Highlights what links has been added
	highlight_history()	

	#Deletes duplicates in the file	
	delete_duplicates(target)
	
     	call(['sort', 'output.txt', '-o', 'output.txt'])


main()
