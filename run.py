import ncmdump
import sys

for i in range(len(sys.argv)):
    if i==0:
        continue
    print(sys.argv[i])
    ncmdump.search_and_dump(sys.argv[i],sys.argv[i])