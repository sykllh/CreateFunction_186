def convert_temparature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        print("Unit harus 'C' atau 'F'")

print("========= KONVERSI SUHU =========")

input_suhu = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan satuan suhu ('C' untuk Celcius atau 'F' untuk Fahreinhait): ")