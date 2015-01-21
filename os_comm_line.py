test
sys=__import__('sys')
def name_(argv):

    if argv[1] == '--un':
        if len(argv)>=3:
            username = argv[2]
            return username
    # else:
    #     input("what is your name:")

if __name__ == '__main__':
    print(sys.argv)

    username = name_(sys.argv)
    if not username:
        username=input("what is your name:")
    print(username)

    if sys.argv[1] == '--city':
        if len(sys.argv)>=3:
            city = sys.argv[2]
        else:
            city=input("Where are your live:")
        print(city)

    if sys.argv [1] == '--age':
        if len(sys.argv)>=3:
            age=sys.argv[2]
        else:
            age=input('How old are your:')
        print(age)

    if sys.argv[1] == "--help":
         print('\nYou can use following arguments: \n\n' ' --un |   Check the name.\n' ' --city | Check the place of birth. \n' ' --age |  Check the age.\n')








    # username = input('What is your name?:')
    # while not len(username) < 5:
    #     print('Invalid number of characters')
    #     username = input('What is your name?:')
    #
    # city = input('Where are you live:')
    #
    # age_is_provided = False
    #
    # while not age_is_provided:
    #     try:
    #         age_is_provided = int(input('How old are you:'))
    #     except ValueError:
    #         age_is_provided = False
    #         print('not int')
    #
    # import getpass
    #
    # p = getpass.getpass(prompt='Password:')
    #
    #
    # print('Username_is_provided: ' + username)
    # print('Age_is_provided: ' + str(age_is_provided))
    # print('City_is_provided: ' + city)
    # print('Your password: ', p)
    #
    #
