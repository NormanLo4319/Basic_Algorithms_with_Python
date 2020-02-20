# Frog Jump Algorithm

# Define JumpStep function, which the frog can only jump two lilypads max (r = 2)
def JumpStep(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return JumpStep(n-1)+JumpStep(n-2)

for i in range(1, 10):
    print(i, 'Lilypads has', JumpStep(i), 'many ways of jump.')