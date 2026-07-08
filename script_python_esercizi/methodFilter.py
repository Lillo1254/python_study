numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,17,18,19,20,30, 40, 50, 60, 70, 80, 90, 100]
maggiori_diciotto = filter(lambda x:x <= 18, numeri)

print(list(maggiori_diciotto))

marchi = ["ferrari", "lamborghini", "audi", "bmw", "alfa romeo", "bugatti", "mclaren", "porsche", "jaguar", "tesla" ]
marchi_filtered = filter(lambda x: len(x) < 6, marchi)

print(list(marchi_filtered))