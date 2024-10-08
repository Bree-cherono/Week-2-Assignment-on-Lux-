#!/usr/bin/env python
# coding: utf-8

# # Data Analysis Boot Camp Week 2 Assignment. 

# 1).What is garbage collection in the context of Python, and why is it important? Can you explain how memory management is handled in Python?
# 

# Garbage collection is cleaning up unused objects .It is a process that helps automatically manage memory. When you create objects in Python like variables, lists, the computer uses memory to store them. Once you're done using these objects and they’re no longer needed, Python automatically frees up that memory so it can be used for other tasks. 
# 
# 

# 2).What are the key differences between NumPy arrays and Python lists, and can you explain the advantages of using NumPy arrays in numerical computations?

# COMPARISON

# 
# 
# 1)NumPy arrays are more memory-efficient than Python lists because they store data in a contiguous block of memory, whereas lists store elements as pointers to objects.
# 
# 2) NumPy arrays require all elements to be of the same data type eg integers , while Python lists can hold mixed data types like integers and Char
# 
# 
# 3)NumPy arrays support element-wise operations, which are faster and more efficient for numerical computations, unlike lists which require loops for such operations.

# ADVANATGES OF NUMPY ARRAYS

# NumPy arrays are optimized for numerical operations and are much faster than Python lists.
# 
# 
# Arrays are more memory-efficient, especially when dealing with large datasets.

# 3).How does list comprehension work in Python, and can you provide an example of using it to generate a list of squared values or filter a list based on a condition?

# List comprehension is a simple way to create lists in Python. Instead of writing long loops to add items to a list, you can write everything in one line. It's a shorter and more readable way to build a list.

# In[19]:


squares = [y**2 for y in range(1, 6)]
squares



# 4). Can you explain the concepts of shallow and deep copying in Python, including when each is appropriate, and how deep copying is implemented?

# A shallow copy creates a new object but does not create copies of the objects inside the original while A deep copy creates a new object and recursively copies all the objects inside the original one, creating new copies .
# 
# 
# Appropriate  to use :A deep copy when you need a completely independent copy of an object and elements while  creates a new object but does not create copies of the objects inside the original.
# Implementation of Shallow Copy:
# 
# 
# import copy
# 
# deep_copy = copy.deepcopy(original)
# 

#  5).Explain with examples the difference between lists and tuples.

# Lists is Mutable that means one  can modify elements, add or remove items.Its Syntax is created using parentheses [], While Tuples is Immutable that is Once created, one  cannot change the elements.
# Its Syntax is created using parentheses (). Examples are as below:

# In[11]:


#List
my_list = [10, 20, 30]
my_list[0] = 40  
my_list


# In[12]:


#Tuple 
#List
my_list = (10, 20, 30)
my_list[0] = 40 #It does not support this
my_list


# In[ ]:




