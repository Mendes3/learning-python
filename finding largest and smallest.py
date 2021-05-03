import heapq

income = [23, 223, 55, 22, 522]
print(heapq.nlargest(3, income))
print(heapq.nsmallest(1, income))

# but if list contains many attributes than we have to do as following
stocks = [
    {'ticker':'tuna','price':12},
    {'ticker': 'apple', 'price': 122},
    {'ticker': 'fb', 'price': 32},
    {'ticker': 'microsoft', 'price': 113},
    {'ticker': 'amazon', 'price': 135},
]
print(heapq.nlargest(2,stocks, key = lambda x: x['price']))
print(heapq.nsmallest(2,stocks, key = lambda x: x['price']))


