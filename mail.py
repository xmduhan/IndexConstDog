# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import path
from os.path import expanduser
import smtplib


def sendMail(receivers,title,content,attachments=[]):
    '''
    功能：
    发送邮件
    
    参数说明:
    receivers 接受者列表，list格式
    title 标题
    content 内容
    attachments 附件列表，list格式
    如何发送成功返回True，否则抛出异常
    
    配置文件：
    该方法使用前需要配置邮件服务器的地址和用户密码，配置文件保存在用户根目录下的.dautils_profile，具体配置案例如下：
    ... ... 
    smtpServer=smtp.domian.com 
    smtpPort=25
    smtpUser=username
    smtpPassword=*********
    smtpSender=username@domian.com
    ... ...
    '''
    try:
        home = expanduser('~')
        profile = path.join(home, '.dautils_profile')
        config = dict(line.strip().split('=') for line in open(profile) if line.find('=') != -1)
        smtpServer = config['smtpServer']
        smtpPort = config['smtpPort']
        smtpUser = config['smtpUser']
        smtpPassword = config['smtpPassword']
        smtpSender = config['smtpSender']
    except Exception as e:
        print u'读取配置信息发生错误，请在您用户的根目录(%s)下添加一个名为".dautils_profile"，并配置相关内容，具体查看sendMail方法帮助。 ' % home
        raise 
    
    # 创建一个带附件的实例
    message = MIMEMultipart()
    
    # 创建内容部分的
    contentPart = MIMEText(content,_subtype='html',_charset='utf-8')
    message.attach(contentPart)
    
    # 创建附件部分
    for filename in attachments:
        # 获取不含路径的文件名
        fn = path.split(filename)[-1]
        attMimeText = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        attMimeText["Content-Type"] = 'application/octet-stream'
        attMimeText["Content-Disposition"] = 'attachment; filename="%s"' % fn
        message.attach(attMimeText)    
    
    #加邮件头
    message['to'] = ','.join(receivers)
    message['from'] = smtpSender
    message['subject'] = title
    
    #发送邮件
    smtp = smtplib.SMTP(smtpServer, smtpPort)
    smtp.login(smtpUser,smtpPassword)
    smtp.sendmail(smtpSender,receivers,message.as_string())
    smtp.quit()
    
    # 返回成功
    return True
    
