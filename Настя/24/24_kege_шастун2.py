f = open('KEGE 24 18029.txt').read()

a = f.split('X')
c_y = 0
c_y_max = 0
min_len_string = 10**10

for i in range(1, len(a) - 1):
    string = a[i]
    if string.count('Y') == c_y_max:
        if len(string ) + 2 < min_len_string:
            min_len_string = len(string) + 2
    if string.count('Y') > c_y_max:
        c_y_max = string.count('Y')
        min_len_string = len(string) + 2     

print(min_len_string)