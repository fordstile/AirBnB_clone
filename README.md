0x00. AirBnB clone - The console
This project is the first step towards building a full web application: the AirBnB clone.
Objectives

How to create a Python package

How to create a command interpreter in Python using the cmd module

What is Unit testing and how to implement it in a large project

How to serialize and deserialize a Class

How to write and read a JSON file

How to manage datetime

What is an UUID

What is *args and how to use it

What is **kwargs and how to use it

How to handle named arguments in a function

Requirements All files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

Installation and execution

Move in to the directory $ cd AirBnB_clone

Execute the console file /AirBnB_clone$ ./console.py

Console commands

The commands available for this command interpreter are:

*create - Creates a new instance of the class passed by argument.

show - Prints the string representation of an instance.

*destroy - Deletes an instance that was already created.

all - Prints string representation of all instances or of all instances of a specified class.

*update - Updates an instance attribute if exists otherwise create it.

help - Show all commands or display information about a specific command.

quit - Exit the console.

EOF - Exit the console.

*create, destroy and update commands save changes into a JSON file.

create - create <class_name>

show - show <class_name> <object_id> ; <class_name>.show(<object_id>)()

destroy - destroy <class_name> <object_id ; <class_name>.destroy(<object_id>)()

all - all <class_name> ; <class_name>.all()

update - update <class_name> <object_id> “” ; .update(<object_id>, , ) ; .update(<object_id>, )

help - help ; help <command_name>

quit - quit

EOF - EOF ; (ctrl + d)
