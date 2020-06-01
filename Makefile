.PHONY: all

all:
	cp /Users/william/bloomstore/index/index.yaml .
	python3 index.py index.yaml
