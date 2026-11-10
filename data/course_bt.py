"""Bilgi Teknolojileri (Öğr. Gör. Erkut BÖLÜKBAŞ) — 1.–5. hafta.

Kaynaklar: 1.hafta.pdf, 2.hafta.pdf, 3.hafta.pdf, 4.hafta-ag.pdf, 5.Hafta-html.pdf (4.hafta 159 sayfa, görüntü tabanlı;
slaytlar görsel olarak okunup aktarıldı).
"""

COURSE = {
    "id": "bt",
    "name": "Bilgi Teknolojileri",
    "short": "BT",
    "icon": "🖥️",
    "color": "#38bdf8",
    "teacher": "Öğr. Gör. Erkut BÖLÜKBAŞ",
    "sources": ["1.hafta.pdf", "2.hafta.pdf", "3.hafta.pdf", "4.hafta-ag.pdf", "5.Hafta-html.pdf"],
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
        {
            "id": "bt-h5",
            "title": "5. Hafta — HTML Temelleri ve Uygulamalar (etiketler, CSS stilleri, liste, resim, tablo, link, form)",
            "sources": ["5.Hafta-html.pdf"],
            "summary": """
#### 1. HTML nedir?
**HTML (HyperText Markup Language) — Hiper Metin İşaretleme Dili:** web sayfalarının **içeriğini ve temel yapısını** oluşturan **işaretleme dilidir**.
* Başlık, paragraf, resim, bağlantı, liste ve tablolar **HTML etiketleriyle** tanımlanır.
* **HTML bir programlama dili DEĞİLDİR**; içeriğin nasıl düzenleneceğini ve ne anlama geldiğini belirtir.
* Dosyalar **.html veya .htm** uzantılıdır; Chrome, Firefox gibi tarayıcılarda görüntülenir. **HTML5** ile modern özellikler geldi; standart gelişmeye devam ediyor.
* Not Defteri, Visual Studio Code, Notepad++ gibi **metin editörleriyle** yazılır.

#### 2. Web sitesi nasıl yayınlanır? (Alan adı, IP, DNS, hosting)
* **Alan adı (domain):** web sitesine ulaşmayı sağlayan **kolay hatırlanabilir adres** (www.google.com, www.eskisehir.edu.tr). Kayıt firmasından **kaydettirilir**,
  daha önce alınmamış olmalı, **belirli süreler için** kaydedilir ve **yenilenmesi** gerekir. Basit sayfa/ücretsiz yayın için zorunlu değildir.
* **IP adresi:** ağdaki cihazların tanınmasını ve iletişimini sağlayan **sayısal adres**. **IPv4:** noktalarla ayrılmış **dört sayı, her biri 0–255** (192.168.123.254).
  Daha geniş kapasiteli **IPv6** da kullanılır. Benzetme: evin posta adresi.
* **DNS (Domain Name System – Alan Adı Sistemi):** **alan adlarını IP adresleriyle eşleştirir**. www.meb.gov.tr yazınca: 1) tarayıcı DNS ile IP'yi öğrenir →
  2) sunucuya bağlanır → 3) gelen sayfa görüntülenir.
* **Uzantılar:** **.com** (commercial – ticari, bugün herkes) · **.edu** (eğitim, Türkiye'de .edu.tr) · **.gov** (devlet, .gov.tr) · **.org** (organization – başlangıçta ticari olmayan) ·
  **.net** (network). **Ülke kodları** (iki harf): **.tr** Türkiye, **.uk** Birleşik Krallık, **.jp** Japonya, **.it** İtalya, **.ch** İsviçre.
  .com/.org/.net sitenin kuruluş türünü **kesin göstermez**.
* **Hosting (barındırma):** site dosyalarının internetten erişilebilir olması için **bir sunucuda saklanması** hizmeti. Sunucular genelde **7/24** çalışır; ücretli/ücretsiz olabilir,
  kendi bilgisayarımız da (ağ/güvenlik ayarlarıyla) sunucu olabilir.
  **Alan adı = adres, hosting = dosyaların saklandığı yer** (mağaza adresi ↔ mağazanın fiziksel alanı).

#### 3. Gerekenler ve kaynak kodu görme
* **Metin editörü** (Not Defteri; VS Code/Notepad++ renklendirme, otomatik tamamlama, hata tespiti) + **web tarayıcısı** (HTML'i yorumlayıp gösterir: Chrome, Firefox, Edge).
* **Sayfa Kaynağını Görüntüle (Ctrl + U):** sunucudan gelen HTML kaynak kodu.
* **İncele (F12):** geliştirici araçları — HTML yapısı ve CSS; **geçici** değişiklik yapılabilir, **sadece kendi tarayıcında** görünür, sayfa yenilenince kaybolur, sitenin gerçek dosyaları değişmez.

#### 4. İlk HTML dosyası
Klasör oluştur → editöre kodu yaz → **index.html** adıyla kaydet (Not Defteri'nde kayıt türü **Tüm Dosyalar**, kodlama **UTF-8**) → çift tıkla.
Dikkat: yanlışlıkla **index.html.txt** olarak kaydedilirse tarayıcıda beklendiği gibi açılmaz.
```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>İlk Sayfam</title>
</head>
<body>
    <h1>Merhaba Dünya!</h1>
    <p>Bu benim ilk HTML sayfam.</p>
</body>
</html>
```
* `<!DOCTYPE html>`: **belge türü bildirimi**, en başta; tarayıcıya **HTML5** olduğunu söyler; **HTML etiketi değildir, kapanışı yoktur**.
* `<html lang="tr">`: belgenin başlangıcı/bitişi; `lang="tr"` sayfa dilinin Türkçe olduğunu belirtir.
* `<head>`: başlık, karakter kodlaması gibi **teknik bilgiler** (görünen içerikte yer almaz). `<meta charset="UTF-8">` **Türkçe karakterlerin** doğru görünmesini sağlar.
* `<title>`: `<head>` içinde; **tarayıcı sekmesinde** görünen başlık. · `<body>`: sayfada **görüntülenen** içerik.

#### 5. Etiketler ve temel öğeler
* Etiketler `<` ve `>` arasına yazılır; çoğu **açılış** `<p>` ve **kapanış** `</p>` (adın önünde **/**) etiketinden oluşur; arası **içerik**. Genel: `<etiket_adi>İçerik</etiket_adi>`.
* Etiketler genellikle **büyük/küçük harfe duyarlı değildir** (`<p>` = `<P>`); okunabilirlik için **küçük harf** önerilir.
* **Kapanışı olmayan** etiketler: `<br>` (satır atla), `<img>` (resim), `<hr>` (yatay çizgi).
* **Başlıklar `<h1>`–`<h6>`:** altı seviye; `<h1>` en üst düzey ve **en büyük**, `<h6>` en küçük. Yalnızca boyut değil **önem sırası/hiyerarşi** belirtir;
  arama motorları ve ekran okuyucular için önemlidir. Öncesinde/sonrasında varsayılan boşluk bırakılır (CSS ile değişir).
* **Paragraf `<p>`:** her `<p>` yeni paragraf; aralarda varsayılan boşluk. Kaynak koddaki **birden fazla boşluk ve satır sonu tek boşluk** sayılır.
* **Satır atlama `<br>`:** aynı paragrafta alt satıra geçer, **kapanışı yok**; HTML5'te `<br>` yeterli, `<br />` da geçerli. Adres, şiir, şarkı sözünde kullanılır.

| `<p>` | `<br>` |
|---|---|
| Yeni paragraf oluşturur | Aynı paragrafta alt satıra geçirir |
| Paragraflar arasında varsayılan boşluk var | Ek paragraf boşluğu oluşturmaz |
| Açılış ve kapanış etiketi var | Kapanış etiketi yok |

* **Yorum:** `<!-- açıklama -->` — tarayıcıda **görüntülenmez**; kodu açıklamak veya bir kodu geçici devre dışı bırakmak için.

#### 6. Nitelikler (attributes) ve CSS ile stil
* Nitelikler etiketlere ek özellik kazandırır; **her zaman açılış etiketinin içinde**, **nitelik="değer"** biçiminde (tırnak önerilir); birden fazla kullanılabilir;
  bazıları (**required, disabled**) değersiz kullanılır.
* **style** niteliği öğeye **CSS** ekler. **CSS (Cascading Style Sheets – Basamaklı Stil Şablonları):** HTML yapıyı/içeriği, **CSS görünümü** belirler.
* `<h1 style="text-align: center;">` → başlık ortalanır. Eski `align="center"` ve **`<font>` etiketi artık önerilmez**, yerine CSS.

| CSS özelliği | Görevi | Örnek |
|---|---|---|
| font-size | Yazı boyutu | `style="font-size: 24px;"` (eski: `<font size="5">`) |
| color | **Metin** rengi | `style="color: red;"` |
| background-color | **Arka plan** rengi (body'de tüm sayfa) | `<body style="background-color: yellow;">` |
| font-family | Yazı tipi; ilki yoksa sıradakini dener | `font-family: Verdana, Arial, sans-serif;` |
| text-align | Hizalama: left, right, center, justify | `style="text-align: justify;"` |

* **Renk tanımlama:** İngilizce isim (red, blue, lightblue) · **HEX:** **#** + 6 karakter, ilk iki **kırmızı**, sonraki iki **yeşil**, son iki **mavi** (**#FF0000** kırmızı, **#00FF00** yeşil, **#0000FF** mavi) ·
  **RGB:** her bileşen **0–255** (**rgb(255, 0, 0)** kırmızı). **#A41A1B = rgb(164, 26, 27)** aynı renk (A4 = 164, 1A = 26, 1B = 27).
* **justify** iki yana yaslar (kelime boşluklarını ayarlar, etkisi çok satırlı metinde görülür); Türkçe gibi soldan sağa dillerde varsayılan **left**.

#### 7. Biçimlendirme etiketleri
| Etiket | Ne yapar? |
|---|---|
| `<strong>` | Önemli metin, genellikle **kalın** |
| `<em>` | Vurgu, genellikle *italik* |
| `<sub>` | **Alt** simge: H`<sub>`2`</sub>`O → H₂O |
| `<sup>` | **Üst** simge: 8`<sup>`2`</sup>` → 8² |
| `<ins>` | Eklenen metin, altı çizili |
| `<s>` | Geçerliliğini yitirmiş metin, üstü çizili |
| `<hr>` | Yatay ayırıcı çizgi (kapanışı yok) |
| `<mark>` | Arka plan rengiyle vurgulama |
| `<abbr title="Birleşmiş Milletler">BM</abbr>` | Kısaltmaya açıklama |
| `<pre>` | **Boşlukları ve satır sonlarını korur** |

#### 8. Listeler
* **Sırasız liste `<ul>`** (unordered list) + **`<li>`** (list item): varsayılan **nokta (•)**; sırası olmayan ürün/özellik listeleri. `type="square"` kare, `type="circle"` daire.
* **Sıralı liste `<ol>`** (ordered list): varsayılan **1, 2, 3…**; işlem adımları, yönergeler.
  * **start:** numaralandırmanın başlangıcı — `<ol start="3">` 3'ten başlar.
  * **type:** `"1"` sayı · `"A"` büyük harf · `"a"` küçük harf · `"I"` büyük Roma · `"i"` küçük Roma.
* **İç içe liste:** bir `<li>` içine yeni `<ul>`/`<ol>` yazılır (Peynir → Beyaz peynir, Kaşar peyniri; Kimya → a. Organik, b. İnorganik).

#### 9. Resimler
`<img src="manzara.jpg" alt="Doğa manzarası">` — **kapanışı yok** (`</img>` yazılmaz).
* **src (source):** dosya yolu/adres. Aynı klasör `"fil.gif"` · alt klasör `"yemekler/kurufasulye.jpg"` · internet `"https://siteadi.com/resim.jpg"` · **bir üst klasör `"../fil.gif"`**.
  Yol yanlışsa veya dosya yoksa resim görünmez.
* **alt:** **alternatif metin** — resim yüklenemezse gösterilir; **ekran okuyucu** kullanan görme engellilere yardım eder. Fare üzerine gelince ipucu göstermek **title**'ın işidir, alt'ın değil.
* **width / height:** piksel (`width="300" height="200"`); orantısız değiştirmek görüntüyü bozar → oranı korumak için sadece width verilebilir.
* **float** (CSS): `style="float: right; width: 200px; margin-left: 15px;"` → resim sağa, metin solundan akar.

#### 10. Tablolar
| Etiket | Görevi |
|---|---|
| `<table>` | Tablonun başı/sonu |
| `<tr>` | Yeni **satır** (table row) |
| `<td>` | **Veri hücresi** (table data) |
| `<th>` | **Başlık hücresi**, genellikle kalın ve ortalı |
| `<thead>` / `<tbody>` | Başlık bölümü / veri satırları grubu |

* **colspan:** hücre **birden fazla sütuna** yayılır (`<th colspan="2">DERS NOTLARI</th>`) · **rowspan:** **birden fazla satıra** yayılır (`<td rowspan="3">FEN BİLİMLERİ</td>`).
* CSS: **border** (kenarlık), width/height, background-color/image, **padding** (hücre içi boşluk), **border-spacing** (hücreler arası boşluk), **border-collapse** (komşu kenarlıkları birleştirir).
  Eski **cellpadding, cellspacing** önerilmez.
* **Uygulama — haftalık ders programı:** başlık "Haftalık Ders Programım", **3 sütun × 6 satır** (1 başlık satırı + 5 gün), başlıklar `<th>` (Gün, Ders Adı, Saat), diğerleri `<td>`, kenarlık görünür.

#### 11. Bağlantılar (linkler)
`<a href="https://www.google.com">Google'a Git</a>` — **a = anchor**, **href = Hypertext Reference** (hedef adres). Varsayılan görünüm mavi ve altı çizili.
* **target:** `_self` mevcut sekme (**varsayılan**) · `_blank` **yeni sekme**.
* Başka sayfa `href="hakkimda.html"` · resim `href="fotograf.jpg" target="_blank"` · PDF `href="ders-notlari.pdf"` · **tıklanabilir resim:** `<a href="…"><img src="logo.png" …></a>`.
* **Sayfa içi bağlantı:** hedefe **id** verilir (`<h2 id="iletisim">`), link `href="#iletisim"`; `#`'ten sonraki ad ile **id aynı olmalı** ("Başa Dön": `href="#baslangic"`).

#### 12. Formlar
`<form>` formun başı/sonu · `<label for="ad">` alanın amacını belirtir · `<input type="text" id="ad" name="ad">` · **name:** gönderildiğinde alanın adı.

| Nitelik / tür | Görevi |
|---|---|
| type="text" | Tek satırlık metin kutusu |
| type="password" | Girilen karakterleri **gizler** |
| type="email" | E-posta adresi |
| placeholder | Kutunun içinde **yol gösterici ipucu** (girilmiş değer değildir) |
| value | **Başlangıç değeri** (`value="Eskişehir"`); submit butonunda **buton yazısı** |
| required | Alanı **zorunlu** kılar (tarayıcı kontrol eder) |
| maxlength | Karakter sayısını sınırlar |

* `<textarea rows="4" cols="30">` çok satırlı metin; **rows** görünür satır sayısı, **cols** yaklaşık karakter genişliği.
* **checkbox:** **birden fazla** seçim · **radio:** gruptan **yalnızca bir** seçim — aynı gruptakilerin **name değeri aynı olmalı** · **select + option:** açılır liste.
* `<input type="submit" value="Gönder">` gönder butonu · **action:** verilerin gönderileceği adres (`action="/kayit"`) · **method:**
  **GET** verileri **URL'nin sorgu bölümüne** ekler (arama) · **POST** verileri **HTTP isteğinin gövdesinde** gönderir (kayıt).
* **HTML sadece formun görünümünü oluşturur; verileri kaydetmek/işlemek için sunucu tarafında çalışan bir sistem gerekir.**
* **Uygulama — öğrenci kayıt formu:** Ad Soyad (text), E-posta (email), Şifre (password) — bu üçü **required**; Sınıf (radio, 1/2), İlgi Alanları (checkbox: Oyun, Müzik, Spor),
  Şehir (select: Eskişehir, Ankara, İstanbul), Hakkımda (textarea), Gönder (submit); her alanın label'ı olmalı.
""",
            "concepts": [
                ("HTML", "HyperText Markup Language; programlama dili değil, işaretleme dili."),
                ("DNS", "Alan adlarını IP adresleriyle eşleştiren sistem."),
                ("Hosting", "Site dosyalarını internetten erişilebilir bir sunucuda barındırma hizmeti."),
                ("<!DOCTYPE html>", "Belge türü bildirimi (HTML5); etiket değil, kapanışı yok."),
                ("<head> / <body>", "Teknik bilgiler (title, meta) / sayfada görünen içerik."),
                ("Nitelik", "Açılış etiketine yazılan nitelik=\"değer\" ek özelliği (src, href, style)."),
                ("CSS", "Cascading Style Sheets; görünümü belirler (color, font-size, text-align)."),
                ("alt", "Resim yüklenmezse görünen, ekran okuyucuların okuduğu alternatif metin."),
                ("colspan / rowspan", "Hücreyi birden çok sütuna / satıra yayar."),
                ("target=\"_blank\"", "Bağlantıyı yeni sekmede açar (varsayılan _self)."),
                ("GET / POST", "Veriyi URL sorgusunda / HTTP isteğinin gövdesinde gönderir."),
                ("radio / checkbox", "Gruptan tek seçim (aynı name) / birden çok seçim."),
            ],
            "must": [
                "HTML = HyperText Markup Language, programlama dili DEĞİL; uzantı .html / .htm",
                "Alan adı = adres · IP (IPv4: 4 sayı, 0–255) · DNS: alan adı → IP · Hosting: dosyaların saklandığı sunucu",
                ".com ticari · .edu eğitim · .gov devlet · .org kuruluş · .net ağ · .tr .uk .jp .it .ch",
                "Ctrl + U kaynak kodu · F12 İncele (değişiklikler geçici, sadece kendi tarayıcında)",
                "<!DOCTYPE html> etiket değil · <title> sekmede görünür · <meta charset=\"UTF-8\"> Türkçe karakter",
                "Kapanışı olmayanlar: <br>, <img>, <hr>",
                "<h1> en büyük/en önemli, <h6> en küçük; <p> paragraf, <br> satır atlama",
                "Yorum <!-- ... --> görünmez",
                "color metin, background-color arka plan; HEX #RRGGBB (#FF0000 kırmızı), RGB 0–255",
                "<ol> type: 1, A, a, I, i · start=\"3\" · <ul> nokta",
                "<img src alt>: alt = alternatif metin (ekran okuyucu); ../ bir üst klasör",
                "<table> <tr> satır, <td> veri, <th> başlık; colspan sütun, rowspan satır birleştirir",
                "<a href> · target=\"_blank\" yeni sekme · href=\"#id\" sayfa içi bağlantı",
                "password gizler · placeholder ipucu · value başlangıç değeri · required zorunlu · maxlength sınır",
                "Radio: aynı name, tek seçim · checkbox çoklu · GET URL'de, POST gövdede",
            ],
            "cheat": [
                {"title": "Temel sayfa iskeleti", "columns": ["Etiket", "Görev"], "rows": [
                    ["`<!DOCTYPE html>`", "HTML5 belge türü bildirimi (etiket değil)"], ["`<html lang=\"tr\">`", "Belgenin başı/sonu, dil"],
                    ["`<head>`", "Teknik bilgiler (görünmez)"], ["`<meta charset=\"UTF-8\">`", "Türkçe karakter desteği"],
                    ["`<title>`", "Tarayıcı sekmesindeki başlık"], ["`<body>`", "Görünen içerik"]]},
                {"title": "Sık etiketler", "columns": ["Etiket", "Görev", "Kapanış"], "rows": [
                    ["`<h1>`–`<h6>`", "Başlık (h1 en büyük)", "Var"], ["`<p>`", "Paragraf", "Var"], ["`<br>`", "Satır atlama", "Yok"],
                    ["`<hr>`", "Yatay çizgi", "Yok"], ["`<img>`", "Resim (src, alt, width, height)", "Yok"], ["`<a>`", "Bağlantı (href, target)", "Var"],
                    ["`<ul>` / `<ol>` / `<li>`", "Sırasız / sıralı liste / madde", "Var"], ["`<table>` `<tr>` `<td>` `<th>`", "Tablo / satır / veri / başlık", "Var"],
                    ["`<form>` `<input>` `<textarea>` `<select>`", "Form öğeleri", "input'ta yok"]]},
                {"title": "CSS (style niteliği)", "columns": ["Özellik", "Örnek değer"], "rows": [
                    ["color", "red · #A41A1B · rgb(164, 26, 27)"], ["background-color", "yellow · lightblue"], ["font-size", "24px"],
                    ["font-family", "Verdana, Arial, sans-serif"], ["text-align", "left · right · center · justify"], ["float", "right / left (resmin yanında metin akışı)"]]},
                {"title": "Form alanları", "columns": ["Kod", "Sonuç"], "rows": [
                    ["type=\"text\" / \"email\" / \"password\"", "Metin / e-posta / gizli karakterli"], ["type=\"checkbox\"", "Çoklu seçim"],
                    ["type=\"radio\" (aynı name)", "Tekli seçim"], ["`<select>` + `<option>`", "Açılır liste"], ["`<textarea rows cols>`", "Çok satırlı metin"],
                    ["type=\"submit\" value=\"Gönder\"", "Gönder butonu"], ["method=\"get\" / \"post\"", "URL sorgusu / istek gövdesi"]]},
                {"title": "Liste type değerleri", "columns": ["type", "Görünüm"], "rows": [
                    ["1", "1, 2, 3"], ["A", "A, B, C"], ["a", "a, b, c"], ["I", "I, II, III"], ["i", "i, ii, iii"], ["ul: square / circle", "■ / ○"]]},
            ],
            "images": [("bt_html_ul_type.jpg", "Sırasız listede type=\"square\" ve type=\"circle\" (5.Hafta-html s.42)"),
                       ("bt_html_ic_ice_liste.jpg", "İç içe liste örneği (s.43)"),
                       ("bt_html_tablo.jpg", "2 satır × 3 sütunlu tablo: thead, tbody, th, td (s.55)"),
                       ("bt_html_rowspan.jpg", "rowspan=\"3\": hücre üç satıra yayılır (s.58)"),
                       ("bt_html_colspan.jpg", "colspan=\"2\": başlık iki sütuna yayılır (s.59)")],
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
        ("HTML'in açılımı ve türü?", "HyperText Markup Language — işaretleme dili, programlama dili değil."),
        ("DNS ne yapar?", "Alan adlarını IP adresleriyle eşleştirir."),
        ("Alan adı ile hosting farkı?", "Alan adı sitenin adresi; hosting dosyaların saklandığı sunucu hizmeti."),
        ("IPv4 adresinin yapısı?", "Noktalarla ayrılmış 4 sayı, her biri 0–255 (192.168.123.254)."),
        ("Ctrl + U ve F12?", "Sayfa kaynağını görüntüle / İncele (geliştirici araçları)."),
        ("<!DOCTYPE html> nedir?", "HTML5 belge türü bildirimi; HTML etiketi değil, kapanışı yok."),
        ("<title> nerede görünür?", "Tarayıcı sekmesinde; <head> içinde yazılır."),
        ("<meta charset=\"UTF-8\"> ne işe yarar?", "Türkçe karakterlerin doğru görüntülenmesini sağlar."),
        ("Kapanış etiketi olmayan etiketler?", "<br>, <img>, <hr>."),
        ("<p> ile <br> farkı?", "<p> yeni paragraf (boşluklu, kapanışlı); <br> aynı paragrafta alt satır (kapanışsız)."),
        ("HTML yorum satırı?", "<!-- açıklama --> (tarayıcıda görünmez)."),
        ("color ile background-color farkı?", "color metin rengini, background-color arka plan rengini değiştirir."),
        ("#FF0000 ve rgb(0, 0, 255)?", "Kırmızı ve mavi."),
        ("<ol type=\"I\"> nasıl numaralandırır?", "Büyük Roma rakamlarıyla: I, II, III."),
        ("<img>'de alt niteliği?", "Alternatif metin: resim yüklenmezse görünür, ekran okuyucular okur."),
        ("src=\"../fil.gif\" ne demek?", "Resim, HTML dosyasının bir üst klasöründe."),
        ("<th> ile <td> farkı?", "<th> başlık hücresi (kalın, ortalı); <td> veri hücresi."),
        ("colspan ve rowspan?", "Hücreyi birden çok sütuna / birden çok satıra yayar."),
        ("target=\"_blank\"?", "Bağlantıyı yeni sekmede açar (varsayılan _self)."),
        ("Sayfa içi bağlantı nasıl yapılır?", "Hedefe id verilir, link href=\"#id\"."),
        ("placeholder ile value farkı?", "placeholder sadece ipucu; value gerçek başlangıç değeri."),
        ("Radio butonlarında tek seçim şartı?", "Aynı gruptakilerin name değeri aynı olmalı."),
        ("GET ile POST farkı?", "GET veriyi URL sorgusuna ekler; POST HTTP isteğinin gövdesinde gönderir."),
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
    {"week": "bt-h5", "q": "HTML için aşağıdakilerden hangisi doğrudur?",
     "options": ["Bir programlama dilidir", "HyperText Markup Language'in kısaltmasıdır ve bir işaretleme dilidir",
                 "Sadece .exe uzantısıyla kaydedilir", "Yalnızca sunucuda çalışır"], "answer": 1,
     "explain": "HTML (Hiper Metin İşaretleme Dili) içeriğin yapısını belirten işaretleme dilidir; programlama dili değildir. Uzantı .html veya .htm."},
    {"week": "bt-h5", "q": "Alan adlarını (www.meb.gov.tr gibi) ilgili IP adresleriyle eşleştiren sistem hangisidir?",
     "options": ["HTTP", "DNS", "Hosting", "HTML"], "answer": 1,
     "explain": "DNS (Domain Name System). Tarayıcı DNS ile IP'yi öğrenir, sunucuya bağlanır, sayfayı gösterir."},
    {"week": "bt-h5", "q": "Bir web sitesinin dosyalarının internetten erişilebilir olması için bir sunucuda saklanmasını sağlayan hizmet hangisidir?",
     "options": ["Alan adı", "DNS", "Hosting", "Tarayıcı"], "answer": 2,
     "explain": "Hosting (barındırma). Alan adı sitenin adresi, hosting ise dosyaların saklandığı yerdir (mağaza adresi ↔ mağazanın kendisi)."},
    {"week": "bt-h5", "q": "Aşağıdakilerden hangisi geçerli bir IPv4 adresidir?",
     "options": ["192.168.123.254", "192.168.300.1", "192.168.1", "256.10.10.10"], "answer": 0,
     "explain": "IPv4: noktalarla ayrılmış dört sayı ve her sayı 0–255 arası. 300 ve 256 aralık dışında; üç sayılı adres eksik."},
    {"week": "bt-h5", "q": "Türkiye'deki üniversitelerin web adreslerinde genellikle hangi uzantı kullanılır?",
     "options": [".com.tr", ".gov.tr", ".edu.tr", ".org.tr"], "answer": 2,
     "explain": ".edu eğitim kurumlarıyla ilişkilidir; Türkiye'de .edu.tr (örn. eskisehir.edu.tr). .gov.tr devlet kurumları içindir."},
    {"week": "bt-h5", "q": ".jp ve .ch ülke kodu uzantıları sırasıyla hangi ülkeleri temsil eder?",
     "options": ["Japonya – Çin", "Japonya – İsviçre", "Jamaika – Şili", "Japonya – Çekya"], "answer": 1,
     "explain": "Slayttaki ülke kodları: .tr Türkiye, .uk Birleşik Krallık, .jp Japonya, .it İtalya, .ch İsviçre."},
    {"week": "bt-h5", "q": "Tarayıcıda F12 (İncele) ile bir sayfanın HTML'inde yapılan değişiklik için hangisi doğrudur?",
     "options": ["Sitenin sunucudaki dosyalarını kalıcı olarak değiştirir", "Tüm ziyaretçiler değişikliği görür",
                 "Sadece kendi tarayıcımızda görünür ve sayfa yenilenince genellikle kaybolur", "Sayfa kaynağını siler"], "answer": 2,
     "explain": "İncele aracındaki değişiklikler geçicidir; web sitesinin gerçek dosyaları değişmez. Ctrl + U ise sayfa kaynağını gösterir."},
    {"week": "bt-h5", "q": "`<!DOCTYPE html>` ifadesi için hangisi doğrudur?",
     "options": ["`<body>` içinde yazılır", "Bir HTML etiketidir ve `</DOCTYPE>` ile kapatılır",
                 "Belgenin en başında yer alır, HTML5 olduğunu bildirir; etiket değildir ve kapanışı yoktur", "Sayfa başlığını belirler"], "answer": 2,
     "explain": "Belge türü bildirimi tarayıcıya HTML5 standardını bildirir. Sekme başlığını `<title>` belirler."},
    {"week": "bt-h5", "q": "Tarayıcı sekmesinde görünen sayfa başlığı hangi etiketle belirlenir ve nerede yazılır?",
     "options": ["`<h1>` — `<body>` içinde", "`<title>` — `<head>` içinde", "`<head>` — `<html>` dışında", "`<meta>` — `<body>` içinde"], "answer": 1,
     "explain": "`<title>` `<head>` içindedir ve sekmede görünür; `<h1>` ise sayfa içeriğindeki ana başlıktır."},
    {"week": "bt-h5", "q": "Türkçe karakterlerin doğru görüntülenmesine yardımcı olan ifade hangisidir?",
     "options": ["`<html lang=\"tr\">`", "`<meta charset=\"UTF-8\">`", "`<title>Türkçe</title>`", "`<!DOCTYPE html>`"], "answer": 1,
     "explain": "`<meta charset=\"UTF-8\">` karakter kodlamasını belirtir. `lang=\"tr\"` sayfanın dilinin Türkçe olduğunu bildirir."},
    {"week": "bt-h5", "q": "Aşağıdaki etiketlerden hangisinin kapanış etiketi YOKTUR?",
     "options": ["`<p>`", "`<h1>`", "`<br>`", "`<title>`"], "answer": 2,
     "explain": "`<br>` (satır atlama), `<img>` (resim) ve `<hr>` (yatay çizgi) kapanışsızdır."},
    {"week": "bt-h5", "q": "HTML başlık etiketleri için hangisi doğrudur?",
     "options": ["`<h6>` en büyük başlıktır", "`<h1>`–`<h6>` arasında altı seviye vardır; `<h1>` en üst düzey ve varsayılan olarak en büyüktür",
                 "Başlık etiketleri yalnızca yazı boyutunu değiştirir", "`<h7>` en alt düzey başlıktır"], "answer": 1,
     "explain": "Başlıklar ayrıca önem sırası/hiyerarşi belirtir; arama motorları ve ekran okuyucular için önemlidir."},
    {"week": "bt-h5", "q": "`<p>` ve `<br>` için hangisi YANLIŞTIR?",
     "options": ["`<p>` yeni paragraf oluşturur", "`<br>` aynı paragrafta alt satıra geçirir", "`<br>` ek paragraf boşluğu oluşturur", "`<br>` etiketinin kapanışı yoktur"], "answer": 2,
     "explain": "Paragraflar arasında varsayılan boşluk vardır; `<br>` ek paragraf boşluğu oluşturmaz."},
    {"week": "bt-h5", "q": "HTML'de tarayıcıda görüntülenmeyen yorum satırı nasıl yazılır?",
     "options": ["`// yorum`", "`/* yorum */`", "`<!-- yorum -->`", "`# yorum`"], "answer": 2,
     "explain": "Yorumlar `<!--` ile başlar `-->` ile biter; kodu geçici devre dışı bırakmak için de kullanılabilir."},
    {"week": "bt-h5", "q": "HTML nitelikleri (attributes) için hangisi doğrudur?",
     "options": ["Kapanış etiketinin içine yazılır", "Her zaman açılış etiketinin içinde, genellikle nitelik=\"değer\" biçiminde yazılır",
                 "Bir etikette yalnızca bir nitelik kullanılabilir", "Hiçbir nitelik değersiz kullanılamaz"], "answer": 1,
     "explain": "Birden fazla nitelik kullanılabilir; required, disabled gibi bazıları değersiz yazılabilir."},
    {"week": "bt-h5", "q": "Günümüzde bir yazının boyutunu değiştirmek için önerilen yöntem hangisidir?",
     "options": ["`<font size=\"5\">`", "`style=\"font-size: 24px;\"`", "`<big>` etiketi", "`size=\"24\"` niteliği"], "answer": 1,
     "explain": "`<font>` etiketi geçerliliğini yitirmiştir; boyut CSS'in font-size özelliğiyle verilir."},
    {"week": "bt-h5", "q": "Bir paragrafın sadece arka plan rengini değiştirmek için hangi CSS özelliği kullanılır?",
     "options": ["color", "background-color", "font-family", "text-align"], "answer": 1,
     "explain": "color metnin rengini, background-color öğenin arka plan rengini değiştirir; body'de kullanılırsa tüm sayfanın arka planı değişir."},
    {"week": "bt-h5", "q": "HEX renk kodu #00FF00 hangi rengi temsil eder?",
     "options": ["Kırmızı", "Yeşil", "Mavi", "Siyah"], "answer": 1,
     "explain": "#RRGGBB: ilk iki karakter kırmızı, sonraki iki yeşil, son iki mavi. #FF0000 kırmızı, #0000FF mavi."},
    {"week": "bt-h5", "q": "`color: #A41A1B;` ile aynı rengi veren RGB değeri hangisidir?",
     "options": ["rgb(164, 26, 27)", "rgb(26, 164, 27)", "rgb(41, 26, 27)", "rgb(255, 26, 27)"], "answer": 0,
     "explain": "A4₁₆ = 164, 1A₁₆ = 26, 1B₁₆ = 27. Slayt iki kodun aynı rengi verdiğini gösterir."},
    {"week": "bt-h5", "q": "Metni hem sol hem sağ kenara hizalamak için kullanılan text-align değeri hangisidir?",
     "options": ["center", "left", "justify", "right"], "answer": 2,
     "explain": "justify kelime boşluklarını ayarlayarak iki yana yaslar; etkisi çok satırlı metinlerde görülür."},
    {"week": "bt-h5", "q": "Boşlukları ve satır sonlarını olduğu gibi koruyan HTML etiketi hangisidir?",
     "options": ["`<mark>`", "`<pre>`", "`<abbr>`", "`<em>`"], "answer": 1,
     "explain": "`<pre>` biçimi korur. `<mark>` vurgulama, `<abbr>` kısaltma açıklaması, `<em>` italik vurgu."},
    {"week": "bt-h5", "q": "H₂O yazımında 2'yi alt simge yapmak için hangi etiket kullanılır?",
     "options": ["`<sup>`", "`<sub>`", "`<s>`", "`<ins>`"], "answer": 1,
     "explain": "`<sub>` alt simge, `<sup>` üst simge (8²), `<s>` üstü çizili, `<ins>` altı çizili eklenen metin."},
    {"week": "bt-h5", "q": "Maddeleri büyük Roma rakamlarıyla (I, II, III) numaralandıran sıralı liste hangisidir?",
     "options": ["`<ol type=\"i\">`", "`<ol type=\"I\">`", "`<ul type=\"I\">`", "`<ol start=\"I\">`"], "answer": 1,
     "explain": "type: \"1\" sayı, \"A\" büyük harf, \"a\" küçük harf, \"I\" büyük Roma, \"i\" küçük Roma. start başlangıç numarasını verir."},
    {"week": "bt-h5", "q": "`<ol start=\"3\">` ile başlayan bir listenin ikinci maddesinin numarası kaçtır?",
     "options": ["2", "3", "4", "5"], "answer": 2,
     "explain": "Liste 3'ten başlar: ilk madde 3, ikinci madde 4."},
    {"week": "bt-h5", "q": "`<img>` etiketindeki alt niteliğinin temel görevi nedir?",
     "options": ["Fare üzerine gelince ipucu göstermek", "Resmin genişliğini ayarlamak",
                 "Resim yüklenemezse görünen ve ekran okuyucuların kullandığı alternatif metni belirtmek", "Resmi sağa yaslamak"], "answer": 2,
     "explain": "Fareyle üzerine gelince ipucu title niteliğinin işidir. Boyut width/height, konum CSS float ile ayarlanır."},
    {"week": "bt-h5", "q": "`<img src=\"../fil.gif\">` yazımında resim nerededir?",
     "options": ["HTML dosyasıyla aynı klasörde", "fil adlı alt klasörde", "HTML dosyasının bir üst klasöründe", "İnternette"], "answer": 2,
     "explain": "../ bir üst klasöre çıkar. Aynı klasör \"fil.gif\", alt klasör \"yemekler/kurufasulye.jpg\"."},
    {"week": "bt-h5", "q": "HTML tablolarında başlık hücresi oluşturan ve genellikle kalın, ortalı görüntülenen etiket hangisidir?",
     "options": ["`<td>`", "`<tr>`", "`<th>`", "`<thead>`"], "answer": 2,
     "explain": "`<th>` başlık hücresi, `<td>` veri hücresi, `<tr>` satır, `<thead>` başlık bölümünü gruplandırır."},
    {"week": "bt-h5", "q": "Bir tablo hücresinin iki sütunu kaplaması için hangi nitelik kullanılır?",
     "options": ["`rowspan=\"2\"`", "`colspan=\"2\"`", "`border=\"2\"`", "`cellspacing=\"2\"`"], "answer": 1,
     "explain": "colspan sütunları, rowspan satırları birleştirir (örn. `<td rowspan=\"3\">FEN BİLİMLERİ</td>`)."},
    {"week": "bt-h5", "q": "Tabloda komşu hücrelerin kenarlıklarının birleşmesini sağlayan CSS özelliği hangisidir?",
     "options": ["padding", "border-spacing", "border-collapse", "background-image"], "answer": 2,
     "explain": "padding hücre içi boşluk, border-spacing ayrı kenarlıklı hücreler arası boşluk, border-collapse kenarlıkları birleştirir."},
    {"week": "bt-h5", "q": "Ders programı uygulamasında (başlık satırı + Pazartesi–Cuma, Gün / Ders Adı / Saat) tablo kaç satır ve kaç sütundan oluşur?",
     "options": ["5 satır, 3 sütun", "6 satır, 3 sütun", "3 satır, 6 sütun", "6 satır, 2 sütun"], "answer": 1,
     "explain": "1 başlık satırı (`<th>`) + 5 gün = 6 satır; Gün, Ders Adı, Saat = 3 sütun."},
    {"week": "bt-h5", "q": "Bir bağlantının yeni sekmede açılması için hangi nitelik kullanılır?",
     "options": ["`target=\"_self\"`", "`target=\"_blank\"`", "`href=\"_new\"`", "`open=\"tab\"`"], "answer": 1,
     "explain": "_blank genellikle yeni sekmede açar; _self (varsayılan) mevcut sekmede açar."},
    {"week": "bt-h5", "q": "Sayfadaki `<h2 id=\"iletisim\">` başlığına giden sayfa içi bağlantı nasıl yazılır?",
     "options": ["`<a href=\"iletisim\">`", "`<a href=\"#iletisim\">`", "`<a id=\"#iletisim\">`", "`<a target=\"iletisim\">`"], "answer": 1,
     "explain": "href içindeki # işaretinden sonraki ifade hedef öğenin id değeriyle aynı olmalıdır."},
    {"week": "bt-h5", "q": "`<a>` etiketindeki href kısaltmasının açılımı nedir?",
     "options": ["Hyper Reference Format", "Hypertext Reference", "HTMLRef", "Home Reference"], "answer": 1,
     "explain": "href (Hypertext Reference) bağlantının hedef adresini belirtir; a = anchor."},
    {"week": "bt-h5", "q": "Form alanında girilen karakterleri gizleyen input türü hangisidir?",
     "options": ["`type=\"text\"`", "`type=\"email\"`", "`type=\"password\"`", "`type=\"hidden\"`"], "answer": 2,
     "explain": "password karakterleri gizler; text tek satır metin, email e-posta adresi içindir."},
    {"week": "bt-h5", "q": "Form alanında placeholder ile value arasındaki fark nedir?",
     "options": ["İkisi de aynıdır", "placeholder sadece yol gösterici ipucudur; value alana gerçek başlangıç değeri verir",
                 "value alanı zorunlu yapar", "placeholder karakter sayısını sınırlar"], "answer": 1,
     "explain": "placeholder kullanıcının girdiği değer değildir. Zorunluluk required, sınır maxlength ile sağlanır."},
    {"week": "bt-h5", "q": "Bir grup radio butonundan yalnızca birinin seçilebilmesi için ne gerekir?",
     "options": ["Her birinin id'si aynı olmalı", "Gruptaki tüm radio butonlarının name değeri aynı olmalı",
                 "value değerleri boş olmalı", "required yazılmalı"], "answer": 1,
     "explain": "Aynı name'e sahip radio'lar bir grup oluşturur ve tek seçime izin verir. checkbox ise birden çok seçime izin verir."},
    {"week": "bt-h5", "q": "Form verilerini URL'nin sorgu bölümüne ekleyerek gönderen yöntem hangisidir?",
     "options": ["POST", "GET", "PUT", "action"], "answer": 1,
     "explain": "GET verileri URL'ye ekler (arama işlemleri); POST HTTP isteğinin gövdesinde gönderir (kayıt işlemleri). action ise gönderim adresidir."},
    {"week": "bt-h5", "q": "Öğrenci kayıt formunda kullanıcının kendini tanıtacağı çok satırlı metin alanı hangi etiketle oluşturulur?",
     "options": ["`<input type=\"text\">`", "`<textarea>`", "`<select>`", "`<label>`"], "answer": 1,
     "explain": "`<textarea rows=\"4\" cols=\"30\">`: rows görünür satır sayısı, cols yaklaşık karakter genişliği."},
    {"week": "bt-h5", "q": "HTML ile hazırlanan bir formdaki verilerin kaydedilmesi için ne gerekir?",
     "options": ["Sadece `<form>` etiketi yeterlidir", "Sunucu tarafında çalışan bir sistem gerekir", "CSS kullanmak gerekir", "Dosyayı .htm olarak kaydetmek gerekir"], "answer": 1,
     "explain": "HTML formun görünümünü ve alanlarını oluşturur; verilerin işlenmesi/kaydedilmesi sunucu tarafında yapılır."},
]
