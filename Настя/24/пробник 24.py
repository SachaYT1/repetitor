f = open('24.txt').read()

f = f.replace('L', 'K').replace('M', 'K').replace('N', 'K')

f = f.replace('2', '1').replace('3', '1')
c_letter = 0
c_digit = 0
balance = [0 for i in range(len(f))]
for i in range(0, len(f)):
    if f[i] == 'K':
        balance[i] = 2
    else:
        balance[i] = -1

print(balance)
s = 0
c = ''
ans = 0
# for key, val in balance.items():
#     s += val
#     if s == 0:
#         ans += 1
# print(ans
#       )

a = []
def min_subarray_len(arr):
    n = len(arr)
    max_len = -float('inf')
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += arr[right]

        while current_sum > 0:
            max_len = max(max_len, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return max_len


print(min_subarray_len(balance))
