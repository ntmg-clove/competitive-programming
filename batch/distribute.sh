#!/usr/bin/bash

if [ -n "$1" ] ; then
    cnt=$1
else
    echo "引数1に数字を指定してください"
    exit 1
fi

cd ..
echo 'templateの作成を行います。'
mkdir ./abc/${cnt}

for level in {a..d}
do
    cp -p ./python/template.py ./abc/local/${level}${cnt}.py
done
