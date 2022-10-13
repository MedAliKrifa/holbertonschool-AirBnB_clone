#!/usr/bin/python3
""""that contains the entry point of the command interpreter"""


import cmd



class HBNBCommand(cmd.Cmd):
    """"console class"""


    prompt = "(hbnb) "

    def do_EOF(self, arg):
        '''exit the program'''

        return True

    def do_quit(self, arg):
        ''''exit the program'''

        return True

    def emptyline(self):
        """"empty like my heart"""
        pass















if __name__ == '__main__':
    HBNBCommand().cmdloop()


    