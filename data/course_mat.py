"""MAT1001 / MAT1005 — Matematik: kümeler ve sayılar, cebirsel ifadelerin çarpanlara ayrılması,
denklemler ve eşitsizlikler, fonksiyonlar, limit kavramı.

Kaynaklar: KÜMELER ve SAYILAR.pdf (+ ALIŞTIRMALAR), CEBİRSEL İFADELERİN ÇARPANLARINA AYRILMASI.pdf,
DENKLEMLER-EŞİTSİZLİKLER.pdf (+ Alıştırmalar), FONKSİYONLAR.pdf, FONKSİYONLAR ve LİMİT ALIŞTIRMALAR.pdf, LİMİT I.pdf.
Formül/grafik içeren sayfalar (LİMİT I tamamen, iki alıştırma PDF'i ve FONKSİYONLAR'ın çoğu görüntü tabanlı) görsel olarak okundu.
Alıştırmaların çözümleri kaynakta yoksa elle hesaplanıp kontrol edildi.
"""

COURSE = {
    "id": "mat",
    "name": "Matematik (MAT1001 / MAT1005)",
    "short": "Matematik",
    "icon": "📐",
    "color": "#f472b6",
    "teacher": "",
    "sources": ["KÜMELER ve SAYILAR.pdf", "KÜMELER ve SAYILAR_ALIŞTIRMALAR.pdf", "CEBİRSEL İFADELERİN ÇARPANLARINA AYRILMASI.pdf",
                "DENKLEMLER-EŞİTSİZLİKLER.pdf", "Denklemler_Eşitsizlikler Alıştırmalar.pdf", "FONKSİYONLAR.pdf",
                "FONKSİYONLAR ve LİMİT ALIŞTIRMALAR.pdf", "LİMİT I.pdf"],
    "weeks": [
        {
            "id": "mat-k1",
            "title": "1. Konu — Kümeler ve Sayılar",
            "sources": ["KÜMELER ve SAYILAR.pdf", "KÜMELER ve SAYILAR_ALIŞTIRMALAR.pdf"],
            "summary": """
**Küme:** iyi tanımlanmış (kesin ayırt edilebilir) nesnelerin topluluğu. "ESTÜ BTMYO'ya kayıtlı öğrenciler" bir kümedir (kayıt listesinden kesin belirlenir);
"orta boylu öğrenciler" küme **değildir** (ölçüt belli değil).
* Elemanlar küçük, kümeler büyük harfle: a ∈ A ("a eleman A"), b ∉ A. Hiç elemanı olmayan küme **boş küme ∅** — küme cebirinde 0'ın rolünü üstlenir.
* **Gösterim:** 1) **Listeleme** {a, b, c} · 2) **Ortak özellik** { x | P(x) } — "P(x)'i sağlayan x'lerin kümesi" · 3) **Venn şeması** (kapalı eğri içine nokta).
  Örn. B = { x | x² = 36 } = {−6, 6} · { x | x sonu 2 ile biten tek doğal sayı } = ∅.

**Küme işlemleri:**
* **Eşit küme** A = B (elemanlar aynı) · **Alt küme** B ⊆ A ⇔ her x ∈ B için x ∈ A · **Öz (has) alt küme** B ⊂ A: B ⊆ A ve A'da B'de olmayan en az bir eleman var.
* **Her küme kendisinin alt kümesidir** (A ⊆ A) · **boş küme her kümenin alt kümesidir** (∅ ⊆ A).
* **Evrensel küme E:** problemle ilgili tüm elemanları içerir (problemden probleme değişir). **Tümleyen** Aᵗ (veya A') = { x | x ∈ E ve x ∉ A }.
  Örn. E = {1,…,8}, A = {1,2,3,4} → Aᵗ = {5,6,7,8}.
* **Birleşim** A ∪ B = { x | x ∈ A **veya** x ∈ B } · **Kesişim** A ∩ B = { x | x ∈ A **ve** x ∈ B } — kesişimi boş olan kümeler **ayrık** ·
  **Fark** A \\ B = { x | x ∈ A ve x ∉ B } = A ∩ Bᵗ.
* A ⊂ B ise A ∪ B = B, A ∩ B = A, A \\ B = ∅ (örn. tek doğal sayılar ⊂ doğal sayılar; B \\ A = çift doğal sayılar).

**Cebirsel özellikler:** birleşme (A ∪ B) ∪ C = A ∪ (B ∪ C) · değişme A ∪ B = B ∪ A · etkisiz/yutan: A ∪ ∅ = A, A ∪ E = E, A ∩ ∅ = ∅, A ∩ E = A ·
dağılma A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C), A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) · **De Morgan: (A ∪ B)ᵗ = Aᵗ ∩ Bᵗ, (A ∩ B)ᵗ = Aᵗ ∪ Bᵗ** ·
kapsama A ⊆ A ∪ B, A ∩ B ⊆ A.

**Sayı kümeleri:** sayma sayıları **N⁺** = {1, 2, 3, …} · doğal sayılar **N** = {0, 1, 2, …} · tam sayılar **Z** = N⁻ ∪ {0} ∪ N⁺ ·
rasyonel **Q** = { a/b | a, b ∈ Z, b ≠ 0 } · irrasyonel **Ir** = R \\ Q (√2, π) · gerçel **R** = Q ∪ Ir · karmaşık **C** = { a + ib | a, b ∈ R, i = √−1 }.
**Kapsama sırası: N ⊂ Z ⊂ Q ⊂ R ⊂ C.**
* **Sıfırla bölme tanımsız:** p/0 = y ⇒ p = 0·y çelişki (p ≠ 0) · **0/0 belirsiz:** 0 = 0·y her y için doğru, tek değer yok.
* **Rasyonel ⇔ devirli ondalık açılım:** 4/3 = 1,333… · 3/11 = 0,2727… · 5/7 = 0,714285714285… · π'nin devirli açılımı yok → irrasyonel.
* **Devirliyi kesre çevirme:** x = 0,125125… ⇒ 1000x − x = 125 ⇒ x = 125/999.
  **Pratik kural:** (virgülsüz sayı − devretmeyen kısım) / (devreden basamak sayısı kadar **9**, devretmeyen ondalık basamak sayısı kadar **0**).
  0,21̄ (1 devrediyor) = (21 − 2)/90 = 19/90 · 6,24̄ (24 devrediyor) = (624 − 6)/99 = 206/33 · 3,913̄ = (3913 − 3)/999 = 3910/999.
* **Sayı ekseni:** pozitifler orijinin sağında, negatifler solunda; eksenle R arasında **1-1 eşleme** vardır. √2 ≈ 1,41, π ≈ 3,14.

**Sıralama / eşitsizlik özellikleri (a, b, c, d ∈ R):** a < b ve b < c ⇒ a < c (geçişme) · a < b ve c < d ⇒ a + c < b + d ·
a < b ⇒ a + k < b + k · **k > 0 ise ak < bk; k < 0 ise ak > bk (negatifle çarpınca yön değişir)** · a > 0 ⇒ 1/a > 0 ·
**0 < a < b ⇒ 1/b < 1/a** · a ≠ b ise a < b veya b < a.

**Aralıklar:** (a, b) açık — uçlar dahil değil · [a, b] kapalı — uçlar dahil · (a, b] soldan açık sağdan kapalı · [a, b) soldan kapalı sağdan açık ·
sınırsız: [a, +∞), (a, +∞), (−∞, b), (−∞, b]. **∞ bir gerçel sayı değildir, yanında daima açık parantez.**
Örn. [3, 8) ∩ (−1, 5) = [3, 5) · (3, 7) ∪ (5, +∞) = (3, +∞).

**Üslü çokluklar:** aⁿ = a·a·…·a (n tane), a taban, n üs · **a⁰ = 1**, **a⁻ⁿ = 1/aⁿ**. a, b ≠ 0, m, n ∈ Z için:
aᵐ·aⁿ = aᵐ⁺ⁿ · aⁿ/aᵐ = aⁿ⁻ᵐ · (aᵐ)ⁿ = aᵐⁿ · (ab)ⁿ = aⁿbⁿ · (a/b)ⁿ = aⁿ/bⁿ · **(a/b)⁻ⁿ = (b/a)ⁿ** · b·aⁿ ± c·aⁿ = (b ± c)aⁿ.
Denklemlerde: a ∉ {−1, 0, 1} ise aⁿ = aᵐ ⇔ n = m · aⁿ = bⁿ: **n tek ise a = b, n çift ise a = b veya a = −b**.
Örnekler: 2⁸ = 256 · 2⁸/32 = 2³ = 8 · (27)² = 729 · (4³/4²)³ = 64 · (8/64)⁻³ = 8³ = 512 · 2⁶·5⁴ = 4·10⁴ = 40000.

**Köklü çokluklar:** a ≥ 0, n ∈ N için bⁿ = a ⇔ b = ⁿ√a = a^(1/n).
* a < 0 ve **n tek** → ⁿ√a = −ⁿ√(−a) (negatif): ∛(−8) = −2 · a < 0 ve **n çift** → ⁿ√a **gerçel sayı değil** (⁴√(−16) tanımsız).
* ⁿ√(ab) = ⁿ√a·ⁿ√b · ⁿ√(a/b) = ⁿ√a / ⁿ√b · c·ⁿ√a ± d·ⁿ√a = (c ± d)·ⁿ√a · ⁵√32 = 2^(5/5) = 2.
* x² = −1'i sağlayan gerçel sayı yoktur: x < 0, x = 0, x > 0 durumlarının hepsinde x² ≥ 0.

**Mutlak değer:** |a| = a'nın orijine uzaklığı: a > 0 ise a, a = 0 ise 0, a < 0 ise −a. |−5| = 5.
Özellikler: |a| = √(a²) · |a|² = a² · |−a| = |a| · −|a| ≤ a ≤ |a| · |a/b| = |a|/|b| · |aⁿ| = |a|ⁿ · |ab| = |a||b| · |a − b| = |b − a| ·
**|a + b| ≤ |a| + |b| (üçgen eşitsizliği)** · ||a| − |b|| ≤ |a − b| · |a| = max{−a, a} · daima |a| ≥ 0.
**Uzaklık:** d(x, a) = |x − a|; A(a) ile B(b) arası d = |b − a|. d(3, 7) = 4 · d(0, −7) = 7.
|x − 3| = 2 → Ç = {1, 5} · |x − 5| < 1 → (4, 6) · |x + 3| > 3 → (−∞, −6) ∪ (0, ∞).

**Alıştırma çözümleri (kaynak cevap anahtarı):** A = {1,2,3}, B = {2,5}: A \\ B = {1,3}, B \\ A = {5}, A ∪ B = {1,2,3,5}, A ∩ B = {2} ·
A ∪ B = {a,b,c,d}, A ∩ B = {a,c}, A \\ B = {b} ⇒ A = {a,b,c}, B = {a,c,d} ·
A = [−3, 7), B = [4, ∞): A ∩ B = [4, 7), A \\ B = [−3, 4), A ∪ Bᵗ = (−∞, 7), B \\ Aᵗ = [4, 7) ·
(3,7) ve [−2,4]: A ∪ B = [−2,7), A ∩ B = (3,4], A \\ B = (4,7), B \\ A = [−2,3] · 3/7 = 0,428571 (428571 devreder) · 37/125 = 0,296 ·
(2⁹³ − 2⁹²)/2⁹⁴ = 2⁹²/2⁹⁴ = 1/4 · √1,44 − ∛0,008 − ⁴√0,0081 = 1,2 − 0,2 − 0,3 = 0,7 · x^(3/2) = 27 ⇒ x = 9.
""",
            "concepts": [
                ("Boş küme ∅", "Elemanı olmayan küme; her kümenin alt kümesidir."),
                ("Öz alt küme", "B ⊂ A: B ⊆ A ve A'da B'de olmayan en az bir eleman var."),
                ("Tümleyen Aᵗ", "Evrensel kümede olup A'da olmayan elemanlar."),
                ("Ayrık kümeler", "Kesişimi boş olan kümeler: A ∩ B = ∅."),
                ("De Morgan", "(A ∪ B)ᵗ = Aᵗ ∩ Bᵗ ve (A ∩ B)ᵗ = Aᵗ ∪ Bᵗ."),
                ("Rasyonel sayı", "a/b (b ≠ 0) yazılabilen; ondalık açılımı devirlidir."),
                ("İrrasyonel sayı", "Devirli ondalık açılımı yok: √2, π."),
                ("Açık / kapalı aralık", "( ) uç dahil değil, [ ] uç dahil; ∞ yanında daima ( )."),
                ("Mutlak değer", "Sayının orijine uzaklığı; |x − a| = x ile a arası uzaklık."),
            ],
            "must": [
                "N ⊂ Z ⊂ Q ⊂ R ⊂ C; N = {0,1,2,…}, N⁺ = {1,2,…}",
                "A \\ B = A ∩ Bᵗ; De Morgan: (A ∪ B)ᵗ = Aᵗ ∩ Bᵗ",
                "∅ her kümenin, A kendisinin alt kümesidir",
                "Rasyonel ⇔ devirli ondalık; devirli → kesir: (sayı − devretmeyen) / (9'lar ve 0'lar)",
                "Negatif sayıyla çarpınca eşitsizlik yön değiştirir; 0 < a < b ⇒ 1/b < 1/a",
                "a⁰ = 1, a⁻ⁿ = 1/aⁿ, (a/b)⁻ⁿ = (b/a)ⁿ; aⁿ·aᵐ = aⁿ⁺ᵐ, (aᵐ)ⁿ = aᵐⁿ",
                "Çift dereceli kökün içi negatif olamaz; tek dereceli kök negatif çıkabilir (∛−8 = −2)",
                "p/0 tanımsız, 0/0 belirsiz",
                "|a| = √(a²); |a + b| ≤ |a| + |b|; d(A, B) = |b − a|",
            ],
            "cheat": [
                {"title": "Küme işlemleri", "columns": ["İşlem", "Tanım", "Not"], "rows": [
                    ["A ∪ B", "x ∈ A veya x ∈ B", "A ⊂ B ise A ∪ B = B"], ["A ∩ B", "x ∈ A ve x ∈ B", "∅ ise ayrık kümeler"],
                    ["A \\ B", "x ∈ A ve x ∉ B", "= A ∩ Bᵗ"], ["Aᵗ", "x ∈ E ve x ∉ A", "(Aᵗ)ᵗ = A"],
                    ["De Morgan", "(A ∪ B)ᵗ = Aᵗ ∩ Bᵗ", "(A ∩ B)ᵗ = Aᵗ ∪ Bᵗ"]]},
                {"title": "Aralıklar", "columns": ["Kümesel yazılış", "Gösterim", "Ad"], "rows": [
                    ["a < x < b", "(a, b)", "Açık aralık"], ["a ≤ x ≤ b", "[a, b]", "Kapalı aralık"],
                    ["a < x ≤ b", "(a, b]", "Soldan açık, sağdan kapalı"], ["a ≤ x < b", "[a, b)", "Soldan kapalı, sağdan açık"],
                    ["x ≥ a", "[a, +∞)", "Sağdan sınırsız"], ["x < b", "(−∞, b)", "Soldan sınırsız"]]},
                {"title": "Üs ve kök kuralları", "columns": ["Kural", "Formül"], "rows": [
                    ["Çarpım", "aᵐ·aⁿ = aᵐ⁺ⁿ"], ["Bölüm", "aⁿ / aᵐ = aⁿ⁻ᵐ"], ["Üssün üssü", "(aᵐ)ⁿ = aᵐⁿ"],
                    ["Negatif üs", "a⁻ⁿ = 1/aⁿ, (a/b)⁻ⁿ = (b/a)ⁿ"], ["Sıfırıncı kuvvet", "a⁰ = 1"],
                    ["Kök ↔ üs", "ⁿ√a = a^(1/n), ⁿ√(aᵐ) = a^(m/n)"], ["Kök çarpımı", "ⁿ√(ab) = ⁿ√a · ⁿ√b"]]},
                {"title": "Mutlak değer", "columns": ["İfade", "Çözüm (a > 0)"], "rows": [
                    ["|x − c| = a", "x = c − a veya x = c + a"], ["|x − c| < a", "c − a < x < c + a"],
                    ["|x − c| > a", "x < c − a veya x > c + a"], ["d(A, B)", "|b − a|"]]},
            ],
            "images": [("mat_mutlak_uzaklik.jpg", "Mutlak değerin geometrik anlamı: |x − 3| = 2, |x − 5| < 1, |x + 3| > 3 (KÜMELER ve SAYILAR s.17)")],
            "templates": [],
        },
        {
            "id": "mat-k2",
            "title": "2. Konu — Cebirsel İfadeler ve Çarpanlara Ayırma",
            "sources": ["CEBİRSEL İFADELERİN ÇARPANLARINA AYRILMASI.pdf"],
            "summary": """
**Temel kavramlar:** **değişken** (x — farklı değerler alır) · **sabit** (5 — hep aynı) · **parametre** (a — bazen sabit bazen değişken gibi işlem görür).
**Cebirsel ifade:** değişken/parametre/sabit ve bunların toplam, fark, çarpımlarını içeren, **eşitlik ya da eşitsizlik içermeyen** ifade: 3x − 5, ax + 2.
**Özdeşlik:** değişkenin **her** değeri için eşit olan iki ifade. (x + 1)² ≡ x² + 2x + 1.

**Önemli özdeşlikler:**
1. (a + b)² = a² + 2ab + b² · 2. (a − b)² = a² − 2ab + b²
3. (a + b + c)² = a² + b² + c² + 2(ab + ac + bc) · 4. (a − b − c)² = a² + b² + c² + 2(−ab − ac + bc)
5. **İki kare farkı: a² − b² = (a − b)(a + b)**
6. (a + b)³ = a³ + 3a²b + 3ab² + b³ · 7. (a − b)³ = a³ − 3a²b + 3ab² − b³
8. **İki küp toplamı: a³ + b³ = (a + b)(a² − ab + b²)** · 9. **İki küp farkı: a³ − b³ = (a − b)(a² + ab + b²)**

Örnekler: (3a − 2b)² = 9a² − 12ab + 4b² · 16 − 25a² = (4 − 5a)(4 + 5a) · 64 + a³ = (4 + a)(16 − 4a + a²) · 8 − y³ = (2 − y)(4 + 2y + y²) ·
(3y + 2z)³ = 27y³ + 54y²z + 36yz² + 8z³ · (x + 1)(x − 1) = x² − 1.

**Çarpanlara ayırma:** bir ifadeyi iki ya da daha çok ifadenin **çarpımı** biçiminde yazmak.

**I. Ortak çarpan parantezine alma:** ax + ay = a(x + y).
2x² − 6x + 10 = 2(x² − 3x + 5) · 5a²b² − 25ab = 5ab(ab − 5) · 5a(x − y) − 3a²(y − x) = a(x − y)(5 + 3a) ·
(a − b)² + (b − a)(2a − 2b) = (a − b)² − 2(a − b)² = −(a − b)² · a⁶ + a⁴ + a² = a²(a⁴ + a² + 1).
**Dikkat:** (y − x) = −(x − y) dönüşümü ortak çarpanı ortaya çıkarır.

**II. Gruplandırma:** ortak çarpan yoksa terimler ikişerli/üçerli gruplanır, her grup kendi içinde paranteze alınır.
a² + ab − ac − bc = a(a + b) − c(a + b) = (a + b)(a − c) · ax + by + bx + ay = (a + b)(x + y) · x³ − x² + x − 1 = (x − 1)(x² + 1) ·
2a³ − b³ + 2ab² − a²b = a²(2a − b) + b²(2a − b) = (2a − b)(a² + b²) · a(x² + 1) + x(a² + 1) = (x + a)(ax + 1) · x(x + 4) − y(y + 4) = (x − y)(x + y + 4).

**III. Özdeşliklerden yararlanma:** x² − 6x + 9 = (x − 3)² · x² − x + 1/4 = (x − 1/2)² · 0,25 + x² + x = (x + 1/2)² ·
25m² − 9n² = (5m − 3n)(5m + 3n) · 4(x + y)² − 9(x − y)² = (5y − x)(5x − y) · (x − y)² − x² = −y(2x − y) ·
**41² − 39² = (41 − 39)(41 + 39) = 160** · x³ + 27 = (x + 3)(x² − 3x + 9) · 8x³ − 0,125 = (2x − 0,5)(4x² + x + 0,25) ·
(a − b − 1)² − 4a(a − b − 1) + 4a² = [(a − b − 1) − 2a]² = (a + b + 1)².

**IV. İkinci dereceden üç terimliler:**
* **x² + bx + c:** toplamı b, çarpımı c olan m, n bulunur → (x + m)(x + n). x² + 7x + 10 = (x + 2)(x + 5).
  x² − 5x + 6 = (x − 2)(x − 3) · x² − 5x − 6 = (x − 6)(x + 1) · x² − 12x + 20 = (x − 2)(x − 10) · x² + 16x − 17 = (x + 17)(x − 1) ·
  x² + 14x + 45 = (x + 5)(x + 9) · x² − 9x + 18 = (x − 3)(x − 6) · x² − 4x − 21 = (x − 7)(x + 3).
  (x² − x)² − (x² − x) − 2: u = x² − x ⇒ (u − 2)(u + 1) = (x − 2)(x + 1)(x² − x + 1).
* **ax² + bx + c (çapraz çarpım):** a = m·n, c = p·q ve **çapraz çarpımların toplamı ortadaki terimi** veriyorsa (mx + p)(nx + q).
  3x² + 10x − 8: 3x·4 = 12x, x·(−2) = −2x, toplam 10x ✓ → (3x − 2)(x + 4).
  8x² + 22x + 15 = (2x + 3)(4x + 5) · 3x² + 10x + 3 = (3x + 1)(x + 3) · 8x² − 10x − 3 = (4x + 1)(2x − 3) · 6x² − 7x − 3 = (3x + 1)(2x − 3) ·
  15x² + 26x + 8 = (3x + 4)(5x + 2) · −4x² + 14x − 6 = −2(2x − 1)(x − 3) · −15x² − 2x + 1 = −(5x − 1)(3x + 1) ·
  a²x² − 2ax + 1 = (ax − 1)² · 9x² − 6x + 1 = (3x − 1)² · 12x² + 7x + 1 = (3x + 1)(4x + 1) · −6x² − x + 1 = (1 − 3x)(2x + 1).

**Rasyonel ifadeler:** A/B (B ≠ 0). **Sadeleştirme:** pay ve payda ayrı ayrı çarpanlarına ayrılır, ortak çarpanlar sadeleşir.
(2a² − 8b²)/(a + 2b) = 2(a − 2b)(a + 2b)/(a + 2b) = **2(a − 2b)** · (15a + 5b)/(9a² − b²) = 5/(3a − b) ·
(4a² + 12ab)/(6a³ − 54ab²) = 2/[3(a − 3b)] · (a² − 6ab + 9b²)/(a − 3b) = a − 3b · (x³ + y³)/(x² − y²) = (x² − xy + y²)/(x − y) ·
(2x² + 2x − 24)/(x² − 2x − 3) = 2(x + 4)/(x + 1) · (a² − 3a − 4)/(a² + a − 20) = (a + 1)/(a + 5) ·
(6a − 4ab − 9b + 6b²)/(4a² − 9b²) = (3 − 2b)(2a − 3b)/[(2a − 3b)(2a + 3b)] = (3 − 2b)/(2a + 3b).
""",
            "concepts": [
                ("Parametre", "Bazen sabit, bazen değişken gibi işlem gören büyüklük (a)."),
                ("Cebirsel ifade", "Eşitlik/eşitsizlik içermeyen değişkenli ifade: 3x − 5."),
                ("Özdeşlik", "Değişkenin her değeri için doğru olan eşitlik."),
                ("İki kare farkı", "a² − b² = (a − b)(a + b)."),
                ("İki küp toplamı/farkı", "a³ ± b³ = (a ± b)(a² ∓ ab + b²)."),
                ("Gruplandırma", "Ortak çarpan yoksa terimleri gruplayıp her grubu paranteze alma."),
                ("Çapraz çarpım", "ax² + bx + c'de çapraz çarpımların toplamı bx'i vermeli."),
                ("Rasyonel ifade", "A/B, B ≠ 0; sadeleştirmek için önce çarpanlara ayır."),
            ],
            "must": [
                "(a ± b)² = a² ± 2ab + b²; a² − b² = (a − b)(a + b)",
                "a³ + b³ = (a + b)(a² − ab + b²); a³ − b³ = (a − b)(a² + ab + b²)",
                "(a ± b)³ = a³ ± 3a²b + 3ab² ± b³",
                "x² + bx + c: toplamı b, çarpımı c olan iki sayı",
                "ax² + bx + c: çapraz çarpımların toplamı ortadaki terim",
                "y − x = −(x − y) ile ortak çarpan yakala",
                "Sadeleştirmeden önce pay ve paydayı ayrı ayrı çarpanlarına ayır; sadece çarpanlar sadeleşir, terimler değil",
            ],
            "cheat": [
                {"title": "Özdeşlikler", "columns": ["Ad", "Açılım"], "rows": [
                    ["Toplamın karesi", "(a + b)² = a² + 2ab + b²"], ["Farkın karesi", "(a − b)² = a² − 2ab + b²"],
                    ["Üç terim karesi", "(a + b + c)² = a² + b² + c² + 2(ab + ac + bc)"], ["İki kare farkı", "a² − b² = (a − b)(a + b)"],
                    ["Toplamın küpü", "(a + b)³ = a³ + 3a²b + 3ab² + b³"], ["Farkın küpü", "(a − b)³ = a³ − 3a²b + 3ab² − b³"],
                    ["İki küp toplamı", "a³ + b³ = (a + b)(a² − ab + b²)"], ["İki küp farkı", "a³ − b³ = (a − b)(a² + ab + b²)"]]},
                {"title": "Çarpanlara ayırma yöntemleri", "columns": ["Yöntem", "Ne zaman?", "Örnek"], "rows": [
                    ["Ortak çarpan", "Her terimde ortak çarpan var", "2x² − 6x + 10 = 2(x² − 3x + 5)"],
                    ["Gruplandırma", "Ortak çarpan yok, 4+ terim", "a² + ab − ac − bc = (a + b)(a − c)"],
                    ["Özdeşlik", "Kare/küp kalıbına benziyor", "x² − 6x + 9 = (x − 3)²"],
                    ["x² + bx + c", "Toplam b, çarpım c", "x² + 7x + 10 = (x + 2)(x + 5)"],
                    ["ax² + bx + c", "Çapraz çarpım", "3x² + 10x − 8 = (3x − 2)(x + 4)"]]},
            ],
            "images": [],
            "templates": [],
        },
        {
            "id": "mat-k3",
            "title": "3. Konu — Denklemler ve Eşitsizlikler",
            "sources": ["DENKLEMLER-EŞİTSİZLİKLER.pdf", "Denklemler_Eşitsizlikler Alıştırmalar.pdf"],
            "summary": """
**Denklem:** değişken içeren ve değişkenin **bazı** değerleri için doğru olan eşitlik. Sağlayan değerler **kök**, köklerin kümesi **çözüm kümesi Ç**.
Sınıflandırma: **bilinmeyen sayısına göre** (x + 3 = 7 bir, 2xy + y = 1 iki, x + 2y + z = 20 üç bilinmeyenli) ve **en yüksek dereceye göre** (1., 2., n. dereceden).

**Birinci derece:** ax + b = 0 (a ≠ 0) → tek çözüm **x = −b/a**, Ç = {−b/a}.
3x + 12 + x − 8 = 10 + 2x + 4 ⇒ 4x + 4 = 2x + 14 ⇒ x = 5 · (2/3)x − (1/2)x = −(1/6)x − 2 → her yanı 6 ile çarp: 4x − 3x = −x − 12 ⇒ x = −6.

**İkinci derece:** ax² + bx + c = 0 (a ≠ 0). **Diskriminant Δ = b² − 4ac:**
* **Δ < 0** → gerçel kök yok, Ç = ∅ (x² − 4x + 5 = 0: Δ = −4)
* **Δ = 0** → eşit (çakışık) iki kök x₁ = x₂ = −b/(2a) (x² − 10x + 25 = 0 → Ç = {5})
* **Δ > 0** → iki farklı kök **x₁,₂ = (−b ± √Δ)/(2a)** (4x² − 8x − 5 = 0: Δ = 144, x = (8 ± 12)/8 → Ç = {−1/2, 5/2})

**Çarpanlara ayırarak çözüm:** çarpım sıfırsa çarpanlardan en az biri sıfırdır.
2x² − 7x + 3 = (2x − 1)(x − 3) = 0 → Ç = {1/2, 3} · x² + 5x + 6 = (x + 2)(x + 3) → Ç = {−3, −2}.
* **c = 0:** ax² + bx = x(ax + b) = 0 → x = 0 veya x = −b/a. 3x² − x = 0 → Ç = {0, 1/3}
* **b = 0:** ax² + c = 0 → x² = −c/a (−c/a ≥ 0 ise) → x = ±√(−c/a). x² − 9 = 0 → Ç = {−3, 3}; x² + 64 = 0 → Ç = ∅

**Yüksek dereceli:** ortak çarpan / gruplandırma ile 1. ve 2. dereceye indirgenir.
x³ + x² = 20x ⇒ x(x + 5)(x − 4) = 0 → Ç = {−5, 0, 4} · x³ + 3x² − x − 3 = (x + 3)(x² − 1) → Ç = {−3, −1, 1}.

**Eşitsizlikler:** ax + b < 0 (≤, >, ≥) birinci derece. **Negatif sayıyla çarpınca/bölünce yön değişir.**
3 + 5x ≤ 3x − 9 ⇒ 2x ≤ −12 ⇒ x ≤ −6 → Ç = (−∞, −6] · 7 ≤ 2 − 5x < 9 ⇒ 5 ≤ −5x < 7 ⇒ (−1/5 ile çarp, yön döner) −7/5 < x ≤ −1 → Ç = (−7/5, −1] ·
5(x − 2) > 9x − 3(2x − 4) ⇒ 2x > 22 ⇒ Ç = (11, +∞).
**İşaret tablosu (1. derece):** ax + b, kök x = −b/a'nın **sağında a ile aynı**, **solunda a'nın ters** işaretini alır.

**İkinci derece eşitsizlik — ax² + bx + c'nin işareti:**
* **Δ > 0** (x₁ < x₂): **kökler dışında a'nın işareti, kökler arasında a'nın tersi** ("dışı aynı, içi ters")
* **Δ = 0:** kökte 0, diğer her yerde a'nın işareti
* **Δ < 0:** her x için a'nın işareti (a > 0 → daima pozitif)
Örnekler: x² − 3x − 4 > 0 → kökler −1, 4 → Ç = (−∞, −1) ∪ (4, +∞) · x² − 5x + 4 ≤ 0 → Ç = [1, 4] · x² + 6x + 9 ≤ 0 → Ç = {−3} · 3x² + x + 4 ≥ 0 (Δ = −47, a > 0) → Ç = R.

**Köklü denklemler:** √P(x) = Q(x) ⇔ P(x) ≥ 0, **Q(x) ≥ 0** ve P(x) = Q(x)². Kare alınır, **bulunan kökler orijinal denklemde denenir** (yabancı kök elenir).
√(3x + 4) − x = 2 ⇒ 3x + 4 = (x + 2)² ⇒ x² + x = 0 → Ç = {−1, 0}.

**Mutlak değerli (a > 0):** |P(x)| = a ⇔ P(x) = ±a · |P(x)| < a ⇔ −a < P(x) < a · |P(x)| > a ⇔ P(x) < −a veya P(x) > a.
|2x − 5| = 3 → Ç = {1, 4} · 1/|x − 3| < 3 ⇒ |x − 3| > 1/3 (x ≠ 3) → Ç = (−∞, 8/3) ∪ (10/3, +∞) · |2x + 3| ≤ 1 → Ç = [−2, −1].
**|P(x)| = negatif sayı → Ç = ∅** (örn. |2x − 8| + 10 = 2).

**Alıştırma çözümleri:**
* 1. derece: 4 + 5(2x − 3) = 3(4x − 1) → x = −4 · 3x − 4(2 − x) = 3(x − 2) − 4 → x = −1/2 · 3[2 − 4(2x − 1)] = 4x − 10 → x = 1 · 5[2 − (2x − 4)] = 2(5 − 3x) → x = 5
* 2. derece: 3x² + x − 2 → {−1, 2/3} · 2x² − x − 3 → {−1, 3/2} · 33x² + 34x − 35 (Δ = 76²) → {−5/3, 7/11} · 8x² − 22x + 15 → {5/4, 3/2} ·
  4x(3x − 2) − 7(3x − 2) → {2/3, 7/4} · 2x(5x − 2) − 3(2 − 5x) = (5x − 2)(2x + 3) → {−3/2, 2/5} · x² − 81 → {±9} · x² + 14x + 49 → {−7} · x² + 64 → ∅ · 25x² − 5x → {0, 1/5}
* Yüksek: 12x³ − 75x → {−5/2, 0, 5/2} · x³ + 4x² + 4x = x(x + 2)² → {−2, 0} · x⁴ + 2x³ − 35x² = x²(x + 7)(x − 5) → {−7, 0, 5} · 2x³ + 16x² + 66x (Δ < 0) → {0}
* Eşitsizlik: 2(5x − 8) ≤ 7(x − 3) → x ≤ −5/3 · 3x − 2(3x − 5) > 4(2x − 1) → x < 14/11 · 4 + 2(3 − 2x) ≤ 4(3x − 5) − 6x → x ≥ 3 ·
  3 + 2(x + 5) ≥ x + 5(x + 1) + 1 → x ≤ 7/4 · 10 − 13(2 − x) < 5(3x − 2) → x > −3 · −3 ≤ 7x − 14 ≤ 3 → [11/7, 17/7]
* Köklü: √(x − 2) − 5 = 0 → 27 · ∛(x + 2) + 3 = 0 → −29 · √(2x − 1) + √x = 2 → {1} · √(x − 1) + √(x + 4) = 5 → {5} · √(x + 1) + x = 5 → {3} (8 yabancı kök) · √(x − 4) + x = 6 → {5}
* Mutlak: |(x + 1)/(2x − 1)| = 3 → {2/7, 4/5} · ||2x − 3| − 1| < 10 → (−4, 7) · |2/(x − 3)| > 1/5 → (−7, 3) ∪ (3, 13) · |4x − 7| ≥ 4 → (−∞, 3/4] ∪ [11/4, ∞) · 6 − |2x + 4| = 1 → {−9/2, 1/2}
* Rasyonel = 0: (x² + x − 12)/(x² − 6x + 3) = 0 → {−4, 3} · (x² + 5x + 6)/(x² + 8x + 15) = 0 → {−2} (−3 paydayı sıfırlar) · (2x³ + 2x² − 4x)/(x³ + 2x² − 3x) = 0 → {−2}
""",
            "concepts": [
                ("Kök", "Denklemi sağlayan değer; kökler kümesi = çözüm kümesi Ç."),
                ("Diskriminant", "Δ = b² − 4ac; köklerin sayısını belirler."),
                ("Çakışık kök", "Δ = 0 → x₁ = x₂ = −b/(2a)."),
                ("İşaret kuralı", "Δ > 0: kökler dışında a'nın işareti, arasında tersi."),
                ("Yabancı kök", "Kare alınca ortaya çıkan ama orijinal denklemi sağlamayan değer."),
                ("Yön değişimi", "Eşitsizlik negatif sayıyla çarpılınca/bölününce yön değiştirir."),
                ("|P(x)| < a", "−a < P(x) < a (a > 0)."),
            ],
            "must": [
                "ax + b = 0 → x = −b/a",
                "Δ = b² − 4ac: < 0 kök yok · = 0 çakışık · > 0 iki kök (−b ± √Δ)/(2a)",
                "Çarpım = 0 ⇒ çarpanlardan biri 0; paydayı sıfırlayan kök çözüm DEĞİL",
                "Negatifle çarp/böl → eşitsizlik yön değiştirir",
                "İkinci derece işaret: dışı a'nın işareti, içi ters; Δ < 0 ve a > 0 → Ç = R",
                "Köklü denklemde kare al, sonra kökleri orijinal denklemde dene",
                "|P| = a ⇔ P = ±a · |P| < a ⇔ −a < P < a · |P| > a ⇔ P < −a veya P > a; |P| = negatif → ∅",
            ],
            "cheat": [
                {"title": "Diskriminant", "columns": ["Δ", "Kökler", "ax² + bx + c işareti"], "rows": [
                    ["Δ > 0", "x₁,₂ = (−b ± √Δ)/(2a)", "Kökler dışında a ile aynı, arasında ters"],
                    ["Δ = 0", "x₁ = x₂ = −b/(2a)", "Kökte 0, diğer yerde a ile aynı"],
                    ["Δ < 0", "Gerçel kök yok (Ç = ∅)", "Her x için a ile aynı"]]},
                {"title": "Mutlak değer ve kök kuralları", "columns": ["Biçim", "Eşdeğeri"], "rows": [
                    ["|P(x)| = a", "P(x) = a veya P(x) = −a"], ["|P(x)| < a", "−a < P(x) < a"],
                    ["|P(x)| > a", "P(x) < −a veya P(x) > a"], ["√P(x) = Q(x)", "P ≥ 0, Q ≥ 0 ve P = Q²"]]},
                {"title": "Hızlı çözüm örnekleri", "columns": ["Soru", "Ç"], "rows": [
                    ["x² − 3x − 4 > 0", "(−∞, −1) ∪ (4, ∞)"], ["x² − 5x + 4 ≤ 0", "[1, 4]"], ["x² + 6x + 9 ≤ 0", "{−3}"],
                    ["3x² + x + 4 ≥ 0", "R"], ["|2x − 5| = 3", "{1, 4}"], ["|2x + 3| ≤ 1", "[−2, −1]"], ["√(3x + 4) − x = 2", "{−1, 0}"]]},
            ],
            "images": [("mat_isaret_tablosu.jpg", "İkinci derece eşitsizliklerin işaret tablosuyla çözümü (DENKLEMLER-EŞİTSİZLİKLER s.9)")],
            "templates": [],
        },
        {
            "id": "mat-k4",
            "title": "4. Konu — Fonksiyonlar",
            "sources": ["FONKSİYONLAR.pdf", "FONKSİYONLAR ve LİMİT ALIŞTIRMALAR.pdf"],
            "summary": """
**Matematiksel model:** problemi matematiksel biçimde (formül, fonksiyon, denklem) ifade etmek; çözüm **cebirsel, nümerik veya geometrik** yolla yapılır.
Modelin çözümü gerçek sonuç olmayabilir ama iyi kurulmuşsa iyi bir yaklaşımdır.

**Fonksiyon:** her x girdisine **bir ve yalnız bir** y çıktısı karşılık getiren kural y = f(x). x **bağımsız**, y **bağımlı** değişken.
**Tanım kümesi Df:** f(x)'i anlamlı yapan x'ler · **Görüntü kümesi Rf:** elde edilen tüm y'ler. Gösterim f: Df ⊆ X → Y.

**Tanım kümesi bulma:** paydayı sıfır yapan x'ler çıkarılır, **çift dereceli kökün içi ≥ 0** olmalı, tek dereceli kökte kısıt yok.
* f(x) = √(x − 1): Df = [1, ∞), Rf = [0, ∞)
* f(x) = (x − 3)/(x² − 7x): Df = R \\ {0, 7}
* f(x) = (x − 2)/(x + 2): Df = R \\ {−2}; x'i çekersek x = 2(1 + y)/(1 − y) → **Rf = R \\ {1}**
* f(x) = 1/(x² + 1): Df = R, 0 < y ≤ 1 → Rf = (0, 1]
* f(x) = (x² − 1)/(x − 1): x = 1'de 0/0 → Df = R \\ {1}; x ≠ 1 için f(x) = x + 1 → Rf = R \\ {2}
* f(x) = 3/(2 + x²): Df = R, Rf = (0, 3/2], f(−x) = f(x) → y-eksenine göre simetrik

**Grafik:** y = f(x)'i sağlayan (x, y) ikilileri. **Düşey doğru testi:** y-eksenine paralel her doğru grafiği **en fazla bir** noktada kesiyorsa grafik bir fonksiyondur.

**Özellikler** (f: A → B):
* **Bire-bir (1-1):** x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂) — **yatay doğru grafiği en fazla bir noktada keser**
* **Örten:** her y ∈ B için f(x) = y olan en az bir x var, f(A) = B — yatay doğru **en az bir** noktada keser · f(A) ⊂ B ise **içine**
* **Artan (azalmayan):** x₁ < x₂ ⇒ f(x₁) ≤ f(x₂) · **azalan (artmayan):** x₁ < x₂ ⇒ f(x₂) ≤ f(x₁) · ikisinden biri → **monoton**
* **Çift:** f(−x) = f(x), **y-eksenine** göre simetrik · **Tek:** f(−x) = −f(x), **orijine** göre simetrik
* **Periyodik:** f(x + T) = f(x), T periyot
Örnek: y = 2x − 1 bire-bir, örten, artan; tek/çift değil · y = x²/2 − 2 bire-bir değil, R'ye örten değil, (−∞, 0)'da azalan (0, ∞)'da artan, **çift**.

**Cebirsel işlemler:** (f ± g)(x) = f(x) ± g(x) · (f·g)(x) = f(x)·g(x) · (f/g)(x) = f(x)/g(x), g(x) ≠ 0.
f = 2x − 3, g = x² + 1: f + g = x² + 2x − 2 · f − g = −x² + 2x − 4 · f·g = 2x³ − 3x² + 2x − 3.
f(x) = x/(1 − x) için (1/2)[f(x) + f(−x)] = x²/(1 − x²) = f(x²).

**Bileşke:** **(g∘f)(x) = g(f(x))** — önce f, sonra g. D(g∘f) = { x ∈ Df | f(x) ∈ Dg }. **Değişme özelliği yok: f∘g ≠ g∘f.**
f = 2x − 3, g = x² + 1: (f∘g)(x) = 2x² − 1, (g∘f)(x) = 4x² − 12x + 10 · f = x³ + 3x + 6, g = x/(1 + x): g(f(2)) = g(20) = 20/21 ·
∛(1/(1 + x²)) = h(g(f(x))), f = 1 + x², g = 1/u, h = ∛v · f = √(x + 1), g = x² + 1: f∘g = √(x² + 2), g∘f = x + 2 · f = |x|, g = x + 3: f∘g = |x + 3|, g∘f = |x| + 3.

**Ters fonksiyon:** **f bire-bir ve örten ise** f⁻¹ vardır: y = f⁻¹(x) ⇔ x = f(y). (f⁻¹)⁻¹ = f · f(f⁻¹(x)) = x, f⁻¹(f(x)) = x.
* 1. yol: y = f(x)'ten x'i çek, sonra x ↔ y yaz · 2. yol: önce x ile y'nin yerini değiştir, sonra y'yi çek.
* **f⁻¹'in grafiği, f'nin grafiğinin y = x doğrusuna (I. açıortay) göre simetriğidir.**
f(x) = 2x − 1 → f⁻¹(x) = (x + 1)/2 · f(x) = 8x³ − 1 → f⁻¹(x) = ∛((x + 1)/8) · f(x) = x + 2 → f⁻¹(x) = x − 2 ·
f(x) = (x + 2)/(2x − 5) → f⁻¹(x) = (5x + 2)/(2x − 1) · f(x) = 2x³ − 1 → f⁻¹(x) = ∛((x + 1)/2) · f(2x − 3) = (x + 1)/(x − 2) ⇒ f(x) = (x + 5)/(x − 1) = f⁻¹(x).

**Fonksiyon türleri:**
* **Polinom:** f(x) = a₀ + a₁x + … + aₙxⁿ (aₙ ≠ 0), n. derece. n = 0 **sabit** (f = a) · n = 1 **doğrusal** (ax + b; a = 1, b = 0 → **birim** f(x) = x) · n = 2 **ikinci derece** · n = 3 **kübik**.
  y = x² − x − 2: (0, −2), (−1, 0), (2, 0), simetri ekseni x = 1/2 · y = x³ − x: (−1, 0), (0, 0), (1, 0).
* **Rasyonel:** h(x) = f(x)/g(x) (f, g polinom). f(x) = (x − 2)/(x + 2): eksenleri (0, −1) ve (2, 0)'da keser, x → ±∞ iken y → 1.
* **Parçalı tanımlı:** tanım kümesinin her parçasında farklı kural. f(x) = x + 1 (x ≤ 3), x − 2 (3 < x ≤ 4), 5 − x (x > 4): f(2) = 3, f(7/2) = 3/2, f(6) = −1.
* **Salt (mutlak) değer:** s: R → [0, ∞), s(x) = |x| = −x (x < 0), 0 (x = 0), x (x > 0); grafik "V" biçimli.

**Alıştırma çözümleri:** f = 3x² − 5x, g = 1 − 3x: f∘g = 27x² − 3x − 2, g∘f = −9x² + 15x + 1 · f = x² − 3x, g = (x + 3)/x²: f(3) − g(2) = −5/4, f(5)/(1 + g(3)) = 6, f(t + 1) = t² − t − 2, g(t) = (t + 3)/t².
""",
            "concepts": [
                ("Fonksiyon", "Her x'e bir ve yalnız bir y karşılık getiren kural."),
                ("Tanım kümesi Df", "f(x)'i anlamlı yapan x'ler (payda ≠ 0, çift kök içi ≥ 0)."),
                ("Görüntü kümesi Rf", "Fonksiyonun aldığı tüm y değerleri."),
                ("Düşey doğru testi", "Dikey doğru grafiği en fazla 1 noktada keserse fonksiyondur."),
                ("Bire-bir", "Farklı x'ler farklı y'ler verir; yatay doğru en fazla 1 noktada keser."),
                ("Örten", "Değer kümesindeki her y en az bir x'in görüntüsü."),
                ("Çift / tek", "f(−x) = f(x) y-eksenine simetrik; f(−x) = −f(x) orijine simetrik."),
                ("Bileşke", "(g∘f)(x) = g(f(x)); genelde f∘g ≠ g∘f."),
                ("Ters fonksiyon", "Bire-bir ve örtende var; grafiği y = x'e göre simetrik."),
                ("Birim fonksiyon", "f(x) = x (doğrusalda a = 1, b = 0)."),
            ],
            "must": [
                "Tanım kümesi: payda ≠ 0, çift dereceli kök içi ≥ 0",
                "Görüntü kümesi için y = f(x)'ten x'i çek ve hangi y'ler için anlamlı bak",
                "Düşey doğru → fonksiyon mu? · Yatay doğru → bire-bir / örten mi?",
                "Çift: f(−x) = f(x), y-ekseni simetrisi · Tek: f(−x) = −f(x), orijin simetrisi",
                "(g∘f)(x) = g(f(x)) — içten dışa; f∘g ≠ g∘f",
                "f⁻¹ için: bire-bir + örten; x ↔ y değiştir, y'yi çek",
                "f⁻¹ grafiği = f'nin y = x'e göre simetriği",
                "Polinom türleri: sabit (n=0), doğrusal (1), ikinci derece (2), kübik (3)",
            ],
            "cheat": [
                {"title": "Fonksiyon özellikleri", "columns": ["Özellik", "Tanım", "Grafik testi"], "rows": [
                    ["Fonksiyon", "Her x'e tek y", "Düşey doğru ≤ 1 nokta"], ["Bire-bir", "x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂)", "Yatay doğru ≤ 1 nokta"],
                    ["Örten", "f(A) = B", "Yatay doğru ≥ 1 nokta"], ["Artan", "x₁ < x₂ ⇒ f(x₁) ≤ f(x₂)", "Soldan sağa yukarı"],
                    ["Çift", "f(−x) = f(x)", "y-eksenine simetrik"], ["Tek", "f(−x) = −f(x)", "Orijine simetrik"],
                    ["Periyodik", "f(x + T) = f(x)", "Aralıklarla tekrar"]]},
                {"title": "Tanım kümesi örnekleri", "columns": ["f(x)", "Df", "Rf"], "rows": [
                    ["√(x − 1)", "[1, ∞)", "[0, ∞)"], ["(x − 2)/(x + 2)", "R \\ {−2}", "R \\ {1}"], ["1/(x² + 1)", "R", "(0, 1]"],
                    ["(x² − 1)/(x − 1)", "R \\ {1}", "R \\ {2}"], ["√(x² − x − 6)", "(−∞, −2] ∪ [3, ∞)", "[0, ∞)"],
                    ["(3x − 1)/(|x − 2| − 4)", "R \\ {−2, 6}", "—"]]},
                {"title": "Ters fonksiyon örnekleri", "columns": ["f(x)", "f⁻¹(x)"], "rows": [
                    ["2x − 1", "(x + 1)/2"], ["x + 2", "x − 2"], ["8x³ − 1", "∛((x + 1)/8)"], ["2x³ − 1", "∛((x + 1)/2)"],
                    ["(x + 2)/(2x − 5)", "(5x + 2)/(2x − 1)"]]},
            ],
            "images": [("mat_bileske.jpg", "Bileşke fonksiyon g∘f şeması (FONKSİYONLAR s.9)"),
                       ("mat_ters_fonksiyon.jpg", "f ve f⁻¹ grafikleri y = x doğrusuna göre simetrik (FONKSİYONLAR s.11)")],
            "templates": [],
        },
        {
            "id": "mat-k5",
            "title": "5. Konu — Limit Kavramı",
            "sources": ["LİMİT I.pdf", "FONKSİYONLAR ve LİMİT ALIŞTIRMALAR.pdf"],
            "summary": """
**Yaklaşma:** x, a'dan farklı değerlerle a'ya istenildiği kadar yakın değerler alıyorsa x → a. **Sağdan** (a'dan büyük değerlerle) **x → a⁺**,
**soldan** (a'dan küçük değerlerle) **x → a⁻**.

**Tanım:** x, a'ya (a'dan farklı değerlerle) yaklaşırken f(x) **tek bir L** sayısına yaklaşıyorsa **lim(x→a) f(x) = L** (veya x → a iken f(x) → L).
Örnek: f(x) = 2x − 3, x → 2⁻ (1,9; 1,99; 1,999…) ve x → 2⁺ (2,1; 2,01…) için f(x) → 1 ⇒ lim(x→2) (2x − 3) = 1.

**Limit yoksa:** f(x) = x + 1 (x ≤ 0), x² (x > 0): x → 0⁻ iken f → 1, x → 0⁺ iken f → 0 → **tek sayıya yaklaşmıyor → lim(x→0) f(x) yoktur.**
Bir noktada limitin olmaması başka noktada da olmadığı anlamına gelmez: aynı f için lim(x→−1) f = 0, lim(x→1) f = 1.

**Tanımsız noktada limit:** f(x) = (x² − 4)/(x + 2) x = −2'de tanımsız (0/0) ama x ≠ −2 için f(x) = x − 2 ⇒ **lim(x→−2) f(x) = −4**.
**Önemli not:** fonksiyon bir noktada tanımsız olsa da o noktada limiti olabilir; o noktadaki değer ile limit arasında doğrudan ilişki yoktur.
**0/0 belirsizliği** limitin olmadığı anlamına gelmez — sadeleştir!

**Limit özellikleri** (lim f = L₁, lim g = L₂ varsa):
1. **Sabit:** lim(x→a) c = c · 2. **Birim:** lim(x→a) x = a
3. **Toplam/fark:** lim[f ± g] = L₁ ± L₂ · 4. **Çarpım:** lim[f·g] = L₁·L₂; özel olarak lim[c·f] = c·lim f
5. Sonlu sayıda fonksiyonun çarpımının limiti limitlerin çarpımı
6. **Bölüm:** lim f/g = L₁/L₂, **L₂ ≠ 0** koşuluyla
7. **Kök:** lim ⁿ√f(x) = ⁿ√L (n çift ise f(x) ≥ 0)
8. **Sıkıştırma:** h(x) ≤ f(x) ≤ g(x) ve lim h = lim g = L ise lim f = L
Örnek: f = x, g = −3 için lim(x→2)[f + g] = 2 + (−3) = −1.

**Sonuçlar:** lim xⁿ = aⁿ · x > 0, r ∈ R için lim xʳ = aʳ · **polinomun limiti = o noktadaki değeri:** lim(x→a) P(x) = P(a).
lim(x→2) (x³ − 5x² + 8) = 8 − 20 + 8 = **−4** · lim(x→8) ∛(x²) = 8^(2/3) = **4** · lim(x→4) √x(3x² − 7x − 1) = 2·(48 − 28 − 1) = **38** ·
lim(x→8) (2∛x + 3)/(4x + 1) = 7/33.

**0/0 durumunda:** çarpanlara ayır veya eşlenikle çarp, sadeleştir, sonra yerine koy.
* lim(x→2) (3x − 6)/(5x² − 20) = lim 3(x − 2)/[5(x − 2)(x + 2)] = 3/(5·4) = **3/20**
* lim(x→9) (x − 9)/(√x − 3) = lim (√x − 3)(√x + 3)/(√x − 3) = lim (√x + 3) = **6** (veya eşlenik √x + 3 ile çarp)

**Tek yönlü limitler:** sağdan lim(x→a⁺) f(x), soldan lim(x→a⁻) f(x).
**lim(x→a) f(x) = L ⇔ lim(x→a⁻) f(x) = lim(x→a⁺) f(x) = L.** Biri yoksa veya eşit değillerse limit yoktur.
* lim(x→0⁺) |x|/x = 1, lim(x→0⁻) |x|/x = −1 → **lim(x→0) |x|/x yoktur**
* f(x) = 3x − 1 (x ≤ 2), x + 3 (x > 2): soldan 5, sağdan 5 → lim(x→2) f(x) = **5**

**Alıştırma çözümleri:** lim(x→−1)(x² + 3x − 1) = −3 · lim(x→0)(x² − √2x + 1) = 1 · lim(x→√2)(x² − √8x + 1) = −1 · lim(x→81) √x = 9 · lim(x→32) ⁵√x = 2 ·
lim(x→1)(2x + 1)(x − 3) = −6 · lim(x→8)(∛x + 1)(3x − 1) = 69 · lim(x→0)(x√x − 1)/(3x + 4) = −1/4 · lim(x→4)(x − 4)/(x + 1) = 0 ·
lim(x→−1)(x³ + 2x − 1)/(x² + 1) = −2 · lim(x→1) ∛(x² + 5x + 2) = 2 · lim(x→0) √(x³ − 4x² + 9) = 3 · lim(x→1)(x + 1)/√(3x − 2) = 2 ·
lim(x→1)(x − 1)/(√x − 1) = 2 · lim(x→2)(x² − 3x + 2)/(x² − 4) = 1/4 · lim(x→0)(x³ − 5x² + 4x)/(x² + 6x) = 2/3 ·
lim(x→4)(x² − 4x)/(x − 4) = 4 · lim(x→−1)(x|x| + 1)/(x + 1) = 2 (x < 0'da x|x| = −x²) · lim(x→2)(x² − ax)/(2x + 5) = 2/3 ⇒ (4 − 2a)/9 = 2/3 ⇒ a = −1.
""",
            "concepts": [
                ("x → a⁺ / x → a⁻", "a'ya sağdan (büyük değerlerle) / soldan (küçük değerlerle) yaklaşma."),
                ("Limit", "x → a iken f(x)'in yaklaştığı tek L sayısı."),
                ("Limitin varlığı", "Sağdan limit = soldan limit = L."),
                ("Polinomun limiti", "lim(x→a) P(x) = P(a)."),
                ("Bölüm özelliği", "lim f/g = L₁/L₂, ancak L₂ ≠ 0 ise."),
                ("0/0", "Belirsizlik; çarpanlara ayır/eşlenikle çarp, sadeleştir."),
                ("Sıkıştırma", "h ≤ f ≤ g ve lim h = lim g = L ise lim f = L."),
            ],
            "must": [
                "lim(x→a) f = L ⇔ soldan limit = sağdan limit = L",
                "Fonksiyon a'da tanımsız olsa da limiti olabilir (değer ≠ limit)",
                "Polinom: limit = yerine koyma P(a)",
                "lim c = c, lim x = a; toplam/çarpım/bölüm limitleri (paydanın limiti ≠ 0)",
                "0/0 → çarpanlara ayır veya eşlenikle çarp: lim(x→9)(x − 9)/(√x − 3) = 6",
                "lim(x→0) |x|/x yoktur (sağdan 1, soldan −1)",
                "Parçalı fonksiyonda kırılma noktasında iki yönlü limiti ayrı ayrı hesapla",
            ],
            "cheat": [
                {"title": "Limit özellikleri", "columns": ["Özellik", "Formül"], "rows": [
                    ["Sabit", "lim c = c"], ["Birim", "lim x = a"], ["Toplam/fark", "lim(f ± g) = L₁ ± L₂"],
                    ["Çarpım", "lim(f·g) = L₁·L₂; lim(c·f) = c·L₁"], ["Bölüm", "lim(f/g) = L₁/L₂ (L₂ ≠ 0)"],
                    ["Kök", "lim ⁿ√f = ⁿ√L"], ["Kuvvet", "lim xⁿ = aⁿ, lim xʳ = aʳ (x > 0)"], ["Sıkıştırma", "h ≤ f ≤ g, lim h = lim g = L ⇒ lim f = L"]]},
                {"title": "Sık çıkan limitler", "columns": ["Limit", "Sonuç", "Yöntem"], "rows": [
                    ["lim(x→2)(2x − 3)", "1", "Yerine koy"], ["lim(x→−2)(x² − 4)/(x + 2)", "−4", "Çarpanlara ayır"],
                    ["lim(x→2)(3x − 6)/(5x² − 20)", "3/20", "Çarpanlara ayır"], ["lim(x→9)(x − 9)/(√x − 3)", "6", "Eşlenik / iki kare farkı"],
                    ["lim(x→1)(x − 1)/(√x − 1)", "2", "Eşlenik"], ["lim(x→0)|x|/x", "Yok", "Sağ 1 ≠ sol −1"],
                    ["lim(x→8)∛(x²)", "4", "8^(2/3)"]]},
            ],
            "images": [("mat_limit_tablo.jpg", "f(x) = 2x − 3 için x → 2⁻ ve x → 2⁺ değer tablosu (LİMİT I s.2)"),
                       ("mat_limit_yok.jpg", "x → 0'da soldan 1, sağdan 0: limit yok (LİMİT I s.4)"),
                       ("mat_tek_yonlu_limit.jpg", "|x|/x: sağdan 1, soldan −1 (LİMİT I s.13)"),
                       ("mat_parcali_limit.jpg", "Parçalı fonksiyonda x → 2 limiti = 5 (LİMİT I s.14)")],
            "templates": [],
        },
    ],
    "flashcards": [
        ("Boş küme hangi kümelerin alt kümesidir?", "Her kümenin (∅ ⊆ A)."),
        ("A \\ B neye eşittir?", "A ∩ Bᵗ."),
        ("De Morgan kuralları?", "(A ∪ B)ᵗ = Aᵗ ∩ Bᵗ, (A ∩ B)ᵗ = Aᵗ ∪ Bᵗ."),
        ("Sayı kümelerinin kapsama sırası?", "N ⊂ Z ⊂ Q ⊂ R ⊂ C."),
        ("Bir sayı ne zaman rasyoneldir?", "Ondalık açılımı devirli ise."),
        ("0,125125… kesir olarak?", "125/999."),
        ("p/0 ve 0/0 nedir?", "p/0 tanımsız (p ≠ 0), 0/0 belirsiz."),
        ("Eşitsizlik negatif sayıyla çarpılırsa?", "Yön değiştirir."),
        ("a⁻ⁿ ve a⁰?", "a⁻ⁿ = 1/aⁿ, a⁰ = 1."),
        ("∛(−8) ve ⁴√(−16)?", "∛(−8) = −2; ⁴√(−16) gerçel sayı değil."),
        ("|a| = √? ", "|a| = √(a²)."),
        ("A(a), B(b) noktaları arası uzaklık?", "|b − a|."),
        ("İki kare farkı?", "a² − b² = (a − b)(a + b)."),
        ("İki küp toplamı?", "a³ + b³ = (a + b)(a² − ab + b²)."),
        ("İki küp farkı?", "a³ − b³ = (a − b)(a² + ab + b²)."),
        ("(a + b)³ açılımı?", "a³ + 3a²b + 3ab² + b³."),
        ("x² + bx + c nasıl ayrılır?", "Toplamı b, çarpımı c olan m, n: (x + m)(x + n)."),
        ("41² − 39² = ?", "(41 − 39)(41 + 39) = 160."),
        ("Diskriminant ve anlamı?", "Δ = b² − 4ac: < 0 kök yok, = 0 çakışık, > 0 iki farklı kök."),
        ("İkinci derece kök formülü?", "x₁,₂ = (−b ± √Δ)/(2a)."),
        ("Δ > 0 iken ax² + bx + c'nin işareti?", "Kökler dışında a ile aynı, kökler arasında ters."),
        ("|P(x)| < a (a > 0) eşdeğeri?", "−a < P(x) < a."),
        ("Köklü denklemde son adım?", "Bulunan kökleri orijinal denklemde dene (yabancı kökü ele)."),
        ("Fonksiyon olma testi?", "Düşey doğru testi: her dikey doğru grafiği en fazla 1 noktada keser."),
        ("Bire-birlik testi?", "Yatay doğru testi: en fazla 1 noktada keser."),
        ("Çift ve tek fonksiyon?", "Çift f(−x) = f(x) y-eksenine simetrik; tek f(−x) = −f(x) orijine simetrik."),
        ("(g∘f)(x) = ?", "g(f(x)); genelde f∘g ≠ g∘f."),
        ("Ters fonksiyonun varlık şartı?", "f bire-bir ve örten olmalı."),
        ("f⁻¹ grafiği nasıl çizilir?", "f'nin grafiğinin y = x doğrusuna göre simetriği."),
        ("f(x) = 2x − 1'in tersi?", "f⁻¹(x) = (x + 1)/2."),
        ("Limitin var olma şartı?", "Sağdan ve soldan limitler var ve eşit."),
        ("Polinomun x → a limiti?", "P(a) — yerine koyma."),
        ("lim(x→0) |x|/x ?", "Yoktur (sağdan 1, soldan −1)."),
        ("lim(x→9) (x − 9)/(√x − 3) ?", "6."),
        ("Tanımsız noktada limit olabilir mi?", "Evet; (x² − 4)/(x + 2) için lim(x→−2) = −4."),
    ],
}


QUESTIONS = [
    # ── Kümeler ve Sayılar ──
    {"week": "mat-k1", "q": "\"MATEMATİK\" ve \"İSTATİSTİK\" kelimelerinin harf kümeleri A ve B ise A ∩ B hangisidir?",
     "options": ["{T, A, K}", "{K, A, T, E}", "{İ, T, A, K}", "{A, T, S, İ}"], "answer": 2,
     "explain": "A = {M, A, T, E, İ, K}, B = {İ, S, T, A, K} → ortak harfler {İ, T, A, K}."},
    {"week": "mat-k1", "q": "A = {1, 3, 5, 7, 9}, B = {3, 5, 9}, C = { x | x² = 9, x ∈ N } ise hangisi YANLIŞTIR?",
     "options": ["C ⊂ A", "A ∩ B ∩ C = C", "B ∪ C ⊂ A", "B ∩ C = B"], "answer": 3,
     "explain": "x doğal sayı olduğundan C = {3} (−3 ∉ N). B ∩ C = {3} ≠ B, diğerleri doğru."},
    {"week": "mat-k1", "q": "N doğal sayılar kümesi ve aN = { ak | k ∈ N } ise 3N ∩ 7N hangisidir?",
     "options": ["3N", "7N", "10N", "21N"], "answer": 3,
     "explain": "Hem 3'ün hem 7'nin katı olan sayılar 21'in katlarıdır: 3N ∩ 7N = 21N."},
    {"week": "mat-k1", "q": "A ve B herhangi iki küme ise A \\ B aşağıdakilerden hangisine EŞİT DEĞİLDİR?",
     "options": ["A ∩ Bᵗ", "(Aᵗ ∪ B)ᵗ", "Bᵗ \\ Aᵗ", "(A ∪ Bᵗ)ᵗ"], "answer": 3,
     "explain": "De Morgan: (A ∪ Bᵗ)ᵗ = Aᵗ ∩ B = B \\ A. Diğerleri: (Aᵗ ∪ B)ᵗ = A ∩ Bᵗ, Bᵗ \\ Aᵗ = Bᵗ ∩ A — hepsi A \\ B."},
    {"week": "mat-k1", "q": "A = { x ∈ N | 1 < x ≤ 8 }, B = { x ∈ N | x ≥ 3 } ise (A ∩ B)ᵗ (evrensel küme N) hangisidir?",
     "options": ["{2, 3}", "{3, 4, 5, 6, 7, 8}", "N \\ {2, 3}", "N \\ {3, 4, 5, 6, 7, 8}"], "answer": 3,
     "explain": "A = {2,…,8}, A ∩ B = {3,…,8}; tümleyeni N \\ {3, 4, 5, 6, 7, 8}."},
    {"week": "mat-k1", "q": "Aşağıdakilerden hangisi rasyonel sayı DEĞİLDİR?",
     "options": ["0,232323…", "1,2677… (7 devreder)", "0,323323332…", "3,576576… (576 devreder)"], "answer": 2,
     "explain": "0,323323332…'de 3'lerin sayısı artıyor, sabit tekrar eden blok yok → devirli değil → irrasyonel."},
    {"week": "mat-k1", "q": "Aşağıdakilerden hangisi irrasyonel sayıdır?",
     "options": ["∛(−8)", "⁴√12", "√18 / √2", "√4"], "answer": 1,
     "explain": "∛(−8) = −2, √18/√2 = √9 = 3, √4 = 2 rasyoneldir; ⁴√12 tam kuvvet değil → irrasyonel."},
    {"week": "mat-k1", "q": "a < b ve ka > kb ise aşağıdakilerden hangisi YANLIŞTIR?",
     "options": ["k³ < 0", "−k > 0", "k > 0", "a − b < 0"], "answer": 2,
     "explain": "Çarpınca eşitsizlik yön değiştirmiş → k < 0. Dolayısıyla k > 0 yanlıştır."},
    {"week": "mat-k1", "q": "a · b > 0 ifadesine denk olan hangisidir?",
     "options": ["a > b", "a > 0", "a² − b² > 0", "a / b > 0"], "answer": 3,
     "explain": "ab > 0 ⇔ a ve b aynı işaretli ⇔ a/b > 0."},
    {"week": "mat-k1", "q": "a > b > 0 ve c = (a + 6b)/b ise c'nin alabileceği değerler hangi aralıktadır?",
     "options": ["(−∞, 6)", "(6, ∞)", "[1, 6]", "(7, ∞)"], "answer": 3,
     "explain": "c = a/b + 6 ve a > b > 0 olduğundan a/b > 1 → c > 7."},
    {"week": "mat-k1", "q": "0,125125… devirli ondalık sayısının kesir karşılığı nedir?",
     "options": ["125/1000", "125/999", "124/999", "125/990"], "answer": 1,
     "explain": "1000x − x = 125 ⇒ 999x = 125 ⇒ x = 125/999."},
    {"week": "mat-k1", "q": "6,242424… (24 devreder) sayısının rasyonel karşılığı nedir?",
     "options": ["206/33", "624/99", "618/100", "62/9"], "answer": 0,
     "explain": "(624 − 6)/99 = 618/99 = 206/33."},
    {"week": "mat-k1", "q": "Sayı kümeleri arasındaki doğru kapsama sırası hangisidir?",
     "options": ["N ⊂ Q ⊂ Z ⊂ R ⊂ C", "Z ⊂ N ⊂ Q ⊂ R ⊂ C", "N ⊂ Z ⊂ Q ⊂ R ⊂ C", "N ⊂ Z ⊂ R ⊂ Q ⊂ C"], "answer": 2,
     "explain": "Doğal ⊂ tam ⊂ rasyonel ⊂ gerçel ⊂ karmaşık."},
    {"week": "mat-k1", "q": "[3, 8) ∩ (−1, 5) işleminin sonucu nedir?",
     "options": ["(−1, 8)", "[3, 5)", "(3, 5]", "[3, 5]"], "answer": 1,
     "explain": "Ortak kısım 3 (dahil) ile 5 (dahil değil) arası: [3, 5)."},
    {"week": "mat-k1", "q": "A = [−3, 7) ve B = [4, ∞) ise A \\ B hangisidir?",
     "options": ["[−3, 4)", "[−3, 4]", "[4, 7)", "(−3, 4)"], "answer": 0,
     "explain": "A'dan 4 ve sonrası çıkarılır: [−3, 4). (Kaynak cevap anahtarı.)"},
    {"week": "mat-k1", "q": "2² · (−1/4)² / (−2)⁴ işleminin sonucu nedir?",
     "options": ["1/16", "1/64", "−1/64", "4"], "answer": 1,
     "explain": "4 · (1/16) / 16 = (1/4)/16 = 1/64 = 2⁻⁶."},
    {"week": "mat-k1", "q": "(2⁹³ − 2⁹²) / 2⁹⁴ işleminin sonucu nedir?",
     "options": ["1/2", "1/4", "2", "1/8"], "answer": 1,
     "explain": "2⁹³ − 2⁹² = 2⁹²(2 − 1) = 2⁹² → 2⁹²/2⁹⁴ = 2⁻² = 1/4."},
    {"week": "mat-k1", "q": "x^(3/2) = 27 ise x kaçtır?",
     "options": ["3", "9", "18", "√27"], "answer": 1,
     "explain": "x = 27^(2/3) = (3³)^(2/3) = 3² = 9."},
    {"week": "mat-k1", "q": "√1,44 − ∛0,008 − ⁴√0,0081 işleminin sonucu nedir?",
     "options": ["0,7", "0,9", "1,0", "−0,2"], "answer": 0,
     "explain": "1,2 − 0,2 − 0,3 = 0,7."},
    {"week": "mat-k1", "q": "|x + 3| > 3 eşitsizliğinin çözüm kümesi nedir?",
     "options": ["(−6, 0)", "(−∞, −6) ∪ (0, ∞)", "(−∞, 0)", "[−6, 0]"], "answer": 1,
     "explain": "−3'e uzaklığı 3'ten büyük olan noktalar: x < −6 veya x > 0."},
    {"week": "mat-k1", "q": "Mutlak değer için hangisi her zaman doğrudur?",
     "options": ["|a + b| = |a| + |b|", "|a + b| ≤ |a| + |b|", "|a − b| = |a| − |b|", "|a| = a"], "answer": 1,
     "explain": "Üçgen eşitsizliği: |a + b| ≤ |a| + |b|. Eşitlik ancak a ve b aynı işaretliyse olur."},

    # ── Çarpanlara ayırma ──
    {"week": "mat-k2", "q": "(3a − 2b)² ifadesinin açılımı hangisidir?",
     "options": ["9a² − 4b²", "9a² − 6ab + 4b²", "9a² − 12ab + 4b²", "9a² + 12ab + 4b²"], "answer": 2,
     "explain": "(3a)² − 2·(3a)·(2b) + (2b)² = 9a² − 12ab + 4b²."},
    {"week": "mat-k2", "q": "16 − 25a² ifadesinin çarpanlarına ayrılmış hali hangisidir?",
     "options": ["(4 − 5a)²", "(4 − 5a)(4 + 5a)", "(16 − 5a)(16 + 5a)", "(4 − 25a)(4 + a)"], "answer": 1,
     "explain": "İki kare farkı: 4² − (5a)² = (4 − 5a)(4 + 5a)."},
    {"week": "mat-k2", "q": "64 + a³ ifadesinin çarpanlarına ayrılışı hangisidir?",
     "options": ["(4 + a)(16 − 4a + a²)", "(4 + a)(16 + 4a + a²)", "(4 − a)(16 + 4a + a²)", "(8 + a)(8 − a)"], "answer": 0,
     "explain": "İki küp toplamı a³ + b³ = (a + b)(a² − ab + b²): 4³ + a³ = (4 + a)(16 − 4a + a²)."},
    {"week": "mat-k2", "q": "a³ − b³ özdeşliği hangisidir?",
     "options": ["(a − b)(a² − ab + b²)", "(a − b)(a² + ab + b²)", "(a + b)(a² − ab + b²)", "(a − b)³"], "answer": 1,
     "explain": "İki küp farkı: a³ − b³ = (a − b)(a² + ab + b²)."},
    {"week": "mat-k2", "q": "a² + ab − ac − bc ifadesi gruplandırma ile nasıl çarpanlara ayrılır?",
     "options": ["(a + b)(a + c)", "(a − b)(a − c)", "(a + b)(a − c)", "(a − b)(a + c)"], "answer": 2,
     "explain": "a(a + b) − c(a + b) = (a + b)(a − c)."},
    {"week": "mat-k2", "q": "x³ − x² + x − 1 ifadesinin çarpanlarına ayrılmış hali hangisidir?",
     "options": ["(x − 1)(x² + 1)", "(x + 1)(x² − 1)", "(x − 1)²(x + 1)", "(x − 1)(x² − 1)"], "answer": 0,
     "explain": "x²(x − 1) + (x − 1) = (x − 1)(x² + 1)."},
    {"week": "mat-k2", "q": "5a(x − y) − 3a²(y − x) ifadesi neye eşittir?",
     "options": ["a(x − y)(5 − 3a)", "a(x − y)(5 + 3a)", "a(y − x)(5 + 3a)", "(x − y)(5a − 3a²)"], "answer": 1,
     "explain": "−3a²(y − x) = +3a²(x − y) → a(x − y)(5 + 3a)."},
    {"week": "mat-k2", "q": "x² + 7x + 10 ifadesinin çarpanlara ayrılmış hali hangisidir?",
     "options": ["(x + 1)(x + 10)", "(x + 2)(x + 5)", "(x − 2)(x − 5)", "(x + 3)(x + 4)"], "answer": 1,
     "explain": "Toplamı 7, çarpımı 10 olan sayılar 2 ve 5."},
    {"week": "mat-k2", "q": "x² − 5x − 6 ifadesinin çarpanlara ayrılmış hali hangisidir?",
     "options": ["(x − 2)(x − 3)", "(x − 6)(x + 1)", "(x + 6)(x − 1)", "(x − 3)(x + 2)"], "answer": 1,
     "explain": "Toplamı −5, çarpımı −6: −6 ve 1 → (x − 6)(x + 1)."},
    {"week": "mat-k2", "q": "3x² + 10x − 8 ifadesinin çarpanları hangisidir?",
     "options": ["(3x + 2)(x − 4)", "(3x − 2)(x + 4)", "(3x − 4)(x + 2)", "(3x + 4)(x − 2)"], "answer": 1,
     "explain": "Çapraz çarpım: 3x·4 = 12x, x·(−2) = −2x, toplam 10x ✓."},
    {"week": "mat-k2", "q": "8x² + 22x + 15 ifadesinin çarpanları hangisidir?",
     "options": ["(2x + 3)(4x + 5)", "(2x + 5)(4x + 3)", "(8x + 5)(x + 3)", "(8x + 3)(x + 5)"], "answer": 0,
     "explain": "(2x + 3)(4x + 5) = 8x² + 10x + 12x + 15 = 8x² + 22x + 15."},
    {"week": "mat-k2", "q": "41² − 39² işleminin sonucu kaçtır?",
     "options": ["4", "80", "160", "320"], "answer": 2,
     "explain": "İki kare farkı: (41 − 39)(41 + 39) = 2 · 80 = 160."},
    {"week": "mat-k2", "q": "x³ + 27 ifadesinin çarpanlara ayrılışı hangisidir?",
     "options": ["(x + 3)(x² + 3x + 9)", "(x + 3)(x² − 3x + 9)", "(x − 3)(x² + 3x + 9)", "(x + 3)³"], "answer": 1,
     "explain": "a³ + b³ = (a + b)(a² − ab + b²) → (x + 3)(x² − 3x + 9)."},
    {"week": "mat-k2", "q": "(2a² − 8b²) / (a + 2b) ifadesinin en sade hali nedir?",
     "options": ["2(a + 2b)", "2(a − 2b)", "a − 2b", "2a − 4b²"], "answer": 1,
     "explain": "2(a² − 4b²) = 2(a − 2b)(a + 2b); (a + 2b) sadeleşir → 2(a − 2b)."},
    {"week": "mat-k2", "q": "(2x² + 2x − 24) / (x² − 2x − 3) ifadesinin en sade hali nedir?",
     "options": ["2(x + 4)/(x + 1)", "2(x − 4)/(x − 1)", "(x + 4)/(x + 1)", "2(x + 3)/(x + 1)"], "answer": 0,
     "explain": "Pay 2(x + 4)(x − 3), payda (x − 3)(x + 1) → 2(x + 4)/(x + 1)."},
    {"week": "mat-k2", "q": "Değişkenin her değeri için doğru olan eşitliğe ne denir?",
     "options": ["Denklem", "Özdeşlik", "Eşitsizlik", "Cebirsel ifade"], "answer": 1,
     "explain": "Özdeşlik her değer için, denklem ise sadece bazı değerler için doğrudur. Cebirsel ifade eşitlik içermez."},

    # ── Denklemler ve eşitsizlikler ──
    {"week": "mat-k3", "q": "3x − (1 − 2x) = 9 denkleminin kökü kaçtır?",
     "options": ["−2", "2", "3", "5"], "answer": 1,
     "explain": "3x − 1 + 2x = 9 ⇒ 5x = 10 ⇒ x = 2."},
    {"week": "mat-k3", "q": "1 − 2 / (1 − 4/(3x)) = 9 denkleminin kökü kaçtır?",
     "options": ["4/3", "16/15", "15/16", "3/4"], "answer": 1,
     "explain": "2/(1 − 4/(3x)) = −8 ⇒ 1 − 4/(3x) = −1/4 ⇒ 4/(3x) = 5/4 ⇒ 3x = 16/5 ⇒ x = 16/15."},
    {"week": "mat-k3", "q": "a/3 + 1/(1 − x) = 8/(x + 2) denkleminin bir kökü 2 ise a kaçtır?",
     "options": ["−9", "5", "6", "9"], "answer": 3,
     "explain": "x = 2: a/3 + 1/(−1) = 8/4 ⇒ a/3 − 1 = 2 ⇒ a = 9."},
    {"week": "mat-k3", "q": "(3x² − 2x − 1) / (x² − 1) = 0 denkleminin çözüm kümesi nedir?",
     "options": ["{−1/3, 1}", "{−1, 1}", "{−1/3}", "{1}"], "answer": 2,
     "explain": "Pay (3x + 1)(x − 1) = 0 → x = −1/3 veya 1; ama x = 1 paydayı sıfırlar → Ç = {−1/3}."},
    {"week": "mat-k3", "q": "4x/5 + 5 = x − (1 + x)/5 denkleminin çözüm kümesi nedir?",
     "options": ["{3}", "{5}", "R", "∅"], "answer": 3,
     "explain": "5 ile çarp: 4x + 25 = 5x − 1 − x = 4x − 1 ⇒ 25 = −1 çelişki → Ç = ∅."},
    {"week": "mat-k3", "q": "3xy + y − 6x − 2 = 0 ise y kaçtır?",
     "options": ["−2", "1", "2", "3"], "answer": 2,
     "explain": "y(3x + 1) − 2(3x + 1) = 0 ⇒ (3x + 1)(y − 2) = 0 ⇒ y = 2."},
    {"week": "mat-k3", "q": "x²(2x − 1) − 3x(2x − 1) + 2(2x − 1) = 0 denkleminin çözüm kümesi nedir?",
     "options": ["{1/2}", "{1, 2}", "{1/2, 1, 2}", "{−1, −2}"], "answer": 2,
     "explain": "(2x − 1)(x² − 3x + 2) = (2x − 1)(x − 1)(x − 2) = 0 → {1/2, 1, 2}."},
    {"week": "mat-k3", "q": "2(3x − 1) > 3x + 4 eşitsizliğinin çözüm kümesi nedir?",
     "options": ["(−∞, 2)", "(−∞, 2]", "(2, ∞)", "[2, ∞)"], "answer": 2,
     "explain": "6x − 2 > 3x + 4 ⇒ 3x > 6 ⇒ x > 2."},
    {"week": "mat-k3", "q": "15 − 5(3 − 2x) ≤ 4(x − 3) eşitsizliğinin çözüm kümesi nedir?",
     "options": ["(−∞, −2]", "[−2, ∞)", "(−2, ∞)", "(−∞, 2)"], "answer": 0,
     "explain": "15 − 15 + 10x ≤ 4x − 12 ⇒ 6x ≤ −12 ⇒ x ≤ −2."},
    {"week": "mat-k3", "q": "√(13 − 4x) − x = 4 − 2x denkleminin çözüm kümesi nedir?",
     "options": ["{1}", "{1, 3}", "{−1, 3}", "{3}"], "answer": 1,
     "explain": "√(13 − 4x) = 4 − x ⇒ 13 − 4x = x² − 8x + 16 ⇒ x² − 4x + 3 = 0 → 1, 3. Deneme: x = 1 → 3 = 3 ✓, x = 3 → 1 = 1 ✓. "
                "(Alıştırma PDF'inin anahtarında {1} yazıyor; iki kök de denklemi sağlar.)"},
    {"week": "mat-k3", "q": "Sayı doğrusunda −9 ile −3 arası taranmış, uçlar boş daire ise bu küme hangi eşitsizlikle ifade edilir?",
     "options": ["−9 ≤ x < −3", "−9 ≤ x ≤ −3", "|x − 6| < 3", "|x + 6| < 3"], "answer": 3,
     "explain": "Orta nokta −6, yarıçap 3, uçlar dahil değil: |x + 6| < 3 ⇔ −9 < x < −3."},
    {"week": "mat-k3", "q": "4x² − 8x − 5 = 0 denkleminin çözüm kümesi nedir?",
     "options": ["{−1/2, 5/2}", "{1/2, −5/2}", "{−5, 1}", "∅"], "answer": 0,
     "explain": "Δ = 64 + 80 = 144; x = (8 ± 12)/8 → 5/2 ve −1/2."},
    {"week": "mat-k3", "q": "x² = 4x − 5 denkleminin gerçel sayılardaki çözüm kümesi nedir?",
     "options": ["{1, 5}", "{−1, 5}", "{2}", "∅"], "answer": 3,
     "explain": "x² − 4x + 5 = 0, Δ = 16 − 20 = −4 < 0 → gerçel kök yok."},
    {"week": "mat-k3", "q": "ax² + bx + c = 0 denkleminde Δ = 0 ise kökler için ne söylenir?",
     "options": ["Gerçel kök yoktur", "Eşit (çakışık) iki kök vardır: −b/(2a)", "İki farklı gerçel kök vardır", "Kökler zıt işaretlidir"], "answer": 1,
     "explain": "Δ = 0 → x₁ = x₂ = −b/(2a). Örn. x² − 10x + 25 = 0 → Ç = {5}."},
    {"week": "mat-k3", "q": "x³ + x² = 20x denkleminin çözüm kümesi nedir?",
     "options": ["{−5, 4}", "{−5, 0, 4}", "{−4, 0, 5}", "{0, 20}"], "answer": 1,
     "explain": "x(x² + x − 20) = x(x + 5)(x − 4) = 0 → {−5, 0, 4}."},
    {"week": "mat-k3", "q": "7 ≤ 2 − 5x < 9 eşitsizliğinin çözüm kümesi nedir?",
     "options": ["[−1, 7/5)", "(−7/5, −1]", "[−7/5, −1)", "(1, 7/5]"], "answer": 1,
     "explain": "5 ≤ −5x < 7; −1/5 ile çarpınca yön döner: −1 ≥ x > −7/5 → (−7/5, −1]."},
    {"week": "mat-k3", "q": "x² − 3x − 4 > 0 eşitsizliğinin çözüm kümesi nedir?",
     "options": ["(−1, 4)", "(−∞, −1) ∪ (4, ∞)", "(−∞, −4) ∪ (1, ∞)", "[−1, 4]"], "answer": 1,
     "explain": "Kökler −1, 4; a = 1 > 0 → kökler dışında pozitif."},
    {"week": "mat-k3", "q": "3x² + x + 4 ≥ 0 eşitsizliğinin çözüm kümesi nedir?",
     "options": ["∅", "R", "(−∞, 0]", "{−1/6}"], "answer": 1,
     "explain": "Δ = 1 − 48 = −47 < 0 ve a = 3 > 0 → ifade daima pozitif → Ç = R."},
    {"week": "mat-k3", "q": "x² + 6x + 9 ≤ 0 eşitsizliğinin çözüm kümesi nedir?",
     "options": ["∅", "{−3}", "(−∞, −3]", "R"], "answer": 1,
     "explain": "(x + 3)² ≤ 0 ancak x = −3'te sağlanır (kare negatif olamaz)."},
    {"week": "mat-k3", "q": "√(3x + 4) − x = 2 denkleminin çözüm kümesi nedir?",
     "options": ["{0}", "{−1}", "{−1, 0}", "{1, 4}"], "answer": 2,
     "explain": "3x + 4 = (x + 2)² ⇒ x² + x = 0 → 0, −1; ikisi de denklemi sağlar."},
    {"week": "mat-k3", "q": "|2x − 5| = 3 denkleminin çözüm kümesi nedir?",
     "options": ["{1, 4}", "{4}", "{−1, 4}", "{1, −4}"], "answer": 0,
     "explain": "2x − 5 = 3 → x = 4; 2x − 5 = −3 → x = 1."},
    {"week": "mat-k3", "q": "|2x + 3| ≤ 1 eşitsizliğinin çözüm kümesi nedir?",
     "options": ["[−2, −1]", "(−2, −1)", "[1, 2]", "(−∞, −2] ∪ [−1, ∞)"], "answer": 0,
     "explain": "−1 ≤ 2x + 3 ≤ 1 ⇒ −4 ≤ 2x ≤ −2 ⇒ −2 ≤ x ≤ −1."},
    {"week": "mat-k3", "q": "1 / |x − 3| < 3 eşitsizliğinin çözüm kümesi nedir?",
     "options": ["(8/3, 10/3)", "(−∞, 8/3) ∪ (10/3, ∞)", "(−∞, 3) ∪ (3, ∞)", "[8/3, 10/3]"], "answer": 1,
     "explain": "x ≠ 3, ters çevir: |x − 3| > 1/3 → x < 8/3 veya x > 10/3."},
    {"week": "mat-k3", "q": "√(x + 1) + x = 5 denkleminin çözüm kümesi nedir?",
     "options": ["{3, 8}", "{3}", "{8}", "∅"], "answer": 1,
     "explain": "√(x + 1) = 5 − x ⇒ x² − 11x + 24 = 0 → 3, 8. x = 8'de sağ taraf −3 < 0 → yabancı kök. Ç = {3}."},
    {"week": "mat-k3", "q": "|2x − 8| + 10 = 2 denkleminin çözüm kümesi nedir?",
     "options": ["{0}", "{4}", "{0, 8}", "∅"], "answer": 3,
     "explain": "|2x − 8| = −8 olur; mutlak değer negatif olamaz → Ç = ∅."},

    # ── Fonksiyonlar ──
    {"week": "mat-k4", "q": "f(x) = √(x² − x − 6) fonksiyonunun en geniş tanım kümesi nedir?",
     "options": ["[−2, 3]", "(−∞, −2] ∪ [3, ∞)", "(−∞, −3] ∪ [2, ∞)", "(−∞, −2) ∪ (3, ∞)"], "answer": 1,
     "explain": "(x − 3)(x + 2) ≥ 0 → kökler dışı: x ≤ −2 veya x ≥ 3 (uçlar dahil, kök içi 0 olabilir)."},
    {"week": "mat-k4", "q": "f(x) = √(x − 3) + √(x + 1) fonksiyonunun en geniş tanım kümesi nedir?",
     "options": ["(−∞, −1] ∪ [3, ∞)", "[−1, ∞)", "[3, ∞)", "(−∞, 3)"], "answer": 2,
     "explain": "x ≥ 3 ve x ≥ −1 aynı anda → x ≥ 3."},
    {"week": "mat-k4", "q": "f(x) = (3x − 1) / (|x − 2| − 4) fonksiyonunun tanım kümesi nedir?",
     "options": ["R \\ {1/3}", "R \\ {−2, 2}", "R \\ {−2, 6}", "R \\ {2}"], "answer": 2,
     "explain": "|x − 2| = 4 ⇒ x = 6 veya x = −2 paydayı sıfırlar."},
    {"week": "mat-k4", "q": "f(x) = (x − 2)/(x + 2) fonksiyonunun görüntü kümesi nedir?",
     "options": ["R \\ {−2}", "R \\ {1}", "R \\ {2}", "R"], "answer": 1,
     "explain": "x = 2(1 + y)/(1 − y) → y ≠ 1 için tanımlı → Rf = R \\ {1}."},
    {"week": "mat-k4", "q": "f(x) = 1/(x² + 1) fonksiyonunun görüntü kümesi nedir?",
     "options": ["(0, 1]", "[0, 1]", "(0, ∞)", "R"], "answer": 0,
     "explain": "x² + 1 ≥ 1 olduğundan 0 < y ≤ 1."},
    {"week": "mat-k4", "q": "Bir grafiğin fonksiyon belirtip belirtmediği hangi testle anlaşılır?",
     "options": ["Yatay doğru testi", "Düşey doğru testi", "Simetri testi", "Açıortay testi"], "answer": 1,
     "explain": "Düşey doğru grafiği en fazla bir noktada kesmeli. Yatay doğru testi bire-birlik/örtenlik içindir."},
    {"week": "mat-k4", "q": "f(−x) = f(x) olan fonksiyon için hangisi doğrudur?",
     "options": ["Tek fonksiyondur, orijine simetriktir", "Çift fonksiyondur, y-eksenine simetriktir",
                 "Periyodiktir", "Bire-birdir"], "answer": 1,
     "explain": "Çift fonksiyon y-eksenine göre simetriktir (örn. x²/2 − 2). Tek fonksiyon: f(−x) = −f(x), orijine simetrik."},
    {"week": "mat-k4", "q": "y = x²/2 − 2 fonksiyonu R'de hangi özelliğe sahiptir?",
     "options": ["Bire-bir", "Artan", "Çift", "Tek"], "answer": 2,
     "explain": "f(−x) = f(x) → çift. Yatay doğrular iki noktada kestiği için bire-bir değil; (−∞, 0)'da azalan, (0, ∞)'da artan."},
    {"week": "mat-k4", "q": "f(x) = 2x − 3 ve g(x) = x² + 1 ise (g∘f)(x) nedir?",
     "options": ["2x² − 1", "4x² − 12x + 10", "4x² − 12x + 9", "2x² + 1"], "answer": 1,
     "explain": "g(f(x)) = (2x − 3)² + 1 = 4x² − 12x + 10. (f∘g)(x) = 2x² − 1 olur; f∘g ≠ g∘f."},
    {"week": "mat-k4", "q": "f(x) = x³ + 3x + 6 ve g(x) = x/(1 + x) ise g(f(2)) kaçtır?",
     "options": ["20", "2/3", "20/21", "21/20"], "answer": 2,
     "explain": "f(2) = 8 + 6 + 6 = 20; g(20) = 20/21."},
    {"week": "mat-k4", "q": "f(x) = 2x − 1 fonksiyonunun tersi nedir?",
     "options": ["(x − 1)/2", "(x + 1)/2", "2x + 1", "1/(2x − 1)"], "answer": 1,
     "explain": "y = 2x − 1 ⇒ x = (y + 1)/2 → f⁻¹(x) = (x + 1)/2."},
    {"week": "mat-k4", "q": "f(x) = (x + 2)/(2x − 5) fonksiyonunun tersi nedir?",
     "options": ["(5x + 2)/(2x − 1)", "(2x − 5)/(x + 2)", "(5x − 2)/(2x + 1)", "(x − 2)/(2x + 5)"], "answer": 0,
     "explain": "x ↔ y: x(2y − 5) = y + 2 ⇒ y(2x − 1) = 5x + 2 ⇒ f⁻¹(x) = (5x + 2)/(2x − 1)."},
    {"week": "mat-k4", "q": "Bir fonksiyonun ters fonksiyonunun var olması için gerekli şart nedir?",
     "options": ["Sürekli olması", "Çift olması", "Bire-bir ve örten olması", "Polinom olması"], "answer": 2,
     "explain": "Yalnızca bire-bir ve örten fonksiyonların tersi vardır."},
    {"week": "mat-k4", "q": "f⁻¹ fonksiyonunun grafiği f'nin grafiğinin hangi doğruya göre simetriğidir?",
     "options": ["x-ekseni", "y-ekseni", "y = x (I. açıortay)", "y = −x"], "answer": 2,
     "explain": "x ile y yer değiştirdiği için grafik y = x doğrusuna göre yansır."},
    {"week": "mat-k4", "q": "f(x) = x + 1 (x ≤ 3), x − 2 (3 < x ≤ 4), 5 − x (x > 4) ise f(6) kaçtır?",
     "options": ["7", "4", "−1", "1"], "answer": 2,
     "explain": "6 > 4 → f(6) = 5 − 6 = −1. Ayrıca f(2) = 3, f(7/2) = 3/2."},
    {"week": "mat-k4", "q": "Polinom fonksiyonlarda n = 1, a = 1, b = 0 alınırsa f(x) = x fonksiyonuna ne denir?",
     "options": ["Sabit fonksiyon", "Birim fonksiyon", "Kübik fonksiyon", "Salt değer fonksiyonu"], "answer": 1,
     "explain": "f(x) = x = I(x) birim fonksiyondur; n = 0 sabit, n = 3 kübik."},
    {"week": "mat-k4", "q": "f(x) = |x| ve g(x) = x + 3 ise (f∘g)(x) nedir?",
     "options": ["|x| + 3", "|x + 3|", "|x| − 3", "x + 3"], "answer": 1,
     "explain": "f(g(x)) = |x + 3|; (g∘f)(x) = |x| + 3 olur."},

    # ── Limit ──
    {"week": "mat-k5", "q": "lim(x→2) (2x − 3) kaçtır?",
     "options": ["−1", "1", "2", "Yoktur"], "answer": 1,
     "explain": "Polinomun limiti yerine koyma: 2·2 − 3 = 1. Tablo da x → 2⁻ ve 2⁺ için f → 1 gösterir."},
    {"week": "mat-k5", "q": "lim(x→2) (x³ − 5x² + 8) kaçtır?",
     "options": ["−4", "4", "0", "8"], "answer": 0,
     "explain": "8 − 20 + 8 = −4."},
    {"week": "mat-k5", "q": "lim(x→−2) (x² − 4)/(x + 2) kaçtır?",
     "options": ["0", "Yoktur (fonksiyon tanımsız)", "−4", "4"], "answer": 2,
     "explain": "0/0; x ≠ −2 için (x − 2)(x + 2)/(x + 2) = x − 2 → −4. Tanımsız noktada limit olabilir."},
    {"week": "mat-k5", "q": "lim(x→2) (3x − 6)/(5x² − 20) kaçtır?",
     "options": ["0", "3/20", "3/10", "Yoktur"], "answer": 1,
     "explain": "3(x − 2)/[5(x − 2)(x + 2)] = 3/(5(x + 2)) → 3/20."},
    {"week": "mat-k5", "q": "lim(x→9) (x − 9)/(√x − 3) kaçtır?",
     "options": ["0", "3", "6", "9"], "answer": 2,
     "explain": "x − 9 = (√x − 3)(√x + 3) → √x + 3 → 6."},
    {"week": "mat-k5", "q": "lim(x→0) |x|/x için hangisi doğrudur?",
     "options": ["1'dir", "−1'dir", "0'dır", "Yoktur"], "answer": 3,
     "explain": "Sağdan limit 1, soldan limit −1; eşit olmadıkları için limit yoktur."},
    {"week": "mat-k5", "q": "f(x) = 3x − 1 (x ≤ 2), x + 3 (x > 2) için lim(x→2) f(x) kaçtır?",
     "options": ["5", "4", "Yoktur", "6"], "answer": 0,
     "explain": "Soldan 3·2 − 1 = 5, sağdan 2 + 3 = 5; eşit → limit 5."},
    {"week": "mat-k5", "q": "f(x) = x + 1 (x ≤ 0), x² (x > 0) için lim(x→0) f(x) için ne söylenir?",
     "options": ["0'dır", "1'dir", "Yoktur", "1/2'dir"], "answer": 2,
     "explain": "Soldan f → 1, sağdan f → 0; tek sayıya yaklaşmıyor → limit yok."},
    {"week": "mat-k5", "q": "lim(x→a) f(x) = L olması için gerek ve yeter şart nedir?",
     "options": ["f(a) = L olması", "f'nin a'da tanımlı olması",
                 "Sağdan ve soldan limitlerin var ve L'ye eşit olması", "Sadece sağdan limitin L olması"], "answer": 2,
     "explain": "lim f = L ⇔ lim(x→a⁻) f = lim(x→a⁺) f = L. Fonksiyonun a'daki değeri limiti belirlemez."},
    {"week": "mat-k5", "q": "Bölümün limiti özelliği lim f/g = L₁/L₂ hangi koşulda kullanılabilir?",
     "options": ["L₁ ≠ 0", "L₂ ≠ 0", "L₁ = L₂", "Her zaman"], "answer": 1,
     "explain": "Paydanın limiti sıfırdan farklı olmalı; L₂ = 0 ise (örn. 0/0) önce sadeleştirme gerekir."},
    {"week": "mat-k5", "q": "lim(x→8) ∛(x²) kaçtır?",
     "options": ["2", "4", "8", "16"], "answer": 1,
     "explain": "8^(2/3) = (2³)^(2/3) = 2² = 4."},
    {"week": "mat-k5", "q": "lim(x→4) (x² − 4x)/(x − 4) kaçtır?",
     "options": ["0", "1", "4", "∞"], "answer": 2,
     "explain": "x(x − 4)/(x − 4) = x → 4."},
    {"week": "mat-k5", "q": "lim(x→−1) (x|x| + 1)/(x + 1) kaçtır?",
     "options": ["−2", "−1", "1", "2"], "answer": 3,
     "explain": "x → −1 iken x < 0, |x| = −x: (1 − x²)/(x + 1) = (1 − x)(1 + x)/(x + 1) = 1 − x → 2."},
    {"week": "mat-k5", "q": "lim(x→2) (x² − ax)/(2x + 5) = 2/3 ise a kaçtır?",
     "options": ["2", "1/2", "0", "−1"], "answer": 3,
     "explain": "(4 − 2a)/9 = 2/3 ⇒ 4 − 2a = 6 ⇒ a = −1."},
    {"week": "mat-k5", "q": "lim(x→2) (x² − 3x + 2)/(x² − 4) kaçtır?",
     "options": ["0", "1/4", "1/2", "Yoktur"], "answer": 1,
     "explain": "(x − 1)(x − 2)/[(x − 2)(x + 2)] = (x − 1)/(x + 2) → 1/4."},
    {"week": "mat-k5", "q": "lim(x→1) (x − 1)/(√x − 1) kaçtır?",
     "options": ["0", "1", "2", "Yoktur"], "answer": 2,
     "explain": "x − 1 = (√x − 1)(√x + 1) → √x + 1 → 2."},
]
