# Overview of Human Protein

>[Protein classes - The Human Protein Atlas](https://www.proteinatlas.org/humanproteome/proteinclasses)
* versions:
```
https://v18.proteinatlas.org/humanproteome/proteinclasses(version of 2018-09-08)
https://v17.proteinatlas.org/humanproteome/proteinclasses
https://v16.proteinatlas.org/humanproteome/proteinclasses
...
```

## 1. Fetch up-to-date proteinclasses



### 1.1 Usage

```bash
python fetch.py
```

### 1.2 What?

* fetch proteinclasses data
* download tsv files into ```./tsv```


## 2. Query protein infomation

### 2.1. make db from tsv files in ```./tsv```

```bash
python query.py --makedb
```

### 2.2. query protein classes or other info

```bash
python query.py -g PIM1
python query.py -g PIM1 -i "Protein class"
python query.py -g PIM1 -i "Gene synonym"
python query.py -g PIM1 -i ""
```

item choices:

```
Gene synonym
Ensembl
Gene description
Chromosome
Position
Protein class
Evidence
Antibody
Reliability (IH)
Reliability (Mouse Brain)
Reliability (IF)
Subcellular location
Prognostic p-value
RNA cancer category
RNA tissue category
RNA TS
RNA TS TPM
TPM max in non-specific
RNA cell line category
```

