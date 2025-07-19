#!/bin/bash
s5cmd --no-sign-request cp "s3://sentinel-s2-l1c/tiles/42/S/YF/2024/6/26/0/B08.jp2" "data/sentinel_scenes/20240626_B08.jp2"
s5cmd --no-sign-request cp "s3://sentinel-s2-l1c/tiles/42/S/YF/2024/6/26/0/metadata.xml" "data/sentinel_scenes/20240626_metadata.xml"
