#!/bin/bash

echo Removing "~" Files
rm *~
echo Removing DC- Files
rm DC-*
echo Removing xml and build dir
rm -rf xml build
mkdir xml build

# atom:set lineEnding=unix grammar=shell tabLength=2 useSoftTabs:

# zypper in daps asciidoc
#   --> 74 packages, 112 MB
# mit ./mmake.sh 2Pager_Main.adoc wird ein Document erzeugt.
echo "==== copy image files ===="

for j in png svg
do
  mkdir -p images/src/${j}
  for i in *.${j} 
  do
     if [ -f "${i}" ]; then
      cp -uv ${i} images/src/${j}/
     fi
  done
done

find images

#
# convert odg to svg:
#
# libreoffice --convert-to svg *odg

#doclist="Asciidoc+Atom-GettingStarted SAP_HA740_certification_notes SAP_HA740_SetupGuide"
doclist="${@:-2Pager_Main.adoc}"
echo doclist $doclist

for doc in $doclist; do
    echo "==== build $doc ===="
    if [ -e "${doc}.adoc" ]; then
        docfile="${doc}.adoc"
    elif [ -e "${doc}.txt" ]; then
        docfile="${doc}.txt"
    else
        docfile="$doc"
    fi
    dcfile="DC-${doc}"
    mkdir -p xml
    asciidoc --doctype=book \
             --backend=docbook \
             --out-file="xml/${doc}.xml" \
             $docfile

#STYLEROOT="../suse2013-ns"
STYLEROOT="/usr/share/xml/docbook/stylesheet/suse2013-ns"
    if [ ! -e "$dcfile" ]; then
       (
cat << HERE
MAIN="${doc}.xml"

STYLEROOT="/usr/share/xml/docbook/stylesheet/suse2013-ns"
#STYLEROOT="../suse2013-ns"
HERE
       ) > $dcfile
    fi
    daps -v0 -d "DC-${doc}" pdf
    daps -d "DC-${doc}" text

done

# alle SVG ergeben ein PDF....
#find build/$1 -iname *.pdf -exec evince {} \;
