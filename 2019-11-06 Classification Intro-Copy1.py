#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


#     pip install "git+git://github.com/bblais/classy" --upgrade

# In[2]:


from classy import *


# #### Please *please* **please** keep your data somewhere outside of our shared google drive.  I don't want 30 copies of big image data sets.

# In[20]:


data=load_excel('/Users/bblais/Desktop/ai373/data/iris.xls',verbose=True)


# In[5]:


data


# In[6]:


data.vectors.shape


# In[8]:


subset=extract_features(data,[0,2])
subset


# In[9]:


plot2D(subset,legend_location='upper left')


# In[10]:


plot_feature_combinations(data)


# ## Classification

# In[21]:


C=NaiveBayes()


# In[22]:


data_train,data_test=split(data,test_size=0.2)


# In[23]:


timeit(reset=True)
C.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())


# In[24]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[15]:


C.means


# In[25]:


C=kNearestNeighbor()


# In[26]:


timeit(reset=True)
C.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())


# In[27]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:





# In[ ]:





# In[22]:


C=BackProp(hidden_layer_sizes = [5],max_iter=10000)
timeit(reset=True)
C.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())

print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[23]:


C.weights


# In[ ]:





# In[28]:


images=image.load_images('/Users/bblais/Desktop/ai373/data/digits')


# In[29]:


data=image.images_to_vectors(images)


# In[30]:


data_train,data_test=split(data)


# In[31]:


C=NaiveBayes()
timeit(reset=True)
C.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())

print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[33]:


C.means.shape


# In[ ]:





# In[ ]:





# In[34]:


image.vector_to_image(C.means[2,:],(8,8))


# In[38]:


images=image.load_images('/Users/bblais/Desktop/ai373/images/all_pieces')


# In[41]:


images.data[0].shape


# In[42]:


data=image.images_to_vectors(images)


# In[7]:


data_train,data_test=split(data)


# In[44]:


C=kNearestNeighbor()
timeit(reset=True)
C.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())

print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


C=CSC()


# In[9]:


timeit(reset=True)
C.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())

print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[17]:


test_image=image.load_images('/Users/bblais/Desktop/ai373/images/all_pieces/black/piece259.png')
test_vector=image.images_to_vectors(test_image)


# In[18]:


C.predict(test_vector.vectors)


# In[ ]:




