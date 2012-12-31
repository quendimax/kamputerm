#!/usr/bin/env python3

import argparse
import collections
import html.parser
import sys
import xml.sax
import xml.sax.handler


class ListInfo:

    def __init__(self):
        self.type = '1'
        self.isFirstItem = True
        self.curNum = 1

    def currentNumber(self):
        if self.type == '1':
            return str(self.curNum)
        else:
            romnumbs = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII')
            return romnumbs[self.curNum - 1]


class HtmlParser(html.parser.HTMLParser):

    def __init__(self, output):
        html.parser.HTMLParser.__init__(self)
        self.out = output
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag == 'br':
            self.out.write(';\\n')
        elif tag == 'ol':
            self.stack.append(ListInfo())
            if len(attrs) > 0 and attrs[0][1] == 'I':
                self.stack[-1].type = 'I'
        elif tag == 'li':
            linf = self.stack[-1]
            if linf.isFirstItem:
                linf.isFirstItem = False
            else:
                self.out.write('\\n')
            for i in range(len(self.stack) - 1):
                self.out.write('\\t')
            self.out.write(linf.currentNumber())
            self.out.write('. ')
            linf.curNum += 1

    def handle_endtag(self, tag):
        if tag == 'ol':
            self.stack.pop()

    def handle_data(self, data):
        data = data.replace('\t', '')
        data = data.replace('\n', '')
        data = data.replace('    ', '\\t')
        self.out.write(data)


class KamputermSaxHandler(xml.sax.handler.ContentHandler):

    def __init__(self, output, lang):
        xml.sax.handler.ContentHandler.__init__(self)
        self.text = ''
        self.reset()
        self.kind = ''
        self.out = output
        self.lang = lang

    def reset(self):
        self.keys = []
        self.synonyms = []
        self.definition = '-'

    def startElement(self, name, attrs):
        if name != 'definition':
            return
        if 'kind' in attrs.getNames():
            self.kind = attrs.getValue('kind')
        else:
            self.kind = 'al'

    def endElement(self, name):
        if name == 'article':
            self.out.write(self.keys[0])
            self.out.write('\t')
            parser = HtmlParser(self.out)
            parser.feed(self.definition)
            self.out.write('\n')
            self.reset()
        elif name == 'key':
            self.keys.append(self.text.strip(' \n\t'))
        elif name == 'definition':
            if self.kind == self.lang or self.kind == 'al':
                self.definition = self.text.strip(' \n\t')
        self.text = ''

    def characters(self, chars):
        self.text += chars


def parseArguments():
    parser = argparse.ArgumentParser(description='Convert from a stardict textual file to a tab file')
    parser.add_argument('input', metavar='FILENAME', nargs='?', default='-', help='input file name. If missing then reads from stdin')
    parser.add_argument('-o', '--output', default='-', metavar='FILENAME', help='output file name. If it don\'t enumerate then writes to stdout')
    parser.add_argument('-r', '--orthography', default='school', choices=['school', 'classic'], help="'classic' or 'school' orthography")
    args = parser.parse_args()
    if args.input == '-':
        args.input = sys.stdin
    else:
        args.input = open(args.input, 'r', encoding='utf8')
    if args.output == '-':
        args.output = sys.stdout
    else:
        args.output = open(args.output, 'w', encoding='utf8')
    if args.orthography == 'school':
        args.orthography = 'by'
    elif args.orthography == 'classic':
        args.orthography = 'be'
    return args


def main():
    args = parseArguments()
    xml.sax.parse(args.input, KamputermSaxHandler(args.output, args.orthography))


if __name__ == '__main__':
    main()
