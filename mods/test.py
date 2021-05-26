import re

with open('GeoLocations/traces_12.98.65.54.traces','r') as logs:
            adresses = []
            for i,line in enumerate(logs):
                if i == 0:
                    print(str(line))
                    continue
                else:
                    if '* * *' in line:
                        adresses.append("*.*.*")
                    else:
                        adresses.append(re.search('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',line).group(1))
            print(adresses)
