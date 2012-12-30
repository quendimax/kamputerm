#!/usr/bin/env python3

import argparse
import html
import sys


def parseArguments():
    parser = argparse.ArgumentParser(description='Convert from a tab file to a qbh (qt phrase book) file')
    parser.add_argument('input', metavar='FILENAME', nargs='?', default='-', help='input file name. If missing then reads from stdin')
    parser.add_argument('-o', '--output', default='-', metavar='FILENAME', help='output file name. If it don\'t enumerate then writes to stdout')
    args = parser.parse_args()
    if args.input == '-':
        args.input = sys.stdin
    else:
        args.input = open(args.input, 'r', encoding='utf8')
    if args.output == '-':
        args.output = sys.stdout
    else:
        args.output = open(args.output, 'w', encoding='utf8')
    return args


def main():
    args = parseArguments()
    out = args.output
    out.write('<!DOCTYPE QPH>\n')
    out.write('<QPH language="be">\n')
    for line in args.input:
        index = line.find('\t')
        if (index == -1):
            print('invalid string: ', line, file=sys.stderr)
        key = html.escape(line[:index])
        definition = line[index+1:].replace('\\n', ' ').replace('\\t', '')
        out.write('<phrase>\n')
        out.write('\t<source>{0}</source>\n'.format(key))
        out.write('\t<target>{0}</target>\n'.format(definition))
        out.write('</phrase>\n')
    out.write('</QPH>')


if __name__ == '__main__':
    main()
