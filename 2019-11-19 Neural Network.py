#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


#     pip install "git+git://github.com/bblais/classy" --upgrade

# In[2]:


from classy import *


# #### Please *please* **please** keep your data somewhere outside of our shared google drive.  I don't want 30 copies of big image data sets.

# In[3]:


data=load_excel('/Users/bblais/Desktop/ai373/data/iris.xls',verbose=True)


# In[4]:


data


# In[5]:


data.vectors.shape


# In[7]:


subset=extract_features(data,[0,2])


# In[8]:


plot2D(subset,legend_location='upper left')


# In[ ]:





# ## Classification

# In[48]:


C=Perceptron()


# In[49]:


data_train,data_test=split(subset,test_size=0.2)


# In[50]:


timeit(reset=True)
C.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())


# In[51]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[52]:


C.weights


# In[53]:


C.predict(array([1.5,5]).reshape(1, -1))


# In[54]:


C.output(array([1.5,5]).reshape(1, -1))


# In[55]:


X=array([1.5,5]).reshape(1, -1)


# In[56]:


X


# In[57]:


dot(X,C.weights.T)+C.biases


# In[58]:


plot2D(data_train,C)


# In[75]:


C=BackProp(max_iter=6000)


# In[76]:


timeit(reset=True)
C.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())


# In[77]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[81]:


plot2D(data_train,C,number_of_grid_points=300)


# In[82]:


[w.shape for w in C.weights]


# In[ ]:




