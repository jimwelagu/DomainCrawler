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

5. Set up Crawler Settings 

   `[1]` Crawler Settings

6. Run the Crawler

   `[5]` Run!
   
## Example
`python activate.py`

```
*************DOMAIN CRAWLER*************
[1] Crawler Settings
[2] View Links
[3] View HTTP Headers
[4] Clear Links
[5] Run!
[6] Exit

Enter Number: 4
```

```
*************DOMAIN CRAWLER*************
[1] Crawler Settings
[2] View Links
[3] View HTTP Headers
[4] Clear Links
[5] Run!
[6] Exit

Enter Number: 1
``` 

```
****************************************
Starting Url: https://twitter.com   
Target Domain: twitter.com
Download Delay [Default: 0]: 0
```
```
*************DOMAIN CRAWLER*************
[1] Crawler Settings
[2] View Links
[3] View HTTP Headers
[4] Clear Links
[5] Run!
[6] Exit

Enter Number: 5
```

```
****************************************
//dev.twitter.com

http://m.twitter.com

https://about.twitter.com

https://apps.twitter.com

https://blog.twitter.com

........
```


### Features
+ Highlight changes when running the crawler multiple times
+ View HTTP headers 
