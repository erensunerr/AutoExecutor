import os
import sys
o=sys.argv[1]
if o=='-h':
	print("It takes one argument as a txt file, Every line will be executed.")
else:
	a=open(o,'r').read()
	print(a)
	a=a.split("\n")
	for i in range(0,len(a)-1):
		os.system(a[i])
