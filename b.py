def greet(bot_name, birth_year):
    print(f"Salut or hello! My name is {bot_name}")
    print(f"I was created in {birth_year}.")


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f"Nice name you got there, {name}!")


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"So your age is {age}!, that's a good time to start programming")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    if int(input()) != 2:
        print("Please, try again.")
    else:
        print("Completed, have a nice day!")


def end():
    print('Congratulations, have a nice day!')

    
#First step -- Greeting log
greet('Marc', '2020')

#Second step
remind_name()

#Third step
guess_age()

#Fourth step
count()

#Fifth step
test()

#Sixth step -- Ending log
end()
