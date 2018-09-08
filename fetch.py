#!/usr/bin/python3
"""
fetch proteinclasses data from 
    https://www.proteinatlas.org/humanproteome/proteinclasses

1. get info from the site.
2. download tsv file of each protein classes(catalog).

"""
import gzip
import os
import re
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import urlopen, urlretrieve


# https://v18.proteinatlas.org/humanproteome/proteinclasses
URL = "https://www.proteinatlas.org/humanproteome/proteinclasses"
HTML_FILE = "proteinclasses.html"
PROTEIN_LIST = "proteinclasses.tsv"


if not os.path.exists("tsv"):
    os.makedirs("tsv")


def fetch_urls():
    global URL, HTML_FILE, PROTEIN_LIST
    # write into html file if not exists.
    content = ""
    if not os.path.exists(HTML_FILE):
        with open(HTML_FILE, 'w') as f:
            content = urlopen(URL).read()
            f.write(str(content))
    else:
        content = open(HTML_FILE).read()
    content = str(content)

    # find catalog and url.
    res = re.findall('''<td nowrap>(.*?)</td>.*?<a href="(.*?)">(.*?)</a>''', content)

    # write all cats into lst file.
    flist = open(PROTEIN_LIST, 'w')
    for catalog, url, num in res:
        url = "https://www.proteinatlas.org" + url + "?format=tsv"
        if catalog.startswith("<b class"):
            catalog_rec = re.findall("<b class.*?>(.*?)</b>", catalog)[0]
        elif catalog.startswith("&nbsp"):
            catalog_rec = catalog.replace("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", "#")
        else:
            catalog_rec = catalog
        # <span title="Not included in parent class">...</span>
        try:
            catalog_rec = re.findall("(.*?)<span", catalog_rec)[0]
        except IndexError:
            pass
        # '/' cannot in filename
        catalog_rec = catalog_rec.replace("/", " or ")
        flist.write("{}\t{}\t{}\n".format(catalog_rec, url, num))
    flist.close()


def download_tsv(filename, url):
    """download .gz file, and extract into tsv file."""
    if not os.path.exists(filename):
        tmp = urlretrieve(url)
        with gzip.open(tmp[0], 'rb') as f_in:
            with open(filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    print("downloaded: {} from {} ...".format(filename, url))


def download_tsvs(n=8):
    """multi-threads of download one tsv."""
    global PROTEIN_LIST
    tasks = []
    for line in open(PROTEIN_LIST):
        catalog, url, num = line.strip().split("\t")
        filename = "tsv/{}.tsv".format(catalog)
        tasks.append((filename, url))
    print("num of download tasks: {}".format(len(tasks)))
    with ThreadPoolExecutor(max_workers=n) as executor:
        for task in tasks:
            executor.submit(download_tsv, *task)


def main():
    fetch_urls()
    download_tsvs()


if __name__ == '__main__':
    main()
