# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def __init__(self):
        self.f = open('file.user.txt', 'w')

    def process_item(self, item, spider):
        # with open('file/user.txt', 'w') as f:
        #     for user in item:
        #         print 'user:' + user
        #         f.write('http://github.com' + user + '\n');
        # f.close()
        self.f.write(item + '\n')
        return item
