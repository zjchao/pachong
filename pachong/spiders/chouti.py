# -*- coding: utf-8 -*-
import scrapy
from  ..items import PachongItem
from scrapy.http.request import Request
from scrapy.selector import HtmlXPathSelector
from  scrapy.http.response.html import HtmlResponse
class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['https://dig.chouti.com/']
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback = self.parse,
                          meta={'cookiejar':1},

                          )

    def my_parse(self,response):

        print(response)
        # print(type(response))
        # print(type(response.request))
        # print(response.request)  # 将请求对象也封装在了response中
        # print(response.url)   #  请求的url
        # print(response.headers)  # 响应的头
        # print(response.headers['Set-Cookie'])  # 原始cookies
        # print('*'*80)
        # print(response.status)

        # self.cookie = response.headers.getlist('Set-Cookie')
        # pages = response.xpath('//div[@id="page-area"]//a[@class="ct_pagepa"]/@href').extract()
        # for page_url in pages:
        #     page_url = "https://dig.chouti.com" + page_url
        #     print(page_url)
        #     yield Request(url=page_url, callback=self.parse)
        # from scrapy.http.cookies import CookieJar
        # cookiejar = CookieJar()
        # cookiejar.extract_cookies(response,response.request)
        # for k,v in cookiejar._cookies.items():
        #     for i, j in v.items():
        #         for m, n in j.items():
        #             self.cookie_dic[m] = n.value
        # yield Request(url='https://dig.chouti.com/login',
        #                 method='POST',
        #               headers={'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'},
        #               body='phone=8618703822417&password=chao124.&oneMonth=',
        #               callback=self.check_login,
        #               # cookies=self.cookie_dic
        #               meta={'cookiejar':response.meta['cookiejar']}
        #               )
        # base_url = 'https://dig.chouti.com/link/vote?linksId='
        # #
        # up_list = response.xpath('//*[@id="content-list"]/div[@class="item"]//div[@class="part2"]/@share-linkid').extract()
        # for i,url in enumerate(up_list) :
        #     up_url = base_url+url
        #     yield Request(
        #         url=up_url,
        #         method='POST',
        #         headers={'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'},
        #         # cookies=self.cookie_dic,
        #         # meta={'cookiejar':response.meta['cookiejar']},
        #         meta={'cookiejar':response.meta['cookiejar']},
        #         callback=self.up_show
        #     )
    def check_login(self,response):

        # from scrapy.http.cookies import CookieJar
        # cookiejar = CookieJar()
        # cookiejar.extract_cookies(response, response.request)
        # temp = {}
        # for k, v in cookiejar._cookies.items():
        #     for i, j in v.items():
        #         for m, n in j.items():
        #             temp[m] = n.value
        # self.cookie_dic.update(temp)
        # print(self.cookie_dic)

        print(response.text)

    def up_show(self, response):
        # self.cook = response.meta['cookiejar']
        # print(self.cook)
        # print('*' * 100)
        print(response.text)


    def parse(self, response):
        # print(response.text)
        # hxp = HtmlXPathSelector(response)
        # a1 = response.xpath('//*[@id="newsContent19444831"]/div[1]/a[1]/text()').extract_first().strip()
        # a2 = response.xpath('//*[@id="newsContent19444831"]/div[1]/a[1]/@href').extract_first()
        a3 = response.xpath('//*[@id="content-list"]/div//a[@class="show-content color-chag"]')
        # a4 = response.xpath('//*[@id="content-list"]/div//a[@class="show-content color-chag"]/text()').extract()
        for a_ele in a3:
            href = a_ele.xpath('./@href').extract_first()
            text = a_ele.xpath('./text()').extract_first()
            item = PachongItem(href =href,text = text.strip() )
            yield item
            yield Request(url='https://dig.chouti.com/', callback=self.my_parse,
                          meta={'cookiejar': 1},

                          )
        # pages = response.xpath('//div[@id="page-area"]//a[@class="ct_pagepa"]/@href').extract()
        # for page_url in pages:
        #     page_url = "https://dig.chouti.com" + page_url
        #     print(page_url)
        #     yield Request(url=page_url, callback=self.parse)


