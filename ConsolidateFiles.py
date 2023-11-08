from pathlib import Path
import re
import os
import filecmp
import shutil

def copyfile(subFilePath: str):
    if os.path.exists(subFilePath):
        with open(subFilePath) as infile:
            for line in infile:
                if 'http://engarde-escrime.com' not in line:
                    outfile.write(line)
                else:
                    outfile.write('<p></p>\n')
        os.remove(subFilePath)


years = ['2017']
for year in years:
    for path in Path(year).rglob('*.htm*'):
        fullpath = path
        path = os.path.basename(path)
        path = os.path.splitext(path)[0]
        path = str(path)
        date = path[0:8]
        if not date.isnumeric():
            continue
        remainder = path[8:]
        if remainder.endswith('P') or remainder.endswith('T') or remainder.endswith('FF') or remainder.endswith('EF') or remainder.endswith('SF') or remainder.endswith('R'):
            compFileName = path[0:-1]
            compFilePath = year + '/' + compFileName + '.htm'
            if os.path.exists(compFilePath):
                continue
            else:
                with open(compFilePath, "a") as outfile:
                    outfile.write("")

                    subFilePath = year + '/' + compFileName + 'R.htm'
                    copyfile(subFilePath)

                    subFilePath = year + '/' + compFileName + 'T.htm'
                    copyfile(subFilePath)
                
                    subFilePath = year + '/' + compFileName + 'P.htm'
                    copyfile(subFilePath)

                    subFilePath = year + '/' + compFileName + 'F.htm'
                    copyfile(subFilePath)