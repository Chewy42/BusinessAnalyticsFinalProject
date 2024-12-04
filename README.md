# MGSC 410 Final Project Repository
By Julian Carbajal and Matthew Favela

## Notes
I had to compress the uncleaned original datasets because they were too large to upload to github.
Some code might not work properly if you don't extract the original datasets to experience the full cleaning process.

## Code Files
1_Dataset_Cleaning.ipynb stands for the first part of the project including initial data cleaning
2.ipynb will probably be used for an EDA
Any jsonl file means JSON Large for larger files.

## Getting Started
1. Run `python3 -m venv venv` for mac or `python -m venv venv` if youre on windows
2. Run `source venv/bin/activate` for mac or `venv\Scripts\activate` if youre on windows
3. Run `pip install -r requirements.txt` to install the necessary packages

## Recreating Subsetting of the Original Dataset
1. Make sure you have the original datasets uncompressed in the datasets/REGEN/UncleanedDatasets folder.
2. Run `python extract_sub_dataset.py` to create a subset of the original dataset. This will output a clothing_sub.jsonl file into the datasets/REGEN/UncleanedDatasets folder.