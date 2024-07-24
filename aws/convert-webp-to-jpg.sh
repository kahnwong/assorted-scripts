#!/bin/bash

export AWS_PROFILE="xxx"
BUCKET_NAME="xxx"
# IMAGE_PREFIX="b20/promotions/"

# ################################
# # DOWNLOAD IMAGES
# ################################
# IFS=$'\n' images=($(cat 44x.txt))
# for i in ${images[@]}
# do
#     aws s3 cp "s3://$BUCKET_NAME/$i" "images/$i"
# done

################################
# PROCESSING
################################
echo "processing JPG images..."
IFS=$'\n' images=($(cat list_test.txt))
for i in ${images[@]}; do
	echo $i
	# # convert webp to jpeg
	# magick mogrify -format JPEG $i

	# remove og webp images
	# rm $i

	# convert filename to lowercase
	JPEG_NAME=$(echo "$i" | sed "s/.webp/.jpg/")
	# # LOWERCASE_NAME=$(echo "$JPEG_NAME" | tr '[:upper:]' '[:lower:]')
	# # mv $JPEG_NAME $LOWERCASE_NAME

	# upload to s3
	aws s3 cp "images/"$JPEG_NAME s3://$BUCKET_NAME/$JPEG_NAME --content-type 'image/jpeg'

	# # # remove uploaded file
	# # rm $LOWERCASE_NAME
done
