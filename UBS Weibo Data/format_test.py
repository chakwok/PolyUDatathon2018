# -*- coding:utf-8 -*-

import json
import os
import sys
import math
import csv


def format_test( tempf ):
    csvreader_temp = tempf.readlines()
    dict_temp = {}
    for row in csvreader_temp:
        [idcomm, label] = row.split( '\t\t' )
        dict_temp[idcomm] = label[0:-1]


if __name__ == "__main__":
    if len( sys.argv ) < 2:
        print( 'Please input your result csv.' )
        sys.exit()
    resultfile = sys.argv[1]

#     resultfile = 'group_1.txt'

    resultfile = open( resultfile, encoding = 'utf8' )

    try:
        format_test( resultfile )
    except:
        print( 'Please check your txt format. Correct format:' )
        print( r'id(\t\t)class(\n)' )
        sys.exit()
    finally:
        pass

    print( 'Your txt looks good!' )
