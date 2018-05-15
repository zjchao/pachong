# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import Mp4Item
# from ..items import MyImgItem
import json

# class Xiaohua100Spider(scrapy.Spider):
#     name = 'xiaohua100'
#     allowed_domains = ['mm131.com']
#     start_urls = ['http://www.mm131.com/xiaohua/1805.html']
#
#     def parse(self, response):
#         img_list = response.xpath('//div[@class="content-pic"]//img/@src').extract()
#         path_list = response.xpath('//div[@class="content-pic"]//img/@alt').extract()
#         # print(path_list)
#         # item 的参数均为列表
#         yield MyImgItem(image_urls=img_list,image_paths=path_list)
#         next_url = 'http://www.mm131.com/xiaohua/'+ response.xpath('//a[text()="下一页"]/@href').extract_first()
#         # print(next_url)
#         yield Request(next_url,callback=self.parse)

class Xiaohua100Spider(scrapy.Spider):
    name = 'xiaohua100'
    allowed_domains = ['mm131.com']
    start_urls = ['http://dv.browser.360.cn/Object.access/upload4cutter/NDQ3NTk2Zjg3MTI2YjhiMGM3ZjVmOTFkOTNjMjUxZjMv6Iue57Gz5ZywLm1wNA==']
    def parse(self, response):
        # img_list = response.xpath('//div[@class="content-pic"]//img/@src').extract()
        # img_list = 'http://dv.browser.360.cn/Object.access/upload4cutter/NDQ3NTk2Zjg3MTI2YjhiMGM3ZjVmOTFkOTNjMjUxZjMv6Iue57Gz5ZywLm1wNA=='
        mp4 = response.body
        path_list = 'haha'
        # print(path_list)
        # item 的参数均为列表
        yield Mp4Item(mp4=mp4,name=path_list)
        # next_url = 'http://www.mm131.com/xiaohua/'+ response.xpath('//a[text()="下一页"]/@href').extract_first()
        # # print(next_url)
        # yield Request(next_url,callback=self.parse)

