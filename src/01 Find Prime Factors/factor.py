def get_prime_factors(number):
# using the same funciton name, write my own code 
# that finds the prime factors of a given number

    div = 2         # start with 2 as the prime number with the smallest absolute value
    pfactors = []   # initialize an empty array to store prime factors called pfactors

    while div <= number:            # WHILE we can still divide number, mod and check for remainders...
        if number%div==0:           # IF no remainders, 
            number=number/div       # then divide number by divisor AND...
            pfactors.append(div)    # add div to list of prime factors, repeat if statement
        else:                       # ELSE there is non-zero remainder, then change divisor to next prime factor
            div+=1 
    return pfactors     # output the list of prime factors that divide the given number





# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
    print(get_prime_factors(999)) # [3, 3, 3, 37] ***My own test case***
