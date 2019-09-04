# download the latest English wikipedia dump

FILE='enwiki-latest-pages-articles.xml.bz2'

echo "get $FILE "

if test -f "$FILE"; then
    echo "$FILE exist - not crawling"
fi


if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist - Crawling might take more than 2 hours"
    curl -L -O -C "https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2"
fi


# extract and clean texts from downloaded wikipedia dump

python wikiextractor/WikiExtractor.py $FILE -b 10M --links --sections -o extracted --no_templates --processes 24

## enwiki-latest-pages-articles.xml.bz2  -b 10M --links --sections -o extracted --no_templates --processes 24