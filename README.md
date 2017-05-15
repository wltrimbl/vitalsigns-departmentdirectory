
This repository contains scripts, data, and data summaries from Propublica's Vital Signs database for providers at
* Massachusetts General Hospital
* San Francicso General Hospital
* University of Chicago Hospital
* a sample of 1000 providers who are the only medicare providers in their zip code ("lonely doctors")

The Vitalsigns database at the time this was collected included data from late 2013-2015.

## What, why?
Propublica has collected and added value to the considerable databases of usage and influence data that medicare has made public.  Some end-user use cases are very well supported by propublica's apps:  "Find payments made to my doctor" with Dollars for Docs and  "Compare surgeons" with surgeon's scorecard.  I, the medical customer, know little about all these doctors and am somewhat reluctant to actually bring the Dollars for Docs printout to my next appointment.

But there is a class of people with insider information about all those doctors--context, personality, professional sub-specializations--the other doctors.  This dataset attempts to put Vital Signs' data for doctors who work in the same place side-by-side, to highlight the ones whose metrics might invite questions among their peers.

## How was this data generated? 

1.  I filtered the [NPI provider database](http://download.cms.gov/nppes/NPI_Files.html) (release 20170507)
for providers at these four locations.
2.  I queried Propublica's [Vital Signs API](https://www.propublica.org/datastore/api/vital-signs-api) on 2017-05-14
3.  Concatenate the results into datafiles 
4.  Extract fields of interest into a table
5.  Sort
6.  Render sorted table as HTML.

## Department directories

* [4000 Boston providers](https://rawgit.com/wltrimbl/vitalsigns-departmentdirectory/master/data/MGHdata.html) 
* [2000 Uchicago providers](https://rawgit.com/wltrimbl/vitalsigns-departmentdirectory/master/data/UCdata.html) 
* [900 SF providers](https://rawgit.com/wltrimbl/vitalsigns-departmentdirectory/master/data/SFGHdata.html)
* [1000 Lonely providers](https://rawgit.com/wltrimbl/vitalsigns-departmentdirectory/master/data/LONEdata.html) 

## What do we find?
* I expected big-city teaching-hospital doctors to receive more payments than their more isolated peers.  This seems to be the case.
* I expected rural doctors to have prescribing patters more similar to each other than to the large-hospital doctors--specifically I expected a few top drugs to be among the most prescribed for many doctors.   This doesn't seem to be so--the lists of most prescribed drugs are all over the map, and for the doctors I have top-5-medicare drug data for, there aren't any drugs that stand out. 
* The majority of the providers in all the sets have no dollarsfordocs payments disclosed.  
* On the data cleaning front, a considerable number of the "lonely providers" are medical professionals such as counselors and physicians assistants who lack prescribing authority; a smaller number are institutuional records that aren't meaningful.

## License, acknowlegements
Thanks to Propublica and the sponsors of its May 2017 hackathon in Chicago, 1871, BetterDoctor, and Yelp.
Thanks Particularly to Dr. Hannah Snyder and Dr. Jon Henry, for offering comments on the data on a Sunday morning.
[CC-BY-2.0](https://creativecommons.org/licenses/by/2.0/)  Will Trimble


