import module_nester
list=["Palin", "Cleese", "Idle", ["pore", "sadden",["maroon", "red"]],["tammy", "tattoo"], "Jones", "Gilliam", "Chapman"]
module_nester.print_lol(list)
#the whole import thing can also be writte as from module_nester import print_lol()

module_nester.print_lol1(list, 0)
module_nester.print_lol1(list, 1)
module_nester.print_lol1(list, 2)
module_nester.print_lol1(list, 3)
module_nester.print_lol1(list, -6)

module_nester.print_lol2(list, 0)
module_nester.print_lol2(list, 1)
module_nester.print_lol2(list, 2)
module_nester.print_lol2(list, 3)
module_nester.print_lol2(list, -9)

module_nester.print_lol3(list, True, 0)
module_nester.print_lol3(list, True, 1)
module_nester.print_lol3(list, True, 2)
module_nester.print_lol3(list, True, 3)
module_nester.print_lol3(list, True, -9)