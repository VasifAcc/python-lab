inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}

# 1. UPDATE: Electronics prices 15% discount
for sku, item in inventory.items():
    if item["category"] == "Electronics":
        item["price"] = round(item["price"] * 0.85, 2)

# 2. LOGIC: if stock 0 add restock_urgent 
for sku, item in inventory.items():
    if item["stock_count"] == 0:
        item["restock_urgent"] = True

# 3. SAFE ACCESS: last_sold if not write "Never" 
for sku, item in inventory.items():
    item.setdefault("last_sold", "Never")

# 4. VIEW
for sku, item in inventory.items():
    print(sku, item)