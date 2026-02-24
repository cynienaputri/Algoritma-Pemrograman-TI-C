def my_function(nilai):
    if not nilai:
        return "Data kosong"
    return sum(nilai) / len(nilai)

data_nilai = [80, 75, 90, 60, 85]
hasil = my_function(data_nilai)

print(hasil)
