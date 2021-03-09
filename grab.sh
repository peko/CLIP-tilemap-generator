#!/bin/bash
cd data

for channel in {0..2599}; do
# wget https://oaiggoh.blob.core.windows.net/microscopeprod/2020-07-25/2020-07-25/contrastive_4x/lucid.feature_vis/_feature_vis/alpha%3DFalse%26negative%3DFalse%26objective%3Dchannel%26op%3Dimage_block_4%252F5%252FAdd_6%253A0%26repeat%3D1%26start%3D2464%26steps%3D4096%26stop%3D2496/channel-$channel.png
wget https://oaiggoh.blob.core.windows.net/microscopeprod/2020-07-25/2020-07-25/contrastive_16x/lucid.feature_vis/_feature_vis/alpha%3DFalse%26negative%3DFalse%26objective%3Dchannel%26op%3Dimage_block_4%252F7%252FAdd_6%253A0%26repeat%3D0%26start%3D0%26steps%3D4096%26stop%3D32/channel-$channel.png

# done
# done
done
