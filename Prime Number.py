
input_number = int(input("Please Enter a Number:\n"))

number_set =[]

def prime_number(number):

    for number in range(1, input_number+1):

        if input_number%number == 0:
        
            number_set.append(number)

    if len(number_set) > 2:

        print(f"{number} is NOT a Prime Number!!")
    
    else:
    
        print(f"{number} is a Prime Number!!")

prime_number(input_number)
    