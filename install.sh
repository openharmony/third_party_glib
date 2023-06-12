#!/bin/bash
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 2.1
# of the License.
#
# Copyright(c) 2023 Huawei Device Co., Ltd.

set -e
cd $1
# tar -zcvf patch.tar.gz *.patch
find . ! -path "*/\.*" ! \( -name patch.tar.gz -o -name glib-2.68.1.tar.xz\
    -o -name BUILD.gn\
    -o -name config.gni\
    -o -name install.sh\
    -o -name bundle.json\
    -o -name OAT.xml\
    -o -name README.OpenSource\
    -o -name glib2.spec\
    -o -name COPYING\
    -o -name backport-patch.log\
    -o -name ".*" \)\
    -prune -print -exec rm -rf {} \;
tar -zxvf patch.tar.gz
tar -xvf glib-2.68.1.tar.xz
mv glib-2.68.1/* .
rm -rf glib-2.68.1
echo "reset working dir success"
file="backport-patch.log"
exec < $file
while read line
do
    line=${line:15}
    echo $line
    patch -p1 < $line --fuzz=0 --no-backup-if-mismatch
done
echo "all file patch success!"
exit 0

