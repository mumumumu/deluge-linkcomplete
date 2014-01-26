#! /bin/bash
# create a hard link upon torrent completion from seeding directory to a temporary directory for post-processing

torrent_id=$1
torrent_name=$2
torrent_path=$3
dest_path=${torrent_path/seeding/temp}

timestamp() {
    date
}

echo -n [$(timestamp)] >> /tmp/deluge_execute.log
cp -Rlv "$torrent_path/$torrent_name" "$dest_path" >> /tmp/deluge_execute.log
