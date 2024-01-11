from cryptography.fernet import Fernet


'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password?: ")
key = load_key() # + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}" + "\n" + f"Password: {fer.decrypt(passw.encode()).decode()}")


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    file = open('password.txt', 'a')  # with open('password.txt', 'a') as f, with automatically closes the file
    file.write(name + " " + "|" + " " + fer.encrypt(pwd.encode()).decode() + "\n")
    file.close()  # no need for this if "file = open('password.txt', 'a')" is used



while True:
    mode = input("Would you like to add a new password or view an existing ones (view / add), press q to quit: ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue