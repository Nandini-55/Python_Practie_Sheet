product=int(input())
sales = list(map(int,input().split()))
maxSales=-float("inf")
minSales=float("inf")
for sale in sales :
    maxSales=sale if sale>maxSales else maxSales
    minSales=minSales if minSales<sale else sale
print(maxSales,minSales)