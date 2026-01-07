items = ["Apple", "Banana", "Cherry"]
prices = [0.50, 0.30, 0.10]
quantities = [4, 2, 10]

grand_total = 0

for line_num, (item, price, qty) in enumerate(zip(items, prices, quantities), start=1):
    line_total = price * qty
    grand_total += line_total
    print(f"Line #{line_num}: {item} x{qty} = ${line_total}")

print("--------------------")
print(f"Grand Total: ${grand_total}")
