#!/bin/sh

while true; do curl -k -O -C - https://52.49.91.111:8443/ghost; done
cat ghost | base64 -d > img.png
