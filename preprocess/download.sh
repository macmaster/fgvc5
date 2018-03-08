#!/bin/bash
# download.sh
# downloads the images from the internet

function process_labeled() {
  sed 1d $csv | while IFS=, read image_id label_id url; do
    echo "($image_id, $label_id, $url)"
    img="img/$1/$image_id.jpg"
    if ! [ -f $img ] && ! [[ $image_id =~ "(121)" ]] && ! [[ $url =~ "www.zhuangshangyin.com" ]]; then
      wget $url -O $img -T 5 -t 2
    fi
  done
}

function process_unlabeled() {
  sed 1d $csv | while IFS=, read image_id url; do
    echo "($image_id, $url)"
    img="img/$1/$image_id.jpg"
    if ! [ -f $img ] && ! [[ $url =~ "www.zhuangshangyin.com" ]]; then
      wget $url -O $img -T 5 -t 2
    fi
  done
}

csv="meta/csv/$1.csv"
if [[ $1 == "train" ]] || [[ $1 == "validation" ]]; then
  process_labeled $1
elif [[ $1 == "test" ]]; then
  process_unlabeled $1
fi
