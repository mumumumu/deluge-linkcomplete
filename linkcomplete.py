#!/usr/bin/env python
import sys
import os
import ctypes

def make_dir(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

def hard_link(src, dst):
    if not os.path.exists(dst):
        print('Creating hard link: {0} <===> {1}'.format(src,dst))
        if(os.name=='nt'):
            ctypes.windll.kernel32.CreateHardLinkW(dst,src,0)
        else:
            os.link(src,dst)
    else:
        print('File {0} already exists'.format(dst))

torrent_id   = sys.argv[1]
torrent_name = sys.argv[2]
save_path    = sys.argv[3]

# PREREQ: #seeding/ and #temp/ directories must exist
src_path  = os.path.join(save_path,torrent_name)
dst_path = src_path.replace('#seeding','#temp')

if os.path.isdir(src_path):
    print('Creating links for folder {0}'.format(src_path))
    make_dir(dst_path)
    for root,dirs,files in os.walk(src_path):
        dst_path = root.replace('#seeding','#temp')
        for d in dirs:
            make_dir(os.path.join(dst_path,d))
        for f in files:
            src = os.path.join(root,f)
            dst = os.path.join(dst_path,f)
            hard_link(src,dst)
else:
    hard_link(src_path,dst_path)

