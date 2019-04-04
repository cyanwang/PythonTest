# coding=utf-8
#列表操作，列表的的数据没有限制
def ListAction():
    list1=['a',1,'20',2,5+6]
    for l in list1:
        print(l)
    #给list添加数据
    list1.append(3)
    list1.remove(list1[2])
    list1.reverse()#反转
    list1.insert(0,'cyan' )#再指定位置输入数据
    print(list1)
    print("输出的是："+list1.pop())#输出最后一个

#元祖不同之处在于元组的元素不能修改。
def TupAction():
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5, 6, 7 )
    tup=tup1+tup2
    print(tup)
    # 以下修改元组元素操作是非法的。
    # tup1[0] = 100
def dictAcrion():
    dict = {'a': 1, 'b': 2, 'b': '3'}  
    print(dict['b']) 
    print(dict)
    print(dict['a'])
#键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下实例：
dictAcrion()
    
    