# Insertion Sort / Araya Sokma Sıralaması

Python ile uygulanmış, çalışma süresi ölçümü (benchmarking) içeren optimize Araya Sokma Sıralaması (Insertion Sort) algoritması.

---

## 🇹🇷 Türkçe

### 📌 Genel Bakış

Araya Sokma Sıralaması (Insertion Sort), diziyi mantıksal olarak sıralı ve sırasız iki parçaya ayıran temel bir sıralama algoritmasıdır. Sırasız alandaki elemanlar sırayla alınarak, sol taraftaki sıralı alt dizide kendilerinden büyük olan elemanlar sağa kaydırılır ve doğru konuma yerleştirilir.

### ⏱️ Karmaşıklık Analizi (Complexity)

| Durum                        | Zaman Karmaşıklığı (Time) | Alan Karmaşıklığı (Space) | Açıklama                           |
| ---------------------------- | ------------------------- | -------------------------- | ----------------------------------- |
| **En İyi Durum (Best)**      | $O(n)$                     | $O(1)$                      | Dizi zaten sıralı olduğunda         |
| **Ortalama Durum (Average)** | $O(n^2)$                   | $O(1)$                      | Rastgele dağılmış elemanlarda       |
| **En Kötü Durum (Worst)**    | $O(n^2)$                   | $O(1)$                      | Dizi tamamen ters sıralı olduğunda  |

### ✨ Özellikler

- **Veri Güvenliği:** Orijinal veriyi mutasyona uğratmamak için `.copy()` ile güvenli işlem.
- **Hassas Ölçüm:** İşlemci sayacı tabanlı yüksek hassasiyetli `time.perf_counter()` ile süre analizi.
- **Optimize Kaydırma (Shift):** Sürekli takas (swap) yerine tek yönlü kaydırma mantığıyla optimize edilmiş atama sayısı.

### 🚀 Kurulum ve Çalıştırma

```
# Repoyu klonlayın
git clone https://github.com/AdilhanAydogmus/insertion-sort.git

# Proje klasörüne geçin
cd insertion-sort

# Algoritmayı çalıştırın
python insertion_sort.py
```

---

## 🇬🇧 English

### 📌 Overview

Insertion Sort is an intuitive, comparison-based sorting algorithm that virtually splits an array into sorted and unsorted subarrays. Values from the unsorted part are picked and placed into the correct position in the sorted part by shifting greater elements to the right.

### ⏱️ Complexity Analysis

| Case             | Time Complexity | Space Complexity | Details                            |
| ---------------- | ---------------- | ------------------ | ------------------------------------ |
| **Best Case**     | $O(n)$            | $O(1)$              | When the array is already sorted     |
| **Average Case**  | $O(n^2)$          | $O(1)$              | Random permutation of elements       |
| **Worst Case**    | $O(n^2)$          | $O(1)$              | When the array is in reverse order   |

### ✨ Key Features

- **Data Integrity:** Protects the original list from in-place mutation using `.copy()`.
- **Benchmarking:** Employs `time.perf_counter()` for high-precision microsecond runtime measurement.
- **Optimized Shift:** Uses element shifting instead of repeated swaps to minimize memory write overhead.

### 🚀 Getting Started

```
# Clone the repository
git clone https://github.com/AdilhanAydogmus/insertion-sort.git

# Navigate to the project directory
cd insertion-sort

# Run the algorithm
python insertion_sort.py
```
