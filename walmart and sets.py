categories= ['1: cereals','2: drinks','3: choclates']
cereals=[{'wheat':20,'maze':30,'rice':40,'barley':60,'oats':100},{'coke':40,'milk':40,'fanta':45,'water':12,'beer':300},{'dairy milk':150, 'kitkat':90, 'bounty':70}]

print('Categories:')
print(*categories,sep='\n')
p=int(input("Choose a category:"))
print(cereals[p],sep='\n')







