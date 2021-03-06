

def pascalFunc(num):
    rows = []
    for n in range(num):
        rows.append([])
        for i in range(n+1):
            if i == 0 or i == n:
                rows[n].append(1)
            else:
                rows[n].append(rows[n-1][i-1] + rows[n-1][i])
    return rows



def pascalGen(num):
    row = []
    for n in range(num):
        row = [1 if i == 0 or i == n else row[i-1] + row[i] for i in range(n+1)]
        yield row



def draw(f, num):
   for row in f(num):
       print (' '.join(map(str, row)).center(num*2)+'\n')


num = 20

print(pascalFunc(num))
#print(list(pascalGen(num)))

draw(pascalGen,  num)



#1545678057.0795971545678239.139683# 1545678720.04322
# 1545678770.1492429
# 1545679287.585141