mkdir new
cd new
csplit -s -z /path/to/INPUT.FA '/>/' '{*}'
for i in xx* ; do \
  n=$(sed 's/>// ; s/ .*// ; 1q' "$i") ; \
  mv "$i" "$n.fa" ; \
 done