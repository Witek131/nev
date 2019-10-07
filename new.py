# coding: utf-8
import random
def make_bingo():
    s = []
    n = random.randint(1, 75)
    for i in range(5):
        s.append(set())
        while len(s[i]) < 5:
            
            s[i].add(n)            
            n = random.randint(1, 75)
        if i == 2:
            s[i] = list(s[i])
            s[i][2] = 0
        s[i] = tuple(s[i])
    return(tuple(s))
