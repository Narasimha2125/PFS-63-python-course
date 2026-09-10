# greater = lambda a,b: a if a>b else b
# print(greater(12,14))
# print(greater(25,65))
# print(greater(45,36))
# print(greater(21,18))

# wish = lambda name: f'Welcome to the hotel {name}'
# print(wish("Baireddy"))
# print(wish("Narasimha"))
# print(wish("Reddy"))

# iseven = lambda n: "even" if n%2==0 else "odd"
# print(iseven(34))
# print(iseven(43))
# print(iseven(54))

# avg = lambda a,b,c: (a+b+c)/3
# print(avg(1,2,3))
# print(avg(44,55,66))
# print(avg(777,888,999))

# domain = lambda mail: (mail.split('@')[-1]).split('-')[0]
# print(domain('narsimha@codegnan.com'))
# print(domain('narsimha@gmail.com'))
# print(domain('narsimha@outlook.com'))

# gst = lambda price : price + price*0.18
# print(gst(1000))
# print(gst(5000))
# print(gst(10000))

# prices = [5467,9754,2345,645,607,3256]
# res = list(map(lambda price : price + price*0.18,prices))
# print(res)

# names = ['Baireddy','narasimha','Reddy']
# res = list(map(lambda name: name.title(),names))
# print(res)

# prices = [3245,9364,2432,8075,100,5467]
# res = list(map(lambda price : price - price*0.3,prices))
# print(res)

# prices = [3245,9364,2432,8075,100,5467]
# res = list(filter(lambda price : price>5000,prices))
# print(res)

# prices = [3245,9364,2432,8075,100,5467]
# res = list(filter(lambda price : price%2==0,prices))
# print(res)

# names = ['Baireddy','narasimha','Reddy']
# res = list(filter(lambda name : len(name)>5,names))
# print(res)

# from functools import reduce 
# l = [1,2,54,764,7543,23,864,5,]
# res = reduce(lambda sum,i:sum+i,l)
# print(res)

# names = ['Baireddy','narasimha','Reddy']
# res = reduce(lambda res,i : res+' '+i,names)
# print(res)

# products = {'sugar':60,
#             'salt':10,
#             'bread':40,
#             'cooking oil':160,
#             'eggs':50
#             }
# print(dict(sorted(products.items())))
# print(dict(sorted(products.items(),reverse=True)))
# print(dict(sorted(products.items(),key = lambda i:i[1])))
# print(dict(sorted(products.items(),key = lambda i:i[1],reverse=True)))