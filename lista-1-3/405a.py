n = int(raw_input())
array = map(int, raw_input().split())
array.sort()
print ' '.join(str(e) for e in array)