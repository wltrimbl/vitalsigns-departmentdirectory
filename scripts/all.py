#!/usr/bin/env python
# Script to iterate trough JSON file with multiple vital signs doctor data bundles
# and dump all the data in a large table.

import os, sys, glob, json

def getfields(data, fields):
    o = []
    if type(fields) == str:
        fields = [fields ]
    for f in fields:
        try:   
            if data[f] is None:
                 o.append("")
            elif type(data[f]) is float or type(data[f]) is int  or type(data[f]) is bool:
                 o.append(str(data[f]))
            elif type(data[f]) is list:
                 o.append(repr(data[f]))
            else:
                 o.append(data[f].encode("utf8")) 
        except KeyError:
            o.append("")
    return o 
n=0
if not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exist")
f=json.loads(open(sys.argv[1]).read().decode("utf8"))
for d in f:
    try: 
        n1 = d["provider_name_prefix_text"]  
    except KeyError:
        n1 = ""
    ff =  d.keys()
    npi = getfields(d, ["npi"] )[0]
    rr = getfields(d, ff) 
    if n == 0 :
        print("\t" + "\t".join(ff))
        n=1
    print(npi + "\t" + "\t".join( rr)) 
