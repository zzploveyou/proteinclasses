# Overview of Human Protein

>[Protein classes - The Human Protein Atlas](https://www.proteinatlas.org/humanproteome/proteinclasses)
* versions:
```
https://v18.proteinatlas.org/humanproteome/proteinclasses(version of 2018-09-08)
https://v17.proteinatlas.org/humanproteome/proteinclasses
https://v16.proteinatlas.org/humanproteome/proteinclasses
...

```

# Example of protein class(catalog)

```bash
$ python query.py -g PIM1
Enzymes
#ENZYME proteins
##Transferases
#Kinases
##CAMK Ser or Thr protein kinases
##MEMSAT-SVM predicted membrane proteins
##SCAMPI predicted membrane proteins
##SPOCTOPUS predicted membrane proteins
Predicted intracellular proteins
Cancer-related genes
#Candidate cancer biomarkers
#COSMIC somatic mutations in cancer genes
##COSMIC Somatic Mutations
##COSMIC Translocations
Mapped to UniProt SWISS-PROT
#UniProt - Evidence at protein level
#########################################################
Cancer-related genes, Enzymes, Predicted intracellular proteins
```

# Example of Gene synonym

```bash
$ python query.py -g PKN1 -i "Gene synonym"
Enzymes
#ENZYME proteins
##Transferases
#Kinases
##AGC Ser or Thr protein kinases
##MEMSAT-SVM predicted membrane proteins
##SPOCTOPUS predicted membrane proteins
Predicted intracellular proteins
Mapped to UniProt SWISS-PROT
#UniProt - Evidence at protein level
Protein evidence (Kim et al 2014)
Protein evidence (Ezkurdia et al 2014)
#########################################################
DBK, MGC46204, PAK1, PKN, PRK1, PRKCL1
```

# Install and Run

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

