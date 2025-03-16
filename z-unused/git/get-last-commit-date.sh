#!/bin/bash

for d in */; do
	(cd "$d" && git log -1 --date=format:"%Y-%m-%d" --format="%ad")
done
