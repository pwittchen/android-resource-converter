# android-resource-converter
Simple Python scripts converting android xml resources to csv file and backwards

Motivation
----------
In international projects sometimes there's a need to send resource files to the client in order to have translated strings. Client doesn't have to understand XML notation and editing two or more files at the same time is unconvenient. It's easier to send file which can be edited in MS Excel or Libre Office Calc.

Scripts in this repository are able to convert xml resources to a single *.csv file ready to open in software for common users (`xml2csv.py`). In addition, there's another script, which can generate xml resource files from *.csv file (`csv2xml.py`).

Usage
-----

### Generating *.csv file

```python
python xml2csv.py <directory_with_xml_files>
```

**Sample output**

```txt
key;strings_english.xml;strings_polish.xml
hello_world;Hello World!;Witaj Świecie!
app_name;My application;Moja aplikacja
```

### Generating *.xml files

```python
$ python csv2xml.py <file_with_translations>.csv
```

**Sample output**

`strings_english.xml`

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<resources>
  <string name="hello_world">Hello World!</string>
  <string name="app_name">My application</string>
</resources>
```

`strings_polish.xml`

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<resources>
  <string name="hello_world">Witaj &#346;wiecie!</string>
  <string name="app_name">Moja aplikacja</string>
</resources>
```

