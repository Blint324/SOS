import time
import random
import os

def random_weight(weight):
    random_num = (random.randint(0, weight))
    if random_num == 0:
        print("True")
    else:
        print("False")
cmd_location = (os.getcwd())
modules_sorandom_installed = False

while True:
    cmd = input(f"{cmd_location}: ")
    if cmd == "printfile":
            printfile_filepath = input("Filepath: ")
            f = open(printfile_filepath)
            printfile_filecontents = f.read()
            print(printfile_filecontents)
    elif cmd == "quit":
        quit(0)
    elif cmd == "math.add":
        mathadd_var1 = input("Number 1: ")
        mathadd_var2 = input("Number 2: ")
        print(int(mathadd_var1) + int(mathadd_var2))
    elif cmd == "math.sub":
        mathsub_var1 = input("Number 1: ")
        mathsub_var2 = input("Number 2: ")
        print(int(mathsub_var1) - int(mathsub_var2))
    elif cmd == "math.div":
        mathdiv_var1 = input("Number 1: ")
        mathdiv_var2 = input("Number 2: ")
        print(int(mathdiv_var1) / int(mathdiv_var2))
    elif cmd == "math.mult":
        mathmult_var1 = input("Number 1: ")
        mathmult_var2 = input("Number 2: ")
        print(int(mathmult_var1) * int(mathmult_var2))
    elif cmd == "math.fib":
        nterms = int(input("Num: "))
        n1, n2 = 0, 1
        count = 0

        if nterms <= 0:
            print("Please enter a positive integer")

        elif nterms == 1:
            print("Fibonacci sequence up to", nterms, ":")
            print(n1)

        else:
            while count < nterms:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
    elif cmd == "dir":
        for root, dirs, files in os.walk(cmd_location):
            for file in files:
                    print(root + "/" + str(file))
    elif cmd == "go":
        cmd_location = input("File: ")
    elif cmd == "del":
        delete_path = input("Path: ")
        os.remove(delete_path)
    elif cmd == "delfold":
        deletefolder_path = input("Path: ")
        os.rmdir(deletefolder_path)
    elif cmd == "help":
        print("Commands:\n"
              "quit\n"
              "math.add\n"
              "math.sub\n"
              "math.mult\n"
              "math.div\n"
              "math.fib\n"
              "go\n"
              "dir\n"
              "del\n"
              "delfold\n"
              "printfile\n"
              "modules\n"
              "install\n")


    elif cmd == "modules":
        print("SoRandom")
    elif cmd == "install":
        modules_install_prompt = str.lower(input("Install: "))
        if modules_install_prompt == "sorandom":
            modules_sorandom_installed = True
            print("Installed!")
        else:
            print("Wrong module!")
    elif cmd == "sorandom.help":
        if modules_sorandom_installed == True:
            print("Commands:\n"
                  "sorandom.randomfloat\n"
                  "sorandom.randomint\n"
                  "sorandom.randomweight")
        else:
            print("Wrong command!")
    elif cmd == "sorandom.randomint":
        if modules_sorandom_installed == True:
            modules_sorandom_randomint_1 = input("From: ")
            modules_sorandom_randomint_2 = input("To: ")
            print(random.randint(int(modules_sorandom_randomint_1), int(modules_sorandom_randomint_2)))
        else:
            print("Wrong command!")
    elif cmd == "sorandom.randomfloat":
        if modules_sorandom_installed == True:
            print(random.random())
        else:
            print("Wrong command!")
    elif cmd == "sorandom.randomweight":
        if modules_sorandom_installed == True:
            modules_sorandom_weightedrandom_prompt = input("Weight (The higher the lower chance!): ")
            random_weight(int(modules_sorandom_weightedrandom_prompt))
        else:
            print("Wrong command!")
    else:
        print("Wrong command!")