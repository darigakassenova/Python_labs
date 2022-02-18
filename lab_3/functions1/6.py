def rev_sent(s):  
    words = s.split(' ') 
    reverse_sentence = ' '.join(reversed(words))  
    return reverse_sentence 
  
a = input()
print (rev_sent(a))