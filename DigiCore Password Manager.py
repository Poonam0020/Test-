menu_options = {
    1: 'Add',
    2: 'View',
    3: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def Add():
    un=input("Enter the username:")
    pwd=input("Enter the password:")
    url=input("Enter the url:")
    comb_string="username: "+un+"\n password: "+pwd+"\n url: "+url+"\n"
    file=open("demo.txt",'a')
    file.write(comb_string)
    file.close()
def View():
    file=open('demo.txt','r')
    content=file.read()
    print(content)

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           Add()
        elif option == 2:
            View()
        elif option == 3:
            print('Thanks for using password manager')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')