"""Bilgi Teknolojileri (Öğr. Gör. Erkut BÖLÜKBAŞ) — 1.–4. hafta.

Kaynaklar: 1.hafta.pdf, 2.hafta.pdf, 3.hafta.pdf, 4.hafta-ag.pdf (159 sayfa, görüntü tabanlı;
slaytlar görsel olarak okunup aktarıldı).
"""

COURSE = {
    "id": "bt",
    "name": "Bilgi Teknolojileri",
    "short": "BT",
    "icon": "🖥️",
    "color": "#38bdf8",
    "teacher": "Öğr. Gör. Erkut BÖLÜKBAŞ",
    "sources": ["1.hafta.pdf", "2.hafta.pdf", "3.hafta.pdf", "4.hafta-ag.pdf"],
    "weeks": [
        {
            "id": "bt-h1",
            "title": "1. Hafta — Bilgi Teknolojisine Giriş",
            "sources": ["1.hafta.pdf"],
            "summary": """
**Bilgi nedir?** Tek ve net bir tanımı yoktur; disipline, kültüre ve döneme göre değişir. Köken: Latince
*informare/informatio* → "şekil vermek / eğitmek". Orta Çağ'da *biçimlendirme*, modern dönemde *iletim*,
20. yy'da bilgi kuramıyla yeniden gündeme geldi. Francis Bacon: **"Bilgi güçtür."**

* **Irzık (2002):** Bilgi doğru olmalıdır; nicelik artışı nitelik artışı demek değildir.
* **Tekeli (2002):** Bilgi toplumun ürünüdür ve görecelidir (baraj örneği: çiftçi "sulama", çevreci "köy sular altında").
* Nesnel görüş: bilgi biz olmasak da vardır · Öznel görüş: insan kavramlarıyla işlenince ortaya çıkar.

**Veri → Enformasyon → Bilgi zinciri** (sınav puanı örneği):

| Kavram | Tanım | Örnek |
|---|---|---|
| **Veri** | İşlenmemiş ham gerçek parçası; tek başına anlamsız, düşük soyutluk | 45, 60, 72, 85, 92 |
| **Enformasyon** | Verinin işlenip bağlama oturtulmuş, özetlenmiş hâli | Ortalama 70,8; en yüksek 92; en düşük 45 |
| **Bilgi** | Eğitim/deneyim/yorumla edinilen genellenebilir içerik; karar vermeyi sağlar. Felsefede *"haklı çıkarılmış doğru inanç"* | "Genel başarı orta; bazı öğrenciler tekrar etmeli" |

**Bilgiden teknolojiye:** Merak → Gözlem → Deneyim → Bilgi → Uygulama = **Teknoloji**. Brooks (1994): *bilim yeni bilgi
üretir, teknoloji bu bilgiyi dönüştürür* (Edison elektriği keşfetmedi ama ampulü icat etti).

**Tarihsel gelişim (kronoloji):**
* Mağara resimleri (Lascaux, Altamira) → ilk bilgi depoları · **Quipu** (İnka, düğümlü ipler) · **Ishango kemiği** (MÖ ~20.000)
* **Abaküs** (MÖ ~2300, ilk taşınabilir hesap aracı) · Romalıların *Calculi* taşları → "calculator" kelimesinin kökeni
* Papirüs (Mısır), kil tablet (Mezopotamya) → bilgi ilk kez sistemli depolandı
* **Kâğıt** MS 105 Çin → 8. yy Semerkand üzerinden İslam dünyası → Avrupa
* **Matbaa** 1450 Gutenberg; ilk çoğaltılan kitap İncil; 1500'e kadar 20 milyon kitap
* Üniversiteler: Bologna (1088), Oxford (1096), Paris (1150)
* **Jacquard dokuma tezgâhı** (1801) → delikli kart → *programlanabilirlik* fikri
* **Charles Babbage:** Difference Engine (1822, tablolar; tamamlanamadı) · **Analytical Engine** (1837): Store=hafıza, **Mill=işlem birimi (CPU)**, delikli kart I/O, koşul ve döngü desteği
* **Ada Lovelace** (1842): Bernoulli sayılarını hesaplayan algoritma → **ilk bilgisayar programı**; makineyi evrensel sembol işleyici olarak gördü
* **Herman Hollerith** (1890): ABD nüfus sayımı, elektrikli delikli kart → Tabulating Machine Company → **IBM**
* **Colossus** (1943, Bletchley Park, Tommy Flowers): Lorenz şifresi, ~2500 vakum tüpü, ikili sistem, saniyede 5000 karakter
* **Alan Turing – Bombe:** Enigma'yı çözen elektromekanik çözümleyici; algoritma ve programlanabilirlik kavramları
* **ENIAC** (1945, Eckert & Mauchly): ~18.000 tüp, 30 ton, 167 m², **onluk sistem**, programlama **elle kablo takarak**; saniyede 5000 toplama, 357 çarpma; insandan 1000 kat hızlı

**Bilgisayar kuşakları:** 1. vakum tüpü (makine dili, manyetik tambur, ENIAC) · 2. **transistör** (Assembly, COBOL/FORTRAN, ferrit çekirdek bellek, IBM 1401) ·
3. **entegre devre (IC)** (çoklu programlama, IBM System/360) · 4. **mikroişlemci** (Intel 4004 – 1971, Apple I/II, Commodore 64, IBM PC 1981) ·
5. yapay zekâ, çok çekirdek, GPU, mobil, bulut.

**İnternet:** ARPANET (1969, ARPA/DARPA) — ilk bağlantı **UCLA–Stanford, 29 Ekim 1969**, "LOGIN" yazılırken sistem çöktü, sadece **"LO"** gitti;
paket anahtarlamalı ilk ağ, TCP/IP'nin temeli. **E-posta:** 1971 Ray Tomlinson, "@" işareti; ilk e-posta içeriği **"QWERTYUIOP"**.
**WWW:** 1989 Tim Berners-Lee, CERN; ilk web sayfası 1991 – info.cern.ch. Web 2.0: herkes hem tüketici hem üretici.

**Bilgi Teknolojileri (BT):** veriyi toplamak, işlemek, depolamak ve iletmek için kullanılan **donanım, yazılım, ağ ve süreçlerin** bütünü.
Amaç: *doğru bilgiyi, doğru kişiye, doğru zamanda* ulaştırmak.

**BT'nin 5 bileşeni:** Donanım · Yazılım (sistem / uygulama / gömülü) · Ağ (LAN, WAN, Internet, Wi‑Fi/4G/5G) · **İnsan (Humanware)** · **Süreç (Process)**.
Senaryo: Doktor (insan) + bilgisayar (donanım) + hasta takip yazılımı (yazılım) + hastane ağı (ağ) + belirlenmiş adımlar (süreç).
""",
            "concepts": [
                ("Veri", "İşlenmemiş ham gerçek; sayım/ölçüm/gözlemle elde edilir, tek başına anlamsız."),
                ("Enformasyon", "Verinin işlenip bağlama oturtulmuş, özetlenmiş hâli."),
                ("Bilgi", "Yorum ve muhakemeyle edinilen, karar vermeyi sağlayan genellenebilir içerik."),
                ("Analytical Engine", "Babbage 1837; Store (hafıza) + Mill (CPU) + delikli kart I/O; ilk genel amaçlı programlanabilir tasarım."),
                ("Humanware", "BT sistemlerinin merkezindeki insan unsuru (kullanan, geliştiren, karar alan)."),
                ("Paket anahtarlama", "ARPANET'in kullandığı, veriyi paketlere bölen iletim yöntemi."),
            ],
            "must": [
                "Veri / Enformasyon / Bilgi ayrımı ve 45-60-72-85-92 örneği",
                "Babbage: Difference Engine 1822, Analytical Engine 1837 (Mill = CPU)",
                "Ada Lovelace = ilk programcı (1842, Bernoulli sayıları)",
                "Hollerith 1890 → IBM; Jacquard 1801 → programlanabilirlik",
                "ENIAC 1945: onluk sistem, kabloyla programlama, ~18.000 tüp",
                "Kuşaklar: tüp → transistör → IC → mikroişlemci (Intel 4004, 1971)",
                "ARPANET 1969 'LO' · e-posta 1971 '@' · WWW 1989 CERN",
                "BT'nin 5 bileşeni: donanım, yazılım, ağ, insan, süreç",
            ],
            "cheat": [
                {"title": "Kronoloji", "columns": ["Yıl", "Olay"], "rows": [
                    ["MÖ ~2300", "Abaküs"], ["MS 105", "Kâğıt (Çin)"], ["1450", "Gutenberg matbaası"],
                    ["1801", "Jacquard delikli kart"], ["1822 / 1837", "Difference / Analytical Engine"],
                    ["1842", "Ada Lovelace – ilk program"], ["1890", "Hollerith nüfus sayımı → IBM"],
                    ["1943", "Colossus"], ["1945", "ENIAC"], ["1969", "ARPANET (LO)"],
                    ["1971", "Intel 4004 · ilk e-posta"], ["1981", "IBM PC"], ["1989 / 1991", "WWW / ilk web sayfası"]]},
                {"title": "Kuşaklar", "columns": ["Kuşak", "Teknoloji", "Örnek"], "rows": [
                    ["1 (1940'lar–1956)", "Vakum tüpü, makine dili, manyetik tambur", "ENIAC"],
                    ["2 (1956–1963)", "Transistör, Assembly/COBOL/FORTRAN", "IBM 1401"],
                    ["3 (1964–1971)", "Entegre devre, çoklu programlama", "IBM System/360"],
                    ["4 (1971–1980'ler)", "Mikroişlemci", "Intel 4004, Apple II, IBM PC"],
                    ["5 (1980'ler–)", "Yapay zekâ, çok çekirdek, GPU, bulut", "Akıllı telefon, IoT"]]},
            ],
            "images": [],
            "templates": [],
        },
        {
            "id": "bt-h2",
            "title": "2. Hafta — Bilgisayar Sistemleri: Donanım ve Yazılım",
            "sources": ["2.hafta.pdf"],
            "summary": """
**Bilgisayar:** girilen bilgileri depolayabilen, aritmetik ve mantıksal işlem yapabilen, sonucu kullanıcıya ileten elektronik makine.
Sistem = **Donanım** (elle tutulur üniteler) + **Yazılım** (donanımın entegre çalışmasını sağlayan programlar).

**Anakart:** tüm bileşenleri bağlayan temel devre kartı. Üzerindekiler: **Yonga seti** (Kuzey köprüsü → CPU, RAM, ekran kartı gibi *yüksek hızlı*;
Güney köprüsü → depolama, USB, ses gibi *düşük hızlı*; yeni kartlarda kuzey köprüsünün görevi CPU'ya dağıtılmıştır), CPU soketi
(Intel **LGA**, AMD **AM4/AM5**), RAM slotları (DDR4/DDR5), PCIe/PCI genişleme yuvaları (PCIe en hızlı), SATA / **M.2 (NVMe)**,
**BIOS/UEFI** çipi (başlatma süreci), güç bağlantıları, I/O paneli. Form faktörleri: **ATX** (en yaygın), Micro ATX, **Mini ITX** (en küçük), E-ATX.
Seçim: işlemci uyumu (soket+yonga seti, ör. Intel Z690, AMD B550), RAM desteği, genişleme yuvaları, depolama bağlantıları, G/Ç portları.

**CPU:** Fetch (komutu al) → Decode (yorumla) → Execute (işle) → Store (sonucu sakla). Bileşenleri: **ALU** (aritmetik/mantık),
**Kontrol Ünitesi** (sıra ve koordinasyon), **Kayıtlar/Registers** (geçici veri). Program diskten **RAM'e** yüklenir, RAM'den CPU'ya aktarılır.
Intel 4004 (1971) 4-bit; bugün 64-bit. Performans: çekirdek sayısı, saat hızı (GHz), mimari, **önbellek (cache)**, transistör sayısı.
Soğutma: hava, su (daha verimli ama pahalı), **ısı borulu** (buharlaşıp yoğunlaşan sıvı); **termal macun** yüzeydeki mikro pürüzleri doldurur.

**Bellek:** RAM geçici, hızlı, kapatınca silinir. **DRAM** sürekli tazelenir, en yaygın · **SRAM** daha hızlı/pahalı, tazelenme gerektirmez → **önbellek** ·
DDR2→DDR5 · **GDDR** ekran kartı belleği (GDDR6) · **ECC** hata düzeltmeli → sunucular. Kapasite önerisi: ofis 4–8 GB, oyun ≥16 GB, profesyonel ≥32 GB.
RAM hızı MHz (3200 > 2400). **ROM:** sadece okunabilir, anakarta tümleşik, kalıcı; BIOS ekranından bilgisine ulaşılır.

**Depolama:** **HDD** manyetik dönen plakalar, okuma/yazma kafası, **RPM** (yüksek RPM → hızlı ama enerji/fiyat artar) ·
**SSD** hareketli parça yok; daha hızlı (açılış ~10 kat), sessiz, dayanıklı, pahalı · Optik: lazer, **1X = 150 KB/s**; **CD 700 MB** (52X=7800 KB/s),
**DVD 4,7 GB** (çift katman 17 GB), **Blu-ray 25 GB** (çift katman 50 GB) · USB bellek (ilk 1980 Toshiba, 2 MB) · SD kart (2001 SanDisk, en küçük fiziksel boyut) · Bulut (Google Drive, OneDrive...).

**Ekran kartı:** GPU + **VRAM** + soğutucu + portlar (HDMI, DisplayPort, VGA, DVI). **Entegre** (CPU içinde, düşük güç: Intel Iris, AMD Radeon Graphics) vs
**Harici** (Nvidia RTX, AMD RX). Terimler: çözünürlük, FPS, VRAM, FPS düşmesi.
**Ses kartı:** **DAC** dijital→analog (hoparlöre), **ADC** analog→dijital (mikrofondan), DSP efekt işlemcisi.
**Ethernet kartı (NIC):** RJ-45 portu, **MAC adresi**, LED, kontrol yongası; dahili (onboard) / harici (PCIe, USB).

**Monitör:** LCD (sıvı kristal, arka aydınlatma) · LED (LCD'nin LED arka aydınlatmalı hâli, en yaygın) · **OLED** (her piksel kendi ışığı; kontrast mükemmel, piksel yanması riski).
Panel: **TN** (en hızlı tepki, oyuncu, renk/açı zayıf) · **IPS** (renk doğruluğu, geniş açı, tasarım) · **VA** (yüksek kontrast, arada).
Özellikler: çözünürlük, yenileme hızı (Hz), tepki süresi (ms), görüş açısı, boyut (inç), panel türü.

**Giriş/çıkış:** Klavye en eski birim; **F klavye** Türkçeye daha uygun. Fare: mekanik (top), optik (LED), lazer (daha detaylı yüzey).
**Yazıcılar:** mürekkep püskürtmeli (fotoğraf), **lazer** (toner, hızlı, ofis), **nokta vuruşlu** (iğne + şerit, **çok nüshalı** fatura/makbuz), **termal** (fiş/bilet, solar),
3D. DPI = inç başına nokta, ppm = dakikadaki sayfa, duplex = çift taraflı.

**Sorun giderme:** Hiç ışık yok → güç kablosu/PSU/güç düğmesi · Fan dönüyor görüntü yok → monitör bağlantısı, ekran kartı, RAM'i çıkar-tak ·
Sürekli donma → RAM, aşırı ısınma, termal macun · **BSOD** → RAM veya sürücü · **Kısa sürekli bip** → RAM · Aniden kapanma → CPU/PSU ısınması.
Araçlar: **Ctrl+Shift+Esc** (Görev Yöneticisi), **msinfo32** (sistem bilgisi), **dxdiag** (ekran kartı), Aygıt Yöneticisi.
""",
            "concepts": [
                ("Kuzey köprüsü", "CPU, RAM, ekran kartı gibi yüksek hızlı bileşenleri yönetir."),
                ("Güney köprüsü", "Depolama, USB, ses gibi düşük hızlı bileşenleri yönetir."),
                ("BIOS/UEFI", "Başlatma sürecini ve donanımın doğru çalışmasını sağlayan anakart yazılımı."),
                ("SRAM", "Tazelenme gerektirmeyen, hızlı ve pahalı bellek; önbellekte kullanılır."),
                ("ECC RAM", "Hata düzeltme kodlu RAM; sunucu ve iş istasyonlarında."),
                ("DAC / ADC", "Ses kartında dijital→analog / analog→dijital çeviriciler."),
                ("RPM", "HDD'nin dakikadaki tur sayısı."),
            ],
            "must": [
                "CPU döngüsü: Fetch → Decode → Execute → Store",
                "CPU = ALU + Kontrol Ünitesi + Registers",
                "Kuzey köprüsü yüksek hız / Güney köprüsü düşük hız",
                "DRAM (tazelenir) vs SRAM (önbellek) vs ECC (sunucu) vs GDDR (GPU)",
                "CD 700 MB · DVD 4,7 GB · Blu-ray 25 GB · 1X = 150 KB/s",
                "TN hızlı / IPS renk / VA kontrast · OLED kendi ışığı",
                "Nokta vuruşlu = çok nüshalı belge; termal = fiş",
                "BSOD → RAM/sürücü · kısa sürekli bip → RAM · msinfo32 / dxdiag",
            ],
            "cheat": [
                {"title": "Bellek türleri", "columns": ["Tür", "Özellik", "Kullanım"], "rows": [
                    ["DRAM", "Sürekli tazelenir, en yaygın", "Ana bellek"], ["SRAM", "Hızlı, pahalı, tazelenmez", "Önbellek (cache)"],
                    ["DDR4/DDR5", "Çift veri hızı, nesiller", "Masaüstü/dizüstü"], ["GDDR6", "Grafik için optimize", "Ekran kartı"],
                    ["ECC", "Hata düzeltme", "Sunucu"], ["ROM", "Kalıcı, sadece okunur", "BIOS"]]},
                {"title": "Optik diskler", "columns": ["Disk", "Kapasite", "Not"], "rows": [
                    ["CD", "700 MB", "52X = 7800 KB/s"], ["DVD", "4,7 GB (çift katman 17 GB)", "12X ≈ 16244 KB/s"],
                    ["Blu-ray", "25 GB (çift katman 50 GB)", "Ultra HD Blu-ray 4K"]]},
                {"title": "Panel türleri", "columns": ["Panel", "Artı", "Eksi"], "rows": [
                    ["TN", "Çok hızlı tepki, ucuz", "Renk ve görüş açısı sınırlı"],
                    ["IPS", "Renk doğruluğu, geniş açı", "Tepki TN'den yavaş"],
                    ["VA", "Yüksek kontrast", "Tepki IPS–TN arası"]]},
            ],
            "images": [("bt_cpu_diyagram.jpg", "CPU nasıl çalışır? Giriş birimi → Kontrol birimi / ALU / Bellek birimi → Çıkış birimleri (2.hafta.pdf s.31)"),
                       ("bt_monitor_ozellikleri.jpg", "Monitörlerde temel teknik özellikler tablosu (2.hafta.pdf s.80)")],
            "templates": [],
        },
        {
            "id": "bt-h3",
            "title": "3. Hafta — Yazılım ve İşletim Sistemleri",
            "sources": ["3.hafta.pdf"],
            "summary": """
**Yazılım:** donanıma *ne yapacağını* söyleyen komutlar, veri yapıları, algoritmalar ve prosedürler bütünü; fiziksel varlığı yoktur.
Özellikleri: İşlevsellik · Kullanılabilirlik · Performans · Güvenlik · **Taşınabilirlik** (farklı platform) · **Ölçeklenebilirlik** (100 → 10.000 kullanıcı) · Bakım/Güncellenebilirlik.
Donanım yazılımsız işlevsiz, yazılım donanımsız var olamaz.

**Yazılım çeşitleri:**
* **Sistem yazılımları:** işletim sistemi, **sürücüler** (driver), yardımcı programlar (antivirüs, disk birleştirme, yedekleme)
* **Uygulama yazılımları:** Office, Photoshop, AutoCAD, EBA, Trello… (sistem yazılımı üzerinde çalışır)
* **Gömülü yazılım:** özel amaçlı, donanımla sıkı entegre, **gerçek zamanlı** (ABS fren), kaynak kısıtlı; güncellemesi zor.

**Lisans türleri:**

| Lisans | Kaynak kodu | Ücret | Örnek |
|---|---|---|---|
| Ticari | Kapalı | Ücretli | MS Office, Photoshop, AutoCAD |
| **Özgür (Free Software)** | Açık — *"free" = özgürlük* | — | GNU/Linux, LibreOffice, GIMP |
| Açık kaynak | Açık | Genelde ücretsiz | Firefox, Apache, MySQL |
| **Freeware** | **Kapalı** | Ücretsiz | Skype, Chrome, WhatsApp |
| Deneme/Demo | Kapalı | Süre/özellik sınırlı | 30 günlük antivirüs |
| **Shareware** | Kapalı | Ücretsiz başlar, sürekli kullanım ücretli | **WinRAR** |

**SDLC (Yazılım Geliştirme Yaşam Döngüsü):** Gereksinim analizi → Tasarım → Kodlama → Test (birim, entegrasyon, sistem, kabul) → Dağıtım → Bakım.
**Şelale (Waterfall):** aşamalar sırayla, geri dönüş zor, belgelendirme yoğun; gereksinimi net projeler (gömülü, askeri).
**Agile (Çevik):** iterasyonlar, sürekli müşteri geri bildirimi, değişikliğe hızlı uyum; web/mobil.

**İşletim sistemi:** donanım ile kullanıcı arasında köprü, kaynak yönetimi, uygulama desteği. Görevleri: donanım, dosya sistemi, arayüz (GUI/CLI),
program yürütme & bellek, güvenlik/erişim, hata yönetimi, çoklu görev. Bileşenleri: **Çekirdek (Kernel)** – bellek, süreç, cihaz yönetimi, güvenlik ·
**Kullanıcı arayüzü** – GUI (Windows masaüstü, Finder) / CLI (Terminal, PowerShell) · **Dosya sistemi** – **NTFS** (Windows), **APFS** (macOS), **EXT4** (Linux).

**İS türleri:** kişisel (Windows, macOS, Linux) · mobil (Android açık kaynak, iOS kapalı) · sunucu (Windows Server, Ubuntu Server, RHEL, Unix) · gömülü (RTOS, Embedded Linux).
**Mimariler:** Tekli görev (**MS-DOS**) / çoklu görev · tek / çok kullanıcı (Unix, Linux Server) ·
**Monolitik çekirdek** (Linux, Unix — yüksek performans, hata tüm sistemi etkiler) · **Mikro çekirdek** (QNX, Minix — güvenli, biraz yavaş) ·
**Hibrit** (Windows NT, macOS XNU) · **RTOS** (FreeRTOS, VxWorks).

**Popüler İS'ler:** Windows (Microsoft, 1985, NT mimarisi, Win 11) · macOS (Unix tabanlı, Sequoia) · Linux (1991 Linus Torvalds) · Android (Google 2008, Linux çekirdeği) ·
iOS (2007) · UNIX (1969 AT&T Bell Labs) · Chrome OS (2009) · **Pardus** (TÜBİTAK ULAKBİM, 2003, **Debian tabanlı**, yerli).
Açık kaynak İS: Linux dağıtımları, Pardus, FreeBSD, Android · Ticari: Windows, macOS, iOS.

**CMD uygulamaları:** `mkdir`, `cd`, `cd ..`, `cd \\`, `dir`, `copy`, `del`, `echo metin > dosya.txt`, `type`, `systeminfo`, `hostname`, `tasklist`,
`taskkill /im notepad.exe`, `ping`, `tracert`, `ipconfig`.
""",
            "concepts": [
                ("Sürücü (Driver)", "Donanım aygıtının işletim sistemiyle uyumlu çalışmasını sağlayan sistem yazılımı."),
                ("Kernel", "İS'nin kalbi; bellek, süreç, cihaz yönetimi ve güvenlik."),
                ("Freeware", "Ücretsiz ama genelde kapalı kaynak (Chrome, WhatsApp)."),
                ("Shareware", "Ücretsiz başlayıp sürekli kullanım için lisans isteyen yazılım (WinRAR)."),
                ("RTOS", "Gerçek zamanlı işletim sistemi; FreeRTOS, VxWorks."),
                ("Hibrit çekirdek", "Monolitik + mikro çekirdek; Windows NT, macOS XNU."),
            ],
            "must": [
                "Sistem / uygulama / gömülü yazılım ayrımı",
                "Özgür yazılım 'free' = özgürlük; Freeware kapalı kaynak",
                "Shareware = WinRAR; Ticari = Office/Photoshop",
                "SDLC 6 aşama; Şelale vs Agile",
                "Monolitik (Linux) / Mikro (QNX, Minix) / Hibrit (Windows NT, XNU)",
                "NTFS – APFS – EXT4 eşleşmesi",
                "MS-DOS tekli görev; Pardus = TÜBİTAK ULAKBİM, Debian tabanlı",
            ],
            "cheat": [
                {"title": "Çekirdek mimarileri", "columns": ["Mimari", "Özellik", "Örnek"], "rows": [
                    ["Monolitik", "Hepsi tek çekirdekte; hızlı, hata tümünü etkiler", "Linux, Unix"],
                    ["Mikro", "Sadece kritik görev çekirdekte; güvenli, biraz yavaş", "QNX, Minix"],
                    ["Hibrit", "İkisinin birleşimi", "Windows NT, macOS XNU"],
                    ["RTOS", "Zamanlama kritik", "FreeRTOS, VxWorks"]]},
                {"title": "CMD hızlı komutlar", "columns": ["Amaç", "Komut"], "rows": [
                    ["Klasör oluştur / gir / üst", "mkdir okul · cd okul · cd .."], ["Listele", "dir"],
                    ["Dosya yaz / oku", "echo merhaba > a.txt · type a.txt"], ["Kopyala / sil", "copy a.txt b.txt · del b.txt"],
                    ["Sistem bilgisi / ad", "systeminfo · hostname"], ["Süreçler / kapat", "tasklist · taskkill /im notepad.exe"],
                    ["Ağ testi", "ping google.com · tracert google.com · ipconfig"]]},
            ],
            "images": [],
            "templates": [],
        },
        {
            "id": "bt-h4",
            "title": "4. Hafta — Ağ Temelleri (topoloji, OSI, cihazlar, kablolar, kablosuz)",
            "sources": ["4.hafta-ag.pdf (159 slayt, görsel olarak okundu)"],
            "summary": """
**Bilgisayar ağı:** veri paylaşımı ve iletişim için birbirine bağlı cihazlar topluluğu. Kullanım: iletişim, donanım/veri/yazılım paylaşımı.
Evrim: 1960'lar ARPANET · 1970'ler TCP/IP · 1980'ler internetin yaygınlaşması · 1990'lar WWW · 2000'ler mobil/kablosuz.
Bileşenler: sunucu, istemci, ağ donanımı, ağ işletim sistemi. **Veri iletim sistemi:** Gönderici · Mesaj · Alıcı · İletim ortamı · **Protokol**.

**İletim yöntemleri:** Paralel (çok kablo, hızlı, pahalı) / **Seri** (tek kablo, yaygın) → Asenkron (eski modem) / Senkron (Ethernet).
**Yön:** **Simplex** tek yön (TV yayını) · **Half duplex** iki yön ama sırayla (telsiz) · **Full duplex** aynı anda iki yön (telefon).
Veri iletim hızı = bps; bant genişliği = kanalın taşıyabileceği maksimum veri.

**Coğrafi ağ türleri:** **PAN** (kişisel, Bluetooth) · **LAN** (ev/ofis/bina) · **MAN** (şehir/kampüs) · **WAN** (ülke/kıta, İnternet) · **SAN** (depolama alan ağı) · **VPN** (internet üzerinden güvenli tünel).
**İntranet** (kurum içi) ⊂ **Ekstranet** (iş ortakları/tedarikçiler) ⊂ **İnternet** (herkes).

**Topolojiler** (fiziksel = kablolar/cihazlar; mantıksal = verinin akışı):
* **Ortak yol (Bus):** tek omurga kablo; ucuz, kolay; omurga arızası tüm ağı etkiler, çarpışma (collision) olur
* **Halka (Ring):** veri halkada **tek yönde** dolaşır; çarpışma az; bir cihaz arızası tüm ağı etkiler, ekleme/çıkarma zor
* **Yıldız (Star):** merkezde hub/switch; **en yaygın**; kurulumu kolay, bir cihaz arızası diğerlerini etkilemez; **merkez arızası tüm ağı etkiler**, daha çok kablo
* **Ağaç (Tree):** hiyerarşik yıldız; ölçeklenebilir; omurga arızası tümünü etkiler
* **Örgü (Mesh):** çoklu bağlantı, **en yüksek güvenilirlik/hata toleransı**; tam (full) / kısmi (partial); pahalı, çok kablo

**OSI referans modeli (7 katman)** — farklı üreticilerin cihazları arasında uyumluluk, standartlaştırma, modülerlik, sorun giderme:

| # | Katman | Kısa soru | Örnek |
|---|---|---|---|
| 7 | Uygulama | Kullanıcının uygulamaları | HTTP, FTP, SMTP, DNS, SSH |
| 6 | Sunum | Verinin formatı ve şifreleme | ASCII/Unicode, JPEG/GIF/PNG, SSL/TLS |
| 5 | Oturum | İletişimi başlatır, sürdürür, bitirir | NFS, checkpoint |
| 4 | Taşıma | Veri sağlam mı, eksik mi gitti? | **TCP** (güvenilir) / **UDP** (bağlantısız) — *segment* |
| 3 | Ağ | Veri hangi yoldan gidecek? | **IP, router** — *paket* |
| 2 | Veri bağlantısı | Veri hangi cihaza gidecek? | **MAC, switch**, Ethernet — *çerçeve* |
| 1 | Fiziksel | Bitler kablodan/havadan nasıl gidiyor? | Kablo, fiber, voltaj — *bit* |

Kapsülleme: veri aşağı inerken her katman **başlık (header)** ekler; kapsül açma (decapsulation) yukarı çıkarken başlıkları çıkarır.

**Ağ cihazları:** **NIC** (MAC adresi; 48 bit, 6 oktet; ilk 3 oktet üretici, son 3 cihaz; ör. 00:11:22:33:44:55) ·
**Hub** – 1. katman, gelen veriyi **tüm portlara** yollar, "MAC'i bilmez", tek şeritli yol · **Switch** – 2. katman, **MAC tablosu** ile sadece hedef porta; "akıllı hub", çok şeritli yol ·
**Bridge (köprü)** – 2. katman, iki ağı bağlar, farklı hızları (10/100 Mbps) birleştirebilir · **Repeater** – 1. katman, sinyali güçlendirir, içeriğe bakmaz ·
**Router** – 3. katman, LAN-LAN/LAN-WAN/WAN-WAN, yönlendirme tablosu · **Access Point** – kablolu ağa kablosuz erişim ·
**Modem** – *modülasyon/demodülasyon*, dijital↔analog; **ADSL** (bakır telefon hattı, teorik 24 Mbps, upload sınırlı) · **VDSL** (ADSL'den ~5 kat hızlı, 100 Mbps'e kadar, kısa mesafe) ·
**Fiber modem** (ışık; 1000 Mbps+, simetrik, düşük gecikme) · **Firewall** (yazılım/donanım tabanlı, kurallara göre paket süzer) · Gateway.

**Kablolar:** **Koaksiyel** (merkez iletken + yalıtkan + metal örgü + dış kılıf; gürültüye dayanıklı; RG-8 **Thicknet 500 m**, RG-58 **Thinnet 185 m**; BNC/T-konnektör; bugün ağırlıklı kablo TV) ·
**Bükümlü çift** (4 çift; büküm parazitten korur) → **UTP** (korumasız, ucuz) / **STP** (metal zırhlı, pahalı, **topraklanmalı**) ·
Kategoriler: CAT1 telefon · CAT2 4 Mbps · CAT3 10 Mbps · CAT4 16 Mbps · **CAT5 100 Mbps, 100 m** · CAT5e gigabit · CAT6 1 Gbps · CAT6A 10 Gbps kısa mesafe · **CAT8 40 Gbps, 2 GHz** ·
Konnektör: **RJ-45** ağ, **RJ-11** telefon · **Fiber optik:** çekirdek (cam/plastik), cladding (yansıtıcı), kılıf; EMI'den etkilenmez, uzun mesafe, güvenli; pahalı, detaylı işçilik.
Simplex/duplex fiber; konnektörler LC, SC, ST, FDDI, MTRJ, MTP/MPO.

**EIA/TIA-568:** **T568A** ve **T568B** (dünyada en yaygın **T568B**). T568B sırası: turuncu-beyaz, turuncu, yeşil-beyaz, mavi, mavi-beyaz, yeşil, kahverengi-beyaz, kahverengi.
**Düz (straight-through):** iki uç aynı şema → **farklı cihazlar** (PC–switch). **Çapraz (crossover):** bir uç A, diğer uç B → **benzer cihazlar** (PC–PC, switch–switch, hub–hub).
Kablo hazırlama 13 adım: kılıf sıyırma → çiftleri çözme → sıraya dizme → ~14 mm kesme → konnektöre sokma (kılıf en az 6 mm içeri, kilit aşağı) → RJ-45 pensesiyle sıkma → test cihazı.

**Kablosuz:** Hertz (1800'ler), Marconi (1901), **Hedy Lamarr 1942 FHSS** (Wi‑Fi/Bluetooth temeli), Telstar 1962, 1G 1983, **IEEE 802.11 – 1997**.
**IR (kızılötesi):** ~10 m, **görüş hattı gerekir**, duvardan geçmez (kumanda, IrDA) · **RF:** uzun mesafe, duvardan geçer.
**Lisanssız spektrum** (2.4/5 GHz; Wi‑Fi, Bluetooth; ücretsiz, girişim çok) / **Lisanslı** (BTK ihaleyle; 4G/5G, TV; girişimden korunur, QoS, pahalı).
Türler: **WPAN** (Bluetooth BLE, Zigbee, Z-Wave) · **WLAN** (~100 m, Wi‑Fi) · **WMAN** (WiMAX) · **WWAN** (GSM/3G/4G/5G, uydu).
Wi‑Fi: 802.11b (Wi‑Fi 1, 2.4 GHz, 11 Mbps) · 802.11g (Wi‑Fi 3, 54 Mbps) · 802.11n (Wi‑Fi 4, 2.4+5 GHz, **MIMO**) · **802.11ac (Wi‑Fi 5, sadece 5 GHz)** · 802.11ax (Wi‑Fi 6/6E, 6 GHz).
Güvenlik evrimi: WEP (kırılır) → WPA → **WPA2 (AES)** → **WPA3** (en güncel). Paylaşımlı ortam: **CSMA/CA**.
Nesiller: 1G analog · 2G GSM dijital ses/SMS · 3G UMTS · 4G LTE (VoLTE) · **5G** çok düşük gecikme, IoT. **GPS** iletişim değil **konumlandırma** (sadece alır); uydu interneti örneği Starlink.
""",
            "concepts": [
                ("Simplex / Half / Full duplex", "Tek yön (TV) / sırayla iki yön (telsiz) / aynı anda iki yön (telefon)."),
                ("Yıldız topoloji", "Merkezi cihaza bağlı; en yaygın; merkez arızası tüm ağı etkiler."),
                ("Mesh", "Çoklu bağlantı, en yüksek hata toleransı, pahalı."),
                ("Düz kablo", "İki uç aynı şema; farklı cihazları (PC–switch) bağlar."),
                ("Çapraz kablo", "Bir uç T568A diğer T568B; benzer cihazları bağlar."),
                ("CSMA/CA", "Kablosuzda paylaşımlı ortamda sırayla konuşma (çarpışmadan kaçınma)."),
            ],
            "must": [
                "OSI 7 katman sırası ve her katmanın 'kısa sorusu'",
                "Hub=1, Repeater=1, Switch/Bridge=2, Router=3. katman",
                "Topoloji avantaj/dezavantajları (yıldız, halka, bus, mesh)",
                "CAT5 100 m · CAT8 40 Gbps · Thinnet 185 m · Thicknet 500 m",
                "T568B renk sırası; düz vs çapraz kullanım yerleri",
                "IR görüş hattı ister; GPS konumlandırmadır, iletişim değil",
                "802.11ac sadece 5 GHz; WPA3 en güncel",
            ],
            "cheat": [
                {"title": "Ağ cihazı ↔ OSI katmanı", "columns": ["Cihaz", "Katman", "Ne yapar"], "rows": [
                    ["Hub", "1 – Fiziksel", "Bitleri tüm portlara tekrarlar"], ["Repeater", "1 – Fiziksel", "Sinyali güçlendirir"],
                    ["Switch", "2 – Veri bağlantısı", "MAC tablosuyla hedef porta iletir"], ["Bridge", "2 – Veri bağlantısı", "İki ağı MAC'e göre bağlar"],
                    ["Router", "3 – Ağ", "IP'ye göre yönlendirir"], ["Firewall", "3+ ", "Kurallara göre süzer"]]},
                {"title": "Ağ türleri", "columns": ["Tür", "Kapsam", "Örnek"], "rows": [
                    ["PAN/WPAN", "Kişisel (~10 m)", "Bluetooth kulaklık"], ["LAN/WLAN", "Bina (~100 m)", "Ofis, Wi‑Fi"],
                    ["MAN/WMAN", "Şehir/kampüs", "Üniversite, WiMAX"], ["WAN/WWAN", "Ülke/kıta", "İnternet, 4G/5G"],
                    ["SAN", "Depolama", "Veri merkezi"], ["VPN", "Sanal tünel", "Uzaktan şirket ağı"]]},
            ],
            "images": [("bt_topoloji_turleri.jpg", "Ağ topoloji türleri: Mesh, Ring, Star, Tree, Bus (4.hafta-ag.pdf s.30)"),
                       ("bt_osi_katmanlari.jpg", "OSI modelinin 7 katmanı (4.hafta-ag.pdf s.45)"),
                       ("bt_t568a_t568b.jpg", "T568A ve T568B renk şemaları (4.hafta-ag.pdf s.118)"),
                       ("bt_duz_capraz.jpg", "Düz ve çapraz kablo bağlantı örnekleri (4.hafta-ag.pdf s.122)"),
                       ("bt_kablosuz_ag_turleri.jpg", "Kablosuz ağ türleri karşılaştırması: WPAN, WLAN, WMAN, WWAN (4.hafta-ag.pdf s.156)")],
            "templates": [],
        },
    ],
    "flashcards": [
        ("Veri mi, enformasyon mu? 'Ortalama 70,8; en yüksek 92'", "Enformasyon — işlenmiş, bağlama oturtulmuş veri."),
        ("Felsefede bilginin tanımı?", "Haklı çıkarılmış doğru inanç."),
        ("Analytical Engine'de 'Mill' neye karşılık gelir?", "İşlem birimi — bugünkü CPU."),
        ("İlk bilgisayar programı kimin?", "Ada Lovelace, 1842 — Bernoulli sayıları algoritması."),
        ("Hollerith'in şirketi neye dönüştü?", "IBM (Tabulating Machine Company)."),
        ("ENIAC hangi sayı sistemini kullanıyordu?", "Onluk (desimal); programlama kablo takılarak yapılırdı."),
        ("3. kuşak bilgisayarların teknolojisi?", "Entegre devre (IC) — IBM System/360."),
        ("ARPANET ilk mesajı?", "'LOGIN' yazılırken çöktü, sadece 'LO' gitti (UCLA–Stanford, 29 Ekim 1969)."),
        ("BT'nin 5 bileşeni?", "Donanım, yazılım, ağ, insan (humanware), süreç."),
        ("CPU komut döngüsü?", "Fetch → Decode → Execute → Store."),
        ("Önbellekte hangi RAM kullanılır?", "SRAM."),
        ("Sunucularda hata düzeltmeli RAM?", "ECC RAM."),
        ("1X optik sürücü hızı?", "150 KB/s."),
        ("Mikrofon sesini dijitale çeviren birim?", "ADC (Analogdan Dijitale Çevirici)."),
        ("Oyuncu için en hızlı tepkili panel?", "TN panel."),
        ("Fatura/makbuz için çok nüshalı yazıcı?", "Nokta vuruşlu (dot matrix)."),
        ("Özgür yazılımda 'free' ne demek?", "Özgürlük — ücretsiz değil."),
        ("WinRAR hangi lisans türü?", "Shareware (paylaşımlı yazılım)."),
        ("Mikro çekirdek örnekleri?", "QNX, Minix."),
        ("Pardus'un tabanı ve geliştiricisi?", "Debian tabanlı; TÜBİTAK ULAKBİM (2003)."),
        ("Switch OSI'nin hangi katmanında?", "2. katman — Veri bağlantısı (MAC)."),
        ("Benzer cihazları bağlayan kablo?", "Çapraz (crossover): bir uç T568A, diğer uç T568B."),
        ("CAT5 maksimum mesafe?", "100 metre."),
        ("Görüş hattı gerektiren kablosuz teknoloji?", "Kızılötesi (IR / IrDA)."),
        ("Sadece 5 GHz çalışan Wi‑Fi standardı?", "802.11ac (Wi‑Fi 5)."),
    ],
}

QUESTIONS = [
    {"week": "bt-h1", "q": "Bir sınavdan elde edilen '45, 60, 72, 85, 92' puanları için 'Bu beş öğrencinin not ortalaması 70,8'dir' ifadesi hangi kavrama örnektir?",
     "options": ["Veri", "Enformasyon", "Bilgi", "Bilgelik"], "answer": 1,
     "explain": "Ham puanlar veridir. Veriler işlenip özetlenerek bağlama oturtulduğunda (ortalama, en yüksek, en düşük) **enformasyon** olur. 'Genel başarı orta, konu tekrarı gerekebilir' gibi yorum ise bilgidir."},
    {"week": "bt-h1", "q": "Felsefede 'bilgi' genellikle nasıl tanımlanır?",
     "options": ["İşlenmemiş ham gerçek", "Haklı çıkarılmış doğru inanç", "Bağlama oturtulmuş veri", "Toplumdan bağımsız nesnel gerçek"], "answer": 1,
     "explain": "1. hafta slaytı: Bilgi, eğitim/deneyim/yorumla edinilen içeriktir; felsefede *haklı çıkarılmış doğru inanç* olarak tanımlanır."},
    {"week": "bt-h1", "q": "Babbage'ın Analytical Engine (1837) tasarımında 'Mill' bileşeni bugünkü hangi birime karşılık gelir?",
     "options": ["RAM", "Sabit disk", "CPU (işlem birimi)", "Ekran kartı"], "answer": 2,
     "explain": "Store = hafıza, **Mill = sayısal işlemleri yapan işlem birimi (bugünkü CPU)**, delikli kartlar = giriş, basılı kâğıt = çıktı."},
    {"week": "bt-h1", "q": "Tarihteki ilk bilgisayar programı kabul edilen Bernoulli sayıları algoritmasını kim yazmıştır?",
     "options": ["Charles Babbage", "Ada Lovelace", "Alan Turing", "Herman Hollerith"], "answer": 1,
     "explain": "Ada Lovelace 1842'de Menabrea'nın notlarına Bernoulli sayılarını hesaplayan algoritmayı ekledi; ilk programcı kabul edilir."},
    {"week": "bt-h1", "q": "Herman Hollerith'in 1890 ABD nüfus sayımı için kurduğu Tabulating Machine Company hangi şirketin temelidir?",
     "options": ["Intel", "Microsoft", "IBM", "Apple"], "answer": 2,
     "explain": "Elektrikli delikli kart sistemi sayımı aylara indirdi; şirket zamanla **IBM**'e dönüştü."},
    {"week": "bt-h1", "q": "Programlanabilirlik kavramının temelini oluşturan delikli kartlı dokuma tezgâhı kime aittir?",
     "options": ["Joseph Jacquard (1801)", "Blaise Pascal (1642)", "Tommy Flowers (1943)", "Gutenberg (1450)"], "answer": 0,
     "explain": "Jacquard tezgâhı her desen için delikli kart kullanıyordu; desenleri otomatik dokuma fikri programlanabilirliğin temelidir."},
    {"week": "bt-h1", "q": "ENIAC ile ilgili aşağıdakilerden hangisi YANLIŞTIR?",
     "options": ["Yaklaşık 18.000 vakum tüpü vardı", "İkili (binary) sistem kullanıyordu", "Programlama elle kablo takarak yapılıyordu", "Top mermisi hesapları için geliştirildi"], "answer": 1,
     "explain": "ENIAC **onluk (desimal)** sistem kullanıyordu. İkili sistem kullanan Colossus'tu. Yeniden programlama = fiziksel yeniden kablolama."},
    {"week": "bt-h1", "q": "Transistörlerin kullanılmaya başlandığı, COBOL/FORTRAN dillerinin ortaya çıktığı kuşak hangisidir?",
     "options": ["1. kuşak", "2. kuşak", "3. kuşak", "4. kuşak"], "answer": 1,
     "explain": "1: vakum tüpü · **2: transistör** (Assembly, COBOL, FORTRAN, ferrit çekirdek, IBM 1401) · 3: entegre devre · 4: mikroişlemci."},
    {"week": "bt-h1", "q": "ARPANET'in UCLA–Stanford arasındaki ilk bağlantısında (29 Ekim 1969) karşı tarafa hangi metin ulaşabildi?",
     "options": ["LOGIN", "LO", "QWERTYUIOP", "HELLO"], "answer": 1,
     "explain": "'LOGIN' yazılırken sistem çöktü, sadece **'LO'** gitti. QWERTYUIOP ise Ray Tomlinson'ın ilk e-postasının içeriğidir (1971)."},
    {"week": "bt-h1", "q": "World Wide Web'i CERN'de tasarlayan kişi kimdir?",
     "options": ["Ray Tomlinson", "Tim Berners-Lee", "Vint Cerf", "Linus Torvalds"], "answer": 1,
     "explain": "Tim Berners-Lee 1989'da CERN'de bilimsel makalelere erişimi kolaylaştırmak için WWW'yi tasarladı; ilk web sayfası 1991, info.cern.ch."},
    {"week": "bt-h1", "q": "Bir doktorun hasta takip yazılımını hastane ağı üzerinden 'önceden belirlenmiş adımlarla' kullanması senaryosunda 'önceden belirlenmiş adımlar' hangi BT bileşenidir?",
     "options": ["Donanım", "Yazılım", "İnsan (Humanware)", "Süreç (Process)"], "answer": 3,
     "explain": "Süreç; iş akışları, otomasyon, güvenlik politikaları gibi adım ve kurallar dizisidir. 'Süreç olmadan BT karmaşa yaratır.'"},
    {"week": "bt-h2", "q": "Anakart yonga setinde CPU, RAM ve ekran kartı gibi yüksek hızlı bileşenleri yöneten kısım hangisidir?",
     "options": ["Güney köprüsü", "Kuzey köprüsü", "BIOS çipi", "SATA denetleyicisi"], "answer": 1,
     "explain": "Kuzey köprüsü yüksek hızlı (CPU, RAM, GPU); güney köprüsü düşük hızlı (depolama, USB, ses) bileşenleri yönetir."},
    {"week": "bt-h2", "q": "CPU'nun bir komutu işleme adımlarının doğru sırası hangisidir?",
     "options": ["Decode → Fetch → Execute → Store", "Fetch → Decode → Execute → Store", "Fetch → Execute → Decode → Store", "Store → Fetch → Decode → Execute"], "answer": 1,
     "explain": "Komut bellekten alınır (Fetch), yorumlanır (Decode), işlenir (Execute), sonuç saklanır (Store)."},
    {"week": "bt-h2", "q": "Tazelenmeye ihtiyaç duymayan, DRAM'den hızlı ve pahalı olup genellikle önbellek olarak kullanılan bellek türü hangisidir?",
     "options": ["SRAM", "GDDR6", "ECC RAM", "ROM"], "answer": 0,
     "explain": "SRAM (Statik RAM) tazelenmeden veri tutar, hızlıdır → önbellek. DRAM ise sürekli tazelenmesi gereken hücrelerden oluşur."},
    {"week": "bt-h2", "q": "Standart bir DVD, bir CD'nin yaklaşık kaç katı veri saklar ve kapasitesi nedir?",
     "options": ["2 kat – 1,4 GB", "7 kat – 4,7 GB", "10 kat – 7 GB", "25 kat – 25 GB"], "answer": 1,
     "explain": "CD 700 MB; DVD bunun **7 katı, 4,7 GB** (çift katman 17 GB); Blu-ray 25 GB (çift katman 50 GB)."},
    {"week": "bt-h2", "q": "Ses kartında mikrofondan gelen analog sesi dijital veriye dönüştüren bileşen hangisidir?",
     "options": ["DAC", "ADC", "DSP", "VRAM"], "answer": 1,
     "explain": "**ADC** analog→dijital (mikrofon); DAC dijital→analog (hoparlör); DSP efekt/filtre işlemcisi."},
    {"week": "bt-h2", "q": "Her pikselin kendi ışığını ürettiği, mükemmel kontrast sunan ancak piksel yanması riski taşıyan ekran teknolojisi hangisidir?",
     "options": ["LCD", "LED", "OLED", "TN"], "answer": 2,
     "explain": "OLED: her piksel kendi ışığını üretir; kontrast ve renk canlılığı mükemmel; dezavantajı fiyat ve piksel yanması."},
    {"week": "bt-h2", "q": "Fatura, makbuz gibi çok nüshalı belgelerin basımında hâlâ yaygın kullanılan yazıcı türü hangisidir?",
     "options": ["Lazer", "Termal", "Nokta vuruşlu", "Mürekkep püskürtmeli"], "answer": 2,
     "explain": "Nokta vuruşlu yazıcılar mürekkepli şeride iğnelerle vurur; çok nüshalı baskı yapabilir, ucuz ve dayanıklıdır ama gürültülüdür."},
    {"week": "bt-h2", "q": "Bilgisayar açılırken kısa ve sürekli bip sesleri çıkarıyor. Ders notuna göre en olası neden nedir?",
     "options": ["Güç kaynağı arızası", "RAM yuvaya tam oturmamış / arızalı", "Ekran kartı sürücüsü eski", "Sabit disk dolu"], "answer": 1,
     "explain": "Soru 7 cevabı: RAM'ler yuvaya tam oturmamış veya arızalı olabilir; çıkarıp tekrar takılmalı, sürerse değiştirilmeli."},
    {"week": "bt-h2", "q": "Windows'ta GPU modeli ve görüntü belleği gibi ekran kartı bilgilerini görmek için Çalıştır (Win+R) penceresine ne yazılır?",
     "options": ["msinfo32", "dxdiag", "devmgmt", "taskmgr"], "answer": 1,
     "explain": "Görev 3: **dxdiag** → Ekran/Display bölümü. msinfo32 sistem bilgisi (BIOS, anakart) içindir."},
    {"week": "bt-h3", "q": "Ücretsiz sunulan ancak kaynak kodu genellikle kapalı olan yazılım lisans türü hangisidir? (Örn: Chrome, WhatsApp)",
     "options": ["Özgür yazılım", "Açık kaynak", "Freeware", "Shareware"], "answer": 2,
     "explain": "Freeware ücretsizdir ama kapalı kaynaktır. Özgür yazılımda 'free' özgürlük demektir ve kaynak açıktır."},
    {"week": "bt-h3", "q": "Kullanıcıya ücretsiz sunulup sürekli kullanım veya ek özellikler için lisans ücreti isteyen WinRAR hangi lisans türüne örnektir?",
     "options": ["Shareware", "Ticari yazılım", "Freeware", "Demo"], "answer": 0,
     "explain": "Paylaşımlı yazılım (Shareware) örneği WinRAR'dır."},
    {"week": "bt-h3", "q": "Tüm aşamaların sırayla tamamlandığı, geri dönüşün zor olduğu ve belgelendirmenin yoğun olduğu yazılım geliştirme modeli hangisidir?",
     "options": ["Agile", "Scrum", "Waterfall (Şelale)", "DevOps"], "answer": 2,
     "explain": "Şelale modeli: analiz → tasarım → kodlama → test → dağıtım → bakım; gereksinimi net projeler (gömülü, askeri) için uygundur."},
    {"week": "bt-h3", "q": "Aşağıdaki eşleştirmelerden hangisi YANLIŞTIR?",
     "options": ["Monolitik çekirdek – Linux", "Mikro çekirdek – QNX", "Hibrit çekirdek – Windows NT", "Mikro çekirdek – macOS XNU"], "answer": 3,
     "explain": "macOS XNU **hibrit** çekirdektir (Windows NT gibi). Mikro çekirdek örnekleri QNX ve Minix'tir."},
    {"week": "bt-h3", "q": "macOS'un kullandığı dosya sistemi hangisidir?",
     "options": ["NTFS", "EXT4", "APFS", "FAT32"], "answer": 2,
     "explain": "NTFS → Windows, **APFS → macOS**, EXT4 → Linux."},
    {"week": "bt-h3", "q": "Aynı anda yalnızca bir uygulama çalıştırabilen (single-tasking) işletim sistemine ders notundaki örnek hangisidir?",
     "options": ["MS-DOS", "Windows 11", "Linux", "Android"], "answer": 0,
     "explain": "Tekli görev: MS-DOS. Çoklu görev modern sistemlerde standarttır (Windows, Linux, macOS)."},
    {"week": "bt-h3", "q": "Yerli ve milli işletim sistemi Pardus için hangisi doğrudur?",
     "options": ["Arch tabanlıdır, ASELSAN geliştirir", "Debian tabanlıdır, TÜBİTAK ULAKBİM geliştirir", "Kapalı kaynaklıdır", "Sadece sunucularda çalışır"], "answer": 1,
     "explain": "Pardus: TÜBİTAK–ULAKBİM (2003), Debian tabanlı, açık kaynak; kamu kurumları ve okullar için optimize."},
    {"week": "bt-h3", "q": "ABS fren sistemi gibi olaylara milisaniyeler içinde tepki vermesi gereken, cihaza özel yazılım türü hangisidir?",
     "options": ["Uygulama yazılımı", "Gömülü yazılım", "Yardımcı program", "Sürücü"], "answer": 1,
     "explain": "Gömülü yazılım: özel amaçlı, donanımla sıkı entegre, gerçek zamanlı ve kaynak kısıtlıdır."},
    {"week": "bt-h4", "q": "Telsiz ile yapılan iletişim hangi iletim yönüne örnektir?",
     "options": ["Simplex", "Half duplex", "Full duplex", "Multiplex"], "answer": 1,
     "explain": "Simplex tek yön (TV yayını), **half duplex** iki yön ama aynı anda tek yön (telsiz), full duplex aynı anda iki yön (telefon)."},
    {"week": "bt-h4", "q": "Merkezi cihazın arızalanması tüm ağı etkileyen, ancak tek bir istemci arızasının diğerlerini etkilemediği ve en yaygın kullanılan topoloji hangisidir?",
     "options": ["Bus", "Ring", "Star (Yıldız)", "Mesh"], "answer": 2,
     "explain": "Yıldız topolojide tüm cihazlar hub/switch'e bağlanır; en yaygın olandır; merkezi cihaz arızası tüm ağı etkiler."},
    {"week": "bt-h4", "q": "En yüksek güvenilirliği ve hata toleransını sağlayan, ancak kurulumu karmaşık ve maliyetli olan topoloji hangisidir?",
     "options": ["Ağaç", "Örgü (Mesh)", "Halka", "Ortak yol"], "answer": 1,
     "explain": "Mesh'te cihazlar birden fazla yolla bağlıdır; bir bağlantı kopsa da iletim sürer. Tam ve kısmi örgü olmak üzere iki türü vardır."},
    {"week": "bt-h4", "q": "OSI modelinde 'Veri hangi cihaza gidecek? (MAC, switch)' sorusunun cevabını veren katman hangisidir?",
     "options": ["1 – Fiziksel", "2 – Veri bağlantısı", "3 – Ağ", "4 – Taşıma"], "answer": 1,
     "explain": "Veri bağlantısı katmanı MAC adresleriyle fiziksel adresleme yapar, çerçeve oluşturur. 'Hangi yoldan?' sorusu 3. katmanındır (IP, router)."},
    {"week": "bt-h4", "q": "Kendisine gelen veriyi, hedefin kim olduğuna bakmadan tüm portlara gönderen ve OSI'nin 1. katmanında çalışan cihaz hangisidir?",
     "options": ["Switch", "Router", "Hub", "Bridge"], "answer": 2,
     "explain": "Hub hangi bilgisayarın kendisine bağlı olduğunu bilmez, veriyi tüm portlara yollar (1. katman). Switch MAC tablosuyla sadece hedef porta gönderir."},
    {"week": "bt-h4", "q": "İki bilgisayarı (PC–PC) doğrudan birbirine bağlamak için hangi kablo kullanılır?",
     "options": ["Düz (straight-through)", "Çapraz (crossover)", "Koaksiyel RG-8", "RJ-11 telefon kablosu"], "answer": 1,
     "explain": "Benzer cihazlar (PC–PC, switch–switch, hub–hub) çapraz kabloyla bağlanır: bir uç T568A, diğer uç T568B."},
    {"week": "bt-h4", "q": "T568B standardında 1. ve 2. pinlerdeki renkler sırasıyla hangisidir?",
     "options": ["Yeşil-beyaz, yeşil", "Turuncu-beyaz, turuncu", "Mavi, mavi-beyaz", "Kahverengi-beyaz, kahverengi"], "answer": 1,
     "explain": "T568B: turuncu-beyaz, turuncu, yeşil-beyaz, mavi, mavi-beyaz, yeşil, kahverengi-beyaz, kahverengi. (T568A'da 1-2 yeşil-beyaz, yeşil'dir.)"},
    {"week": "bt-h4", "q": "40 Gigabit Ethernet'i destekleyen, 2 GHz'e kadar frekansta çalışabilen en yeni UTP kategori hangisidir?",
     "options": ["CAT5e", "CAT6", "CAT6A", "CAT8"], "answer": 3,
     "explain": "CAT8: en yeni ve en hızlı; 40 Gbps, 2 GHz; veri merkezleri için ideal."},
    {"week": "bt-h4", "q": "Kızılötesi (IR) iletişim için aşağıdakilerden hangisi doğrudur?",
     "options": ["Duvarlardan rahatça geçer", "Cihazlar arasında görüş hattı gerektirir", "Lisanslı spektrumdadır", "Kilometrelerce menzile sahiptir"], "answer": 1,
     "explain": "IR kısa mesafelidir (~10 m), görüş hattı (line-of-sight) gerekir ve engellerden geçemez (TV kumandası, IrDA)."},
    {"week": "bt-h4", "q": "GPS ile ilgili hangisi doğrudur?",
     "options": ["Uydulara veri gönderir", "Bir iletişim teknolojisidir", "Sadece sinyal alır, konum hesaplar", "WLAN teknolojisidir"], "answer": 2,
     "explain": "DİKKAT notu: GPS iletişim değil **konumlandırma** teknolojisidir; cihaz uyduya veri göndermez, sadece alır (receive-only)."},
    {"week": "bt-h4", "q": "Modern Wi‑Fi ve Bluetooth'un temelini atan frekans atlamalı yayılı spektrum (FHSS) tekniğinin patentini 1942'de alan kişi kimdir?",
     "options": ["Guglielmo Marconi", "Heinrich Hertz", "Hedy Lamarr", "Nikola Tesla"], "answer": 2,
     "explain": "Hedy Lamarr 1942'de FHSS patentini aldı. Marconi 1901'de Atlantik ötesine telsiz telgraf gönderdi."},
]
