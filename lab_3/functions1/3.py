heads = 35
legs = 94
'''
4x + 2y = 94
x + y = 35 -----> x = 12; y = 23
'''

def num(numheads, numlegs):
    for i in range(1, numheads+1):
        for j in range(1, numheads+1):
            if i+j==numheads and 2*i+4*j==94:
                print('rabbits =', i)
                print('chickens =', j)




num(heads, legs)
        