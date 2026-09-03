l = [23,45,56,78,90,33,44]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
         sum=sum+i
         print(i,l[i])
         print(sum)
         
n = int(input("Enter the number:"))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"Factorial of {n} is {fact}")

data = {}
n = int(input("Enter the no of students:"))
max_marks = 0
for i in range(n):
    name = input("Enter the name:")
    marks = int(input("Enter the marks:"))
    if marks > max_marks:
        max_marks = marks
        data[name] = marks
        print(data)
        print("Maximum Marks:", max_marks)

bill = {}
total_price = 0
n = int(input("enter the no of items:"))
for i in range(n):
         item = input("enter the items name:")
         price = int(input("enter the price:"))
         qty = int(input("enter the qunatitiy:"))
         bill[item] = [price, qty]
         final_price = price * qty
         total_price += final_price
         print(f"Total for {item}: {final_price}")
         print(bill,total_price)

          