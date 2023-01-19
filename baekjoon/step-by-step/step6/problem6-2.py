import sys
stc = sys.stdin.readline().strip()
print(stc.count(" ")+1) if stc else print(0)