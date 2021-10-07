dur=13650
melt \
screenshots/.all.png ttl=150 length=$dur \
-attach crop center=1 \
-attach affine transition.cycle=150 transition.mirror_off=1 transition.geometry="0=-5%/-5%:110%x110%;150=0%/0%:100%x100%" \
-filter luma cycle=150 duration=15 \
-transition mix \
-profile atsc_1080p_30 \
-consumer avformat:output.mp4 acodec=libmp3lame vcodec=libx264
