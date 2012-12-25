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
        self.beDefinition = ''
        self.byDefinition = ''
        self.mtDefinition = ''
        self.rmDefinition = ''
        self.kind = ''
        self.out = open('dictionary.html', 'w', encoding='utf8')

    def startDocument(self):
        self.out.write('<html><head>')
        self.out.write('<meta http-equiv="Content-Type" content="text/html;charset=utf8" />')
        self.out.write('<style>')
        for line in open('../css/article-style.css'):
            self.out.write(line)
        self.out.write('</style></head><body><table border="1" cellspacing="0" cellpadding="4">')
        self.out.write('<tr><th>Тэрмін</th><th>Сынонім</th><th>Пераклад (школьны правапіс)</th>')
        self.out.write('<th>Пераклад (класічны правапіс)</th><th>Сустрэчы</th><th>Каметар</th>')

    def endDocument(self):
        self.out.write('</table></body></html>')

    def startElement(self, name, attrs):
        if name != 'definition':
            return
        self.kind = attrs.getValue('kind')
        
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
            self.out.write('</td>\n<td>')
            self.out.write(self.byDefinition)
            self.out.write('</td>\n<td>')
            self.out.write(self.beDefinition)
            self.out.write('</td>\n<td>')
            self.out.write(self.mtDefinition)
            self.out.write('</td>\n<td>')
            self.out.write(self.rmDefinition)
            self.out.write('</tr>\n')
            #TODO end
            self.key = ''
            self.keys = []
            self.synonym = ''
            self.synonyms = []
            self.beDefinition = ''
            self.byDefinition = ''
            self.mtDefinition = ''
            self.rmDefinition = ''
        elif name == 'key':
            self.keys.append(self.text.strip(' \n\t'))
        elif name == 'synonym':
            self.synonyms.append(self.text.strip(' \n\t'))
        elif name == 'definition':
            definition = self.text.strip(' \n\t')
            if self.kind == 'be':
                self.beDefinition = definition
            if self.kind == 'by':
                self.byDefinition = definition
            if self.kind == 'mt':
                self.mtDefinition = definition
            if self.kind == 'rm':
                self.rmDefinition = definition
            if self.kind == 'al':
                self.beDefinition = definition
                self.byDefinition = definition
        self.text = ''

    def characters(self, chars):
        self.text += chars

def main():
    xml.sax.parse(open('../src/kamputerm.xml', encoding='utf8'), KamputermSaxHandler())

if __name__ == '__main__':
    main()
