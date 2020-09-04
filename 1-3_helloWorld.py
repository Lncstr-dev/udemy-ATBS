# Adam Lancaster
# this program will ask for name and age, and then greet user accordingly. 

def main():
    name = namePrompt()
    age = agePrompt()
    greeting(name, age)

def namePrompt():
# function will prompt user to enter name and then return value. 
    userName = str(input('what is your name? '))
    return userName

def agePrompt():
# function will prompt user to enter age and then return value.
    userAge = int(input('what is your age? '))
    return userAge

def greeting(name, age):
# function will greet user based on input values.
    print('hello ', name, ', pleased to meet you.', sep='')
    print('the length of your name is:', str(len(name)), 'characters.')
    print('you are currently', age, 'years old. in 1 year, you will be',
        str((age + 1)), 'years old.')

main()

