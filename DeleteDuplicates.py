from pathlib import Path
import re
import os
import filecmp

years = ['2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007']
for year in years:
    for path in Path(year).rglob('*.html'):
        replacedPath = str(path).replace('html', 'htm')
        if os.path.isfile(replacedPath):
            if filecmp.cmp(path, replacedPath):
                os.remove(path)
            else:
                print(path)