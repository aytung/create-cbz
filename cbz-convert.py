# first, list all directories
# remove all non-directories (with extensions)
import os
import subprocess
import sys 
fileencoding = sys.getfilesystemencoding()
# then, for each of those folders, convert into a zip
# keep track of all zip files
# then, convert all of those into cbz files if current cbz non-existing
wdItems = os.listdir(path=".")
wdFiles = [wdItem for wdItem in wdItems if "." in wdItems]
wdDirs = [wdItem for wdItem in wdItems if "." not in wdItem]


for wdDir in wdDirs:
	destination = wdDir + ".cbz"	
	zipFile = wdDir + ".zip"
	if destination not in wdFiles:
		subprocess.call(["zip", "-r", destination, wdDir] )








