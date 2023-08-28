'''this is the module_nester.py and here we are calling a function called print_lol that will help us solving a program that may contains list or nested list'''
def print_lol(the_list):
    '''this function takes a positional argument called the_list which possibly has more nested lists. using this argument each item on the list is recursively printed on the screen on its own line'''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

def print_lol1(the_list, level):
    '''this function takes a positional argument called the_list which possibly has more nested lists. using this argument each item on teh list is recursively pronted on te screen. A second argument called “level" is used to insert tab-stops when a nested list is encountered'''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            for tab_stop in range(level):
                print("\t",end="")
                print(each_item)

def print_lol2(the_list, level=0):
    '''this function takes a positional argument called the_list which possibly has more nested lists. using this argument each item on teh list is recursively pronted on te screen. A second argument called “level" is used to insert tab-stops when a nested list is encountered'''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            for tab_stop in range(level):
                print("\t",end="")
                print(each_item)

def print_lol3(the_list, indent=False, level=0):
    '''this function takes a positional argument called the_list which possibly has more nested lists. using this argument each item on teh list is recursively pronted on te screen. A second argument called “level" is used to insert tab-stops when a nested list is encountered'''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end="")
                    print(each_item)

def print_lol3(the_list, indent=False, level=0, fh=sys.stdout):
    '''this function takes a positional argument called the_list which possibly has more nested lists. using this argument each item on teh list is recursively pronted on te screen. A second argument called “level" is used to insert tab-stops when a nested list is encountered'''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end="",file=fh)
                    print(each_item,file=fh)