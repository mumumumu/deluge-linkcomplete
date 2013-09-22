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
            ctypes.windll.kernel32.CreateHardLinkW(u'',u'',0)
        else:
            os.link(src,dst)
    else:
        print('File {0} already exists'.format(dst))

torrent_id   = sys.argv[1]
torrent_name = sys.argv[2]
save_path    = sys.argv[3]

src_path  = os.path.join(save_path,torrent_name)
dest_path = os.path.join(os.path.dirname(save_path),'#temp')

if os.path.isdir(src_path):
    print('Creating links for folder {0}'.format(src_path))
    dest_path = os.path.join(dest_path, torrent_name)
    make_dir(dest_path)
    for f in os.listdir(src_path):
        src = os.path.join(src_path,f)
        dst = os.path.join(dest_path,f)
        hard_link(src,dst)
else:
    make_dir(dest_path)
    src = src_path
    dst = os.path.join(dest_path,torrent_name)
    hard_link(src,dst)

