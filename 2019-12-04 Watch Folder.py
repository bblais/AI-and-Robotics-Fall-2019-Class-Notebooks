#!/usr/bin/env python
# coding: utf-8

# In[1]:


def watch_folder(path='.',delay=1,
                 modified=True,created=True,
                verbose=True,dot=True):
    from time import sleep
    
    import os
    import glob
    from datetime import datetime
    
    if verbose:
        print("Watching ",path)
        
    db={}
    original_files=os.listdir('/Users/bblais/tmp')
    for fname in original_files:
        db[fname]=os.path.getmtime(os.path.join(path,fname))
    
    print("Found %d files to watch." % len(db))
    
    try:
        while True:

            new_files=os.listdir('/Users/bblais/tmp')

            for fname in new_files:
                full_fname=os.path.join(path,fname)
                if not fname in db:  # created
                    if not created:
                        continue

                    db[fname]=os.path.getmtime(full_fname)
                    if verbose:
                        print("\nNew File",fname)
                    yield full_fname
                elif db[fname]!=os.path.getmtime(full_fname):  # modified
                    if not modified:
                        continue

                    db[fname]=os.path.getmtime(full_fname)
                    if verbose:
                        print("\nModified File",fname)
                    yield full_fname
                else:
                    pass

            if dot:
                print(".",end="")
            sleep(delay)
    except KeyboardInterrupt:
        pass
    
    if verbose:
        print("done.")


# In[2]:


for fname in watch_folder('/Users/bblais/tmp'):
    print("Do something with ",fname)


# In[3]:


def scp(fname1,fname2):
    cmd='pscp "%s" "pi@10.2.2.23:%s" -pw robots1234' % (fname1,fname2)
    print(cmd)
    os.system(cmd)
    
def cp(fname1,fname2):
    cmd='cp "%s" "%s"' % (fname1,fname2)
    print(cmd)
    os.system(cmd)    


# In[27]:


def small_fname(fname):
    import os
    base,rest=os.path.split(fname)
    return rest


# ## this part on the laptop

# In[28]:


for fname in watch_folder('/Users/bblais/tmp'):
    print("Do something with ",fname)
    cp(fname,'/Users/bblais/Desktop/%s' % small_fname(fname))


# ## this part can be on the robot

# In[29]:


def take_picture_from_folder(folder_name='.',
                             save_filename='current_board.jpg',
                            ):
    for fname in watch_folder(folder_name):    
        print("Do something with ",fname)
        break
        
    cp(fname,save_filename)


# In[32]:


take_picture_from_folder('/Users/bblais/tmp','/Users/bblais/Desktop/current_board.jpg')


# In[6]:


def fact(N):
    s=1
    for i in range(1,N+1):
        s=s*i
        
    return s


# In[13]:


fact(20000)


# In[ ]:




