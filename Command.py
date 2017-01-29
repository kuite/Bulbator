import Generator
from xml.dom import minidom

# parse xml
accounts_info = minidom.parse('source.xml')

emails_xml = Generator.create_bulk(accounts_info)

print(emails_xml)
