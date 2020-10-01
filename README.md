# Prime-Number
Generate The Prime Number
# Try New Method

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
