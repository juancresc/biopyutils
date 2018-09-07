#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sam2pandas(sam, output=False):
    sam_file = open(sam,'r')
    for line in sam_file:
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-s", "--sam", help="SAM file (.sam)", required=True)
    parser.add_argument("-o", "--output", help="Output file (.csv)", required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    sam2pandas(args.sam, args.output)
