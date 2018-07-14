#!/usr/local/bin/python
import myutils
import sys
import os

yamlFiles = myutils.getListOfFilesRecursive(sys.argv[1], "*.yaml")

for yamlFile in yamlFiles:
	print("Deleting: %s" % yamlFile)
	os.remove(yamlFile)


