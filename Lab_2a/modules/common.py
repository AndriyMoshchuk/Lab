import datetime
import sys
import random
import math
from math import sqrt


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def com_function():
    numb = random.randint(0, 1)
    if numb == 0:
        for j in range(100):
            if j % 2 == 0:
                print(j," ")
    elif numb == 1:
        for j in range(100):
            if j % 2 == 1:
                print(j, " ")

def er_function():
    numb = random.randint(-4, 4)
    result =  sqrt(numb)
    print(result)