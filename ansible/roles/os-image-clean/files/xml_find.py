#!/usr/bin/python3
import sys
input = sys.stdin.read()
tag_name = sys.argv[1]
tag = input[input.find('<{}>'.format(tag_name)) + 8 : input.find('</{}>'.format(tag_name))]
print(tag)
