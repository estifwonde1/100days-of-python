print("prime_number checker since we are too lazy to check it ourselves")
n = int(input("input the number u wanted to be check \n"))

def prime_checker(n):
    is_prime = True
    for i in range (2,n):
        if n % i == 0:
            is_prime=False
    if is_prime == True:
        print(f"the number {n} is prime")
    else:
        print("get that phony number outta here")
prime_checker(n)
