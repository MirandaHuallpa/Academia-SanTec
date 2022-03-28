def maximumPoints(k, costs):
    # Write your code here
    if costs == [] or k == 0:
        return 0

    n = len(costs)
    suma = sum(costs)
    salto = False
    while suma > k:
        indice = costs.index(max(costs))
        if not salto and indice != n-1:
            salto = True
            costs.pop(indice)
        else:
            elem = costs.pop()
        suma = sum(costs)
        n = len(costs)
        
    return n

def maximumPoints(k, costs):
    # Write your code here
    if costs == [] or k == 0:
        return 0

    