#coding:utf-8
__author__ = 'JYC103'

import requests,re,json,html2text,sys,time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


url = r'http://www.douban.com/group/tianhezufang/'
nowtiem = time.strftime('%m-%d %H:%M',time.localtime(time.time()))
#print nowtiem



def get_tiezi():
    get_url = requests.get(url)
    print get_url.status_code
    soup = BeautifulSoup(get_url.text)
    soup_olt = soup.find_all("table",class_="olt")
    soup_tr = soup.find_all("tr",class_="")
    a_list = soup.find_all('a')
    b_list = soup.find_all("tr",class_="")
    abc = u'天河'.decode('utf-8')
    title_href_str=''
    for i in b_list:

        if len(i.contents) > 1 and abc in i.td.a.get('title'):
            tiezi_time = (unicode(i.contents[-2].string)).encode('utf-8')
            i_title = i.td.a.get('title')
            i_href = i.td.a.get('href')
            str_i_title = i_title.encode('utf-8')
            str_i_href = i_href.encode('utf-8')
            title_href = '<a href="%s">%s</a><br>' %(str_i_href,str_i_title)
            title_href_str = title_href_str+'\n'+title_href
    #print "title_href_str is: %s" %title_href_str
    return title_href_str



# if __name__=='__main__':
#     get_tiezi()






