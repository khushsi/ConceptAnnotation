# download the latest English wikipedia dump

FILE='enwiki-latest-pages-articles.xml.bz2'
#curl -L -O -C - "https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2"

# extract and clean texts from downloaded wikipedia dump
#python wikiextractor/WikiExtractor.py $FILE -b 10M --links  -o extracted --no_templates --processes 24
#for d in extracted/*/ ; do
#    for infile in ${d}wiki* ; do
#      outdir=`echo ${infile}| awk -F "/" '{print "processed/"$(NF-1)}' `
#      outfile=`echo ${infile} | awk -F "/" '{print "processed/"$(NF-1)"/"$NF}'`
#      echo $outdir
#      mkdir -p ${outdir}
#      python wiki/wiki-corpus-prepare.py $infile $outfile
#
#    done
#done
#
## merge all the wikipedia text file
#cat processed/*/wiki_* > wiki_data_file


for d in extracted/*/ ; do
    for infile in ${d}wiki* ; do
      outdir=`echo ${infile}| awk -F "/" '{print "title/"$(NF-1)}' `
      outfile=`echo ${infile} | awk -F "/" '{print "title/"$(NF-1)"/"$NF}'`
      echo $outdir
      mkdir -p ${outdir}
      python wiki/wiki-title-prepare.py $infile $outfile

    done
done

## merge all the wikipedia text
cat title/*/wiki_* > wiki_titles
