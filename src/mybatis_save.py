#!/usr/bin/python3
from xml.dom.minidom import parse
import xml.dom.minidom


DOMTree = xml.dom.minidom.parse("c:\\Users\\yangkaiqi1\\Desktop\\1.xml")
collection = DOMTree.documentElement

res = collection.getElementsByTagName("result")
for rr in res:
    print(rr.getAttribute('column')+",")
print("------------")
# {payLineId,jdbcType=BIGINT}

for rr in res:
    print("#{"+rr.getAttribute('property')+","+"jdbcType="+rr.getAttribute('jdbcType')+"},")

