"""BTP239 — Bilgisayar Donanımı: bilgisayarın tanımı, tarihçesi, sınıflandırılması, sayı sistemleri;
kasa, güç kaynağı ve UPS; anakart (form faktörü, yonga seti, veri yolları, portlar, IRQ/DMA).

Kaynaklar: BTP239_Hafta01.pdf, btp239_h1_donusumler.pdf (font kodlaması bozuk; slaytlar görsel olarak okundu),
BTP239_Hafta02.pdf, BTP239_Hafta03.pdf (görsel slaytlar ayrıca okundu).
"""

COURSE = {
    "id": "donanim",
    "name": "BTP239 · Bilgisayar Donanımı",
    "short": "BTP239",
    "icon": "🧮",
    "color": "#a78bfa",
    "teacher": "",
    "sources": ["BTP239_Hafta01.pdf", "btp239_h1_donusumler.pdf", "BTP239_Hafta02.pdf", "BTP239_Hafta03.pdf"],
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
        {
            "id": "dn-h2",
            "title": "2. Hafta — Donanımın Tanımı ve Yapısı, Kasa, Güç Kaynağı (PSU) ve UPS",
            "sources": ["BTP239_Hafta02.pdf"],
            "summary": """
**Donanım:** bilgisayarı oluşturan **fiziksel parçaların tümü** — elle tutulur, gözle görülür. **İç donanım:** kasanın içindekiler · **Dış donanım:** kasanın dışındakiler.
**Yazılım:** bilgisayarı belirli işlevleri yerine getirmek üzere yöneten **kodlanmış komutlar dizisi**; donanıma "ne yapacağını" söyler; diğer adı **program**. Türleri: **uygulama** ve **sistem** yazılımları.
**Bilgisayar = Donanım + Yazılım.** Donanım bileşenleri: CPU · Giriş, Çıkış, Depolama birimleri · RAM, Kontrol Birimi, Aritmetik ve Mantıksal İşlem Birimi (ALU).
Şema: Donanım → **Ana birimler** (HDD, RAM, işlemci, ekran kartı, anakart, power supply) + **Çevre birimleri** (girdi / çıktı) · Yazılım → işletim sistemi (Windows, DOS, Unix, Linux, MacOS) + diğer (oyun, ofis, antivirüs…).

**CPU (işlemci):** en önemli parça, "bilgisayarın beyni". Üç temel işlem: **1)** ALU ile matematiksel ve mantıksal işlemler **2)** bellekteki verilerin yerlerini değiştirme **3)** komutlara göre hareket ve yeni görev başlatma.
İşlemci kodları **16'lık (heksadesimal)** yapıdadır → **makine kodu**; her işlemcide ayrı tanımlıdır. Program = işlemcide tanımlı kodların belirli bir mantıkla sıralanmasıyla oluşan komut blokları.
**Akıllı donanım:** kendine has işlemcisi olan donanım → ana işlemcinin yükünü hafifletir, zaman kazandırır.

**Giriş birimleri:** klavye, fare, (dokunmatik) ekran, disket/CD/DVD-ROM, tarayıcı, mikrofon, modem · **Çıkış:** ekran, yazıcı, **çizici (plotter)**, hoparlör, disket/CD/DVD ·
**Depolama:** sabit disk, disket, CD/DVD-ROM, flash disk (USB bellek), hafıza kartı, taşınabilir HDD.

**Kasa:** parçaları bir arada tutan metal/plastik kutu; **tozdan, darbeden ve elektromanyetik parazitten** korur.
İyi kasa: **genişletilebilirlik, sessiz çalışma, standartlara uyum ve kalite, montaj-bakım kolaylığı, yaralanmalara karşı önlem**.
Sınıflandırma: yerleşime göre (dikey/yatay) · büyüklüğe göre (full, mid, mini) · kullanım amacına göre (masaüstü, sunucu, rack-mount).
* **Full-tower:** dikey, **en büyük** PC kasası, **60–90 cm**, küçük sunucularda; ATX + MicroATX; en az 3, bazen 5 sabit disk yeri; yerde durması uygun.
* **Mid-tower:** dikey, orta boy, **50–60 cm**; ATX + MicroATX; esnek tasarım → **en sık tercih edilen**; full-tower'dan az sürücü bölmesi.
* **Mini-tower:** dikey, mid-tower'dan alçak ama biraz geniş; **MicroATX**; **terfi (upgrade) için iyi değil**, iç soğutması en düşük.
* **Masaüstü (desktop):** **yatay**, üzerine ekran konur, yer tasarrufu; gelişme kapasitesi kısıtlı; terfi planlanmayan hazır PC'ler.
* **Slim:** hem dikey hem yatay; genelde mid-tower büyüklüğünde; ince, şık, modern.
* **Sunucu kasası:** çok sayıda bölme ve genişleme yuvası, büyük, dikdörtgen değil **kare** biçimli.
* **Rack-mount:** büyük şirketlerde çok sayıda sunucu düşey rafta; boy **U (unit)** ile: **1U = 1,75 inç** (4U = 4 × 1,75 = **7 inç**); genişlik **her zaman 19 inç (48,3 cm)**.

**Sürücü bölmeleri:** harici (kasa dışından erişilir: disket, CD/DVD-ROM) ve dâhili (kasa açılır: sabit disk). İki boy: **3½ inç** (harici → disket, dâhili → **sabit disk**) ve
**5¼ inç** (eski 5¼ disket sürücülerinden kalma; bugün **CD/DVD-ROM optik sürücüler** için; 3½ HDD takmak için özel kafesler var).

**Güç kaynağı (PSU):** aslında güç *üretmez*; **gerilim düşürücü transformatör** gibi çalışır → **220 V AC**'yi düşük voltajlı **DC**'ye çevirir: **12 V, 5 V, 3,3 V**.
Tipler: **AT** (eski, anakartta **P8/P9**) · **ATX** (modern, tek **P1**; ATX, MicroATX, FlexATX). Ortak özellikler: güç bağlantısı (priz), anakart gücü, çevre birimi konnektörleri, **fan** (PSU'yu ve kasayı soğutur).
Kaliteyi belirleyen iki özellik: **güç değeri (Watt)** ve **konnektör tipi**. Piyasada **250–1800 W**; sıradan kullanıcıya **en az 400–500 W** güvenli.
Tipik değerler: AGP kart 20–30 W · PCI kart 5 W · Ethernet 4 W · RAM 25–30 W · disket 5 W · CD-ROM 10–25 W · HDD 5200 rpm 5–11 W · HDD 7200 rpm 5–15 W ·
Dual Core 65–100 W · Core 2 Quad 95–150 W · anakart 20–30 W.
**Yetersiz güç belirtileri:** POST tamamlanamaz (POST ekranında kalır) · POST biter ama OS yüklenmez · OS yüklenir ama yük binince **sürekli yeniden başlar**.

**Konnektörler:** anakarta → **P8/P9** (AT; **siyah kablolar yan yana** takılır, aksi hâlde **anakart yanabilir**; çıkıntı ters takmayı önler) ve **P1** (ATX; 5 V ve 12 V'a ek **3,3 V**; **20 pin → yeni sistemlerde 24 pin**).
Çevre birimlerine → **Molex** (5/12 V aygıtlar; çentikli, sertçe itilir; **sarı 12 V, kırmızı 5 V, siyah toprak**) · **SATA** (SATA diskler; **15 pin, L şekli**; yoksa Molex-SATA dönüştürücü) ·
**Mini** (3½ disket sürücü standardı; ters takıp bozmak kolay).

**UPS (kesintisiz güç kaynağı):** şebekedeki çöküntü, yükselme, ani değişim, harmonik gibi dalgalanmalara karşı korur **ve** kesinti sırasında enerji üreterek sistemin devamlılığını sağlar.
**3 bileşen:** **Akü** (kesintide besler) · **Dönüştürücü / İnvertör** (akünün **DC**'sini **AC**'ye çevirir) · **Şarj ünitesi** (220 V **AC**'yi akünün depolayacağı **DC**'ye çevirir).
Karakteristikler: **VA değeri** (sağlayabileceği en fazla güç; invertör kapasitesine ve nominal AC voltaja bağlı) · **çalışma (yedekleme) süresi** (bağlı cihazların çektiği güç, ortam sıcaklığı, şarj düzeyi, dönüşüm verimi) ·
**çıkış dalga şekli** (çoğunlukla sinüzoidal) · durum lambaları (normal / aşırı yük / aküde) · aşırı yük koruması (veya sadece sigorta) · **devreye girme zamanı 2–4 ms** (uzun olan tercih edilmez).
Alırken: topraklı priz, geniş voltaj aralığı, otomatik voltaj regülasyonu, aşırı yük ve kısa devre koruması, **cold start** (elektrik yokken aküden başlatma), anahtarlama süresi ~2 ms.
""",
            "concepts": [
                ("İç / dış donanım", "Kasanın içindeki / dışındaki fiziksel bileşenler."),
                ("Makine kodu", "İşlemciye özgü, heksadesimal yapıdaki komut kodları."),
                ("Akıllı donanım", "Kendi işlemcisi olan, ana CPU'nun yükünü hafifleten donanım."),
                ("1U", "Rack-mount kasa yükseklik birimi = 1,75 inç; genişlik 19 inç."),
                ("PSU", "220 V AC'yi 12 V, 5 V, 3,3 V DC'ye çeviren güç kaynağı."),
                ("P1", "ATX anakart güç konnektörü; 20 → 24 pin, 3,3 V hattı da içerir."),
                ("İnvertör", "UPS'te akünün DC gerilimini AC'ye çeviren dönüştürücü."),
                ("VA değeri", "UPS'in sağlayabileceği en fazla güç."),
            ],
            "must": [
                "Yazılımın diğer adı: program · türleri: uygulama + sistem",
                "CPU'nun 3 işlemi: ALU işlemleri, bellekte veri taşıma, komuta göre görev başlatma",
                "Makine kodu heksadesimal ve işlemciye özgü · akıllı donanım = kendi işlemcisi var",
                "Full 60–90 cm (en büyük) · Mid 50–60 cm (en yaygın) · Mini MicroATX (terfiye uygun değil)",
                "Rack: 1U = 1,75 inç, 4U = 7 inç, genişlik her zaman 19 inç (48,3 cm)",
                "3½ inç → HDD (dâhili) / disket (harici) · 5¼ inç → CD/DVD-ROM",
                "PSU: 220 V AC → 12 V / 5 V / 3,3 V DC · AT = P8/P9, ATX = P1 (24 pin)",
                "P8/P9: siyah kablolar yan yana, yoksa anakart yanar",
                "Molex: sarı 12 V, kırmızı 5 V, siyah toprak · SATA güç 15 pin, L şekli",
                "Yetersiz güç: POST'ta kalma, OS yüklenememe, sürekli reset · en az 400–500 W",
                "UPS = akü + invertör (DC→AC) + şarj ünitesi (AC→DC) · devreye girme 2–4 ms",
            ],
            "cheat": [
                {"title": "Kasa türleri", "columns": ["Kasa", "Yerleşim", "Boyut / anakart", "Not"], "rows": [
                    ["Full-tower", "Dikey", "60–90 cm · ATX, MicroATX", "En büyük; küçük sunucular; 3–5 HDD yeri"],
                    ["Mid-tower", "Dikey", "50–60 cm · ATX, MicroATX", "En sık tercih edilen"],
                    ["Mini-tower", "Dikey", "Mid'den alçak · MicroATX", "Terfiye uygun değil, soğutma en düşük"],
                    ["Masaüstü", "Yatay", "Üstüne ekran konur", "Gelişme kapasitesi kısıtlı"],
                    ["Slim", "Dikey / yatay", "≈ mid-tower", "İnce, şık, yer tasarrufu"],
                    ["Sunucu", "—", "Büyük, kare biçim", "Çok bölme ve genişleme yuvası"],
                    ["Rack-mount", "Raf", "1U = 1,75 inç, 19 inç genişlik", "Büyük şirket veri merkezleri"]]},
                {"title": "Güç konnektörleri", "columns": ["Konnektör", "Nereye?", "Özellik"], "rows": [
                    ["P8/P9", "AT anakart", "Siyah kablolar yan yana; ters takılırsa anakart yanar"],
                    ["P1", "ATX anakart", "20 → 24 pin; 3,3 V + 5 V + 12 V"],
                    ["Molex", "5/12 V aygıtlar", "Sarı 12 V · kırmızı 5 V · siyah toprak"],
                    ["SATA", "SATA sabit disk", "15 pin, L şekli; Molex-SATA dönüştürücü var"],
                    ["Mini", "3½ disket sürücü", "Ters takıp bozmak kolay"]]},
                {"title": "Tipik güç gereksinimleri", "columns": ["Donanım", "Güç"], "rows": [
                    ["AGP kart", "20–30 W"], ["PCI kart", "5 W"], ["Ethernet kartı", "4 W"], ["RAM", "25–30 W"], ["Disket sürücü", "5 W"],
                    ["CD-ROM", "10–25 W"], ["HDD 5200 rpm", "5–11 W"], ["HDD 7200 rpm", "5–15 W"], ["Dual Core", "65–100 W"],
                    ["Core 2 Quad", "95–150 W"], ["Anakart", "20–30 W"]]},
                {"title": "UPS", "columns": ["Bileşen / özellik", "Açıklama"], "rows": [
                    ["Akü", "Kesintide sistemi besler"], ["Dönüştürücü (invertör)", "DC → AC"], ["Şarj ünitesi", "220 V AC → DC (aküyü doldurur)"],
                    ["VA değeri", "Sağlayabileceği en fazla güç"], ["Çalışma süresi", "Yük, sıcaklık, şarj düzeyi, verim"],
                    ["Dalga şekli", "Çoğunlukla sinüzoidal"], ["Devreye girme", "2–4 ms (alırken ~2 ms)"], ["Cold start", "Elektrik yokken aküden açılabilme"]]},
            ],
            "images": [("dn_bilgisayar_bilesenleri.jpg", "Bilgisayar ve bileşenleri: donanım (ana birimler, çevre birimleri) ve yazılım (BTP239_Hafta02 s.12)")],
            "templates": ["c_watt_hesabi"],
        },
        {
            "id": "dn-h3",
            "title": "3. Hafta — Anakart: Form Faktörü, Yonga Seti, Veri Yolları, Portlar, IRQ ve DMA",
            "sources": ["BTP239_Hafta03.pdf"],
            "summary": """
**Anakart üzerindekiler (s.2):** PCI, PCI-E ve **PCI-E 16x (ekran kartı)** yuvaları · giriş/çıkış portları · **12 V güç bağlantısı** · **işlemci soketi** · **kuzey köprüsü** · **RAM slotları** ·
**anakart güç kablosu soketi** · disket sürücü bağlantısı · **güney köprüsü** · IDE ve SATA girişleri · kasa ön panel bağlantıları · **BIOS pili**.

**Form faktörü:** anakartın fiziksel yapısı, boyutu, şekli; soket ve slotların dizilimi, sayısı, yerleşimi, **montaj delik sayısı**.

| Form faktörü | Boyut (mm) | En fazla slot |
|---|---|---|
| **ATX** | 305×244 | 7 |
| **Micro ATX** | 244×244 | 4 |
| Flex ATX | 229×191 | 3 |
| BTX | 325×266 | 7 |
| Micro BTX | 264×267 | 4 |
| **Mini-ITX** | 170×170 | 1 |
| Nano-ITX | 120×120 | 1 |
| **Pico-ITX** | 100×72 | – |

Montaj noktaları: **Mini-ITX → C, F, H, J** · MicroATX → B, C, F, H, J, L, M, R, S · ATX → A, C, F, G, H, J, K, L, M.
C, F, H, J üçünde de ortak → **küçük kart, büyük kasaya** takılabilir.

**Yonga seti (chipset):** anakart performansını belirler; anakarttaki **en büyük iki çipten biri**; birimler arası veri alışverişini yönetir; desteklenen **işlemci tipi, bellek tipi ve boyutu, çevre birimleri**ni belirler.
Eski sistemlerde iki parça: **Kuzey köprüsü (Northbridge)** — CPU'ya **FSB (Front Side Bus)** ile bağlı; **RAM** ve **PCI Express x16** (ekran kartı) gibi hızlı birimler.
**Güney köprüsü (Southbridge)** — kuzeye **DMI (Direct Media Interface)** ile bağlı; **S-ATA, USB, IDE, PCI, PCIe x1, HD-Audio, Super I/O (LPC), BIOS (flash, SPI), System Management Bus** gibi yavaş birimler.
Yeni sistemler: **tek yongalı sistem**.

**Veri yolları (BUS):** **adres yolu** (işlemciden birimlere tek yönlü; hangi adres?) ve **veri yolu** (çift yönlü; veri taşır) + kontrol hatları (MWTC, MRDC, IOWC, IORC); ROM, RAM, klavye, yazıcı bu yollara bağlı.
**Genişleme yuvaları:**
* **ISA** (Industry Standard Architecture) — **ilk** veri yolu, **siyah** yuvalar, **8 ve 16 bit**, artık üretilmiyor.
* **PCI** (Peripheral Component Interconnect) — **beyaz** yuvalar, **32 ve 64 bit**, ISA'dan büyük yuva, **tak-çalıştır**, **33 / 66 MHz**; LAN, SCSI, USB kartları.
* **AGP** (Advanced Graphics Port) — ekran kartı; **paralel**, **32 bit**; **1x, 2x, 4x, 8x**, **her çarpan 266 MB/s** (8x ≈ 2128 MB/s); **0,8 V, 1,5 V, 3,3 V**; yerini PCIe'ye bıraktı.
* **PCIe** (PCI Express) — **seri**; **her hat tek yön için 250 MB/s** (PCIe 1.x); **x16 = 4 GB/s**; PCI'daki **paylaşımlı** yol yerine **ayrı (noktadan noktaya) yollar**; **x1, x4, x8, x16** slotlar; PCI'dan çok daha hızlı.
  Nesiller ~her 3 yılda bant genişliğini ikiye katlar: PCIe 1.0 (2003, 2,5 GT/s) · 2.0 (2007, 5) · 3.0 (2010, 8, 128b/130b) · 4.0 (2017, 16) · 5.0 (2019, 32) · 6.0 (2021, 64 GT/s, PAM-4).

**USB:** evrensel seri veri yolu, **tak-çalıştır**, harici birimler. **USB 2.0 port siyah**; A/B tipi **4 pin**, mini/mikro **5 pin**. **USB 3.0 port mavi**, **9 pin**.

| USB | İsim | Yıl | Hız | Güç | Konnektör |
|---|---|---|---|---|---|
| 1.1 | – | 1998 | 12 Mbps | 150 mA, 5 V, 0,75 W | A, B |
| **2.0** | **High Speed** | 2000 | **480 Mbps** | 500 mA, 5 V, 2,5 W | A, B |
| **3.0** | **SuperSpeed** | 2008 | **5 Gbps** | 1,5 A, 5 V, 7,5 W | A, B |
| 3.1 | SuperSpeed+ | 2013 | 10 Gbps | 5/12/20 V, 100 W | **C** |
| 3.2 | SuperSpeed+ | 2017 | 20 Gbps | 5 A, 20 V, 100 W | C |
| **4.0** | SuperSpeed+ | 2019 | **40 Gbps** | 5 A, 20 V, 100 W | C |

**Arka panel portları:** PS/2 klavye (mor) ve fare (yeşil) · VGA/D-sub · DVI-I · HDMI · IEEE 1394a (FireWire) · optik S/PDIF çıkış · eSATA · USB 2.0 / 3.0 · **RJ-45 Gigabit LAN** · analog ses.

**Anakart seçimi:** **soket tipi** (LGA 1366, LGA 2066, **AM4 1331 pin**, **TR4 4094 pin**) · **FSB hızı** · bellek desteği · slot tipi ve sayısı · tümleşik kartlar · **disk arayüzü (SATA / IDE-PATA)**.
**Ek özellikler:** aşırı gerilim, aşırı ısınma, elektrik kesilmesi, statik elektrik, nem korumaları · **ikili BIOS** · üzerinde hazır sistemler · overclock kolaylığı · donanım arıza göstergeleri ·
USB ile hızlı/kapalıyken şarj · akıllı güç yönetimi · kolay BIOS yedekleme · otomatik performans optimizasyonu.

**IRQ (kesme istekleri):** **0–15, 16 hat**; bir aygıt **tek** IRQ kullanır; iki aygıt aynı IRQ'yu kullanırsa **IRQ çakışması → sistem kilitlenebilir**.
**IRQ 0 sistem saati** · **1 klavye** · 2 programlanabilir (COM3/COM4, modem) · 3 COM2 · 4 COM1 · 5 ses kartı (LPT2) · **6 disket denetleyicisi** · **7 LPT1** (ilk paralel port) ·
**8 gerçek zamanlı saat (RTC)** · 9–11 serbest (ağ, ses, SCSI, PCI) · **12 PS/2 fare** · **13 FPU (matematik işlemci)** · **14 birinci IDE** · **15 ikinci IDE**.
**DMA kanalları:** aygıtların **doğrudan bellek** ile veri alışverişi yaptığı yollar (CPU'yu meşgul etmeden); **8 kanal, 0–7**; ses kartı, disket, yazıcı portu, ağ kartı.
""",
            "concepts": [
                ("Form faktörü", "Anakartın boyutu, şekli, slot/soket dizilimi ve montaj delikleri."),
                ("Yonga seti", "Birimler arası veri trafiğini yöneten, desteklenen CPU/RAM'i belirleyen çip(ler)."),
                ("Kuzey köprüsü", "CPU (FSB), RAM ve PCIe x16 gibi hızlı birimler."),
                ("Güney köprüsü", "SATA, USB, PCI, ses, BIOS gibi yavaş birimler; kuzeye DMI ile bağlı."),
                ("PCIe hattı", "Seri, ayrı yol; tek yönde 250 MB/s; x16 = 4 GB/s."),
                ("IRQ", "Aygıtın CPU'dan dikkat istediği kesme hattı (0–15)."),
                ("DMA", "CPU'ya uğramadan doğrudan bellek erişimi; 8 kanal (0–7)."),
            ],
            "must": [
                "ATX 305×244 (7 slot) · Micro ATX 244×244 (4) · Mini-ITX 170×170 (1) · en küçük Pico-ITX 100×72",
                "Mini-ITX montaj noktaları C, F, H, J — ATX ve MicroATX'te de var",
                "Kuzey: CPU-FSB, RAM, PCIe x16 · Güney: SATA, USB, PCI, ses, BIOS (DMI ile bağlı)",
                "ISA: ilk, siyah, 8/16 bit · PCI: beyaz, 32/64 bit, 33/66 MHz, tak-çalıştır",
                "AGP: paralel, 32 bit, çarpan başına 266 MB/s, 0,8/1,5/3,3 V",
                "PCIe: seri, hat başına 250 MB/s, x16 = 4 GB/s, ayrı yollar",
                "USB 2.0 siyah 4 pin 480 Mbps · USB 3.0 mavi 9 pin 5 Gbps · USB 4.0 40 Gbps",
                "AM4 1331 pin · TR4 4094 pin",
                "16 IRQ (0–15): 0 saat, 1 klavye, 6 disket, 8 RTC, 12 PS/2 fare, 13 FPU, 14/15 IDE",
                "IRQ çakışması → kilitlenme · DMA 8 kanal (0–7)",
            ],
            "cheat": [
                {"title": "Form faktörleri", "columns": ["Form faktörü", "Boyut (mm)", "En fazla slot", "Montaj noktaları"], "rows": [
                    ["ATX", "305×244", "7", "A, C, F, G, H, J, K, L, M"], ["Micro ATX", "244×244", "4", "B, C, F, H, J, L, M, R, S"],
                    ["Flex ATX", "229×191", "3", "—"], ["BTX", "325×266", "7", "—"], ["Micro BTX", "264×267", "4", "—"],
                    ["Mini-ITX", "170×170", "1", "C, F, H, J"], ["Nano-ITX", "120×120", "1", "—"], ["Pico-ITX", "100×72", "–", "—"]]},
                {"title": "Genişleme yuvaları", "columns": ["Yuva", "Renk / iletişim", "Genişlik", "Hız"], "rows": [
                    ["ISA", "Siyah", "8 / 16 bit", "İlk veri yolu, artık yok"], ["PCI", "Beyaz, paylaşımlı", "32 / 64 bit", "33 / 66 MHz, tak-çalıştır"],
                    ["AGP", "Paralel", "32 bit", "Çarpan × 266 MB/s (1x–8x)"], ["PCIe", "Seri, ayrı yollar", "x1, x4, x8, x16", "Hat başına 250 MB/s; x16 = 4 GB/s"]]},
                {"title": "IRQ tablosu", "columns": ["IRQ", "Aygıt"], "rows": [
                    ["0", "Sistem saati"], ["1", "Klavye"], ["2", "Programlanabilir (COM3/4, modem)"], ["3", "COM2"], ["4", "COM1"], ["5", "Ses kartı / LPT2"],
                    ["6", "Disket denetleyicisi"], ["7", "LPT1 (paralel port)"], ["8", "Gerçek zamanlı saat"], ["9–11", "Serbest (ağ, ses, SCSI, PCI)"],
                    ["12", "PS/2 fare"], ["13", "FPU (matematik işlemci)"], ["14", "Birinci IDE"], ["15", "İkinci IDE"]]},
                {"title": "Kuzey ve güney köprüsü", "columns": ["Köprü", "Bağlı birimler"], "rows": [
                    ["Kuzey (Northbridge)", "CPU (FSB), RAM, PCI Express x16"],
                    ["Güney (Southbridge)", "S-ATA, USB, IDE, PCI, PCIe x1, HD-Audio, Super I/O, BIOS (flash), SMBus"]]},
            ],
            "images": [("dn_anakart.jpg", "Anakart üzerindeki bileşenler (BTP239_Hafta03 s.2)"),
                       ("dn_form_faktoru.jpg", "Form faktörü boyutları ve en fazla slot sayısı (s.4)"),
                       ("dn_kuzey_guney.jpg", "Kuzey-güney köprüsü mimarisi (s.10)"),
                       ("dn_usb_tablo.jpg", "USB sürümleri: hız, güç ve konnektör (s.22)"),
                       ("dn_portlar.jpg", "Anakart arka panel portları (s.23)")],
            "templates": ["c_bant_genisligi"],
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
        ("Yazılımın diğer adı ve türleri?", "Program; uygulama ve sistem yazılımları."),
        ("Akıllı donanım nedir?", "Kendine has işlemcisi olan, ana CPU'nun yükünü hafifleten donanım."),
        ("En büyük PC kasası ve yüksekliği?", "Full-tower, 60–90 cm."),
        ("En sık tercih edilen kasa?", "Mid-tower (50–60 cm)."),
        ("1U ve rack genişliği?", "1U = 1,75 inç; genişlik her zaman 19 inç (48,3 cm)."),
        ("5¼ inç bölmeler bugün ne için kullanılır?", "CD-ROM / DVD-ROM optik sürücüler."),
        ("PSU hangi voltajları üretir?", "220 V AC → 12 V, 5 V, 3,3 V DC."),
        ("AT ve ATX anakart güç konnektörleri?", "AT: P8/P9 · ATX: P1 (20 → 24 pin)."),
        ("Molex kablo renkleri?", "Sarı 12 V · kırmızı 5 V · siyah toprak."),
        ("SATA güç konnektörü kaç pin?", "15 pin, L şeklinde."),
        ("UPS'in 3 bileşeni?", "Akü · dönüştürücü/invertör (DC→AC) · şarj ünitesi (AC→DC)."),
        ("UPS devreye girme süresi?", "2–4 ms."),
        ("ATX / Micro ATX / Mini-ITX boyutları?", "305×244 · 244×244 · 170×170 mm."),
        ("Kuzey köprüsüne bağlı birimler?", "CPU (FSB), RAM, PCIe x16."),
        ("ISA ve PCI yuva renkleri?", "ISA siyah · PCI beyaz."),
        ("AGP 8x bant genişliği?", "8 × 266 = 2128 MB/s (~2,1 GB/s)."),
        ("PCIe x16 bant genişliği?", "16 × 250 MB/s = 4 GB/s (tek yön)."),
        ("USB 2.0 ve 3.0 port renkleri / pin sayıları?", "2.0 siyah, 4 pin · 3.0 mavi, 9 pin."),
        ("IRQ 0, 1, 8, 12, 13?", "Sistem saati, klavye, RTC, PS/2 fare, FPU."),
        ("Kaç IRQ ve kaç DMA kanalı vardır?", "16 IRQ (0–15) · 8 DMA (0–7)."),
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
    # ───────────────────────── 2. Hafta · Donanım, Kasa, Güç Kaynağı, UPS ─────────────────────────
    {"week": "dn-h2", "q": "Bilgisayarı belirli işlevleri yerine getirmek üzere yöneten kodlanmış komutlar dizisine ne ad verilir?",
     "options": ["Donanım", "Yazılım (program)", "Yonga seti", "Makine dili tablosu"], "answer": 1,
     "explain": "Yazılım donanıma 'ne yapacağını' söyler; diğer adı programdır. Uygulama ve sistem yazılımları olarak ikiye ayrılır."},
    {"week": "dn-h2", "q": "Aşağıdakilerden hangisi CPU'nun gerçekleştirdiği üç temel işlemden biri DEĞİLDİR?",
     "options": ["ALU aracılığıyla matematiksel ve mantıksal işlemler", "Bellekteki verilerin yerlerini değiştirme", "Komutlara göre hareket edip yeni görev başlatma", "220 V AC gerilimi DC'ye dönüştürme"], "answer": 3,
     "explain": "AC → DC dönüşümü güç kaynağının (PSU) işidir. CPU'nun 3 işlemi: ALU işlemleri, bellekte veri taşıma, komutlara göre görev başlatma."},
    {"week": "dn-h2", "q": "İşlemci üzerinde çalışan makine kodları için hangisi doğrudur?",
     "options": ["Onluk (desimal) yapıdadır ve tüm işlemcilerde aynıdır", "16'lık (heksadesimal) yapıdadır ve her işlemcide ayrı tanımlıdır", "Sadece ikilik yapıdadır ve işletim sistemi tanımlar", "Sekizlik yapıdadır ve BIOS'ta saklanır"], "answer": 1,
     "explain": "Slayt: işlemci kodları 16'lık (heksadesimal) yapıdadır, bunlara makine kodu denir ve her işlemcide ayrı tanımlıdır."},
    {"week": "dn-h2", "q": "Kendine has işlemcisi olan ve ana işlemcinin yükünü hafifleten donanımlara ne ad verilir?",
     "options": ["Çevre birimi", "Akıllı donanım", "Gömülü yazılım", "Yonga seti"], "answer": 1,
     "explain": "Akıllı donanım kendi işlemcisiyle iş yapar; ana işlemci artan zamanda başka görevleri yerine getirir, zaman kazanılır."},
    {"week": "dn-h2", "q": "Aşağıdakilerden hangisi slayta göre bir ÇIKIŞ birimidir?",
     "options": ["Tarayıcı (scanner)", "Mikrofon", "Çizici (plotter)", "Klavye"], "answer": 2,
     "explain": "Çıkış birimleri: ekran, yazıcı, çizici (plotter), hoparlör, disket/CD/DVD. Tarayıcı, mikrofon ve klavye giriş birimidir."},
    {"week": "dn-h2", "q": "Aşağıdakilerden hangisi iyi bir bilgisayar kasasında bulunması gereken özelliklerden biri DEĞİLDİR?",
     "options": ["Genişletilebilirlik", "Sessiz çalışma", "Yüksek watt değeri", "Montaj ve bakım kolaylığı"], "answer": 2,
     "explain": "Kasa özellikleri: genişletilebilirlik, sessiz çalışma, standartlara uyum ve kalite, montaj-bakım kolaylığı, yaralanmalara karşı önlem. Watt, güç kaynağının özelliğidir."},
    {"week": "dn-h2", "q": "En büyük boyuta sahip, 60–90 cm yüksekliğinde, daha çok küçük sunucularda kullanılan dikey kasa türü hangisidir?",
     "options": ["Mid-tower", "Full-tower", "Mini-tower", "Slim"], "answer": 1,
     "explain": "Full-tower: en büyük PC kasası, 60–90 cm, ATX/MicroATX, en az 3 bazen 5 sabit disk yeri. Mid-tower 50–60 cm."},
    {"week": "dn-h2", "q": "Esnek tasarımı ve çoğu kullanıcıya yeterli alanı sayesinde en sık tercih edilen kasa türü hangisidir?",
     "options": ["Full-tower", "Mid-tower", "Masaüstü (desktop)", "Sunucu kasası"], "answer": 1,
     "explain": "Mid-tower: orta boy (50–60 cm), ATX ve MicroATX destekler, sıklıkla tercih edilir."},
    {"week": "dn-h2", "q": "MicroATX anakart için uygun olan, ileride terfi yapmayı planlayanlar için iyi bir seçim olmayan ve iç soğutması en düşük kasa hangisidir?",
     "options": ["Mini-tower", "Full-tower", "Rack-mount", "Sunucu kasası"], "answer": 0,
     "explain": "Mini-tower mid-tower'dan alçak ve biraz geniştir; terfiye uygun değildir ve iç soğutmanın en düşük düzeyini sunar."},
    {"week": "dn-h2", "q": "3U yüksekliğindeki bir rack-mount kasa kaç inç yüksekliğindedir?",
     "options": ["3 inç", "5,25 inç", "7 inç", "19 inç"], "answer": 1,
     "explain": "1U = 1,75 inç → 3 × 1,75 = **5,25 inç**. (Slayt örneği: 4U = 7 inç.)"},
    {"week": "dn-h2", "q": "Rack-mount kasaların standart raflara uyabilmesi için genişliği her zaman ne kadardır?",
     "options": ["17 inç", "19 inç (48,3 cm)", "21 inç", "1,75 inç"], "answer": 1,
     "explain": "Genişlik her zaman 19 inç (48,3 cm); yükseklik U birimiyle (1U = 1,75 inç) ifade edilir."},
    {"week": "dn-h2", "q": "Günümüzde 5¼ inçlik sürücü bölmeleri hangi aygıtlar için kullanılmaya devam etmektedir?",
     "options": ["Sabit diskler", "Disket sürücüler", "CD-ROM / DVD-ROM optik sürücüler", "Güç kaynakları"], "answer": 2,
     "explain": "5¼ disketler kullanılmasa da optik sürücüler 5¼ bölmeye ihtiyaç duyar. Sabit diskler dâhili 3½ inç bölmelere takılır."},
    {"week": "dn-h2", "q": "Bilgisayar güç kaynağı (PSU) için hangisi doğrudur?",
     "options": ["Kendi elektriğini üretir", "220 V AC'yi 12 V, 5 V ve 3,3 V DC'ye dönüştüren gerilim düşürücü olarak çalışır", "DC'yi 220 V AC'ye dönüştürür", "Sadece 12 V üretir"], "answer": 1,
     "explain": "Slayt: \"Bir PC güç kaynağı aslında hiç güç sağlamaz\" — gerilim düşürücü transformatör gibi AC'yi düşük voltajlı DC'ye çevirir."},
    {"week": "dn-h2", "q": "Aşağıdaki voltajlardan hangisi PC güç kaynağının ürettiği DC voltajlardan biri DEĞİLDİR?",
     "options": ["12 V", "5 V", "3,3 V", "24 V"], "answer": 3,
     "explain": "Dönüştürülen voltajlar 12 V, 5 V ve 3,3 V'tur. ('24' P1 konnektörünün pin sayısıdır, voltaj değil.)"},
    {"week": "dn-h2", "q": "ATX tip güç kaynağı anakarta hangi konnektörle bağlanır?",
     "options": ["P8/P9", "P1", "Molex", "Mini"], "answer": 1,
     "explain": "AT (eski) → P8/P9 · ATX (modern) → tek P1 konnektörü (önceleri 20, yenilerde 24 pin; 3,3 V hattı da var)."},
    {"week": "dn-h2", "q": "P8/P9 konnektörleri takılırken siyah kablolar yan yana gelmezse ne olur?",
     "options": ["Bilgisayar sadece açılmaz", "Anakart yanabilir", "Fan ters döner", "Hiçbir şey olmaz"], "answer": 1,
     "explain": "UYARI slaytı: siyah kablolar yan yana gelmezse anakart yanabilir. Çıkıntı ters takmayı önlemeye yardımcı olur."},
    {"week": "dn-h2", "q": "Molex konnektöründe sarı kablo kaç volt taşır?",
     "options": ["3,3 V", "5 V", "12 V", "Toprak (0 V)"], "answer": 2,
     "explain": "Molex: **sarı 12 V**, kırmızı 5 V, siyah toprak (ground)."},
    {"week": "dn-h2", "q": "SATA güç konnektörü için hangisi doğrudur?",
     "options": ["4 pinli, dikdörtgen", "15 pinli, L şeklinde", "24 pinli, çıkıntılı", "9 pinli, mavi"], "answer": 1,
     "explain": "SATA güç konnektörü 15 pin ve L şeklindedir. Güç kaynağında yoksa Molex-SATA dönüştürücü kullanılır."},
    {"week": "dn-h2", "q": "Slayttaki tipik değerlerin ÜST sınırlarına göre: anakart + Dual Core işlemci + RAM + HDD (7200 rpm) + CD-ROM toplam kaç watt çeker?",
     "options": ["150 W", "180 W", "200 W", "250 W"], "answer": 2,
     "explain": "30 + 100 + 30 + 15 + 25 = **200 W**. Ek bileşenler için pay bırakılır; sıradan kullanıcıya en az 400–500 W önerilir."},
    {"week": "dn-h2", "q": "Aşağıdakilerden hangisi yetersiz güç durumunda görülen sorunlardan biri DEĞİLDİR?",
     "options": ["POST tamamlanamaz, POST ekranında kalınır", "POST tamamlanır ama işletim sistemi yüklenmez", "Yük bindikçe bilgisayar sürekli yeniden başlar", "Monitörde ölü pikseller oluşur"], "answer": 3,
     "explain": "Slayttaki üç belirti: POST'ta kalma, OS'in yüklenememesi, yük binince sürekli yeniden başlama."},
    {"week": "dn-h2", "q": "UPS'te akünün sağladığı DC gerilimi AC gerilime dönüştüren bileşen hangisidir?",
     "options": ["Şarj ünitesi", "Dönüştürücü (invertör)", "Akü", "Sigorta"], "answer": 1,
     "explain": "UPS = akü (kesintide besler) + **invertör (DC → AC)** + şarj ünitesi (220 V AC → akünün depolayacağı DC)."},
    {"week": "dn-h2", "q": "Normal şartlarda bir UPS'in devreye girme süresi ne kadar olmalıdır?",
     "options": ["2–4 ms", "20–40 ms", "0,2–0,4 s", "2–4 s"], "answer": 0,
     "explain": "Devreye girme zamanı 2–4 ms olmalı; daha uzun olanlar tercih edilmemeli. Satın alırken anahtarlama süresi ~2 ms."},
    {"week": "dn-h2", "q": "Elektrikler kesikken UPS'in aküden başlatılabilmesi özelliğine ne ad verilir?",
     "options": ["Hot swap", "Cold start", "Overclock", "Plug and play"], "answer": 1,
     "explain": "Cold start: AC şebeke yokken sadece güç anahtarına basarak UPS'i aküden çalıştırabilme."},
    # ───────────────────────── 3. Hafta · Anakart ─────────────────────────
    {"week": "dn-h3", "q": "Anakartın fiziksel yapısı, boyutu, şekli, soket/slot dizilimi ve montaj delik sayısını ifade eden kavram hangisidir?",
     "options": ["Yonga seti", "Form faktörü", "Veri yolu", "Soket tipi"], "answer": 1,
     "explain": "Form faktörü; ATX, Micro ATX, Mini-ITX gibi standartlarla belirlenir."},
    {"week": "dn-h3", "q": "ATX form faktörlü anakartın boyutları ve en fazla slot sayısı hangisidir?",
     "options": ["244×244 mm – 4 slot", "305×244 mm – 7 slot", "170×170 mm – 1 slot", "325×266 mm – 4 slot"], "answer": 1,
     "explain": "ATX 305×244 (7) · Micro ATX 244×244 (4) · Mini-ITX 170×170 (1) · BTX 325×266 (7)."},
    {"week": "dn-h3", "q": "Tablodaki form faktörlerinden en küçüğü hangisidir?",
     "options": ["Mini-ITX", "Nano-ITX", "Pico-ITX", "Flex ATX"], "answer": 2,
     "explain": "Pico-ITX 100×72 mm · Nano-ITX 120×120 · Mini-ITX 170×170 · Flex ATX 229×191."},
    {"week": "dn-h3", "q": "Mini-ITX anakart montaj noktaları C, F, H, J'dir. Bu noktalar ATX ve MicroATX listelerinde de bulunduğuna göre hangisi söylenebilir?",
     "options": ["Mini-ITX kart ATX kasaya takılamaz", "Mini-ITX kart MicroATX ve ATX kasalara da monte edilebilir", "ATX kart Mini-ITX kasaya sığar", "Montaj noktaları form faktörüyle ilgisizdir"], "answer": 1,
     "explain": "MicroATX: B, C, F, H, J, L, M, R, S · ATX: A, C, F, G, H, J, K, L, M → C, F, H, J ortak; küçük kart büyük kasaya takılabilir."},
    {"week": "dn-h3", "q": "Yonga seti (chipset) için hangisi YANLIŞTIR?",
     "options": ["Anakart üzerindeki en büyük iki çipten biridir", "Desteklenen işlemci ve bellek tipini belirler", "Donanım birimleri arasındaki veri alışverişini yönetir", "Güç kaynağının watt değerini belirler"], "answer": 3,
     "explain": "Yonga seti anakart performansını, işlemci/bellek tipini ve çevre birimlerini belirler. Watt değeri PSU'ya aittir."},
    {"week": "dn-h3", "q": "Kuzey-güney köprüsü mimarisinde RAM ve PCI Express x16 (ekran kartı) hangi yongaya bağlıdır?",
     "options": ["Güney köprüsü", "Kuzey köprüsü", "Super I/O", "BIOS"], "answer": 1,
     "explain": "Kuzey köprüsü CPU'ya FSB ile bağlıdır ve hızlı birimleri (RAM, PCIe x16) yönetir. Güney köprüsü SATA, USB, PCI, ses, BIOS gibi yavaş birimleri."},
    {"week": "dn-h3", "q": "Diyagrama göre BIOS (flash), USB portları ve S-ATA aygıtları hangi yongaya bağlıdır?",
     "options": ["Kuzey köprüsü", "Güney köprüsü", "Doğrudan CPU", "RAM"], "answer": 1,
     "explain": "Southbridge: S-ATA, USB, IDE, PCI, PCIe x1, HD-Audio, Super I/O (LPC), BIOS (SPI), SMBus. Kuzeye DMI ile bağlanır."},
    {"week": "dn-h3", "q": "İlk üretilen, siyah yuvalı, 8 ve 16 bitlik veri yolu genişliğine sahip ve artık üretilmeyen veri yolu hangisidir?",
     "options": ["PCI", "ISA", "AGP", "PCIe"], "answer": 1,
     "explain": "ISA (Industry Standard Architecture). PCI beyaz yuvalı, 32/64 bit."},
    {"week": "dn-h3", "q": "PCI veri yolu için hangisi doğrudur?",
     "options": ["Siyah yuvalı, 8/16 bit", "Beyaz yuvalı, 32/64 bit, 33/66 MHz, tak-çalıştır destekli", "Seri iletişim, x16 hat", "Sadece ekran kartı için, 266 MB/s çarpanlı"], "answer": 1,
     "explain": "PCI: beyaz yuvalar, 32 ve 64 bit sürümler, ISA'dan büyük yuva, tak-çalıştır, 33/66 MHz; LAN, SCSI, USB kartları."},
    {"week": "dn-h3", "q": "AGP 4x ekran kartı yuvasının bant genişliği yaklaşık ne kadardır?",
     "options": ["266 MB/s", "532 MB/s", "1064 MB/s", "4 GB/s"], "answer": 2,
     "explain": "AGP'de her çarpan 266 MB/s → 4 × 266 = **1064 MB/s** (8x = 2128 MB/s)."},
    {"week": "dn-h3", "q": "AGP için hangisi YANLIŞTIR?",
     "options": ["Paralel iletişim kullanır", "32 bitlik veri yolu genişliğine sahiptir", "0,8 V, 1,5 V ve 3,3 V standartlarında üretilir", "Seri iletişimle her hatta 250 MB/s sağlar"], "answer": 3,
     "explain": "Seri iletişim ve hat başına 250 MB/s PCIe'nin özelliğidir. AGP paraleldir ve yerini PCIe'ye bırakmıştır."},
    {"week": "dn-h3", "q": "Her hattı tek yön için 250 MB/s sağlayan PCIe'de x4 bir yuvanın tek yöndeki bant genişliği nedir?",
     "options": ["250 MB/s", "1 GB/s", "2 GB/s", "4 GB/s"], "answer": 1,
     "explain": "4 × 250 MB/s = **1000 MB/s ≈ 1 GB/s**. x16 = 16 × 250 = 4 GB/s."},
    {"week": "dn-h3", "q": "PCIe'yi PCI'dan ayıran temel özellik hangisidir?",
     "options": ["Paylaşımlı paralel yol kullanması", "Her aygıt için ayrı (noktadan noktaya) seri yollar kullanması", "Sadece 33 MHz'de çalışması", "Siyah yuvalara sahip olması"], "answer": 1,
     "explain": "PCIe seri haberleşir ve PCI'daki gibi paylaşımlı yollar yerine ayrı yollar kullanır; x1, x4, x8, x16 slotlar."},
    {"week": "dn-h3", "q": "Mavi renkli ve 9 pinli USB portu hangi sürümdür?",
     "options": ["USB 1.1", "USB 2.0", "USB 3.0", "USB 4.0"], "answer": 2,
     "explain": "USB 2.0 siyah (A/B 4 pin, mini/mikro 5 pin) · USB 3.0 mavi, 9 pin."},
    {"week": "dn-h3", "q": "\"High Speed\" olarak adlandırılan USB 2.0'ın bant genişliği nedir?",
     "options": ["12 Mbps", "480 Mbps", "5 Gbps", "10 Gbps"], "answer": 1,
     "explain": "USB 1.1 12 Mbps · **2.0 High Speed 480 Mbps (2000)** · 3.0 SuperSpeed 5 Gbps · 3.1 10 Gbps · 3.2 20 Gbps · 4.0 40 Gbps."},
    {"week": "dn-h3", "q": "Tabloya göre yalnızca C tipi konnektör kullanan ve 40 Gbps hıza ulaşan USB sürümü hangisidir?",
     "options": ["USB 3.0", "USB 3.1", "USB 3.2", "USB 4.0"], "answer": 3,
     "explain": "USB 4.0 (2019) 40 Gbps, 5 A / 20 V / 100 W, C tipi. USB 3.1 10 Gbps, 3.2 20 Gbps (ikisi de C)."},
    {"week": "dn-h3", "q": "Aşağıdaki işlemci soketlerinden hangisi 1331 pinlidir?",
     "options": ["LGA 1366", "LGA 2066", "AM4", "TR4"], "answer": 2,
     "explain": "AM4 1331 pin · TR4 4094 pin · LGA soketlerde sayı adın içindedir (1366, 2066)."},
    {"week": "dn-h3", "q": "Aşağıdakilerden hangisi slayttaki anakart seçim kriterlerinden biri DEĞİLDİR?",
     "options": ["Soket tipi", "FSB hızı", "Bellek desteği", "Monitör çözünürlüğü"], "answer": 3,
     "explain": "Kriterler: soket tipi, FSB hızı, bellek desteği, slot tipi ve sayısı, tümleşik kartlar, disk arayüzü (SATA / IDE-PATA)."},
    {"week": "dn-h3", "q": "IRQ (kesme istekleri) için hangisi doğrudur?",
     "options": ["32 hat vardır, bir aygıt birden çok IRQ kullanır", "0–15 arası 16 hat vardır; iki aygıt aynı IRQ'yu kullanırsa çakışma olur ve sistem kilitlenebilir", "IRQ'lar yalnızca USB aygıtlar içindir", "IRQ çakışması sistemi hızlandırır"], "answer": 1,
     "explain": "Bir aygıt sadece bir IRQ kullanır; 16 IRQ hattı (0–15). Çakışma → sistem kilitlenebilir."},
    {"week": "dn-h3", "q": "IRQ 1 hangi aygıta atanmıştır?",
     "options": ["Sistem saati", "Klavye", "PS/2 fare", "Birinci IDE kanalı"], "answer": 1,
     "explain": "IRQ 0 sistem saati · **IRQ 1 klavye** · IRQ 12 PS/2 fare · IRQ 14 birinci IDE."},
    {"week": "dn-h3", "q": "IRQ 13 hangi birim tarafından kullanılır?",
     "options": ["Gerçek zamanlı saat", "FPU (matematik işlemci)", "Disket sürücü denetleyicisi", "LPT1"], "answer": 1,
     "explain": "IRQ 13 FPU · IRQ 8 gerçek zamanlı saat · IRQ 6 disket denetleyicisi · IRQ 7 LPT1."},
    {"week": "dn-h3", "q": "Aygıtların doğrudan bellek ile veri alışverişi için kullandığı DMA kanalları kaç tanedir?",
     "options": ["4 (0–3)", "8 (0–7)", "16 (0–15)", "2 (0–1)"], "answer": 1,
     "explain": "Bir PC'de 8 DMA kanalı vardır (0–7); ses kartı, disket sürücü, yazıcı portu, ağ kartı kullanır. (IRQ ise 16 hat.)"},
]
