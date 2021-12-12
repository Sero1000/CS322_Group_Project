import os
import csv
import re

from pc.utils.utils import *
from pc.utils.omegaconf_utils import read_yaml

paths = read_yaml("configs/data_paths.yaml")
OUTPUT_DIR = os.path.join(paths.save_dir, 'tatoeba')

with open(paths.tatoeba, 'r') as f:
    tatoeba_csv = f.readlines()
    for i in range(len(tatoeba_csv)):
        tatoeba_csv[i] = re.sub(r'\t+', ' ', tatoeba_csv[i])
        tatoeba_csv[i] = ' '.join(tatoeba_csv[i].split()[2:])
    tatoeba = [clean_text(row.strip()) for row in tatoeba_csv]


write_dataset(tatoeba, os.path.join(OUTPUT_DIR, paths.tatoeba.split('/')[-1]))

split_train_val(os.path.join(OUTPUT_DIR, paths.tatoeba.split('/')[-1]), OUTPUT_DIR)