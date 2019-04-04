# coding=utf-8
import os 
pid=os.fork()#不是linux系统。没有fork()函数
if(pid==0):#代表这个是子进程
   print("我是子进程：%s",os.getpid())
else:
    print("我是父进程")
    