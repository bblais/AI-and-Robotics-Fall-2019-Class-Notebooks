#!/usr/bin/env python
# coding: utf-8

# In[56]:


get_ipython().run_line_magic('pylab', 'inline')


# In[66]:


def to_string(arr):
    import json
    s=json.dumps(arr.tolist())
    return s

def from_string(s):
    import json
    from numpy import array
    arr=array(json.loads(s))
    return arr

def take_picture(): # takes a random one from the list
    # replace this function with one that actually takes a picture
    from glob import glob
    from random import choice
    from pylab import imread
    
    fnames=glob('/Users/bblais/Desktop/ai373/images/board images/*.jpg')
    
    arr=imread(choice(fnames))
    return to_string(arr)

def take_picture():  # takes the newest one in the list
    # replace this function with one that actually takes a picture
    from glob import glob
    import os
    fnames=glob('/Users/bblais/Desktop/ai373/images/board images/*.jpg')

    newest = max(fnames, key=os.path.getctime)
    arr=imread(newest)
    return to_string(arr)


# In[67]:


a=rand(3,4)
a


# In[68]:


from_string(to_string(a))


# In[69]:


arr=from_string(take_picture())
imshow(arr)


# In[61]:


from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8001),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_function(take_picture)

    # Run the server's main loop
    server.serve_forever()


# In[ ]:




