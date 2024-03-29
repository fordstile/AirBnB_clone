#!/usr/bin/python3
"""
Module for the entry point of the HBnB console.
"""

import cmd
import json
import os
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in arg.split()]
        else:
            lexer = arg[:brackets.span()[0]].split()
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = arg[:curly_braces.span()[0]].split()
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Class to represent the HBNB console."""

    prompt = '(hbnb) '

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid
        """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Display string representation of a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    obj_list.append(obj.to_dict())
                elif len(argl) == 0:
                    obj_list.append(obj.to_dict())
            print([str(obj) for obj in obj_list])


def do_count(self, arg):
    """Counts the instances of a class."""
    argl = parse(arg)
    count = 0
    for obj in storage.all().values():
        if argl[0] == obj.__class__.__name__:
            count += 1
    print(count)


def do_update(self, arg):
    """Updates the instance by adding or updating attribute."""
    argl = parse(arg)
    objdict = storage.all()
    if len(argl) == 0:
        print("** class name missing **")
        return False
    if argl[0] not in self.__classes:
        print("** class doesn't exist **")
        return False
    if len(argl) == 1:
        print("** instance id missing **")
        return False
    if "{}.{}".format(argl[0], argl[1]) not in objdict:
        print("** no instance found **")
        return False
    if len(argl) == 2:
        print("** attribute name missing **")
        return False
    if len(argl) == 3:
        print("** value missing **")
        return False
    key = "{}.{}".format(argl[0], argl[1])
    obj = objdict[key]
    if len(argl) == 4:
        value = argl[3]
        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            pass
        setattr(obj, argl[2], value)
    elif isinstance(json.loads(argl[2]), dict):
        attribute_dict = json.loads(argl[2])
        for k, v in attribute_dict.items():
            setattr(obj, k, v)
    obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
