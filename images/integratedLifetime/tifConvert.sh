for PHOTO in *.tif
do
    BASE=`basename $PHOTO .tif`
    convert -verbose -quality 01 "$PHOTO" "./$BASE.png"
done 
