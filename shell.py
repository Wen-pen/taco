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

class currpath(Command):
    name = "currpath"

    def __init__(self, argument):
        super().__init__(argument)
        self.func()
    
    def func(self):
        print(os.getcwd())

class cd(CommandWithArg):
    name = "cd"
    def __init__(self, argument):
        super().__init__(argument)

    def func(self):
        os.chdir(f"{self.argument}/")
        currpath(None)

class Shell:
    command_list = [cd, currpath]
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