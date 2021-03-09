#!/bin/bash
for i in {0..2559}
do
echo $i
label="OpenAI CLIP Resnet 50 4x"
convert -font iosevka-regular.ttf -pointsize 27 -size 400x caption:"$label" /tmp/caption_1.jpg
label=$(cat data/text/text_$i.txt | sed -E 's/(\\u....)|([^a-zA-z ])//g' | sed -E 's/(^\s+)|(\s+$)//g' | grep -v -e '^$' | tr '\n' ',' | sed 's/,/, /g' | sed -E 's/(\s+)|(,\s*$:)/ /g')
label="https://microscope-azure-edge.openai.com/models/\ncontrastive_4x/image_block_4_5_Add_6_0/$i\n\nLabels: $label"
convert -font iosevka-light.ttf -pointsize 15 -size 400x caption:"$label" /tmp/caption_2.jpg

montage data/hires/channel-$i-[1-6].jpg -tile 2x3 -geometry +32+32 /tmp/hires.jpg
montage /tmp/caption_[12].jpg data/examples/channel_${i}_[12].jpg -tile x4 -geometry +32+32 /tmp/example.jpg

montage /tmp/hires.jpg /tmp/example.jpg -tile 2x -geometry +16+16 -gravity south data/posters/CLIP_Resnet_50-$i.jpg
done

