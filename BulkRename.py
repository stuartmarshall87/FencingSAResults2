from pathlib import Path
import re
import os

years = ['2008', '2009', '2010', '2011', '2012']
for year in years:
    for path in Path(year).rglob('*.htm*'):
        splitPath = re.split('\.|\_|\\\\', str(path))[1:]
        
        splitPath.remove('html')
        if len(splitPath) > 4:
            date = splitPath[0] + ('00' + splitPath[1])[-2:] + ('00' + splitPath[2])[-2:]
            #print(date)
            rename = True
            for index in range(3, len(splitPath)):
                value = splitPath[index]
                match value:
                    case 'foil':
                        splitPath[index] = 'F'
                    case 'epee':
                        splitPath[index] = 'E'
                    case 'sabre':
                        splitPath[index] = 'S'
                    case 'open':
                        splitPath[index] = 'O'
                    case 'veteran':
                        splitPath[index] = 'V'
                    case 'veterans':
                        splitPath[index] = 'V'
                    case 'Intermediate':
                        splitPath[index] = 'I'
                    case 'intermediate':
                        splitPath[index] = 'I'
                    case 'novice':
                        splitPath[index] = 'N'
                    case 'u20':
                        splitPath[index] = 'U20'
                    case 'u17':
                        splitPath[index] = 'U17'
                    case 'u15':
                        splitPath[index] = 'U15'
                    case 'u13':
                        splitPath[index] = 'U13'
                    case 'u11':
                        splitPath[index] = 'U11'
                    case 'u17u20':
                        splitPath[index] = 'U17U20'
                    case 'u17u20':
                        splitPath[index] = 'U17U20'
                        
                    case 'mens':
                        splitPath[index] = 'M'
                    case 'womens':
                        splitPath[index] = 'W'
                    case _:
                        print(path)
                        print(splitPath[index])   
                        rename = False     
            combinePath = year + '\\' + date + ''.join(splitPath[3:]) + '.html'
            
            if rename:
                os.rename(path, combinePath)
