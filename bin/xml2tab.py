#!/usr/bin/env python3

import argparse
import sys
import xml.sax
import xml.sax.handler

class KamputerSaxHandler(xml.sax.handler.ContentHandler):

    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)

def parseArguments():
    parser = argparse.ArgumentParser(description='Convert from a stardict textual file to a tab file')
    parser.add_argument('input', metavar='FILENAME', help='input file name. If - then reads from stdin')
    parser.add_argument('-o', '--output', default='-', metavar='FILENAME', help='output file name. If it don\'t enumerate then writes to stdout')
    parser.add_argument('-g', '--orthography', default='school', help="'classical' or 'school' orthography")
    return parser.parse_args()

def main():
    parseArguments()

if __name__ == '__main__':
    main()
