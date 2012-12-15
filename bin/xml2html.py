#!/usr/bin/env python3

import sys
import xml.sax
import xml.sax.handler


class KamputermSaxHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.text = ''
        self.keys = []
        self.synonyms = []
        self.definition = ''
        self.out = open('dictionary.html', 'w', encoding='utf8')

    def startDocument(self):
        self.out.write('<html><head>')
        self.out.write('<meta http-equiv="Content-Type" content="text/html;charset=utf8">')
        self.out.write('<style>')
        for line in open('../css/article-style.css'):
            self.out.write(line)
        self.out.write('</style></head><body><table border="1" cellspacing="0">')
        self.out.write('<tr><th>Тэрмін</th><th>Сынонім</th><th>Пераклад</th>')

    def endDocument(self):
        self.out.write('</table></body></html>')

    def endElement(self, name):
        if name == 'article':
            #TODO start
            self.out.write('<tr><td>')
            #for key in self.keys:
            self.out.write(self.keys[0])
            self.out.write('<br>')
            self.out.write('</td><td>')
            if len(self.synonyms) > 0:
                for synonym in self.synonyms:
                    self.out.write(synonym)
                    self.out.write('<br>')
            else:
                self.out.write('-')
            self.out.write('</td><td>')
            self.out.write(self.definition)
            self.out.write('</tr>')
            #TODO end
            self.key = ''
            self.keys = []
            self.synonym = ''
            self.synonyms = []
            self.definition = ''
        elif name == 'key':
            self.keys.append(self.text.strip(' \n\t'))
        elif name == 'synonym':
            self.synonyms.append(self.text.strip(' \n\t'))
        elif name == 'definition':
            self.definition = self.text.strip(' \n\t')
        self.text = ''

    def characters(self, chars):
        self.text += chars

def main():
    xml.sax.parse(open('../src/kamputerm.xml', encoding='utf8'), KamputermSaxHandler())

if __name__ == '__main__':
    main()
