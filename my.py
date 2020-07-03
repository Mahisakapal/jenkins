num=[1,2,3,4,9,8,7,6,5]

for i in num:
    
    print (i)
print("               this is new list            ")
i =0 

while i < len(num):
    i+=1
    
    print(i)
print("               this is new list            ")


num1 = [[1, 2, 3,], [8, 9, 7], [4, 6, 5]]

print(num1[1])
print("               this is new list            ")


for sublist in num1:
    for i in sublist :
        print(i, end = "")   # here we use , end = "" to print in on row or in line 


