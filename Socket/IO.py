# coding=utf-8
try:
   f = open('D:/Cyan/Test.txt', 'r')
   #print(f.readline())#这个是一个列表，['haha  ha\n', '1212\n', '12121   我的\n', '打完球回家   等我回去']

   for line in f.readlines():
         print("这行的内容是:"+line.replace(' ',''))
         
   f = open('D:/Cyan/Test.txt', 'w')
   f.add('Hello, world!')
   f.close()


except Exception as e:
   print(e)
a="  hello"
print(a.strip())
#python 的strip函数没有办法出去中间的空格
