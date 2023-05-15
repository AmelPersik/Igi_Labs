from container import Container
import json
import os.path

class CLI:
    # loading users and creating basic container
    def __init__(self):
        self.users = list()
        if os.path.exists("users.txt"):
            with open("users.txt", 'r') as ufile:
                self.users = list(json.load(ufile))
        self.container = Container()

    # main function representing interactive users' work
    def start(self):
        while True:
            uname = input("Enter your nickname:\t")
            if uname not in self.users:
                self.users.append(uname)
                with open("users.txt", 'w') as ufile:
                    ufile.write(json.dumps(self.users))
                    print('User {} was successfully added'.format(uname))
            print('welcome, {}!'.format(uname))
            answer = ""
            while answer != "yes" and answer != "no":
                answer = input('Would you like to load your container (if exists)? (yes/no):\t')
            if answer == "yes":
                if os.path.exists(uname + '.txt'):
                    self.container.load(uname + '.txt')
                    print("Container loaded!")
                else:
                    print("You don't have saved container yet(")
            print(
                'Commands:'
                '\nadd [e1 e2 ... en]   --   add element(s) to container'
                '\nremove [e1 e2 ... en]   --   remove element(s) from container'
                '\nfind [e1 e2 ... en]   --   check if element(s) is(are) in container'
                '\nlist   --   list all the elements in container'
                '\ngrep [regex]   --   try to find elements matching with given regular expression'
                '\nsave   --   save changes to file. IT\'S THE ONLY WAY TO SAVE UR CHANGES'
                '\nload   --   load previous container\'s state from file'
                '\nclear   --   delete all elements from'
                '\nswitch   --   change user. Your current changes WILL NOT BE SAVED'
                '\nexit   --   kill program. Your current changes WILL NOT BE SAVED'
            )
            while True:
                u_command = list()
                while len(u_command) == 0:
                    u_command = list(input().split())
                u_func, u_args = u_command[0], u_command[1:]
                if u_func == 'add':
                    if len(u_args) > 0:
                        self.container.add(u_args)
                elif u_func == 'remove':
                    if len(u_args) > 0:
                        self.container.remove(u_args)
                elif u_func == 'find':
                    if len(u_args) > 0:
                        self.container.find(u_args)
                elif u_func == 'list':
                    self.container.list()
                elif u_func == 'grep':
                    if len(u_args) == 1:
                        self.container.grep(u_args[0])
                    elif len(u_args) > 1:
                        print('Looking for matches with only 1st argument')
                        self.container.grep(u_args[0])
                elif u_func == 'save':
                    self.container.save(uname + '.txt')
                elif u_func == 'load':
                    self.container.load(uname + '.txt')
                elif u_func == 'clear':
                    answer = ""
                    while answer != "yes" and answer != "no":
                        answer = input('Are you sure you want to delete all elements in your container? (yes/no):\t')
                    if answer == "yes":
                        self.container.clear()
                elif u_func == 'switch':
                    answer = ""
                    while answer != "yes" and answer != "no":
                        answer = input('Are you sure you want to switch user without saving the latest changes? '
                                       '(yes/no):\t')
                    if answer == "yes":
                        self.container = Container()
                        break
                elif u_func == 'exit':
                    answer = ""
                    while answer != "yes" and answer != "no":
                        answer = input('Are you sure you want to exit without saving the latest changes? (yes/no):\t')
                    if answer == "yes":
                        exit()


cli = CLI()
cli.start()