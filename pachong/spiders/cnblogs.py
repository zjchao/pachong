# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy import Request

from ..items import PachongItem
from ..items import MyImgItem

class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.mm131.com/qingchun/']

    # start_urls = ['http://www.cnblogs.com/post/prevnext?postId=5433925&blogId=133379&dateCreated=2016/4/26%2010:03:00&postType=2']
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url,callback=self.parse)
    # def parse(self, response):
    #     if  '/articles/' in  response.url:
    #         title = response.xpath('//*[@id="cb_post_title_url"][1]')
    #         yield PachongItem(text = title.xpath('text()').extract_first(),
    #                           href = title.xpath('@href').extract_first()
    #                           )
    #         text = response.xpath('//script[re:test(text(),"cb_blogId=")]/text()').extract_first()
    #         ret = re.search("cb_blogId=(\d+),cb_entryId=(\d+),.*?cb_entryCreatedDate='(.*)'", text).groups()
    #         url = 'http://www.cnblogs.com/post/prevnext?postId={1}&blogId={0}&dateCreated={2}&postType=2'.format(*ret)
    #         yield Request(url=url,callback=self.parse)
    #     else:
    #         a_list = response.xpath('//a[@title]')
    #         for a_ele in a_list:
    #             href = a_ele.xpath('@href').extract_first()
    #             yield Request(url=href,callback=self.parse)



    def parse(self, response):
        img_list = response.xpath('//*[@id="cnblogs_post_body"]/p[6]/img/@src').extract()
        print(img_list)
        url_list = [ img_url for img_url in img_list ]
        yield MyImgItem(image_urls=url_list)


