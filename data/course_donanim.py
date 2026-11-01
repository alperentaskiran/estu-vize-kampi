"""BTP239 — Bilgisayar Donanımı: bilgisayarın tanımı, tarihçesi, sınıflandırılması ve sayı sistemleri.

Kaynaklar: BTP239_Hafta01.pdf, btp239_h1_donusumler.pdf (font kodlaması bozuk; slaytlar görsel olarak okundu).
"""

COURSE = {
    "id": "donanim",
    "name": "BTP239 · Bilgisayar Donanımı",
    "short": "BTP239",
    "icon": "🧮",
    "color": "#a78bfa",
    "teacher": "",
    "sources": ["BTP239_Hafta01.pdf", "btp239_h1_donusumler.pdf"],
    "weeks": [
        {
            "id": "dn-h1",
            "title": "1. Hafta — Bilgisayarın Tanımı, Tarihçesi ve Sınıflandırılması",
            "sources": ["BTP239_Hafta01.pdf"],
            "summary": """
**Bilgisayar:** veriyi alan, işleyen, saklayan ve sonuç üreten elektronik cihaz; komutları (programları) otomatik yerine getirir.
**Girdi → İşlem → Çıktı → Saklama** döngüsüyle çalışır; saat sinyaliyle senkronize, **ikili (0/1)** sistem üzerine kurulu.
Temel özellikleri: hız, doğruluk, saklama kapasitesi, otomasyon. **Kendi başına karar vermez.**

* **Veri:** işlenmemiş ham bilgi (sayı, metin, görüntü, ses) — örn. sınıftaki notlar · **Bilgi:** işlenmiş, anlam kazanmış veri — "Sınıfın ortalaması 72"
* **Donanım:** fiziksel, aşınır/bozulur/değiştirilir · **Yazılım:** komutlar bütünü, kopyalanır/güncellenir
* Temel bileşenler: CPU (beyin), RAM (geçici çalışma alanı), HDD/SSD (kalıcı), anakart, **PSU** (güç kaynağı), G/Ç birimleri
* Avantajlar: hız, doğruluk, saklama, otomasyon, iletişim, ekonomiklik · Sınırlılıklar: programsız çalışamaz, sezgi/etik yok, elektriğe bağımlı,
  arızaya/siber saldırıya açık, **GIGO ilkesi (Garbage In, Garbage Out — çöp girerse çöp çıkar)**

**Tarihçe:**
* **Abaküs** (MÖ 3000) — bilinen ilk hesap aracı, boncuklarla toplama/çıkarma, mekanik ve elle
* **1642 Blaise Pascal – Pascaline:** dişlilerle çalışan ilk mekanik hesap makinesi, **sadece toplama-çıkarma**
* **1671 Leibniz Çarkı:** **çarpma ve bölme** de yapabiliyordu; ikili sayı sistemi üzerine çalıştı
* **1837 Babbage – Analitik Makine:** delikli kartla programlanabilir ilk tasarım (ALU, bellek, G/Ç öngörülüyordu); **Ada Lovelace** ilk algoritmalar → "dünyanın ilk programcısı"
* **1890 Hollerith:** delikli kartlarla nüfus sayımı **8 yıldan 1 yıla** indi → IBM; delikli kartlar 1970'lere kadar kullanıldı
* **1941 Konrad Zuse – Z3** (Almanya): ilk programlanabilir **elektromekanik** bilgisayar, **röle** kullandı
* **1944 Howard Aiken – MARK I** (ABD): 17 m, 4,5 ton, saniyede ~3 toplama
* **1945 ENIAC:** ilk genel amaçlı elektronik bilgisayar; **17.468 vakum tüpü**, ~27 ton, 167 m², saniyede 5.000 toplama, ~150 kW; balistik hesaplar
* **1945 John von Neumann – saklı program kavramı:** program da veri gibi bellekte tutulur; **EDVAC (1951)** ilk saklı programlı bilgisayar;
  **5 birim: Giriş, Çıkış, Bellek, ALU, Kontrol Birimi**; bugünkü bilgisayarlar hâlâ bu mimariyi kullanır

**Kuşaklar:** 1. (1940–56) vakum tüpü, makine dili, delikli kart; ENIAC, EDVAC, UNIVAC · 2. (1956–63) transistör, COBOL/FORTRAN; IBM 1401, IBM 7090 ·
3. (1964–71) entegre devre, **işletim sistemleri ortaya çıktı**, klavye/monitör standart; IBM System/360, PDP-8 ·
4. (1971–günümüz) mikroişlemci; **Intel 4004 ilk ticari mikroişlemci**, 1981 IBM PC, 1984 Apple Macintosh, GUI/fare/internet ·
5. (günümüz–) yapay zekâ, **kuantum (qubit)**, biyo/DNA bilgisayarlar (araştırma aşamasında).
Enerji/hız: 1. kuşak oda boyutu, 150 kW, 5.000 işlem/s · 2. dolap, 10 kW, 100.000 · 3. masa, 1 kW, 1.000.000 · 4. el boyutu, 50 W, milyarlarca.

**Moore Yasası** (Gordon Moore, 1965, Intel kurucularından): çip üzerindeki transistör sayısı **her 2 yılda ikiye katlanır**; 50+ yıl geçerli kaldı, artık fiziksel sınırlara (5 nm altı) yaklaşıldı.

**Türkiye'de bilgisayar:** **1960 Karayolları Genel Müdürlüğü** (ilk bilgisayar) · 1964 DİE · 1970'ler üniversiteler · 1980'ler PC · **1993 TÜBİTAK öncülüğünde internet** · 2000'ler evler/okullar · 2010'lar mobil.

**Sınıflandırma:**
* **Büyüklük/kapasite:** Süper (en hızlı, paralel binlerce işlemci; hava tahmini, nükleer simülasyon, YZ eğitimi; *Frontier, Fugaku, Summit*) ·
  **Mainframe** (bankalar, sigorta, devlet; binlerce kullanıcı, 7/24; *IBM z Series, Fujitsu BS2000*) · Mini (orta ölçek, departman sunucusu; yerini bulut aldı) ·
  Mikro/kişisel (tek kullanıcı; masaüstü, dizüstü, tablet, telefon) · **Gömülü** (mikrodenetleyici, tek iş; çamaşır makinesi, mikrodalga, otomobil ECU, ATM)
* **Kullanım amacı:** genel amaçlı (yazılım yükleyerek işlev değişir) / özel amaçlı (ATM, navigasyon, tıbbi görüntüleme; yazılımı genelde değiştirilemez)
* **Veri işleme:** **Analog** (sürekli fiziksel büyüklük — termometre, eski uçak göstergesi) · **Dijital** (0/1, günümüz) · **Hibrit** (yoğun bakım monitörü, bazı simülatörler)
* **Fiziksel yapı:** masaüstü, dizüstü, tablet, akıllı telefon, sunucu, iş istasyonu. Aynı bilgisayar birden fazla gruba girebilir.
""",
            "concepts": [
                ("GIGO", "Garbage In, Garbage Out — yanlış girdi yanlış çıktı üretir."),
                ("Saklı program", "von Neumann: program da veri gibi bellekte tutulur (EDVAC, 1951)."),
                ("Moore Yasası", "Transistör sayısı her 2 yılda ikiye katlanır (1965)."),
                ("Mainframe", "Bankalarda binlerce kullanıcıya 7/24 hizmet veren ana çerçeve bilgisayar."),
                ("Gömülü sistem", "Başka cihazın içinde, tek işe adanmış, mikrodenetleyicili bilgisayar."),
                ("Hibrit bilgisayar", "Analog + dijital; yoğun bakım monitörü."),
            ],
            "must": [
                "Pascaline 1642 (toplama-çıkarma) vs Leibniz 1671 (çarpma-bölme)",
                "Z3 1941 röle · MARK I 1944 · ENIAC 1945 (17.468 tüp)",
                "Von Neumann: saklı program, EDVAC 1951, 5 birim",
                "Kuşak ↔ teknoloji ↔ örnek eşleştirmesi",
                "Moore Yasası = 2 yılda 2 kat",
                "Türkiye: 1960 Karayolları, 1993 internet",
                "Süper / mainframe / mini / mikro / gömülü örnekleri; analog-dijital-hibrit örnekleri",
            ],
            "cheat": [
                {"title": "Sınıflandırma kriterleri", "columns": ["Kriter", "Gruplar", "Örnek"], "rows": [
                    ["Büyüklük", "Süper · Mainframe · Mini · Mikro · Gömülü", "Fugaku · IBM z · departman sunucusu · laptop · ECU"],
                    ["Amaç", "Genel · Özel", "Ofis PC · ATM"], ["Veri işleme", "Analog · Dijital · Hibrit", "Termometre · PC · yoğun bakım monitörü"],
                    ["Fiziksel yapı", "Masaüstü · dizüstü · tablet · telefon · sunucu · iş istasyonu", "—"]]},
                {"title": "Kuşak karşılaştırma", "columns": ["Kuşak", "Boyut / Enerji", "Hız"], "rows": [
                    ["1", "Oda / 150 kW", "5.000 işlem/s"], ["2", "Dolap / 10 kW", "100.000 işlem/s"], ["3", "Masa / 1 kW", "1.000.000 işlem/s"],
                    ["4", "El / 50 W", "Milyarlarca işlem/s"], ["5", "Çip (potansiyel)", "Kuantum üstünlüğü"]]},
            ],
            "images": [],
            "templates": [],
        },
        {
            "id": "dn-h1b",
            "title": "1. Hafta (Ek) — Sayı Sistemleri ve Dönüşümler",
            "sources": ["btp239_h1_donusumler.pdf"],
            "summary": """
**Bilgisayar:** aritmetik (+, −, ×, ÷), mantıksal (<, >, =, VE, VEYA, ÖZEL-VEYA) işlemler; hızlı, hatasız; donanım + yazılım.
Örnek: klavyede **F** → ASCII (onluk) **70** → ikilik **1000110**.

**ASCII** (American Standard Code for Information Interchange): alfabetik/sayısal olmayan bilgiyi temsil eder. Standart tablo **0–127**, genişletilmiş **128–255**.

**Sayı sistemleri:** İkilik (2) · Sekizlik/Oktal (8: 0–7) · Onluk/Desimal (10) · Onaltılık/Heksadesimal (16: 0–9, A=10 … F=15).
**BIT** = BInary digiT, en küçük bellek birimi. **4 bit = 1 Nibble**, **8 bit = 1 Byte**, 1 KB = 1024 B = 2¹⁰ B, 1 MB = 2²⁰, 1 GB = 2³⁰, 1 TB = 2⁴⁰, PB 2⁵⁰, EB 2⁶⁰, ZB 2⁷⁰, YB 2⁸⁰.
Basamak ağırlıkları 2ⁿ⁻¹ … 2¹, 2⁰. En soldaki **MSB** (Most Significant Bit), en sağdaki **LSB** (Least Significant Bit).

**Yöntemler:**
1. **X tabanı → Onluk:** her basamak × taban^konum, topla. (10101)₂ = 16+0+4+0+1 = **21** · (403)₈ = 4·64+0+3 = **259** · (B03)₁₆ = 11·256+0+3 = **2819**
2. **Onluk → X tabanı:** sürekli tabana böl, kalanları **aşağıdan yukarı** (son bölüm MSB) oku. 37 → (100101)₂ · 67 → (103)₈ · 97 → (61)₁₆
3. **Sekizlik ↔ İkilik:** her basamak **3 bit**. (723)₈ = 111 010 011 · (100 101 011 110)₂ = (4536)₈ (sağdan 3'lü grupla, solu 0 ile tamamla)
4. **Onaltılık ↔ İkilik:** her basamak **4 bit**. (BE04)₁₆ = 1011 1110 0000 0100 · (11 1101 0101 1111)₂ → 0011 1101 0101 1111 = **(3D5F)₁₆**

**Slaytlardaki boş örneklerin çözümleri:** (110110)₂ = **54** · 192 = (11000000)₂ = (300)₈ = (C0)₁₆ · (24301)₈ = **10433** · (4056)₈ = (100000101110)₂ ·
(01111000011101110)₂ = (170356)₈ · (FA1B)₁₆ = **64027** · (C75F2)₁₆ = (11000111010111110010)₂ · (1000000010100011)₂ = **(80A3)₁₆**.

**Örnek sorular:** "Bilgisayar Donanımı" (boşluk dahil **19 karakter**) → ASCII'de karakter başına 1 bayt → **19 bayt = 152 bit**.
132 → 1 bayt yeter (0–255) · 67256 → 2 bayt yetmez (en çok 65535) → **3 bayt**.
""",
            "concepts": [
                ("Nibble", "4 bit."), ("Byte", "8 bit; bir karakteri temsil eder (ASCII)."),
                ("MSB / LSB", "En değerli (en sol) / en az değerli (en sağ) bit."),
                ("ASCII", "Standart 0–127, genişletilmiş 128–255 kod tablosu."),
                ("Oktal ↔ ikilik", "Her sekizlik basamak 3 bit."), ("Hex ↔ ikilik", "Her onaltılık basamak 4 bit."),
            ],
            "must": [
                "Bölme yönteminde kalanlar aşağıdan yukarı okunur (ilk kalan LSB)",
                "Oktal 3 bit, hex 4 bit grupla — sağdan başla, solu 0 ile doldur",
                "1 KB = 1024 B = 2¹⁰ B; 4 bit = nibble",
                "'F' = 70 = 1000110",
                "Kaç bayt? 1 bayt ≤ 255, 2 bayt ≤ 65535, 3 bayt ≤ 16.777.215",
            ],
            "cheat": [
                {"title": "Hızlı dönüşüm tablosu", "columns": ["Onluk", "İkilik", "Oktal", "Hex"], "rows": [
                    [str(i), format(i, "04b"), format(i, "o"), format(i, "X")] for i in range(16)]},
                {"title": "Birimler", "columns": ["Birim", "Değer"], "rows": [
                    ["Nibble", "4 bit"], ["Byte", "8 bit"], ["KB", "2¹⁰ B = 1024 B"], ["MB", "2²⁰ B"], ["GB", "2³⁰ B"], ["TB", "2⁴⁰ B"],
                    ["PB", "2⁵⁰ B"], ["EB", "2⁶⁰ B"], ["ZB", "2⁷⁰ B"], ["YB", "2⁸⁰ B"]]},
            ],
            "images": [],
            "templates": ["c_taban_donusum"],
        },
    ],
    "flashcards": [
        ("GIGO ilkesi?", "Garbage In, Garbage Out — çöp girerse çöp çıkar."),
        ("Pascaline hangi işlemleri yapabiliyordu?", "Sadece toplama ve çıkarma (1642)."),
        ("Leibniz Çarkı'nın Pascaline'den farkı?", "Çarpma ve bölme de yapabiliyordu (1671)."),
        ("Röle kullanan ilk programlanabilir elektromekanik bilgisayar?", "Konrad Zuse – Z3 (1941)."),
        ("ENIAC'taki vakum tüpü sayısı (BTP239 slaytı)?", "17.468."),
        ("Von Neumann mimarisinin 5 birimi?", "Giriş, Çıkış, Bellek, ALU, Kontrol Birimi."),
        ("İlk saklı programlı bilgisayar?", "EDVAC (1951)."),
        ("Moore Yasası?", "Çipteki transistör sayısı her 2 yılda ikiye katlanır."),
        ("Türkiye'ye ilk bilgisayar hangi kuruma geldi?", "Karayolları Genel Müdürlüğü (1960)."),
        ("Hibrit bilgisayar örneği?", "Yoğun bakım monitörü."),
        ("(10101)₂ = ?", "21"),
        ("37 = (?)₂", "100101"),
        ("(403)₈ = ?", "259"),
        ("(B03)₁₆ = ?", "2819"),
        ("(11110101011111)₂ = (?)₁₆", "3D5F"),
        ("'F' karakterinin ASCII kodu?", "70 → 1000110"),
        ("67256 kaç baytla ifade edilir?", "3 bayt (2 bayt en fazla 65535)."),
    ],
}

QUESTIONS = [
    {"week": "dn-h1", "q": "Yanlış programlanan bir bilgisayarın yanlış sonuç üretmesini ifade eden ilke hangisidir?",
     "options": ["Moore Yasası", "GIGO", "Von Neumann ilkesi", "Saklı program"], "answer": 1,
     "explain": "GIGO (Garbage In, Garbage Out): çöp girerse çöp çıkar. Bilgisayarın sınırlılıklarından biridir."},
    {"week": "dn-h1", "q": "Dişlilerle çalışan ilk mekanik hesap makinesi Pascaline (1642) hangi işlemleri yapabiliyordu?",
     "options": ["Dört işlem", "Sadece toplama ve çıkarma", "Sadece çarpma ve bölme", "İkili sayı işlemleri"], "answer": 1,
     "explain": "Pascaline yalnızca toplama-çıkarma yapardı. Leibniz Çarkı (1671) çarpma ve bölmeyi de ekledi."},
    {"week": "dn-h1", "q": "Röle denilen elektromekanik anahtarlar kullanan ilk programlanabilir elektromekanik bilgisayar hangisidir?",
     "options": ["MARK I", "ENIAC", "Z3", "EDVAC"], "answer": 2,
     "explain": "Konrad Zuse – Z3 (1941, Almanya). MARK I (1944, Howard Aiken) 17 m uzunluğunda, 4,5 tonluk ABD makinesidir."},
    {"week": "dn-h1", "q": "'Program da veri gibi bellekte tutulur' fikrini ortaya koyan ve bugünkü bilgisayarların hâlâ kullandığı mimari hangisidir?",
     "options": ["Harvard mimarisi", "Von Neumann mimarisi", "Babbage mimarisi", "RISC mimarisi"], "answer": 1,
     "explain": "John von Neumann (1945) saklı program kavramı; EDVAC (1951) ilk saklı programlı bilgisayar; 5 birim: Giriş, Çıkış, Bellek, ALU, Kontrol."},
    {"week": "dn-h1", "q": "Von Neumann mimarisindeki beş birim arasında hangisi YOKTUR?",
     "options": ["ALU", "Kontrol birimi", "Ekran kartı", "Bellek"], "answer": 2,
     "explain": "Beş birim: Giriş, Çıkış, Bellek, ALU, Kontrol Birimi. Ekran kartı bu temel modelin birimi değildir."},
    {"week": "dn-h1", "q": "İşletim sistemlerinin ortaya çıktığı, klavye ve monitörün standart hâle geldiği kuşak hangisidir?",
     "options": ["1. kuşak", "2. kuşak", "3. kuşak", "4. kuşak"], "answer": 2,
     "explain": "3. kuşak (1964–1971): entegre devreler, yüzlerce transistör tek çipte, işletim sistemleri, klavye/monitör standart; IBM System/360, PDP-8."},
    {"week": "dn-h1", "q": "Moore Yasası neyi ifade eder?",
     "options": ["İşlemci hızı her yıl iki katına çıkar", "Çip üzerindeki transistör sayısı yaklaşık her 2 yılda ikiye katlanır", "Bellek fiyatı her 2 yılda yarıya iner", "Enerji tüketimi her kuşakta 10 kat azalır"], "answer": 1,
     "explain": "Gordon Moore (1965, Intel kurucularından) gözlemi; 50 yıldan fazla geçerli kaldı, artık fiziksel sınırlara yaklaşıldı."},
    {"week": "dn-h1", "q": "Türkiye'ye gelen ilk bilgisayar 1960 yılında hangi kurumdaydı?",
     "options": ["TÜBİTAK", "Devlet İstatistik Enstitüsü", "Karayolları Genel Müdürlüğü", "ODTÜ"], "answer": 2,
     "explain": "1960 Karayolları Genel Müdürlüğü; 1964 DİE; 1993 TÜBİTAK öncülüğünde internet altyapısı."},
    {"week": "dn-h1", "q": "Hollerith'in delikli kart sistemi ABD nüfus sayımının süresini ne kadara indirdi (BTP239 slaytına göre)?",
     "options": ["8 yıldan 1 yıla", "10 yıldan 5 yıla", "2 yıldan 6 aya", "1 yıldan 1 aya"], "answer": 0,
     "explain": "Sayım süresi 8 yıldan 1 yıla indi; şirketi zamanla IBM'e dönüştü."},
    {"week": "dn-h1", "q": "Bankalar ve sigorta şirketlerinde binlerce kullanıcıya aynı anda, 7/24 hizmet veren bilgisayar sınıfı hangisidir?",
     "options": ["Süper bilgisayar", "Mainframe (ana çerçeve)", "Mini bilgisayar", "Gömülü sistem"], "answer": 1,
     "explain": "Mainframe: büyük kurumların veri merkezleri, yüksek güvenilirlik; IBM z Series, Fujitsu BS2000."},
    {"week": "dn-h1", "q": "Çamaşır makinesi, mikrodalga ve otomobil ECU'su hangi bilgisayar sınıfına girer?",
     "options": ["Mini bilgisayar", "Mikro bilgisayar", "Gömülü sistem", "İş istasyonu"], "answer": 2,
     "explain": "Gömülü sistemler başka cihazın içine yerleştirilmiş, tek işe adanmış, mikrodenetleyicili bilgisayarlardır."},
    {"week": "dn-h1", "q": "Yoğun bakım monitörleri veri işleme biçimine göre hangi tür bilgisayara örnektir?",
     "options": ["Analog", "Dijital", "Hibrit", "Kuantum"], "answer": 2,
     "explain": "Hibrit = analog + dijital. Analog örnek: termometre, eski uçak göstergeleri."},
    {"week": "dn-h1", "q": "Aşağıdakilerden hangisi süper bilgisayara örnek DEĞİLDİR?",
     "options": ["Frontier", "Fugaku", "Summit", "IBM z Series"], "answer": 3,
     "explain": "IBM z Series bir mainframe'dir. Frontier, Fugaku ve Summit süper bilgisayar örnekleridir."},
    {"week": "dn-h1b", "q": "(10101)₂ sayısının onluk karşılığı nedir?",
     "options": ["19", "21", "23", "42"], "answer": 1,
     "explain": "1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰ = 16 + 0 + 4 + 0 + 1 = **21**."},
    {"week": "dn-h1b", "q": "(110110)₂ sayısının onluk karşılığı nedir?",
     "options": ["46", "52", "54", "108"], "answer": 2,
     "explain": "32 + 16 + 0 + 4 + 2 + 0 = **54**."},
    {"week": "dn-h1b", "q": "(37)₁₀ sayısının ikilik karşılığı nedir?",
     "options": ["100101", "101001", "100011", "110001"], "answer": 0,
     "explain": "37/2=18 k1, 18/2=9 k0, 9/2=4 k1, 4/2=2 k0, 2/2=1 k0, son 1 → aşağıdan yukarı **100101**."},
    {"week": "dn-h1b", "q": "(192)₁₀ sayısının ikilik karşılığı nedir?",
     "options": ["10100000", "11000000", "11100000", "10010000"], "answer": 1,
     "explain": "192 = 128 + 64 → **11000000**. (IP adreslerinde 192.168… ilk oktetinin ikiliği.)"},
    {"week": "dn-h1b", "q": "(403)₈ sayısının onluk karşılığı nedir?",
     "options": ["259", "403", "323", "263"], "answer": 0,
     "explain": "4×8² + 0×8¹ + 3×8⁰ = 256 + 0 + 3 = **259**."},
    {"week": "dn-h1b", "q": "(24301)₈ sayısının onluk karşılığı nedir?",
     "options": ["10433", "10241", "9985", "12545"], "answer": 0,
     "explain": "2×4096 + 4×512 + 3×64 + 0×8 + 1 = 8192 + 2048 + 192 + 0 + 1 = **10433**."},
    {"week": "dn-h1b", "q": "(67)₁₀ sayısının sekizlik karşılığı nedir?",
     "options": ["(83)₈", "(103)₈", "(130)₈", "(43)₈"], "answer": 1,
     "explain": "67/8 = 8 kalan 3; 8/8 = 1 kalan 0; son 1 → **(103)₈**."},
    {"week": "dn-h1b", "q": "(723)₈ sayısının ikilik karşılığı nedir?",
     "options": ["111010011", "111011010", "110010011", "111010110"], "answer": 0,
     "explain": "Her oktal basamak 3 bit: 7→111, 2→010, 3→011 → **111010011**."},
    {"week": "dn-h1b", "q": "(100101011110)₂ sayısının sekizlik karşılığı nedir?",
     "options": ["(4536)₈", "(4527)₈", "(2536)₈", "(4636)₈"], "answer": 0,
     "explain": "Sağdan 3'lü grupla: 100|101|011|110 → 4 5 3 6 → **(4536)₈**."},
    {"week": "dn-h1b", "q": "(B03)₁₆ sayısının onluk karşılığı nedir?",
     "options": ["2819", "2803", "1795", "11003"], "answer": 0,
     "explain": "B=11 → 11×256 + 0×16 + 3×1 = 2816 + 3 = **2819**."},
    {"week": "dn-h1b", "q": "(FA1B)₁₆ sayısının onluk karşılığı nedir?",
     "options": ["64027", "64011", "62747", "65051"], "answer": 0,
     "explain": "15×4096 + 10×256 + 1×16 + 11 = 61440 + 2560 + 16 + 11 = **64027**."},
    {"week": "dn-h1b", "q": "(97)₁₀ sayısının onaltılık karşılığı nedir?",
     "options": ["(61)₁₆", "(16)₁₆", "(97)₁₆", "(5F)₁₆"], "answer": 0,
     "explain": "97/16 = 6 kalan 1 → **(61)₁₆**. (ASCII'de 97 = 'a'.)"},
    {"week": "dn-h1b", "q": "(BE04)₁₆ sayısının ikilik karşılığı nedir?",
     "options": ["1011111000000100", "1011111000000010", "1101111000000100", "1011111100000100"], "answer": 0,
     "explain": "Her hex basamak 4 bit: B=1011, E=1110, 0=0000, 4=0100 → **1011 1110 0000 0100**."},
    {"week": "dn-h1b", "q": "(11110101011111)₂ sayısının onaltılık karşılığı nedir?",
     "options": ["(3D5F)₁₆", "(F57C)₁₆", "(3D5E)₁₆", "(7AAF)₁₆"], "answer": 0,
     "explain": "Sağdan 4'lü grupla, solu 0 ile tamamla: 0011|1101|0101|1111 → 3 D 5 F."},
    {"week": "dn-h1b", "q": "(1000000010100011)₂ sayısının onaltılık karşılığı nedir?",
     "options": ["(80A3)₁₆", "(8A03)₁₆", "(80B3)₁₆", "(40A3)₁₆"], "answer": 0,
     "explain": "1000|0000|1010|0011 → 8 0 A 3 → **(80A3)₁₆**."},
    {"week": "dn-h1b", "q": "Klavyede basılan 'F' karakterinin ASCII kodu ve ikilik karşılığı hangisidir?",
     "options": ["65 – 1000001", "70 – 1000110", "102 – 1100110", "70 – 1000111"], "answer": 1,
     "explain": "Slayt örneği: F → onluk 70 → ikilik **1000110**. (Küçük 'f' = 102.)"},
    {"week": "dn-h1b", "q": "4 bitten oluşan birime ne ad verilir?",
     "options": ["Byte", "Word", "Nibble", "Kilobit"], "answer": 2,
     "explain": "4 bit = 1 Nibble, 8 bit = 1 Byte."},
    {"week": "dn-h1b", "q": "67256 sayısı en az kaç bayt ile ifade edilebilir?",
     "options": ["1 bayt", "2 bayt", "3 bayt", "4 bayt"], "answer": 2,
     "explain": "1 bayt en fazla 255, 2 bayt en fazla 65535 tutar. 67256 > 65535 olduğundan **3 bayt** gerekir (en fazla 16.777.215)."},
    {"week": "dn-h1b", "q": "\"Bilgisayar Donanımı\" ifadesi ASCII'de (karakter başına 1 bayt, boşluk dahil) kaç bit yer kaplar?",
     "options": ["144 bit", "152 bit", "160 bit", "19 bit"], "answer": 1,
     "explain": "Bilgisayar (10) + boşluk (1) + Donanımı (8) = 19 karakter = 19 bayt = 19 × 8 = **152 bit**."},
    {"week": "dn-h1b", "q": "Standart ASCII kod tablosu hangi aralığı kapsar?",
     "options": ["0 – 255", "0 – 127", "1 – 128", "128 – 255"], "answer": 1,
     "explain": "Standart ASCII 0–127; genişletilmiş ASCII 128–255."},
]
