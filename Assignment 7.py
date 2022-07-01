#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1. What is the name of the feature responsible for generating Regex objects?

#The feature responsible for generating Regex object is re module. If we want to perform an regular expression kind of operation then we 
#should import re module.
import re


# In[ ]:


#2. Why do raw strings often appear in Regex objects?

Raw strings are used so that backslashes do not have to be escaped. backslash(/) escapes single('') and double quote("")
hence the raw string can't be ended with odd number of baclslashes

for eg:
    re.match(r"\\", r"\\")
    if we don't use raw string (r) then we have to use ("\\\\") backslashes
    as raw string can't be end with odd number of backslashes
    


# In[7]:


#3. What is the return value of the search() method?

"""The search() method in python regualr expression return the first occurance of the position of the searched pattern that matches in the string else
it would return None when the pattern doesn't match in the string
"""
#for eg:

import re
str="Hello Test boy"

pos=re.search("l",str)
print("The psoition of the whilte space in the string is:- ",pos.start())

    


# In[15]:


#4. From a Match item, how do you get the actual strings that match the pattern?

#Ans:-  The group() method returns strings of the matched text.

#5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover?
#Group 2? Group 1?

"""Ans:- Group 0 is the entire match,
    group 1 covers the first set of parentheses, 
    and group 2 covers the second set of parentheses."""
    
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group())
"""print(mo.group(0))
print(mo.group(1))
print(mo.group(2))"""


# In[ ]:


#6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell
#a regex that you want it to fit real parentheses and periods?

Ans: Periods and parentheses can be escaped with a backslash: \., \(, and \).


# In[ ]:


#7. The findall() method returns a string list or a list of string tuples. What causes it to return one of
#the two options?

Ans: If the regex has no groups, a list of strings is returned. 
    If the regex has groups, a list of tuples of strings is returned.


# In[5]:


#8. In standard expressions, what does the | character mean?

#Ans:- The | character signifies matching “either, or” between two groups.

import re

txt="The test is simple and learn to great"

x=re.findall("simple|learn",txt)
#print(x)
for i in x:
    print(i,end=",")
print(" ")
if x:
    print("atleast one pattern matches")
else:
    print("searched pattern not found in the string")


# In[ ]:


#9. In regular expressions, what does the character stand for?

No charchter mentioned in the question. Kindly do let me know the character.


# In[12]:


#10.In regular expressions, what is the difference between the + and * characters?

#Ans- + matches one or more charcter and * matches zero or more character.
import re

txt="The test is simple and learn to great"

x=re.findall("thi+",txt)
y=re.findall("thi*",txt)
print(x)
print(y)

"""for i in x:
    print(i,end=",")
print(" ")"""

if x or y:
    print("atleast one pattern matches")
else:
    print("searched pattern not found in the string")


# In[ ]:


#11. What is the difference between {4} and {4,5} in regular expression?

Ans:- {4} Matches exactly 3 instances of the preceeding group and {4,5} match the instances between 4 and 5.


# In[ ]:


#12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular
#expressions?

Ans: The \d, \w, and \s shorthand character classes match a single digit, word, or white space character, respectively 
    in the serached string.
    re.search("\d",txt)
    re.search("\w",txt)
    re.search("\s",txt)


# In[ ]:


#13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?

Ans: The \D, \W, and \S shorthand character classes match a single character that is not a digit, word, or space character, respectively.
    


# In[ ]:


#14. What is the difference between .* and .*?

Ans- *. performs a greedy match where as .*? performs non greedy match.


# In[ ]:


#15. What is the syntax for matching both numbers and lowercase letters with a character class?

Ans: Either [0-9a-z] 
    or [a-z0-9]


# In[ ]:


#16. What is the procedure for making a normal expression in regax case insensitive?

Ans: Passing re.I or re.IGNORECASE as the second argument to re.compile() will make the matching case insensitive.


# In[ ]:


#17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd
#argument in re.compile()?

Ans: The . character normally matches any character except the newline character. If re.DOTALL is passed as the second argument to re.compile(), 
    then the dot will also match newline characters.


# In[14]:


#18. If numReg = re.compile(r&#39;\d+&#39;), what will numRegex.sub(&#39;X&#39;, &#39;11 drummers, 10 pipers, five rings, 4
#hen&#39;) return?

#Ans: 'X drummers, X pipers, five rings, X hens'
import re

numReg = re.compile(r'\d+')
numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')

print(numReg)


# In[ ]:


#19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?

Ans: The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile()


# In[ ]:


"""20. How would you write a regex that match a number with comma for every three digits? It must
match the given following:
&#39;42&#39;
&#39;1,234&#39;
&#39;6,368,745&#39;

but not the following:
&#39;12,34,567&#39; (which has only two digits between the commas)
&#39;1234&#39; (which lacks commas)"""

Ans: e.compile(r'^\d{1,3}(,{3})*$') will create this regex, but other regex strings can produce a similar regular expression.


# In[ ]:


"""21. How would you write a regex that matches the full name of someone whose last name is
Watanabe? You can assume that the first name that comes before it will always be one word that
begins with a capital letter. The regex must match the following:
&#39;Haruto Watanabe&#39;
&#39;Alice Watanabe&#39;
&#39;RoboCop Watanabe&#39;
but not the following:
&#39;haruto Watanabe&#39; (where the first name is not capitalized)
&#39;Mr. Watanabe&#39; (where the preceding word has a nonletter character)
&#39;Watanabe&#39; (which has no first name)
&#39;Haruto watanabe&#39; (where Watanabe is not capitalized)"""

Ans: re.compile(r'[A-Z][a-z]*\sWatanabe')


# In[ ]:


"""22. How would you write a regex that matches a sentence where the first word is either Alice, Bob,
or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs;
and the sentence ends with a period? This regex should be case-insensitive. It must match the
following:
&#39;Alice eats apples.&#39;
&#39;Bob pets cats.&#39;
&#39;Carol throws baseballs.&#39;
&#39;Alice throws Apples.&#39;
&#39;BOB EATS CATS.&#39;
but not the following:
&#39;RoboCop eats apples.&#39;
&#39;ALICE THROWS FOOTBALLS.&#39;
&#39;Carol eats 7 cats.&#39;"""

Ans: re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\ s(apples|cats|baseballs)\.', re.IGNORECASE)

