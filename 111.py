# 请你补充代码，让两位囚徒输入自己的选择，将其存成变量a,b
end1 =  1
'''认罪'''
end2 = 2
'''抵赖''' 
name = ['张三','李四','王五']
a = {}

#for i in range a:
    
print(type(name))    
   
while True:
    for i in name :
        b = input('你认罪吗')
        a[i] = b
        print(a)
    if a['张三'] == end1 and a['李四'] == end1:
        print('两人各判10年')
        break
    elif a['张三'] == end2 and a['李四'] == end2:
        print('各判3年')
        break
    elif a['张三'] == end2 or a['李四'] ==end2 :
        if a['张三'] == end2:
            print('张三判二十年')
            break
        else :
            print('李四判十年')
            break

    break
    #避免死循环
    #hahahhhhhhahah

