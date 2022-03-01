import sys

res = {}

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        res[len(i)] = i

print(res)

