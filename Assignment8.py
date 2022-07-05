#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Is the Python Standard Library included with PyInputPlus?

Yes the Python Standard Library included with PyInputPlus and this is the python module used to take input with additional validation.
Will ask user keep entering the input until they enter a valid input

pip install PyInputPlus to install the this module


# In[ ]:


#2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?

pyinputplus as pypi because to be the alisas name this is the perfect name to be represent and easy to use.

import pyinputplus as pyip
a=pyip.inputInt(min=5 , max=9)


# In[ ]:


3. How do you distinguish between inputInt() and inputFloat()?

inputInt()= Accepts integer as input and also takes additional parameter as min , max, greater than and less than bounds but the
return value is always an integer.

inputFloat()=Accepts floating point values as input and also takes additional parameter as min , max, greater than and less than bounds but the
return value is always a floating point .


# In[1]:


#4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

import pyinputplus as pyip
a=pyip.inputInt(min=0 , max=99)


# In[ ]:


#5. What is transferred to the keyword arguments allowRegexes and blockRegexes?

when we enter strng as input to the function to the keyword arguments that allowsRegexes and blockRegexes, timeout and limit.


# In[2]:


#6. If a blank input is entered three times, what does inputStr(limit=3) do?

import pyinputplus as pyip

str=pyip.inputStr(limit=3)

RetryLimitException: is displayed when we tried to enter blank input 3 times.


# In[6]:


#7. If blank input is entered three times, what does inputStr(limit=3, default="hello") do?

import pyinputplus as pyip

test=pyip.inputStr(limit=3, default="hello")

The below message is displayed when we try to enter blank input to the inputStr.


# In[ ]:




