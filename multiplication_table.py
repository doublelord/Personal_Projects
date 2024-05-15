print("   |   1    2    3    4    5    6    7    8    9   10   11   12   13   14   ")
print("---+------------------------------------------------------------------------")
for column in range(1, 15):
    print((str(column) + '|').rjust(4), end='')
    for row in range(1, 15):
        product = str(row*column)
        print(f"{product.rjust(4)}" + ' ', end='')
    print()
