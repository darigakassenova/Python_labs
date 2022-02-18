def prime(n): 
    if n == 1: 
        return False 
    for i in range(2, n): 
        if n%i == 0: 
            return False 
    return True 
 
 
def list_prime(lst): 
	prime_list =[] 
	for i in lst: 
		x = prime(int(i)) 
		if x == True: 
			prime_list.append(i) 
	return prime_list 
	 
a = input().split()
print(list_prime(a))
