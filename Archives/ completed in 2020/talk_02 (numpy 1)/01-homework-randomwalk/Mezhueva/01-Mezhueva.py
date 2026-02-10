#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


###Пункт 1
np.random.seed(42)
walk_line=np.array([0])
for i in range(999):
  step=(2*np.random.randint(0,2)-1)
  step=step+walk_line[-1]
  if step<0:
   step=0
  walk_line=np.append(walk_line,step)
print(walk_line)


# In[3]:


# минимальное значение по y
walk_line_min = np.amin(walk_line[1:999])
print(walk_line_min)


# In[4]:


# максимальное значение по y
walk_line_max = np.amax(walk_line[0:999])
print(walk_line_max)


# In[5]:


# находим мин по х
index_min = np.where(walk_line==walk_line_min)
one=np.ones(1, dtype=int)
position_min=index_min[0]+one
min_x=position_min[0]
print(min_x)


# In[6]:


# находим макс по x
index_max = np.where(walk_line == walk_line_max)
position_max=index_max[0]+one
max_x=position_max[0]
print(max_x)   


# In[7]:


markers=np.append(min_x,max_x)
markers=list(markers)
plt.plot(walk_line,'-bp',color='#4b0082', markevery=markers,markersize=10, linewidth=1)
plt.annotate('min',xy=(min_x,walk_line_min), fontsize=16, color= 'lightcoral')
plt.annotate('max',xy=(max_x,walk_line_max), fontsize=14, color= 'lightcoral')
plt.title('Random walk', size=18)
plt.ylabel('Steps', size=16, labelpad=20)
plt.xlabel('Amount of steps', size=16, labelpad=20)


# In[ ]:



    
   
       


# In[9]:





# In[ ]:




