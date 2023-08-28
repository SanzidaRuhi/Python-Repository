'''this is the module_nester.py and here we are calling a function called print_lol that will help us solving a program that may contains list or nested list'''
def print_lol(the_list):
    '''this function takes a positional argument called the_list which possibly has more nested lists. using this argument each item on the list is recursively printed on the screen on its own line'''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)