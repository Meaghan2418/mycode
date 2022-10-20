#!/usr/bin/env python3

# importing 
import shutil
import os

# force start in home directory
os.chdir('/home/student/mycode/')

# calling the shutil function
shutil.move('raynor.obj', 'ceph_storage/')

# promt for new name
xname = input('What is the new name for kerrigan.obj? ')

#rename the current file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

