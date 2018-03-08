# scrape.py
# create the list of image ids.

import sys
import json
from pprint import pprint

dataset = sys.argv[1]
data = json.load(open('meta/json/%s.json' % dataset))

def parse_labeled_set(dataset):
    csv.write("image_id,label_id,url\n")
    for image in zip(data['images'], data['annotations']):
        if image[0]['image_id'] == image[1]['image_id']:
            csv.write("%s,%s,%s\n" % (
                image[0]['image_id'],
                image[1]['label_id'],
                image[0]['url'][0]
            ))

def parse_unlabeled_set(dataset):
    csv.write("image_id,url\n")
    for image in data['images']:
        csv.write("%s,%s\n" % (
            image['image_id'],
            image['url'][0]
        ))

with open('meta/csv/%s.csv' % dataset, 'w+') as csv:
    if dataset in ['train', 'validation']:
        parse_labeled_set(dataset)
    elif dataset in ['test']:
        parse_unlabeled_set(dataset)

