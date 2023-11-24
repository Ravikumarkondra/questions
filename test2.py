# 3. prime number code

# a = int(input("enter a number : "))
# i,temp =0, 0
# for i in range(2,a//2):
#     if a%2 == 0 :
#         temp = 1
#         break
# if temp == 1 :
#     print("given number is not prime : ")
# else :
#     print("given number is prime : ")    


# 2. method 2

for i in range(2,101) :

        for j in range(2,101):
            if (i%j) == 0:
                break

        if i == j:
                print(i, end=',') 


# 3. method 3