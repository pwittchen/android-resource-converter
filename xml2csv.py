#!/usr/bin/python -u

# usage: $ python xml2csv.py <directory_with_xml_files>

from xml.dom import minidom
import csv
import os
import sys

directory_with_android_resources = sys.argv[1]
xml_files = os.listdir(directory_with_android_resources)
xml_parsed_files = []
translations = []
translations_dictionary = {}

for xml_file in xml_files:
    resources_xml_file = directory_with_android_resources + "/" + xml_file
    xml_parsed_files.append(minidom.parse(resources_xml_file).getElementsByTagName('string'))

for xml_parsed_file in xml_parsed_files:
    for translation_key in xml_parsed_file:
        # for quotation nodes
        if len(translation_key.childNodes) > 0:
            translations.append({translation_key.attributes['name'].value: translation_key.childNodes[0].nodeValue})

for translation in translations:
    for key, value in translation.items():
        if key not in translations_dictionary:
            translations_dictionary[key] = [value]
        else:
            if value not in translations_dictionary[key]:
                translations_dictionary[key].append(value)

writer = csv.writer(open("translations.csv", "w"), delimiter='\t', quotechar='',
                    skipinitialspace=False, quoting=csv.QUOTE_NONE)
writer.writerow(['key'] + xml_files)
# Sort one values, such as translatable="false" elements
for translation_key in sorted(translations_dictionary, key=lambda k: len(translations_dictionary[k]), reverse=True):
    print "\ntranslation_key: " + translation_key

    translation_values = []
    for translation in translations_dictionary[translation_key]:
        entersRemoved = " ".join(translation.encode('utf-8').split("\n"))
        multiSpacesRemoved = " ".join(entersRemoved.split())
        tabReplaced = "\\t".join(multiSpacesRemoved.split("\t"))
        translation_values.append(tabReplaced)
        print "translation : " + tabReplaced

    writer.writerow([translation_key] + translation_values)
