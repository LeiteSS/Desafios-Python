a = input().split()
product_code1 = int(a[0])
product_unit1 = int(a[1])
product_price1 = float(a[2])
b = input().split()
product_code2 = int(b[0])
product_unit2 = int(b[1])
product_price2 = float(b[2])
total = (product_price1 * product_unit1) + (product_price2 * product_unit2)
print("VALOR A PAGAR: R$ %.2f" % total)