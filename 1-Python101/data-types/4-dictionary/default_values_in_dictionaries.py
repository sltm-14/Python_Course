
my_dict = {"item": "ball","price":10.0}

my_Item    = my_dict["item"]
item_Price = my_dict.get("price",0)
count      = my_dict.get("count","This is the default value when the key does not exists")

print(my_Item)
print(item_Price)
print(count)


brand = my_dict.setdefault("brand",0) # <-- the ey is now added to the dictionary
print(count)
print(my_dict)
