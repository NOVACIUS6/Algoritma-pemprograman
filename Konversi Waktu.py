def jam_ke_detik(jam):
  """
  Fungsi untuk mengkonversi jam ke detik.

  Args:
    jam: Jumlah jam yang ingin dikonversi.

  Returns:
    Jumlah detik yang setara dengan jumlah jam yang diberikan.
  """

  detik = jam * 3600
  return detik

# Input jumlah jam
jumlah_jam = int(input("Masukkan jumlah jam: "))

# Konversi ke detik
jumlah_detik = jam_ke_detik(jumlah_jam)

# Tampilkan hasil
print(jumlah_jam, "jam sama dengan", jumlah_detik, "detik")