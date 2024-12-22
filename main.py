products = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
l = 0

print("\nLista zakupów: ")
for shop, product in products.items():
    produkty = [p.capitalize() for p in product] 
    print(f"Idę do {shop.capitalize()} i kupuję tam {produkty}")
    l = l + len(product)
print(f"W sumie kupuję {l} produktów\n")

