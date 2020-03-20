import os

from bs4 import BeautifulSoup as xml_parser

filename = "sat.xml"
file_stream = open(filename, 'r')

content = xml_parser(file_stream.read(), features="xml")

