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

print("Dodatkowa zmiana do nowego commit")

print("\n\033[1mPatryku, Życzę Ci spokojnych i radosnych Świąt, pełnych inspiracji i odpoczynku. \nNiech Nowy Rok przyniesie Ci satysfakcję z osiągnięć, nowe wyzwania i wiele sukcesów w świecie kodu i AI. \nDziękuję za Twoje wsparcie.\n\033[0m")