# d={1:2,"a":"apple",4:16}
# res=d.setdefault(3,"three")
# print(res,d)
# res=d.pop(1)
# print(res,d)

d={}
l=[1,"a",2,"b",3]
# res=d.fromkeys(l,5)  #{1: 5, 'a': 5, 2: 5, 'b': 5, 3: 5}
# res1={}.fromkeys([1,2,3],"py")  #{1: 'py', 2: 'py', 3: 'py'}
res2={}.fromkeys("rat","py")  #{'r': 'py', 'a': 'py', 't': 'py'}
print(res2)