#使用小括号创建元组
t=('hello',[10,20,30],'python','world')
print(t)

#使用内置函数tuple()创建数组
t=tuple('helloworld')
print(t)

t=tuple([20,30,40,10])
print(t)

print('10在元组中是否存在',(10 in t))
print('10在元组是不存在',(10 not in t))
print('最小值：',max(t))
print('最大值：',min(t))
print('len',len(t))
print('t.index',t.index(10))
print('t.count',t.count(10))

t=(10)
print(t,type(t))

y=(10,)
print(y,type(y))