#.1
# def cj(a,b,c,d):
#     s = [a,b,c,d]
#     e = sorted(s)
#     best = e[3]
#     count = 0
#     for i in s:
#         if i >= best - 10:
#             print('student %d score is %s and grade is A'%(count,i))
#             count += 1
#             continue
#         if i >= best - 20:
#             print('student %d score is %s and grade is B'%(count,i))
#             count += 1
#             continue
#         if i >= best - 30:
#             print('student %d score is %s and grade is C'%(count,i))
#             count += 1
#             continue
#         if i >= best - 40:
#             print('student %d score is %s and grade is D'%(count,i))
#             count += 1
#             continue

# cj(40,55,70,58)

#.2
# def nx():
#     a = [1,4,2,6,3,7,10,20,15]
#     b = sorted(a,reverse=True)
#     print(b)
# nx()

#.3
# a = [2,5,6,5,4,3,23,43,2]
# b = []
# count = 1
# for i in a:
#     if i not in b:
#         b.append(i)
# for j in range(len(b)):
#     print(b[j])
   


#.5
# import random
# c = []
# a = 0
# b = 0
# c = 0
# d = 0
# e = 0
# f = 0
# g = 0
# h = 0
# i = 0
# j = 0
# for x in range(1000):
#     s = random.randint(0,9)
#     if s == 0:
#         a += 1
#     if s == 1:
#         b += 1
#     if s == 2:
#         c += 1
#     if s == 3:
#         d += 1
#     if s == 4:
#         e += 1
#     if s == 5:
#         f += 1
#     if s == 6:
#         g += 1
#     if s == 7:
#         h += 1
#     if s == 8:
#         i += 1  
#     if s == 9:
#         j += 1    
# print(a,b,c,d,e,f,g,h,i,j,)
#.6
# def a(a,b,c,d,e,f,g,h,i,j):
#     b = [a,b,c,d,e,f,g,h,i,j]
#     s = b.index(min(b))
#     print(s)
# a(10,5,6,5,1,3,23,43,1,40)
#.7
# import random
# def a(a,b,c,d,e,f,g,h,i,j):
#     x = [a,b,c,d,e,f,g,h,i,j]
#     random.shuffle(x)
#     print(x)
# a(1,2,3,4,5,6,7,8,9,10)
#.8
# def a(a,b,c,d,e,f,g,h,i,j):
#     a = [a,b,c,d,e,f,g,h,i,j]
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)
#     print(b)
# a(1,2,3,2,1,6,3,4,5,2)
# #.9
# def a(a,b,c,d,e,f,g,h,i,j):
#     a = [a,b,c,d,e,f,g,h,i,j]
#     if a == sorted(a):
#         print('the list is already sorted')
#         return True
#     else:
#         print('the list is not sorted')
# a(1,2,3,4,5,6,7,8,9,10)
#.10
# def p(a,b,c,d,e,f,g,h,i,j):
#     x = [a,b,c,d,e,f,g,h,i,j]
#     for k in range(9):
#         for m in range(9 - k):
#             if x[m] > x[m + 1]:
#                 t = x[m]
#                 x[m] = x[m + 1]
#                 x[m +1 ] = t
#                 continue
#     print(x)
# p(10,2,3,11,22,8,7,6,9,1)
