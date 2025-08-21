def calculate_discount(price, discount_percent):
    if discount_percent < 20:
        return price
    else:
        return ((100 - discount_percent) / 100) * price

price = input("Enter price: ")
discount_percent = input("Enter discount: ")

print(calculate_discount(int(price), int(discount_percent)))
