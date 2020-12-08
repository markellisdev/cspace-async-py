import scrapy
import random
from scrapy.exporters import JsonLinesItemExporter
from imagescrapy.items import KittenImage

urls=[]
# generate random pairs for images to place in urls above
randomlist = []
for i in range(0,128):
    # n = random.randint(1,1000)
    s =  'https://placekitten.com/{}/{}'.format(random.randint(1,1000), random.randint(1,1000))    
    urls.append(s)
print(urls)
# print(random.choice(randomlist))

# create string for images
# for i in range(0,5):
#     s =  'https://placekitten.com/{}/{}'.format(random.choice(randomlist), random.choice(randomlist))
    # print("s is: ", s)

class QuotesSpider(scrapy.Spider):
    name = "image_spider"


#### Actually don't have to use the start_requests function since it's built in. Can just use start_urls
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    start_urls = [
        'https://placekitten.com/200/300',
    ]

#### Parse to actually gather targeted info
    # def parse(self, response):

    #     		# grab the URL of the image
    #     img = response.css("img").xpath("@src")
    #     imageURL = img.extract_first()
    #     print(imageURL)
    # def parse (self, response):
    #     url= response.css("//img")
    #     yield KittenImage(image_urls=[url.xpath('@src').extract_first()])

    def parse(self, response):
        # img_urls = urls
        # yield KittenImage(image_urls=[img_urls])
        item = KittenImage()
        img_urls = urls
        item['image_urls'] = img_urls
        return item

        		# yield the result
        # yield KittenImage(image_urls=[imageURL])
