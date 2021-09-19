t = int(input())
highPrice = []
highQuality = []
for i in range(t):
    price, quality = map(int,input().split())
    if price>quality:
        highPrice.append([price,quality])
    elif quality>price:
        highQuality.append([price,quality])
    
# if min(highPrice[1])<max(highQuality[1]) and min(highPrice[0])>max(highQuality[0]):
#     print("Happy Alex")
# else:
#     print("Poor Alex")
print(highPrice[0][0],highPrice[1][1])