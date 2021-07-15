import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

# ============���巢���ʼ�============

def send_mail(file_new):

    smtpserver = "smtp.qq.com"      
    port = 465                     
    sender = "837548605@qq.com"   
    psw = "wopkzlwdwavlbdif"       
    receiver = "2240531513@qq.com" 

    # =========�༭�ʼ�����=========
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
   
    msg = MIMEMultipart()
    msg["from"] = sender    
    msg["to"] = receiver    
    msg["subject"] = "赵杭大傻逼"  

   
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)   

    
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'  
    msg.attach(att)    

    
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())    
    smtp.quit()     


