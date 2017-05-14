for STEM in UCdata SFGHdata MGHdata LONEdata
do
./data2highlights.py $STEM.json  > $STEM.hl
grep \# $STEM.hl > $STEM.csv
grep -v \# $STEM.hl | sort -n -k 2 -t \$ -r >> $STEM.csv
cat $STEM.csv | csv2html.pl > $STEM.html
rm $STEM.hl
./all.py $STEM.json > $STEM.dump.csv
done
