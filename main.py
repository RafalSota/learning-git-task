products = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

for shop, product in products.items():
    produkty = [p.capitalize() for p in product] 
    print(f"Idę do {shop.capitalize()} i kupuję tam {produkty}")