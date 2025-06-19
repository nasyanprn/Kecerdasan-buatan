from sklearn.neighbors import KNeighborsClassifier

# Dataset sederhana: [nilai, kehadiran], label: 1=Lulus, 0=Tidak Lulus
X = [
    [80, 90],
    [65, 80],
    [75, 70],
    [60, 60],
    [90, 95]
]
y = [1, 0, 0, 0, 1]  # Label target

# Buat model k-NN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Data mahasiswa baru yang akan diprediksi
mahasiswa_baru = [[70, 85]]  # Nilai 70, kehadiran 85%

# Prediksi
hasil = model.predict(mahasiswa_baru)

print("Hasil prediksi:")
if hasil[0] == 1:
    print("Lulus")
else:
    print("Tidak Lulus")
