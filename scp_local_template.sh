#!/bin/sh

## scp copy file to remote server
local_file=""

dest_serv=""
dest_dir=""

scp ${local_file} ${dest_serv}:${dest_dir}

## Execute remote command 
#remote_command=""
#ssh ${dest_serv} ${remote_command}