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
        translations.append({translation_key.attributes['name'].value: translation_key.childNodes[0].nodeValue})

for translation in translations:
    for key, value in translation.items():
        if key not in translations_dictionary:
            translations_dictionary[key] = [value]
        else:
            translations_dictionary[key].append(value)

writer = csv.writer(open("translations.csv", "w"), delimiter=';', quoting=csv.QUOTE_NONE)
writer.writerow(['key'] + xml_files)
for translation_key in translations_dictionary:
    translation_values = []
    for translation in translations_dictionary[translation_key]:
        translation_values.append(translation.encode('utf-8'))
    writer.writerow([translation_key] + translation_values)
