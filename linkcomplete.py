#!/usr/bin/env python

from sys import argv
from syslog import syslog
from os import link

print('deluge test: linkcomplete script started running')

torrent_id   = argv[1]
torrent_name = argv[2]
save_path    = argv[3]

print('torrent details ' + torrent_id + ' ' + torrent_name + ' ' + save_path)
