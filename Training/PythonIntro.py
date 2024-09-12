"""
Python Introduction
9/12/24
Author : Porter Martin
"""
# A variable to store an integer

def printVarInfo():
    '''
    This simple function prints out the types of two local variables
    :return:
    '''
    x = 5
    print(type(x))

    y = 3.1
    print(type(y))

def methodThatAcceptsData(x, y, z):
    """
    This method accepts three variables and prints out their data types
    :param x: First variable
    :param y: Second variable
    :param z: Third variable
    :return:
    """
    print("x is ", type(x))
    print("y is ", type(y))
    print("z is ", type(z))

methodThatAcceptsData(100,[0, 1, 2, 3, 4, 5], 'WVU')
#printVarInfo()


#
# ips = ['192.168.10.1', 10, '192.168.10.3', '192.168.10.4']
# print(type(ips))
# print(type(ips[2]))
# print(ips[0] + ips[3])
# print(ips)
# for ip in ips:
#     print(ip)
# if (ips[1] >=20):
#     print('The value is indeed greater than 20')
# else:
#     print('The value is NOT greater than 20')
#
# name = "Porter Martin"
# yourName = 'Sarah Conor'
#
#
# print(type(name))
# print(type(yourName))
