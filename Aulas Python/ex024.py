# digite o nome de uma cidade que possua "santos ou santo"
cidade = input("digite o nome da sua cidade: ").strip()

#nome da cidade
print(F"o nome da sua cidade e {cidade}")

#conferindo se o nome da cidade possui santo
print(cidade[:5].upper() == "SANTO")
