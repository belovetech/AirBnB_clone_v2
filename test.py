#!/usr/bin/python3

archive_path = 'versions/web_static_20170315003959.tgz'

archive = archive_path.split('/')[1]
filename = archive.split('.')[0]

print(filename)
