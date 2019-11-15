#!/usr/bin/python3

# -*- coding:utf-8 -*-
import io
import sys
import requests
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# chaihezi正在发售
url = 'http://www.chaihezi.com/node/category/on_sale/'
nexturl = url
comment = 1
with open('chaihezisold.csv', 'a', encoding='utf-8') as f1:
    f1.write('title,description,thumb,link,detail,thumbs,orderlink,price,time\n')
    while True:
        print("第"+str(comment)+'页'+"===================")
        html = requests.get(nexturl, allow_redirects=False).content
        pages = etree.HTML(html)
        # 配图
        pictures = pages.xpath(
            './/div[@class="post-row"]/article/div/div[1]/a/img/@data-lazy-src')
        # 标题
        title = pages.xpath(
            './/div[@class="post-row"]/article/div/h2[@class="post-title"]/a/@title')
        # 原文链接
        links = pages.xpath(
            '..//div[@class="post-row"]/article/div/div[1]/a/@href')
        description = []
        # 简介
        descriptions = pages.xpath('.//div[@class="entry excerpt"]//text()')
        price = []
        for i in descriptions:
            res = ''
            for j in range(len(i)):
                line = i[j].strip()
                if line != '':
                    res += line
            res = res.replace(',', '，')
            description.append(res)
        pictures_all = []
        orderlink_all = []
        date_all = []
        detail_alls = []
        for link in links:
            html = requests.get(link).content
            pages = etree.HTML(html)
            print(link)
            # 订购链接
            orderlinks = pages.xpath(
                './/div[@class="entry-inner"]/table//a/@href')
            orderlinks = ' '.join(map(str, orderlinks))
            orderlink_all.append(orderlinks)
            # 发布时间
            date = pages.xpath('.//div[@class="post-inner group"]/p[1]/text()')
            # 详情内容
            detail = pages.xpath('.//div[@class="entry-inner"]/p//text()')
            # 详情中配图
            picturesall = pages.xpath(
                './/div[@class="entry-inner"]//p/a/img/@data-lazy-src')
            picturesall = ' '.join(map(str, picturesall))
            pictures_all.append(picturesall)
            detail_all = ''
            for deta in range(len(detail)):
                line = detail[deta].strip()
                if line != '':
                    detail_all += line
                detail_all = detail_all.replace(',', '，')
            detail_alls.append(detail_all)
            res = ''
            for i in range(len(date)):
                line = date[i].strip()
                if line != '':
                    res += line
                res = res.replace('by· ', '')
            date_all.append(res)
            pric = ''
            price.append(pric)
        print(pictures_all)
        print(orderlink_all)
        print(date_all)
        print(detail_alls)

        for i in range(len(title)):
            sold = {
                'url': title[i],
                'description': description[i],
                'pictures': pictures[i],
                'links': links[i],
                'detail_alls': detail_alls[i],
                'pictures_all': pictures_all[i],
                'orderlink_all': orderlink_all[i],
                'price': price[i],
                'date_all': date_all[i]

            }
            f1.write(sold['url'] + ',')
            f1.write(sold['description'] + ',')
            f1.write(sold['pictures'] + ',')
            f1.write(sold['links'] + ',')
            f1.write(sold['detail_alls'] + ',')
            f1.write(sold['pictures_all'] + ',')
            f1.write(sold['orderlink_all'] + ',')
            f1.write(sold['price'] + ',')
            f1.write(sold['date_all'] + '\n')

        html = requests.get(nexturl).content
        pages = etree.HTML(html)
        # 翻页
        nexts = pages.xpath(
            './/div[@class="wp-pagenavi"]/a[@class="nextpostslink"]/@href')
        if len(nexts) == 0:
            # final page
            break
        else:
            next = nexts[0]
            if next == nexturl:
                break
            else:
                nexturl = next
                comment += 1


f1.close()
