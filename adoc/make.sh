#!/bin/bash

#
# convert odg to svg:
#
# libreoffice --convert-to svg *odg
#
# ALL other libreoffice windows must eb closed for the scripted SVG creation
#

#doclist="Asciidoc+Atom-GettingStarted SAP_HA740_certification_notes SAP_HA740_SetupGuide"
doclist="SLES4SAP-hana-scaleOut-PerfOpt-12"

function make_directories()
{
    mkdir -p xml images/src/{eps,pdf,png,svg,dia} images/export
}

function make_graphics()
{
    ( cd images
        files=$(find  . -maxdepth 1 -type f -or -type l )
        for f in $files; do 
            f=${f#./}
            fType=${f##*.}; 
            case "$fType" in
                svg | png | pdf | eps | dia )
                    (cd src/$fType; if [ ! -e $f ]; then ln -s ../../$f .; fi) 
                    (cd ..; if [ ! -e $f ]; then ln -s images/$f .; fi) 
                    ;;
                odg )
                    fSVG=${f%.odg}.svg
                    if [ ! -e "export/${fSVG}" ]; then
                        # echo "${f} found, but ${fSVG} is missing"
                        libreoffice --convert-to svg  --outdir export "${f}"
                    fi
                    #
                    # create link for daps/docbook
                    #
                    (cd src/svg; if [ ! -e "${fSVG}" ]; then ln -s ../../export/"${fSVG}" .; fi) 
                    # 
                    # create link for atom preview
                    #
                    (cd ..; if [ ! -e "$fSVG" ]; then ln -s images/export/"$fSVG" .; fi) 
                    ;;
                gitignore )
                    # just ignore this 'file type'
                    ;;
                * ) 
                    echo "file type $fType ($f) currently not handeled"
                    ;;
            esac
        done
    )
}

function make_docbook() # ascidoc -> docbook
{
    # asciidoc --doctype=book \
    asciidoctor --doctype=article \
             --backend=docbook \
             --out-file="xml/${doc}.xml" \
             $docfile
    if [ ! -e "DC-${doc}" ]; then
        cat >DC-${doc} <<EOD
MAIN="${doc}.xml"
STYLEROOT="/usr/share/xml/docbook/stylesheet/suse2013-ns"
#STYLEROOT="/usr/share/xml/docbook/stylesheet/suse"
DRAFT=yes
ROLE="sbp"
PROFROLE="sbp"
EOD
    fi
}

function make_pdf() # docbook -> PDF
{
        daps -d "DC-${doc}" pdf
}

function make_text() # docbook -> TEXT
{
        daps -d "DC-${doc}" text
}

make_directories
make_graphics

for doc in $doclist; do
    echo "==== build $doc ===="
    if [ -e "${doc}.adoc" ]; then
        docfile="${doc}.adoc"
    elif [ -e "${doc}.txt" ]; then
        docfile="${doc}.txt"
    else
        docfile="$doc"
    fi
    if true; then
        make_docbook
    else
        echo "SKIP ascidoc/asciidoctor"
    fi

    if true; then
        make_pdf
        # make_text
    else
        echo "SKIP daps"
    fi
done
