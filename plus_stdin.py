##!/usr/bin/python3
import sys

def tonum(s):
>>>>>>> 0db6538ba16d7b78142da41f7e3c0cedabc04534
    try:
        return int(s)
    except:
        return float(s)

ans = 0
for line in sys.stdin:
    line = line.rstrip()
    ans += tonum(line)

print(ans)
