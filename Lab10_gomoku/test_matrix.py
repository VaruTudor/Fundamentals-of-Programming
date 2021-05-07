m = [[0 for _ in range (5)]for _ in range(5)]

# secondary diagonals
print ('SECONDARY DIAGONALS')
print('\n')
for i in range(11):
    if i < 5:        
        for d in range(i+1):
            pos = m[d][i-d]
            print(d,i-d)
    else:
        for d in range(i-4,4+1):
            pos = m[d][i-d]
            print(d,i-d)

# main diagonals
print('\n')
print('MAIN DIAGONALS')
print('\n')
for i in range(5):
    for d in range(4-i,5):
        pos = m[d-(4-i)][d]
        print(d-(4-i),d)
for i in range(3,-1,-1):
    for d in range(4-i,5):
        pos = m[d][d-(4-i)]
        print(d,d-(4-i))