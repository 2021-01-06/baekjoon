# 브루투스 접근
# 모든경우를 다 확인해야지 가장 싼 세트 메뉴를 구할 수 있땅
h_prices, d_prices = [], []
for i in range(3):
    h_prices.append(int(input()))

for i in range(2):
    d_prices.append(int(input()))

price = float('inf')
for i in range(3):
    for j in range(2):
        if price > h_prices[i] + d_prices[j] - 50:
            price = h_prices[i] + d_prices[j] - 50

print(price)