#((w → z) ∧ (¬ x → z)) → ((z ≡ w) ∨ (y ∧ ¬ x))
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not((not w or z) and (x or z)) or ((z == w) or (y and (not x)))
                if not f:
                    print(x, y, z, w)