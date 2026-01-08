
print("Realizo cambios en el ejemplo 1")

a = [] 
b =  [ [] for i in range(5) ]
c =  [[ [] for i in range(5) ] for j in range(5)]
c[4][0] = "JA"
c[3][3:] = ["CRIStia"] * 2 

print(c)