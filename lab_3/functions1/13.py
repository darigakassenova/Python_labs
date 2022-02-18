import random
num = random.randint(1, 20)
name = input("Hello, What's your name?\n")
cnt = 0
print('Well, '+ name + ', I am thinking of a number between 1 and 20.')
while True:
    a = int(input())
    cnt += 1
    if a < num:
        print('Your guess is too low')
        print('Take a guess.')
    if a > num:
        print('Your guess is too high')
        print('Take a guess.')
    if a==num:
        print('You guessed my number in ' + str(cnt) + ' guesses!')
        break