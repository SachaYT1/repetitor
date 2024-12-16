f= open('24_1428.txt').read().strip()

f = f.replace('XY', 'X Y').replace('XZ', 'X Z')

a = f.split()

ans = [len(c) for c in a]
print(max(ans))