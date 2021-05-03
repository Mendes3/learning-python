stocks ={
    'goog' : 760,
    'fb' : 210,
    'amazon' : 321,
    'apple' : 121,
    'yahoo': 443
}
print(min(zip(stocks.keys(),stocks.values())))
print(min(stocks))
print(min(stocks.values()))
print(max(zip(stocks.keys(),stocks.values())))
print(sorted(zip(stocks.keys(),stocks.values())))
print(sorted(zip(stocks.values(),stocks.keys())))