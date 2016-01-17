#!/usr/bin/python -u

# usage: $ python csv2xml.py <file_with_translations>.csv

import csv
from lxml import etree
import sys

reader = csv.reader(open(sys.argv[1], "rb"), delimiter='\t', quotechar='',
                    skipinitialspace=False, quoting=csv.QUOTE_NONE)
translations = []
roots = []

for row in reader:
    if row[0] == "key":
        translations = row
        translations.pop(0)
        break

for translation in translations:
    roots.append(etree.Element("resources"))

for row in reader:
    if row[0] != "key":
        number_of_translations = len(row) - 1
        for i in range(0, number_of_translations):
            string_resource = etree.SubElement(roots[i], "string")
            string_resource.set("name", row[0])
            string_resource.text = row[i + 1].decode('utf-8')
            if number_of_translations == 1:
                string_resource.set("translatable", "false")

xml_file_header = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"

for i in range(0, len(translations)):
    xml_string = etree.tostring(roots[i], encoding='unicode', method='xml', pretty_print=True, xml_declaration=False)
    pretty_xml_string = xml_file_header
    pretty_xml_string += xml_string 
    xml_file = open(translations[i], "w")
    xml_file.write(pretty_xml_string.encode('utf-8'))
    xml_file.close()
