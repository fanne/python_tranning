__author__ = 'JYC103'
#coding:utf-8
import requests,sys,configparser,json,html2text
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding( "utf-8" )

def zhihu_login():
    global get_cookies
    login_url = r'http://www.zhihu.com/login'
    login_request = requests.get(login_url)
    login_request.encoding='utf-8'

    login_text = BeautifulSoup(login_request.text)
    xsrf = login_text.find("input",{"name":"_xsrf"})['value']

    cf = configparser.ConfigParser()
    cf.read("config.ini")
    email = cf.get("info","zhihu_email")
    password = cf.get("info","zhihu_password")

    headers = {
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.8",
        'Connection': "keep-alive",
        'Host':"www.zhihu.com",
        'Referer':"http://www.zhihu.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest"
    }
    loginfo = {'_xsrf':xsrf,
               'email':email,
               'password':password,
               'rememberme':'y'}

    login_session = requests.session()
    login = login_session.post(login_url,headers=headers,data=loginfo,timeout=10)
    get_cookies = login.cookies

    if login.status_code == 200 and login.json()["r"] != 1:
        print "Login secesse!"
        #return get_cookies
    else:
        print "Login fail"
        exit(1)

def content(url):
    get_one_page=requests.get(url,cookies=get_cookies)
    get_one_page.encoding='utf-8'
    json_one_page=get_one_page.json()
    page_txt=json_one_page['content']
    md_page_txt=html2text.html2text(page_txt)
    print md_page_txt
    print '\n'
    return md_page_txt

def zhuanlan_article():
    Zhuanlan_Url=r'http://zhuanlan.zhihu.com'
    for i in range(50):
        Zhuanlan_api_url=r'http://zhuanlan.zhihu.com/api/columns/agBJB/posts?limit=10&offset=%s' %((i)*10)
        get_next_page=requests.get(Zhuanlan_api_url,cookies=get_cookies)
        next_page_json=get_next_page.json()
        if get_next_page.status_code == 200 and len(next_page_json) == 10:
            #print page_url
            for i_json in range(len(next_page_json)):
                i_json
                print next_page_json[i_json]['title']
                page_title=next_page_json[i_json]['title']
                print Zhuanlan_Url+next_page_json[i_json]['url']
                href_url =  Zhuanlan_Url+next_page_json[i_json]['href']
                f=open('article_dir/%s' %page_title,'w')
                f.write(content(href_url))
                f.close()
                content(href_url)
        else:
            exit(1)

if __name__=='__main__':
    zhihu_login()
    zhuanlan_article()









