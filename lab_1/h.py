s = str(input())
t = input() 
for i in range(len(s)): 
    if(t in s):
        if(s.index(t)==s.rindex(t)):
            print(s.index(t))
        else:
            print(s.index(t), s.rindex(t))
        break
        
