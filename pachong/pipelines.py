# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class FilePipeline(object):

    def __init__(self,path):
        self.path = path

    @classmethod
    def from_crawler(cls,crawler):
        path = crawler.settings.get('QM_FILE_PATH')
        return cls(path)

    def process_item(self, item, spider):
        self.f.write(item['mp4'])
        self.f.flush()
        return item
    def open_spider(self,spider):
        self.f = open(self.path,'wb')

    def close_spider(self,spider):
        self.f.close()
        pass


class DBPipeline():

    def __init__(self,conn):
        self.conn = conn

    @classmethod
    def from_crawler(cls,crawler):
        import pymysql
        conn = pymysql.connect(host='127.0.0.1',password='123',port=3306,db='s10',user='root',charset='utf8')
        # pool = crawler.settings.get('MYSQLPOOL')
        return cls(conn)

    def process_item(self,item,spider):
        print(item['href'],item['text'])
        self.cursor.execute('insert into url (url,title) VALUES (%s,%s)',(item['href'],item['text']))

        return item
    def open_spider(self,spider):
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.conn.commit()
        self.conn.close()


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={'item':item,'index':item['image_urls'].index(image_url)})

    # 重写了原来类中的图片名称
    def file_path(self, request, response=None, info=None):
        item = request.meta.get('item')
        index = request.meta.get('index')
        return  'full/%s.jpg'%item['image_paths'][index]
    # 重写了原来类中的缩略图名称
    def thumb_path(self, request, thumb_id, response=None, info=None):
        item = request.meta.get('item')
        index = request.meta.get('index')
        return 'thumbs/%s/%s.jpg' % (thumb_id,item['image_paths'][index])

