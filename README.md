# DomainCrawler

## Description
The following webcrawler will search for all links under a target domain. The web crawler utilizes [Scrapy](https://scrapy.org/), applicaton framework for writing web spiders that crawl through the web.

## Get Started
1. Download and Install 
 
   + [Scrapy](https://doc.scrapy.org/en/latest/intro/install.html) 
 
   + [py-term](https://github.com/gravmatt/py-term)
 
   + or Install using pip `pip install -r requirements.txt`

2. Navigate to the spider's directory

    `cd webcrawler/spider/`

3. Run the webcrawler

    `python activate.py`

4. Make sure list of links is empty
`[4]` Clear Links

## Example
`python activate.py`
```
Starting URL: https://twitter.com
Target Domain: twitter.com
Download Delay [Default: 0]: 0
```
`cat output.txt`
```
/dev.twitter.com
http://m.twitter.com
https://about.twitter.com
https://apps.twitter.com
https://blog.twitter.com
.....
```
### Features
+ Highlight changes when running the crawler multiple times
