#extract 1/10th of the dataset into a new jsonl file

import json
import pandas as pd

def extract_sub_dataset(file_path, output_path, fraction=0.1):
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i % (1/fraction) == 0:
                with open(output_path, 'a', encoding='utf-8') as out_file:
                    out_file.write(line)

extract_sub_dataset("datasets/REGEN/clothing.jsonl", "datasets/REGEN/clothing_sub.jsonl")
