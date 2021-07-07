import re
from decimal import *

lcauses = dict() # List of causes: { str cause : (int n_nations, dec. points)}

with open("nations.xml") as f:
    for line in f:
        matches = re.findall(r'<CAUSE type="([a-zA-Z ]*)">([0-9\.]*)<\/CAUSE>', line, re.M)
        for match in matches:
            if match[0] in lcauses:
                nnat, pts = lcauses[match[0]]
                lcauses[match[0]] = (nnat+1, pts+Decimal(match[1]))
            else:
                lcauses[match[0]] = (1, Decimal(match[1]))

with open("result.csv", 'w') as f:
    f.write("cause,number of nations,total points\n")
    for i in lcauses:
        f.write(f"{i},{lcauses[i][0]},{lcauses[i][1]}\n")
