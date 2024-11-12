def selang(jamAwal, menitAwal, detikAwal, jamAkhir, menitAkhir, detikAhir):
    selisihJam = jamAkhir - jamAwal
    selisihMenit = menitAkhir - menitAwal
    selisihDetik = detikAhir - detikAwal
    
    return selisihJam, selisihMenit, selisihDetik

print("\nWaktu Awal: \n")
jamAwal = int(input("Masukkan jam: "))
menitAwal = int(input("Masukkan menit: "))
detikAwal = int(input("Masukkan detik: "))

print("\nWaktu Akhir: \n")
jamAkhir = int(input("Masukkan jam: "))
menitAkhir = int(input("Masukkan menit: "))
detikAhir = int(input("Masukkan detik: "))

selisihJam, selisihMenit, selisihDetik = selang(jamAwal, menitAwal, detikAwal, jamAkhir, menitAkhir, detikAhir)

print(f"Hasil akhir: {selisihJam} Jam {selisihMenit} Menit {selisihDetik}Detik")