#!/bin/bash
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 2.1
# of the License.
#
# Copyright(c) 2023 Huawei Device Co., Ltd.

set -e
cd $1
if [ -d "glib-2.68.1" ];then
    rm -rf glib-2.68.1
fi
tar -xvf glib-2.68.1.tar.xz
cd glib-2.68.1
patch -p1 < $1/backport-lib-openharmony-glib.patch
exit 0
