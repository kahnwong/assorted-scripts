#!/bin/bash

for d in */; do
	(cd "$d" && git log -1 --format="%an")
done
