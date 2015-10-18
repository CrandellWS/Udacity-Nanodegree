from new_module import new_module

class New_Program():
    """ This Class is just an example program with a purpose of learning

    It will print it's own name.

    Args:
        report_name: A boolean to determine if it should print it's name
        report_module: A boolean to determine if it should print it's module

    Returns:
        None
    """

    def __init__(self, report_name, report_module):
        if(report_name):
            print(New_Program.__name__)
        if(report_module):
            print(New_Program.print_something_else.__module__)

    def print_something_else():
        print(ok)

New_Program(1,0) # prints New_Program
New_Program(0,1) # prints __main__

new_module.New_Module(1,0) # prints New_Module
new_module.New_Module(0,1) # prints new_module.new_module
