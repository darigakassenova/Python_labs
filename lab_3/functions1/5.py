from itertools import permutations
def func(s):
    a = list(s)
    p = list(permutations(a))
    for i in p:
        print(''.join(i))

s = input() 
func(s)