#!/usr/bin/python3
""""that contains the entry point of the command interpreter"""


import cmd
from curses import keyname
from multiprocessing.sharedctypes import Value
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place


classes = {
    "BaseModel": BaseModel,
    "State": State,
    "City": City,
    "User": User,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review}


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

    def do_create(self, arg):
        """"creare a new instance"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return

        if (arg[0] not in classes):
            print("** class doesn't exist **")
            return
        obj = eval("{}()".format(arg[0]))
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """"show the string representation of an instance based on the class name and id"""

        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return

        if (arg[0] not in classes):
            print("** class doesn't exist **")
            return

        if (len(arg) == 1):
            print('** instance id missing **')

        else:
            objs = models.storage.all()
            arg = arg[0] + '.' + arg[1]
            if (arg in objs):
                print(objs[arg])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return

        if (arg[0] not in classes):
            print("** class doesn't exist **")
            return

        if (len(arg) < 2):
            print('** instance id missing **')
            return
        objs = models.storage.all()
        arg = arg[0] + '.' + arg[1]
        if (arg in objs):
            del objs[arg]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, arg):
        """"print all"""
        arg = arg.split()
        obj = storage.all()
        lisst = []
        if arg:
            if arg[0] not in classes:
                print("** class doesn't exist **")
                return
            for k, v in obj.items():
                if arg[0] in k:
                    lisst.append(obj[k].__str__())
        else:
            for k, v in obj.items():
                lisst.append(obj[k].__str__())
        print(lisst)

    def do_update(self, arg):
        """"Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        args = arg.split(" ")
        if len(arg) == 0:
            print('** class name missing **')
            return

        if (args[0] not in classes):
            print("** class doesn't exist **")
            return

        if (len(args) == 1):
            print('** instance id missing **')
            return

        if (len(args) == 2):
            print('** attribute name missing **')
            return
        if (len(args) == 3):
            print('** value missing **')
            return
        if (len(args) > 4):
            return
        else:
            obj = "{}.{}".format(args[0], args[1])
            all_obj = storage.all()
            update_item = False
            for k, v in all_obj.items():
                if obj == k:
                    update_item = True
                    setattr(all_obj[obj], args[2], args[3])
            if update_item:
                storage.save()
            else:
                print('** no instance found **')

        """objs = models.storage.all()
        inst = args[0] +'.' + args[1]
        if (inst in objs):
            print(objs[inst])
        else:
            print("** no instance found **")
            return
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        attribute_value = arg.split('"')
        if len(attribute_value) == 1:
            print("** value missing **")     
            return
        attribute = arg[2]
        try:
            v = getattr(objs[inst], attribute)
            t = type(v)
            setattr(objs[inst], attribute, t(attribute_value[1]))
        except:
            setattr(objs[inst], attribute, attribute_value[1])

        storage.save()"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
