
This repository contains scripts, data, and data summaries from Propublica's Vital Signs database for providers at
* Massachusetts General Hospital
* San Francicso General Hospital
* University of Chicago Hospital
* a sample of 1000 providers who are the only medicare providers in their zip code ("lonely doctors")

= How was this data generated? =

1.  I filtered the NPI provider database 
http://download.cms.gov/nppes/NPI_Files.html
for providers at these four locations.
2.  I queried Propublica's Vital Signs API
3.  Concatenated the results into datafiles 
4.  Extract fields of interest into a table
5.  Sort
6.  Render sorted table as HTML.


* [4000 Boston providers](http://www.mcs.anl.gov/~trimble/nodi/MGHdata.html) 
* [2000 Uchicago providers](http://www.mcs.anl.gov/~trimble/nodi/UCdata.html)
* [900 SF providers](http://www.mcs.anl.gov/~trimble/nodi/SFGHdata.html) 
* [1000 Lonely providers](http://www.mcs.anl.gov/~trimble/nodi/LONEdata.html)  



