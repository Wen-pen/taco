import os

class Command:
    name = ""
    def __init__(self, argument):
        self.argument = argument

    def str_rep(self):
        """
        Returns string representation
        """
        print(self.name)

class CommandWithArg(Command):
    def __init__(self, argument):
        super().__init__(argument)
        self.check_none()

    def check_none(self):
        if self.argument == None:
            print("You can't eat a taco without the filling")
        else:
            self.func()

    def func(self):
        pass

class check(Command):
    name = "check"
    directory = ""

    def __init__(self, argument):
        super().__init__(argument)
        self.func()
    
    def func(self):
        print(os.getcwd())
        self.directory = os.getcwd()

class shift(CommandWithArg):
    name = "shift"
    def __init__(self, argument):
        super().__init__(argument)

    def func(self):
        os.chdir(f"{self.argument}/")
        check(None)

class boop(CommandWithArg):
    name = 'boop'
    def __init__(self, argument):
        super().__init__(argument)

    def func(self):
        with open(f"{self.argument}", 'w') as file:
            file.close()
            print(f"Created filename {self.argument}")
        
class boopdir(CommandWithArg):
    name = "boopdir"
    def __init__(self, argument):
        super().__init__(argument)
    
    def func(self):
        self.check = check(None)
        os.mkdir(self.check.directory + f"\{self.argument}")

class Shell:
    command_list = [shift, check, boop, boopdir]
    def __init__(self):
        while True:
            command = input("taco> ")
            if command == "Exit":
                break
            self.handle(command)
    
    def handle(self, command):
        comm_list = command.split()
        if len(comm_list) == 1:
            comm_list.append(None)
        for comm in self.command_list:
            arg = comm_list[1]
            if comm.name == comm_list[0]:
                comm(arg)
                    
if __name__ == "__main__":
    Shell()