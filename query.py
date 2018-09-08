"""
query protein classes.
"""

import argparse
from glob import glob
from collections import defaultdict
import os
import pickle


DATABASE = "proteinclasses.pkl"
PROTEIN_LIST = "proteinclasses.tsv"


def makedb():
    protein_catalogs = defaultdict(list)
    for tsvfile in glob("tsv/*.tsv"):
        catalog = os.path.basename(os.path.splitext(tsvfile)[0])
        n = 0
        indexes = []
        for line in open(tsvfile):
            dic = {}
            if n == 0:
                indexes = line.strip().split("\t")
                n = 1
            else:
                tmp = line.strip().split("\t")
                for ind, value in zip(indexes[1:], tmp[1:]):
                    dic[ind] = value
                protein_catalogs[tmp[0]].append((catalog, dic))
    with open(DATABASE, 'wb') as f_pkl:
        pickle.dump(protein_catalogs, f_pkl)


def query(gene, item):
    global DATABASE, PROTEIN_LIST
    classes = []
    for line in open(PROTEIN_LIST):
        classes.append(line.split("\t")[0])
    with open(DATABASE, 'rb') as f_pkl:
        protein_catalogs = pickle.load(f_pkl)
    sorted_res = sorted(protein_catalogs[gene], key=lambda i: classes.index(i[0]))
    res = set()
    for (catalog, dic) in sorted_res:
        print("{}".format(catalog))
        # in case of multi-result in different catalogs.
        res.add(dic[item])
    print("#########################################################")
    for i in res:
        print(i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''query protein catalogs.''')
    parser.add_argument('--makedb', action='store_true',
                        help='make catalogs db if specified.')
    parser.add_argument('-g', '--gene',
                        help='input gene name.')
    parser.add_argument('-i', dest='item', default='Protein class',
                        choices=['Gene synonym', 'Ensembl', 'Gene description',
                                 'Chromosome', 'Position', 'Protein class',
                                 'Evidence', 'Antibody', 'Reliability (IH)',
                                 'Reliability (Mouse Brain)', 'Reliability (IF)',
                                 'Subcellular location', 'Prognostic p-value',
                                 'RNA cancer category', 'RNA tissue category',
                                 'RNA TS', 'RNA TS TPM', 'TPM max in non-specific',
                                 'RNA cell line category'],
                        help='specify query item.')
    args = parser.parse_args()
    if args.makedb:
        makedb()
    else:
        if args.gene:
            query(args.gene, args.item)
        else:
            parser.print_help()
