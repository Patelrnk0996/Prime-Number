# Prime is a diveded by itself and 1.

a = int(input("Enter The Number: "))
# for loop ma a ni value suthi divided kari jose jo divesible hoy to te not prime
for i in range(2, a):
    if a%i==0:
        print("Not Prime Number")
        break         # jo a divisible hoy to te prime number print karya j karse etle ek var not prime
                        # number mali jay to pachi break thai jay
else:
    print("Prime Number")





#------------Method - 2------------
# import time
# def is_Prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n % i==0:
#             return False
#     return True
#
# t0 = time.time()
# c = 0
#
# for n in range(1, 10000):
#     x = is_Prime(n)
#     c += x
# print("Total prime numbers in range :",c)
#
# t1 = time.time()
# print("Time required :",t1 - t0)
