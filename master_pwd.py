from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
# write_key()
def load_key():
    file = open('key.key',"rb")
    key = file.read()
    file.close()
    return key
print('WELLCOME')
mst = input('Enter the the master password: ')
key = load_key() + mst.encode()
fer = Fernet(key)
def add():
    usr = input("enter the user name: ")
    pwd = input('enter the password: ')
    with open('psd.txt','a') as f:
        f.write(usr+"|"+fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('psd.txt', 'r') as f:
        for i in f.readlines():
            data = i.rstrip()
            user, password = data.split('|')
            print("user name: ", user,"password: ", fer.decrypt(password.encode()).decode())
def clr():
    with open('psd.txt', 'r+') as f:
        f.truncate()

while True: 
    opt = input("Weather you want to add a password or view(add/view), Enter q to quit and d for delete:  ").lower()
    if opt == 'q':
        print('THANK YOU')
        quit()
    if opt == 'add':
        add()
    elif opt == 'view':
        view()
    elif opt == 'd':
        clr()
    

