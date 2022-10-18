#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display the second item on the list
    print(list1[1])

    # create a new list
    list2 = ["juniper"]

    #extend list1 by list2 adding them together
    list1.extend(list2)

    #display the combined list
    print(list1)

    # create a third list
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # using the append option
    list1.append(list3)

    # display the new complex list1
    print(list1)

    # display the listof IP addresses
    print(list1[4])

    # display the first item in the list of IP addresses
    print(list1[4][0])

main()

