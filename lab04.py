import string


groceries=['bananas','strawberries','apples','bread']
groceries.append('champagne')
print 'LIST'
print groceries

print
print
groceries.remove('bread')
print 'THis is the new list'
print groceries



#c
print
print

messi_item=raw_input('please input item to obtain aisle: ')
messi_itemc=messi_item[:1]
letters=map(chr,range(97,123))
if messi_itemc in letters:
    print messi_item ,'can be found in aisle' ,messi_itemc




print
print

print 'Exercise 2'
#Exercise 2c

item_price={'apples':'sphic_apples','bananas':'spic_bananas',
            'bread':'sphic_bread',
            'carrots':'spic_carrots',
            'champagne':'spic_champagne',
            'strawberries':'sphic_strawberries'
            }
print item_price

print 'Modifing price in data structure'
item_price['strawberries']='wpic_strawberries'
print '\n\n\n\n\n\n\n\n'
print 'After modification we have this',item_price




#Exercise 2d













             
