#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def Specialfile(dir):
  filenames=os.listdir(dir)
  files=[]
  for filename in filenames:
    if re.search(r'__\w+__',filename):
      print 'fn:',filename
      path=os.path.join(dir,filename)
      abspath=os.path.abspath(path)
      files.append(abspath)
      print abspath
  return  files

# Copy file to dir
def toDir(files,targetdir):  
  print 'dir:',targetdir  
  
  for filepath in files:
    shutil.copy(filepath,targetdir)


  
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)
  
  if len(args) ==1:
    filelist=Specialfile(args[0])
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':    
    todir = args[1]
    filelist=Specialfile(args[-1])
    path=os.path.join(args[-1],todir)
    abspath=os.path.abspath(path)    
    if not(os.path.exists(abspath)) : 
      os.mkdir(abspath)
    
    print 'k:',abspath
    del args[0:2]
    toDir(filelist,abspath)
  
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
