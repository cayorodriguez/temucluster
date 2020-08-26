#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:00:10 2020

@author: crodri
"""

import cgi
import os, sys
os.chdir('/home/crodri/GIT/TEMUcluster')

from lxml import etree as ET
#from pymongo import MongoClient
from optparse import OptionParser

directorio = "/home/crodri/BSC/similitud_cc/corpus_casos_clinicos/radioccc"
outfilename = "test_dir_cluster"
def createCarrotFile(directorio,outfilename):
    if directorio.endswith(os.sep):
        pass
    else:
        directorio = directorio + os.sep
    #from pymongo import MongoClient
    # Gather data
    filesindir = os.listdir(directorio)
    #Initialize XML document
    tree = ET.parse("base.xml")
    root = tree.getroot()
    a = ET.Element('query')
    a.text = directorio.split(os.sep)[-1]#fecha[1:]
    root.insert(0,a)
    n = 0
    #Write each tweet
    for file in filesindir:
        doc = open(directorio+file).read().strip()
        n += 1
        print(file)
        d = ET.Element('document')
        s = ET.SubElement(d, 'snippet')
        s.text = cgi.escape(doc)
        t = ET.SubElement(d, 'title')
        t.text = doc[:120]#str(doc['created_at_date'])
        u = ET.SubElement(d, 'url')
        u.text = directorio+file
        #alldocs.append(d)
        root.insert(-1,d)
    print(n,"filess Processed")
    tree.write(outfilename+".xml", pretty_print=True)


def main(argv=None):
    parser = OptionParser()
    parser.add_option("-d", "--directorio", dest="directorio",
                    help="directorio a clusterizar")
    parser.add_option("-f", "--filename", dest="filename",
                    help="archivo de salida", default="directorio_a_clusterizar")
    (options, args) = parser.parse_args(argv)
    if options.directorio:
        createCarrotFile(options.directorio,options.filename)
    else:
        print("Especifique directorio a clusterizar")
 

if __name__ == "__main__":
  sys.exit(main())