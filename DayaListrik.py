def hitung_daya_listrik(tegangan, hambatan):
    """
    Fungsi untuk menghitung daya listrik.

    Args:
        tegangan (float): Nilai tegangan dalam volt.
        hambatan (float): Nilai hambatan dalam R.

    Returns:
        float: Nilai daya listrik dalam watt.
    """

    daya = tegangan**2 / hambatan
    return daya

# Input nilai dari pengguna
tegangan = float(input("Masukan Nilai tegangan (V):"))
hambatan = float(input("Masukan Nilai hambatan (R):"))

# Hitung daya listrik
daya_listrik = hitung_daya_listrik(tegangan, hambatan)

# Tampilkan hasil
print("Daya listrik yang dikonsumsi lampu:", daya_listrik, "watt")