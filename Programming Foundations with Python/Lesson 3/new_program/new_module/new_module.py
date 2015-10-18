
class New_Module():
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
            print(New_Module.__name__)
        if(report_module):
            print(New_Module.print_something_else.__module__)

    def print_something_else():
        print(ok)
