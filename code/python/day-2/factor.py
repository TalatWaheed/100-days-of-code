def get_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors
number = int(input("Enter a number: "))
list_of_factors = get_factors(number)
print("factors of {} are: {}".format(number,list_of_factors))
