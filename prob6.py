def merge_inventory(warehouse_A, warehouse_B):
    total_inventory = {}
    critical_stock = []

    all_products = set(warehouse_A) | set(warehouse_B)

    for product in all_products:
        qty = warehouse_A.get(product, 0) + warehouse_B.get(product, 0)
        total_inventory[product] = qty

        if qty < 10:
            critical_stock.append(product)

    return total_inventory, critical_stock

warehouse_A = {"apple": 5, "banana": 20, "orange": 3}
warehouse_B = {"apple": 2, "grape": 15, "orange": 4}

total_inventory, critical_stock = merge_inventory(warehouse_A, warehouse_B)

print("Total Inventory:", total_inventory)
print("Critical Stock:", critical_stock)
