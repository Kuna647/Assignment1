#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. How do you distinguish between shutil.copy() and shutil.copytree()?

shutil.copy--It is a method available in python to copy the content of the soure file to destination with out the metadata(creation date and modification informtion)
if nthe detination is a directory then the entire file will be copied to there if the dest is an existing file then the content
of the file will be replaced.

import shutil

destionation=shutil.copy(src,dest)

shutil.copytree:- It is the method in python that will copy the whole metadata directory from the source to the destination

destination1=shutil.copytree(src,dest)



# In[ ]:


#2. What function is used to rename files?

To rename a file we need to import OS module and need to rename a file by calling a function.

import os

os.rename("old name","new name")


# In[ ]:


#3. What is the difference between the delete functions in the send2trash and shutil modules?

1. delete function in send2thrash-- To delete the files from the specifed path for temporaraly instead of permananently we should
use send2thrash.send2thrash() function.
It will prevent the permanent deletion of the file.

import send2trash
  
send2trash.send2trash("/location/to/file")

2.  delete function in shutil module-- To delete the files recursively from the directory and subdirectory, and to delete the content
of the file permanently we should use shutil.rmtree() function.

import shutil

shutil.rmtree (path, ignore_errors=False, onerror=None)


# In[ ]:


#4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is
#equivalent to File objects’ open() method?

The method which is equivalent to file object open method id ZipFile(arg)

import zipfile

with ZipFile("pass the path and mode of file") as zip:




# In[2]:


"""5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf
or .jpg). Copy these files from whatever location they are in to a new folder."""


import os, shutil

def selectiveCopy(folder, extensions, destFolder):
	folder = os.path.abspath(folder)
	destFolder = os.path.abspath(destFolder)
	print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			name, extension = os.path.splitext(filename)
			if extension in extensions:
				fileAbsPath = foldername + os.path.sep + filename
				print('Coping', fileAbsPath, 'to', destFolder)
				shutil.copy(fileAbsPath, destFolder)

extensions = ['.php', '.py','.txt']
folder = 'randomFolder'
destFolder = 'selectiveFolder'
selectiveCopy(folder, extensions, destFolder)


# In[ ]:




