#!/usr/bin/env python
# coding: utf-8

# In[5]:


#source1: https://www.runoob.com/python3/python3-99-table.html
#source2: https://www.itread01.com/content/1542909663.html

for i in range(1, 101):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, format(i*j,",")), end='')
    print()


# In[ ]:




