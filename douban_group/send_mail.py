#coding:utf-8
__author__ = 'JYC103'
import smtplib,os
from email.mime.text import MIMEText
from email.header import Header
from douban_zufang import get_tiezi

HOST = 'smtp.163.com'
FROM = os.environ.get('MAIL_USERNAME')
PASSWD = os.environ.get('MAIL_PASSWORD')
SUBJECT = Header('爬取豆瓣租房小组信息',charset='utf-8')
TO = 'juanmao_love@126.com'

def makemail(tiezi):
    txt = '<html><body>%s Context<br></body></html>' %tiezi
    msg = MIMEText(txt,_subtype='html',_charset='utf-8')
    #msg = MIMEText("%s" %tiezi,_subtype='plain',_charset='utf-8')
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = TO
    print msg.as_string()
    print repr(msg.as_string())
    return msg

def main():
    msg = makemail(tiezi=get_tiezi())
    server = smtplib.SMTP()
    server.connect(HOST,25)
    server.login(FROM,PASSWD)
    server.sendmail(FROM,TO,msg.as_string())
    server.quit()

if __name__=="__main__":
    main()