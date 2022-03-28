from itertools import combinations

def getMaximumGrossValue(arr):
    # Write your code here
    valores = []
    n = len(arr)
    comb = combinations([num for num in range(1,n+1)],3)
    
    for i in comb:
        indice1,indice2,indice3 = i
        valor_bruto = sum(arr[0:indice1-1])-sum(arr[indice1-1:indice2-1])+sum(arr[indice2-1:indice3-1])-sum(arr[indice3-1:n])
        valores.append(valor_bruto)
        
    if valores == []:
        return 1
    else:
        return max(valores)

res = getMaximumGrossValue([-1,1,-2,-2])
print(res)