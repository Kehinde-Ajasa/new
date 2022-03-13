try:
    print('This is an HCF software')
    while True:
        num1, num2 = input('Enter the numbers and separate by a space: ').split()  # using the .split method to allow users enter the two numbers on the same line
        my_factors = []  # creating an empty list


        def hcf_two_number(x, y):
            global num1, num2, my_factors  # Refering to the variables that are not within the function
            """function to help find the hcf of two given numbers"""
            if x > y:
                reference_divisor = y
            else:
                reference_divisor = x
            for i in range(1, (y + 1)):
                if (y % i) == 0 and (x % i == 0):
                    my_factors.append(i)
            return f' The H.C.F of {int(num1):,} and {int(num2):,} is {my_factors[(len(my_factors) - 1):len(my_factors)]}'
        print(hcf_two_number(int(num1), int(num2)))

        
        try_again = input('Do you want to run this code again(y/n): ').lower()
        if try_again == 'y':
            continue
        else:
            break
except SyntaxError:
    print('Check the numbers entered')
except ValueError:
   print('ONLY NUMBERS ARE ALLOWED\nAlso confirm that you have separated the numbers with a space')