#(￢z ≡ x) ⋀ ((x ⋁ w) ≡ y)
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not z) == x) and ((x or w) == y)
                if f:
                    print(x, y, z, w)

