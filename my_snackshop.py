snack_name = "chips"
price = 1.50
quantity = 5
is_avalaible = True

print("Snacke :", snack_name)
print("price :", price)
print("quantity :",quantity)
print("is it avaliable :", is_avalaible)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_avalaible))


total = price * quantity
print("total value is ",total)
print("sale price", price -.25)
print("double stock", quantity*2)

print("is price under 2 dollars", price < 2)
print("is quantity more then 5 ", quantity>5)
print("is price excatly 1,50", price==1.50)

shop_name = "Quick" + " " + "Bites"
print("shop name", shop_name)
print("letter in snack  name", len(snack_name))
print("first letter", snack_name[0])

price_a=1.50
price_b = 3.00
print("before", price_a,"and", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("after:", price_a,"and",price_b)