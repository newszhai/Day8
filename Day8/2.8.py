def get_sun(num):
    s=0
    for i in range(1,num+1):
        s+=i
    print(f'1到{num}之间的累加和为：{s}')

#函数的调用
get_sun(10)#1-10之间的和
get_sun(100)#1-10之间的和
get_sun(1000)#1-10之间的和
