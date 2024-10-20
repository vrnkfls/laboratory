# TODO Найдите количество книг, которое можно разместить на дискете

disk_m = 1.44
pages = 100
lines= 50
simvols = 25
b = 4

disk_b = disk_m * 1024 * 1024
book = pages * lines * simvols * b
allb= disk_b // book

print("Количество книг, помещающихся на дискету:", int(allb))
