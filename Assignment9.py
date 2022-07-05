#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. To what does a relative path refer?

Relative path means the path of a certain file relative to the current working directory. for eg.
if the current wd of a file is c://user/pythonprojects/path.py then the relative path for the file would be path.py


# In[ ]:


#2. What does an absolute path start with your operating system?

An absolute path is defined as specifying the location of a file or directory from the root directory (/). 
In other words,we can say that an absolute path is a complete path from start of actual file system from / directory.


# In[1]:


#3. What do the functions os.getcwd() and os.chdir() do?
import os
os.getcwd()#-- this function is used to get the current working directory where the work is being done.


#os.chdir()#-- this function in python is used to change the directory from one directory to another directory/



# In[2]:


os.mkdir("Changedir")


# In[6]:


#to change the current workng directory

os.chdir(os.getcwd() +"/"+ "Changedir")


# In[7]:


os.getcwd()


# In[ ]:


#4. What are the . and .. folders?

. means root change to root directory where as .. means to move to the previous folder to the current folder.


# In[ ]:


#5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

dir name--\eggs\spam.txt
base name--C:\bacon


# In[ ]:


#6. What are the three “mode” arguments that can be passed to the open() function?

Read mode: open('test.txt', 'r'),
Write mode: open('test.txt', 'w'), 
Append mode: open('test.txt', 'a')


# In[ ]:


#7. What happens if an existing file is opened in write mode?

If an existing file is opened in write mode then the contents of the file is disarded and the new file is created with empty
contents.


# In[ ]:


#8. How do you tell the difference between read() and readlines()?

read()-- this function will read all the contents of the file at one go where and stores a strong varibale
readlines()- it wil read all the contents line by lineand return the object as list type with all the lines.

