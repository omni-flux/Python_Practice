n:int = 5
temp:int = n
fact:int = 1

while n>=1:
    fact*=n
    n=n-1

print(f'the factorial of {temp} is {fact}')
print('the factorial of {} is {}'.format(temp,fact))
