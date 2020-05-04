print(2)
print(3)

for j in range(4, 200):

    je_prastevilo = True
    for mozni_delitelj in range(2, j): #dovolj je da gremo do vključno korena
        if j % mozni_delitelj == 0:
            je_prastevilo = False
                    
    if je_prastevilo:
        print(j)
