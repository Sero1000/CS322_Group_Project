import xml.etree.ElementTree as ET
import os
import re

from pc.utils.utils import clean_text, write_dataset
from pc.utils.omegaconf_utils import read_yaml


paths = read_yaml("configs/data_paths.yaml")
OUTPUT_DIR = os.path.join(paths.save_dir, 'ted_talks')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Train parser

tree = ET.parse(paths.ted_talks.train)
root = tree.getroot()
ted_talks_train = []

for transcript in root.findall('transcript'):
    txt = transcript.text.strip()
    txt = [clean_text(t) for t in txt.split('\n')]
    ted_talks_train += txt

ted_talks_train = [clean_text(text) for text in ted_talks_train]
ted_talks_train = [s[2:] if s[:2] == ', ' else s for s in ted_talks_train]
ted_talks_train = [s[1:] if s[:1] == ',' else s for s in ted_talks_train]

write_dataset(ted_talks_train, os.path.join(OUTPUT_DIR, 'ted_talks_train.txt'))



ted_talks_train = []

for transcript in root.findall('transcript'):
	txt = transcript.text.strip()
	
	txt = [clean_text(t) for t in txt.split('\n')]
	ted_talks_train += txt

ted_talks_train = [clean_text(text) for text in ted_talks_train]
ted_talks_train = [s[2:] if s[:2] == ', ' else s for s in ted_talks_train]
ted_talks_train = [s[1:] if s[:1] == ',' else s for s in ted_talks_train]

write_dataset(ted_talks_train, os.path.join(OUTPUT_DIR, 'ted_talks_train.txt'))

# Dev parser

xmlp = ET.XMLParser(encoding="utf-8")
tree = ET.parse(paths.ted_talks.dev, parser=xmlp)
root = tree.getroot()

docs = []
for doc_id in range(len(root[0])):
	doc = root[0][doc_id]
	for seg in doc.iter('seg'):
		docs.append(seg.text.strip())


ted_talks_dev = [re.sub(r'\s+', ' ', d) for d in docs]

ted_talks_dev = [clean_text(text) for text in ted_talks_dev]

ted_talks_dev = [s[2:] if s[:2] == ', ' else s for s in ted_talks_dev]
ted_talks_dev = [s[1:] if s[:1] == ',' else s for s in ted_talks_dev]

write_dataset(ted_talks_dev, os.path.join(OUTPUT_DIR, 'ted_talks_dev.txt'))

# Test parser

xmlp = ET.XMLParser(encoding="utf-8")
tree = ET.parse(paths.ted_talks.test, parser=xmlp)
root = tree.getroot()

docs = []
for doc_id in range(len(root[0])):
	doc = root[0][doc_id]
	for seg in doc.iter('seg'):
		docs.append(seg.text.strip())


ted_talks_test = [re.sub(r'\s+', ' ', d) for d in docs]

ted_talks_test = [clean_text(text) for text in ted_talks_test]

ted_talks_test = [s[2:] if s[:2] == ', ' else s for s in ted_talks_test]
ted_talks_test = [s[1:] if s[:1] == ',' else s for s in ted_talks_test]

write_dataset(ted_talks_test, os.path.join(OUTPUT_DIR, 'ted_talks_test.txt'))