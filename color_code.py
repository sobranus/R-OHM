# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 09:32:43 2022

@author: ASUS
"""
import random

# c_random = random.randint(0, 11)
not_o = (10, 11)
not_e = (0, 3, 4, 9)

# print(c_random)
# if c_random not in not_o:
#     print(c_random)

# print(c_random)
# N = c_random

RC = {
0: (0, 0, 0),
1: (102, 51, 0),
2: (255, 0, 0),
3: (255, 128, 0),
4: (255, 255, 0),
5: (0, 255, 0),
6: (0, 0, 255),
7: (102, 0, 102),
8: (100, 100, 100),
9: (255, 255, 255),
10: (200, 175, 0),
11: (210, 210, 210)
}

c1 = 0
c2 = 0
c3 = 0
c4 = 0
e_c = (1, 2, 5, 6, 7, 8, 10, 11)

for i in range(4):
    if c1 == 0:
        c_random = random.randint(0, 9)
        c1 = c_random
        continue
    if c2 == 0:
        c_random = random.randint(0, 9)
        c2 = c_random
        continue
    if c3 == 0:
        c_random = random.randint(0, 11)
        c3 = c_random
        continue
    if c4 == 0:
        c_random = random.choice(e_c)
        c4 = c_random
        
print(c1, c2, c3, c4)
    

# print(RC[N])