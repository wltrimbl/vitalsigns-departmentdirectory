#!/usr/bin/env python
# script that takes a JSON file with multiple doctor JSON bundles and 
# outputs a tab-delimited, html-decorated highlight table

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
                 o.append(";".join(data[f]))
            else:
                 o.append(data[f].encode("utf8")) 

#                 o.append(repr(data[f]))
#            else: 
#                 o.append(data[f])
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
    fn, ln = getfields(d, ["provider_first_name", "provider_last_name_legal_name"] ) 
    specialty = getfields(d, ["provider_specialty_display" ] )[0]
#    print ("##" + specialty[0:7] + "##")
    if specialty[0:7] == "Student":
         specialty = "Student" 
    ff=  ["total_payment_amount", "provider_first_name", "provider_last_name_legal_name", "provider_specialty_display", "percentage_of_patients_receiving_narcotics", "percentage_of_patients_of_peers_receiving_narcotics", "total_payment_amount", "number_of_prescriptions", "speaking_payment", 'brand_name_prescriber', 'drug_price']  
    npi = getfields(d, ["npi"] )[0]
#    fn, ln, disp, narc, narc2, tpa, npr = getfields(d, ff) 
    rr = getfields(d, ff) 
#    print ("G", g) 
    VS  = "https://projects.propublica.org/vital-signs/doctor/" + npi
    drugs = getfields(d, "top_5_drugs_for_doctor")[0].upper()
    TABLE = []
    LEGEND = []
    LEGEND.append("Total payments (2.5yrs)")
    if getfields(d, ["total_payment_amount"])[0] != "null" :
         #TABLE.append("$ <span style=color:red>{}</span>".format(getfields(d, ["total_payment_amount"])[0]) )
         TABLE.append("${}".format(getfields(d, ["total_payment_amount"])[0]) )
    else:
         #TABLE.append("$ <span style=color:green> 0.00 </span>")
         TABLE.append("$0.00")
    LEGEND.append("Name")
    LEGEND.append("Specialty")
    if True: 
         TABLE.append("<A HREF={} >{} </A>".format(VS, fn+" " +ln)  )
         TABLE.append(specialty)
    else:
         TABLE.append("")
         TABLE.append("")
    
    LEGEND.append("Medicare prescriptions")
    if getfields(d, ["number_of_prescriptions"])[0] != "null" :
         TABLE.append("<span style=color:black>{} </span>".format(getfields(d, ["number_of_prescriptions"])[0]) )
    else:
         TABLE.append("$ <span style=color:green> </span>")
    LEGEND.append("Drug cost")
    if getfields(d, ["drug_price"])[0] == "Far more than peers" :
         TABLE.append("<span style=color:red>High drug cost</span>")
    else:
         TABLE.append("<span style=color:green>Nothing unusual</span>")

    LEGEND.append("Brand name?")
    if getfields(d, ["brand_name_prescriber"])[0]  == "Far more than peers" :
         TABLE.append("<span style=color:red>Brand-name prescriber</span>")
    else:
         TABLE.append("<span style=color:green>Nothing unusual</span>")
    LEGEND.append("Speaking payment")
    if getfields(d, ["speaking_payment"])[0]  == "True" :
         TABLE.append("<span style=color:red>Speaking payment</span>")
    else:
         TABLE.append("<span style=color:green>Nothing unusual</span>")
    LEGEND.append("Most-prescribed medicare drugs")
    if drugs: 
         TABLE.append("{}".format(drugs))
    else:
         TABLE.append("") ;
    if n ==0:
        print ("#"+"\t".join(LEGEND) ) 
        n =1
    print ("\t".join(TABLE)+ "" ) 
 
#    print(npi + "\t" + "\t".join( rr)) 
