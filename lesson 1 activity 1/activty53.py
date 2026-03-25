s1={1,2,3}
s2={4,3,5}
s3=list(zip(s1,s2))
print(s3)
l1=[1,2,3]
l2=[4,6,7]
for x,y in zip(l1,l2[::-1]):
    print(x,y)
stocks=('adani','reliance','chatgpt')
prices=(1221,2324,10000)
newdict={stocks:prices for stocks,prices in zip(stocks,prices)}
print(newdict)