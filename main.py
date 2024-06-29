import time
import random
import os
import datetime

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
        mathfib_time_start = time.time()
        mathfib_prompt = int(input("Num: "))
        mathfib_start1, mathfib_start2 = 0, 1
        mathfib_count = 0

        if mathfib_prompt <= 0:
            print("Please enter a positive integer")

        elif mathfib_prompt == 1:
            print("Fibonacci sequence up to", mathfib_prompt, ":")
            print(mathfib_start1)

        else:
            while mathfib_count < mathfib_prompt:
                print(mathfib_start1)
                mathfib_add = mathfib_start1 + mathfib_start2
                mathfib_start1 = mathfib_start2
                mathfib_start2 = mathfib_add
                mathfib_count += 1
            mathfib_time_end = time.time()
            mathfib_time_length = mathfib_time_end - mathfib_time_start
            print(f"{mathfib_time_length} seconds to generate")
    elif cmd == "ls":
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
              "ls\n"
              "del\n"
              "delfold\n"
              "printfile\n"
              "modules\n"
              "install\n"
              "ping\n"
              "openfile\n"
              "makefile\n"
              "writefile\n"
              "date\n"
              "rename")
    elif cmd == "modules":
        print("SoRandom")
        print("SoGames")
    elif cmd == "install":
        modules_install_prompt = str.lower(input("Install: "))
        if modules_install_prompt == "sorandom":
            modules_sorandom_installed = True
            print("Installed!")
        elif modules_install_prompt == "sogames":
            modules_sogames_installed = True
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
            if modules_sorandom_randomint_1.isnumeric() == True and modules_sorandom_randomint_2.isnumeric() == True:
                print(random.randint(int(modules_sorandom_randomint_1), int(modules_sorandom_randomint_2)))
            else:
                print("Not a number!")
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
            if modules_sorandom_weightedrandom_prompt.isnumeric() == True:
                random_weight(int(modules_sorandom_weightedrandom_prompt))
            else:
                print("Not a number!")
        else:
            print("Wrong command!")
    elif cmd == "sogames.help":
        if modules_sogames_installed == True:
            print("sogames.rps")
        else:
            print("Wrong command!")
    elif cmd == "sogames.rps":
        if modules_sogames_installed == True:
            modules_sogames_rps_prompt = str.lower(input("What will you choose? (R, P, S): "))
            modules_sogames_rps_enemychoice = random.randint(1, 3)
            if modules_sogames_rps_prompt == "r":
                if modules_sogames_rps_enemychoice == 1:
                    print("Enemy chooses Rock, Tie!")
                elif modules_sogames_rps_enemychoice == 2:
                    print("Enemy chooses Paper, You lose!")
                elif modules_sogames_rps_enemychoice == 3:
                    print("Enemy chooses Scissors, You win!")
            elif modules_sogames_rps_prompt == "p":
                if modules_sogames_rps_enemychoice == 1:
                    print("Enemy chooses Rock, You win!")
                elif modules_sogames_rps_enemychoice == 2:
                    print("Enemy chooses Paper, Tie!")
                elif modules_sogames_rps_enemychoice == 3:
                    print("Enemy chooses Scissors, You lose!")
            if modules_sogames_rps_prompt == "s":
                if modules_sogames_rps_enemychoice == 1:
                    print("Enemy chooses Rock, You lose!")
                elif modules_sogames_rps_enemychoice == 2:
                    print("Enemy chooses Paper, You win!")
                elif modules_sogames_rps_enemychoice == 3:
                    print("Enemy chooses Scissors, Tie!")
        else:
            print("Wrong command!")
    elif cmd == "openfile":
        openfile_prompt = input("File destination: ")
        os.system(openfile_prompt)
        print(f"Opened {openfile_prompt}!")
    elif cmd == "makefile":
        makefile_prompt = input("Location and name (example: DRIVER:\FOLDER\FILENAME): ")
        f = open(f"{makefile_prompt}", "x")
        f.close()
    elif cmd == "writefile":
        writefile_prompt = input("File: ")
        f = open(f"{writefile_prompt}", "w+")
        writefile_write = input("Write text: ")
        f.write(f"{writefile_write}")
    elif cmd == "ping":
        ping_start = time.time()
        print("Pong!")
        ping_end = time.time()
        ping_length = ping_end - ping_start
        print(f"{ping_length} seconds!")
    elif cmd == "date":
        print(datetime.datetime.now())
    elif cmd == "rename":
        rename_prompt = input("File path: ")
        rename_prompt2 = input("New path: ")
        os.rename(rename_prompt, rename_prompt2)
    else:
        print("Wrong command!")