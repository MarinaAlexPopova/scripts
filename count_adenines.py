#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#@created: 19 Sept 2021
#@author: Marina Popova

import argparse

def main(input_file):
    with open(input_file) as file:
        A_count=0
        for i in file:
            if '>' not in i:
                A_count += i.upper().count('A')
    print(A_count)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Counting A in the file')
    parser.add_argument('-i','--input', help='Input file', required=True)
    args = parser.parse_args()
    
    input_file = args.input

    main(input_file)

