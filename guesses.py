# this code is a game where the program guesses a number
from random import randint
try:
    while True:
        minimum_number, maximum_num = input('ENTER THE MINIMUM AND MAXIMUM NUMBER AND SEPARATE WITH A SPACE: ').split()
        amount_of_trial = 0
        while True:
            amount_of_trial += 1

            def computer_guess(first_comp_guess):

                """function to return the random integer the 1st computer guesses"""
                return first_comp_guess
            first_comp_result = computer_guess((randint((int(minimum_number)), (int(maximum_num)))))



            def computer_guess(second_comp_guess):

                """function to return the random integer the 2nd computer guesses"""
                return second_comp_guess
            second_comp_result = computer_guess((randint((int(minimum_number)), (int(maximum_num)))))


            def computer_guess(third_comp_guess):

                """function to return the random integer 3rd computer guesses"""
                return third_comp_guess
            third_comp_result = computer_guess((randint((int(minimum_number)), (int(maximum_num)))))



            def computer_guess(fourth_comp_guess):

                """function to return the random integer the 4th computer guesses"""
                return fourth_comp_guess
            fourth_comp_result = computer_guess((randint((int(minimum_number)), (int(maximum_num)))))



            print(f'COMPUTER 1---->({first_comp_result}) COMPUTER 2---->({second_comp_result}) COMPUTER---> 3({third_comp_result}) COMPUTER---> 4({fourth_comp_result})\n')
            if first_comp_result == second_comp_result and second_comp_result == third_comp_result and third_comp_result == fourth_comp_result:
                print(f'COMPUTER 1--->{first_comp_result} COMPUTER 2--->{second_comp_result} COMPUTER 3--->{third_comp_result} COMPUTER 4--->{fourth_comp_result}\n')
                print(f"HURRAY we got it after {amount_of_trial-1:,} guesses")
                break
            else:
                print('')
                continue
        try_again = input('WOULD YOU LIKE TO RUN THIS CODE AGAIN (Y/N): ')
        if try_again.lower() == 'y':
            continue
        elif try_again.lower() == 'n':
            break
        else:
            print('option not available')
            break
except ValueError:
    print('ONLY NUMBERS ARE ALLOWED!!!')
