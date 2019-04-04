# coding utf-8 

import smtplib 
from email.mime.text import MIMEText
from email.utils import formataddr
import email.mime.multipart
import email.mime.text

my_sender="1825705216@qq.com"  # 发件人邮箱账号
my_pass = "ymvnfowjbhzichih"     # 发件人邮箱密码(注意这个密码不是QQ邮箱的密码，是在QQ邮箱的SMTP中生成的授权码)
my_user="2788653649@qq.com"    # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
      
        msg = MIMEText('Python 邮件发送测试...')
        msg=email.mime.multipart.MIMEMultipart()         
        msg['From']=formataddr(["cyan",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["嗯",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="Python邮件发送请求"                # 邮件的主题，也可以说是标题
      
        #server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25        
        server = smtplib.SMTP()
        print("1")
        server.connect("smtp.qq.com", 25)    # 25 为 SMTP 端口号
        print("1")
        server.login(my_sender,my_pass.encode)  # 括号中对应的是发件人邮箱账号、邮箱密码
        print("2")
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        print("3")
        server.quit()  # 关闭连接
    except smtplib.SMTPException as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
        print(e)
    return ret
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")