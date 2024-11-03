modal_awal = 100000000
persentase_laba = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]
laba_per_bulan = []
bulan = 1

while bulan <= 8:
    laba = modal_awal * persentase_laba[bulan-1]
    laba_per_bulan.append(laba)
    bulan += 1

for i in range(8):
    print(f"Laba bulan ke - {i + 1} sebesar", int(laba_per_bulan[i]))

total_laba = int(sum(laba_per_bulan))

print("Total laba yang didapat dari 8 bulan adalah", total_laba)
