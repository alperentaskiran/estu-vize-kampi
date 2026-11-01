"""Bilgisayar Ağları (BBO1001, Cisco Networking Basics / BNET) — 1.–6. hafta.

Kaynaklar: hafta_1_ag_dunyasi_v4.pdf, hafta_2_kablosuz_ve_ev_agi.pdf,
hafta_3_katmanli_modeller_ve_ag_ortamlari.pdf (görüntü tabanlı), packet tracer PDU uygulaması.docx,
Ağ_Modellerinde_Kapsülleme_ve_Dekapsülleme.png, hafta4_Erişim Katmanı_MAC Address_Switch (görüntü tabanlı, 44 slayt),
hafta_5_ipv4_ipv6_ve_subnetting.pdf, Hafta6_DHCP_ve_NAT_ile_Ağ_Adresleme v1.pdf (görüntü tabanlı),
Hafta6_bilgisayar_aglari_dhcp_nat_sunumu_V2.pdf.
"""

COURSE = {
    "id": "ag",
    "name": "Bilgisayar Ağları (Cisco BNET)",
    "short": "AĞ",
    "icon": "🌐",
    "color": "#34d399",
    "teacher": "",
    "sources": ["hafta_1…hafta_5 PDF'leri", "Hafta6 DHCP/NAT (v1 + V2)", "hafta4 Erişim Katmanı", "packet tracer PDU uygulaması.docx",
                "Ağ_Modellerinde_Kapsülleme_ve_Dekapsülleme.png"],
    "weeks": [
        {
            "id": "ag-h1",
            "title": "1. Hafta — Ağ Dünyasına Giriş ve Temel Bileşenler",
            "sources": ["hafta_1_ag_dunyasi_v4.pdf"],
            "summary": """
**Ağların rolü:** SOHO (ev/küçük ofis, tek tümleşik router) · Mobil & IoT (Wi‑Fi, 5G, Bluetooth) · Kurumsal (Layer 2/3 switch, firewall, fiber).

**Sinyal türleri:**

| Ortam | Sinyal | Avantaj | Kısıt |
|---|---|---|---|
| Bakır (UTP Cat5e/6, koaksiyel) | Voltaj değişimi | Ucuz, kolay kurulum | **EMI**, ~**100 m** sınırı |
| Fiber optik | Işık darbeleri (lazer/LED) | Çok yüksek bant genişliği, parazitsiz | Pahalı, hassas işçilik |
| Kablosuz | Elektromanyetik/radyo dalgası | Mobilite | Duvar sönümlemesi, frekans çakışması |

* **Bant genişliği (Bandwidth):** ortamın *teorik* olarak birim zamanda taşıyabileceği **maksimum** veri (100 Mbps hat)
* **Aktarım hızı (Throughput):** belirli anda *fiilen* başarıyla aktarılan **gerçek** hız (yoğunlukta 65 Mbps)
* **Gecikme (Latency):** kaynaktan hedefe geçen süre; trafik, cihaz işleme süresi, paket kaybı throughput'u düşürür

**Mimariler:** **İstemci-Sunucu** — roller belirgin, merkezi yönetim (güvenlik, yedek, yetki), HTTP/SMTP/FTP sunucuları, güçlü donanım gerekir ·
**P2P** — her cihaz hem istemci hem sunucu, merkeziyetsiz, kurulumu kolay (SOHO paylaşım, BitTorrent, Blockchain); güvenlik takibi zor, cihaz arttıkça performans düşer.

**3 temel eleman:** **Uç cihazlar** (PC, telefon, IP telefon, sunucu, yazıcı, IP kamera) · **Ara cihazlar** (switch, router, wireless AP, firewall) · **Ağ ortamları** (UTP, fiber, radyo).

**ISP bağlantı yöntemleri:** Cable (TV koaksiyel) · **DSL** (bakır telefon hattı, ADSL/VDSL) · **Fiber FTTH/FTTB** (simetrik, yüksek hız) · Hücresel 4G/5G · **Uydu** (kırsal/uzak bölge).

**Vaka:** 20 kişilik mimarlık bürosu, 100 Mbps fiber; 2 çalışanın kontrolsüz **P2P/Torrent** trafiği throughput'u **15 Mbps**'e düşürdü, VoIP kesildi →
P2P kısıtlandı, VoIP'ye öncelik veren **QoS** kuralları, kurumsal Layer 2 switch.

**Lab:** 2 PC + Server + Cisco **2960** switch, **düz bakır kablo**; PC0 192.168.1.10, PC1 .11, Server .100 /24; `ping 192.168.1.100`; Simulation Mode'da ICMP/HTTP izleme.
""",
            "concepts": [
                ("Bandwidth", "Teorik maksimum taşıma kapasitesi."), ("Throughput", "Fiilen ölçülen gerçek aktarım hızı."),
                ("Latency", "Verinin kaynaktan hedefe ulaşma süresi."), ("QoS", "Belirli trafiğe (VoIP) öncelik veren hizmet kalitesi kuralları."),
                ("Ara cihaz", "Veriyi kaynaktan hedefe yönlendiren cihaz: switch, router, AP, firewall."),
            ],
            "must": ["Bandwidth (teorik) ≠ Throughput (gerçek)", "Bakır EMI + ~100 m; fiber ışık; kablosuz radyo",
                     "Client-Server vs P2P özellikleri", "Uç / ara cihaz / ortam ayrımı", "DSL = telefon hattı; Cable = TV koaksiyel"],
            "cheat": [{"title": "Uç vs Ara cihaz", "columns": ["Uç cihaz", "Ara cihaz"], "rows": [
                ["PC, laptop", "Switch"], ["Akıllı telefon", "Router"], ["IP telefon, IP kamera", "Wireless Access Point"], ["Sunucu, yazıcı", "Firewall"]]}],
            "images": [],
            "templates": [],
        },
        {
            "id": "ag-h2",
            "title": "2. Hafta — Kablosuz/Mobil Ağlar ve Ev Ağı Kurulumu",
            "sources": ["hafta_2_kablosuz_ve_ev_agi.pdf"],
            "summary": """
**Kablosuz teknolojiler:** **Wi‑Fi (IEEE 802.11)** WLAN, 2.4/5 GHz, AP üzerinden · **Bluetooth (IEEE 802.15.1)** PAN, düşük güç, eşleştirme (pairing) ·
**Hücresel 3G/4G/5G** WAN, baz istasyonları, 5G çok düşük gecikme · **NFC** ~**4 cm**, temassız ödeme (Apple Pay, Google Wallet).

**Mobil güvenlik:** tanınmayan açık ağlarda otomatik bağlantıyı kapat · kullanılmayan Bluetooth'u kapat · roaming kontrolü · hotspot ·
Açık Wi‑Fi'da **sniffing** ve **Rogue AP** riski → **VPN** · biyometrik/güçlü ekran kilidi · uygulama izinlerini kısıtla.

**SOHO router** = Switch + Access Point + Router + Firewall tek kutuda. **WAN portu** ISP modemine; **LAN portları** dahili switch; **AP** radyo vericisi.

**2.4 GHz vs 5 GHz:**

| | 2.4 GHz | 5 GHz |
|---|---|---|
| Menzil / duvar | Daha uzak, duvardan kolay geçer | Kısa, engel geçirgenliği az |
| Hız | Düşük/orta (802.11n ~450 Mbps) | Çok yüksek (ac/ax 1 Gbps+) |
| Kanal | **Sadece 3 çakışmayan kanal: 1, 6, 11**; mikrodalga/Bluetooth paraziti | **24+ çakışmayan kanal** |

Standartlar: **802.11n (Wi‑Fi 4)** çift bant · **802.11ac (Wi‑Fi 5)** 5 GHz · **802.11ax (Wi‑Fi 6/6E)** 2.4/5/6 GHz yüksek yoğunluk.

**WLAN güvenliği:** SSID = ağ adı; **SSID broadcast'i kapatmak gerçek güvenlik değildir** (tarayıcıyla bulunur) · varsayılan admin parolasını değiştir ·
**WEP** güvensiz · **WPA2-Personal (AES)** yaygın standart · **WPA3-Personal (SAE)** brute-force'a karşı üstün · **MAC filtreleme** (ağır yönetim yükü) ·
**Misafir ağı** (LAN'dan izole) · **WPS kapalı tutulmalı** (PIN açığı).

**Vaka (kafe):** Open (şifresiz) Wi‑Fi → paketler dinlendi (Wireshark) + **AP Client Isolation kapalı** → müşteriler birbirine erişti.
Çözüm: WPA2-AES + günlük değişen parola (fişe basılı), Client Isolation açık, personel için ayrı VLAN/SSID.

**Lab:** WRT300N router, cable modem; Internet Setup = DHCP; LAN IP **192.168.0.1/24**, DHCP Server enabled; SSID 'MYO_EvAgi', WPA2 Personal AES; laptop WPC300N kartı;
tarayıcıdan 192.168.0.1 yönetim paneli.
""",
            "concepts": [
                ("NFC", "~4 cm menzilli; temassız ödeme."), ("Bluetooth", "IEEE 802.15.1, PAN, pairing."),
                ("Rogue AP", "Sahte erişim noktası."), ("Client Isolation", "Aynı AP'deki kablosuz istemcilerin birbirine erişimini engeller."),
                ("SAE", "WPA3'ün kimlik doğrulaması; brute-force'a dayanıklı."), ("WPS", "PIN açığı nedeniyle kapatılması gereken hızlı kurulum özelliği."),
            ],
            "must": ["Wi‑Fi 802.11 / Bluetooth 802.15.1 / NFC ~4 cm", "2.4 GHz çakışmayan kanallar: 1, 6, 11",
                     "802.11ac = Wi‑Fi 5 (5 GHz), 802.11ax = Wi‑Fi 6/6E", "SSID gizlemek güvenlik değildir", "WEP < WPA2 (AES) < WPA3 (SAE); WPS kapalı",
                     "SOHO router = switch + AP + router + firewall"],
            "cheat": [{"title": "Wi‑Fi standartları", "columns": ["Standart", "Ad", "Bant"], "rows": [
                ["802.11b", "Wi‑Fi 1", "2.4 GHz, 11 Mbps"], ["802.11g", "Wi‑Fi 3", "2.4 GHz, 54 Mbps"], ["802.11n", "Wi‑Fi 4", "2.4 + 5 GHz, MIMO"],
                ["802.11ac", "Wi‑Fi 5", "5 GHz"], ["802.11ax", "Wi‑Fi 6/6E", "2.4/5/6 GHz"]]}],
            "images": [],
            "templates": [],
        },
        {
            "id": "ag-h3",
            "title": "3. Hafta — İletişim İlkeleri, Katmanlı Modeller ve Ağ Ortamları",
            "sources": ["hafta_3_katmanli_modeller_ve_ag_ortamlari.pdf (görsel)", "packet tracer PDU uygulaması.docx", "Ağ_Modellerinde_Kapsülleme_ve_Dekapsülleme.png"],
            "summary": """
**İletişim ilkeleri (protokol kuralları):** 1) **Kodlama (encoding)** — mesajı elektrik/ışık/radyo sinyaline çevirme · 2) **Biçimlendirme & kapsülleme** — başlık bilgileri ·
3) **Boyutlandırma & zamanlama** — uzun mesajları segmentlere bölme, akış kontrolü, yanıt bekleme süresi · 4) **Teslimat seçenekleri** — Unicast (bire-bir), Multicast (bire-grup), Broadcast (bire-hepsi).

**Açık standartlar:** **IEEE** fiziksel & veri bağlantısı (802.3 Ethernet, 802.11 Wi‑Fi) · **IETF/RFC** mantıksal iletişim (RFC 791 – IPv4) · **IANA & ICANN** IP tahsisi ve DNS · **ISO & ITU-T** OSI modeli.
**Neden katmanlı mimari?** Tek parça sistemde küçük hata tüm ağı çökertir; katmanlarda bir katmandaki değişiklik diğerini etkilemez.

**OSI vs TCP/IP:** OSI (7) eğitim ve arıza tespiti haritası; TCP/IP (4) internetin gerçek motoru.
OSI 7-6-5 → **Uygulama** · OSI 4 → **Taşıma** · OSI 3 → **İnternet** · OSI 2-1 → **Ağ Erişimi**.

**Kapsülleme (gönderici, yukarıdan aşağı):**

| Katman | TCP/IP | PDU | Eklenen başlık |
|---|---|---|---|
| 5–7 | Uygulama | **Veri (Data)** | Ham kullanıcı mesajı (HTTP, DNS, FTP) |
| 4 | Taşıma | **Segment** | TCP/UDP başlığı (kaynak & hedef **port**) |
| 3 | İnternet/Ağ | **Paket** | IP başlığı (kaynak & hedef **IP**) |
| 2 | Veri bağlantısı | **Çerçeve (Frame)** | MAC başlığı + **FCS** kuyruğu (hata kontrolü) |
| 1 | Fiziksel | **Bitler** | Elektrik, ışık veya radyo sinyalleri |

**Dekapsülleme (alıcı, aşağıdan yukarı):** L1 bitler alınır → L2 **cihaz kendi MAC'ini doğrularsa** çerçeve sökülür → L3 IP doğrulanırsa paket sökülür → L4 port kontrol edilir, TCP/UDP başlığı çıkarılır → L7 uygulamaya teslim.
**Önemli kural:** alıcı sadece kendi katmanıyla eşleşen adres bilgisini okur, uymuyorsa paketi **düşürür (drop)**.

**Packet Tracer PDU lab'ı:** PC1 192.168.1.10 → switch 2960 → Server1 192.168.1.100 (HTTP ON), düz kablo. Simulation mode, filtre sadece HTTP (ve TCP).
Out Layers: L7 HTTP GET · L4 TCP **kaynak port 1025** (rastgele), **hedef port 80** · L3 IP · L2 Ethernet II + FCS · L1 bitler.
**Switch'te sadece L1 ve L2 aktiftir** — IP/HTTP katmanlarını açmaz, hedef MAC'e bakar. Router eklenirse L2 MAC adresleri her atlamada değişir.

**Ağ ortamları:** **UTP** (bükümlü çift, Ethernet'in yaygın standardı) · **Fiber** (cam çekirdek, ışık palsleri) · **Koaksiyel** (bakır çekirdek, metal kalkan; geniş bant/kablo TV).
Karşılaştırma: Bakır elektriksel, **100 m / 10 Gbps'e kadar**, EMI'ye hassas · Fiber ışık, **100 km / 100+ Gbps**, EMI'ye tam bağışık · Wi‑Fi radyo, **~50 m / 1–9 Gbps**, gürültüye açık.

**Vaka – otomotiv fabrikasında EMI krizi:** robotların elektromanyetik paraziti UTP'deki sinyalleri bozdu (kablolar anten gibi davrandı) → kritik omurga **fiber optiğe** geçirildi; manyetik alan ışığı bükemez, parazit %100 engellendi.
""",
            "concepts": [
                ("PDU", "Protokol Veri Birimi: Veri → Segment → Paket → Çerçeve → Bit."), ("FCS", "Çerçeve kuyruğundaki hata kontrol alanı (CRC)."),
                ("Kapsülleme", "Her katmanın veriye kendi başlığını eklemesi."), ("Dekapsülleme", "Alıcıda başlıkların sırayla sökülmesi."),
                ("IEEE", "Fiziksel & veri bağlantısı standartları (802.3, 802.11)."), ("IANA/ICANN", "IP tahsisi ve DNS yönetimi."),
            ],
            "must": ["PDU sırası: Veri – Segment – Paket – Çerçeve – Bit", "L4 port, L3 IP, L2 MAC + FCS", "OSI 7 ↔ TCP/IP 4 eşlemesi",
                     "Switch sadece L1-L2'yi açar", "HTTP hedef port 80; istemci portu rastgele (1025)", "EMI ortamında fiber; fiber 100 km / 100+ Gbps",
                     "4 iletişim ilkesi: kodlama, biçimlendirme/kapsülleme, boyutlandırma/zamanlama, teslimat"],
            "cheat": [{"title": "Ortam karşılaştırma", "columns": ["", "Bakır (UTP)", "Fiber", "Kablosuz"], "rows": [
                ["Sinyal", "Elektriksel", "Işık palsleri", "Radyo dalgaları"], ["Mesafe & hız", "100 m / 10 Gbps", "100 km / 100+ Gbps", "~50 m / 1–9 Gbps"],
                ["EMI", "Hassas", "Tam bağışık", "Gürültüye açık"]]}],
            "images": [("ag_kapsulleme_infografik.jpg", "Kapsülleme ve dekapsülleme süreci + PDU dönüşüm tablosu (Ağ_Modellerinde_Kapsülleme_ve_Dekapsülleme.png)"),
                       ("ag_osi_vs_tcpip.jpg", "OSI vs TCP/IP referans modelleri (hafta 3, s.6)"),
                       ("ag_kapsulleme_asamalari.jpg", "Kapsülleme: verinin zırh kuşanma süreci (hafta 3, s.7)"),
                       ("ag_dekapsulleme.jpg", "De-kapsülleme ve 'önemli kural' (hafta 3, s.8)"),
                       ("ag_unicast_multicast_broadcast.jpg", "Teslimatın geometrisi: unicast / multicast / broadcast (hafta 3, s.3)"),
                       ("ag_ortam_karsilastirma.jpg", "Ortam karşılaştırma matrisi (hafta 3, s.10)")],
            "templates": [],
        },
        {
            "id": "ag-h4",
            "title": "4. Hafta — Erişim Katmanı, Ethernet, MAC Adresi ve Layer 2 Switch",
            "sources": ["hafta4_Erişim Katmanı_MAC Address_Switch (Access Layer).pdf (44 slayt, görsel)"],
            "summary": """
**Erişim katmanı:** uç cihazların ağa bağlandığı sınır. 4 görevi: **Bağlantı** · **Anahtarlama** (MAC tablosuna göre doğru porta) · **Performans** (her port ayrı fiziksel bağlantı, full-duplex) · **Kontrol** (Port Security, VLAN, erişim politikaları).

**Hub / Switch / Router:** Hub fiziksel katman, bitleri tüm portlara tekrarlar → **ortak collision domain** · Switch veri bağlantısı katmanı, MAC tablosuyla port seçer → **her port ayrı collision domain** · Router ağ katmanı, IP ağına göre yönlendirir → **broadcast alanlarını ayırır**.

**IEEE 802.3 Ethernet:** 100BASE-TX 100 Mb/s bakır · 1000BASE-T 1 Gb/s Cat5e+ · 10GBASE-T 10 Gb/s Cat6a · 10GBASE-SR 10 Gb/s çok modlu fiber. (802.3 = Ethernet, 802.11 = Wi‑Fi.)
Bakır/UTP: RJ-45, ekonomik, EMI'den etkilenir, yatay bağlantı **100 m** · Fiber: uzak mesafe, EMI'ye dayanıklı, çok/tek modlu → binalar arası tercih edilir.
**Half-duplex:** bir anda tek yön (eski paylaşımlı Ethernet/hub) · **Full-duplex:** iki yön eş zamanlı (switch + uygun NIC).

**Ethernet II çerçevesi:** `Preamble+SFD (8 B) | Hedef MAC (6) | Kaynak MAC (6) | EtherType (2) | Veri/Payload (46–1500) | FCS (4)`
* Preamble/SFD fiziksel iletimde kullanılır, **64–1518 B sayımına girmez**
* **Minimum: 6+6+2+46+4 = 64 bayt** · **Maksimum (etiketsiz): 14 + 1500 + 4 = 1518 bayt**
* Payload 46'dan azsa **padding** eklenir (20 B veri → 26 B padding)
* **FCS** CRC-32 ile bit hatalarını **saptar; düzeltmez**
* **EtherType:** **0x0800 IPv4** · **0x0806 ARP** (IPv4→MAC çözümleme) · **0x86DD IPv6**

**MAC adresi:** **48 bit, 6 bayt, 12 hex rakam** (00:60:2F:AA:BB:CC); her iki hex = 1 bayt. **İlk 24 bit OUI** (üretici) + son 24 bit üreticinin atadığı kısım.
OUI üreticiyi tanır, kimliği kesin ispatlamaz. **BIA** (Burned-In Address) fabrika MAC'i; İS/sanal arayüz/gizlilik yazılımsal MAC kullanabilir → MAC = *yerel bağlantı kimliği*, değişmez kişi kimliği değil.
**MAC vs IP:** MAC yerel bağlantıda çerçeve teslimi, 48 bit, switch hedef MAC'e bakar · IP ağlar arası mantıksal adresleme, IPv4 32 / IPv6 128 bit, router hedef IP ağına bakar.
**Router araya girince:** 1. atlama MAC A → Router MAC; 2. atlama Router MAC → MAC B (her bağlantıda L2 başlığı farklı, IP aynı).

**Layer 2 switch'in 3 davranışı:** 1) **Öğrenme** – gelen çerçevenin **kaynak MAC**'ini ve giriş portunu tabloya yazar · 2) **İletme** – hedef MAC biliniyorsa uygun porta ·
3) **Flooding** – hedef bilinmiyorsa veya broadcast ise aynı VLAN'daki diğer portlara. *Önce kaynak öğrenilir, sonra hedef için karar verilir.*
MAC tablosu **IP değil MAC–port** eşleşmesi tutar (AA:..:01 → Fa0/1 DYNAMIC).
Bilinen unicast → tek porta · Bilinmeyen unicast → flood · Broadcast (FF:FF:FF:FF:FF:FF) → flood. **Flood, geldiği porta geri gönderilmez.**

**Ping öncesi ARP:** PC-A hedef IP'nin MAC'ini bilmez → "192.168.1.11 kimde?" **ARP Request (broadcast)** → PC-B **ARP Reply** ile MAC'ini bildirir → ICMP Echo Request. ARP aynı IPv4 yerel ağında IP→MAC çözümlemesidir.

**Collision domain:** hub ortak alan; switch her port ayrı; full-duplex'te çakışma beklenmez · **Broadcast domain:** tek VLAN'lı switch = **1 alan**; farklı VLAN'lar ayrı; router arayüzleri ayırır.
**Store-and-forward:** çerçevenin tamamını alır, FCS denetler, hatalıyı atar; gecikme alma süresine bağlı · **Cut-through:** hedef MAC okununca iletmeye başlar; düşük gecikme, hatalı çerçeveyi iletme riski.
**Vaka – MAC tablosu taşırma:** sahte kaynak MAC'lerle tablo doldurulur → bilinmeyen unicast flooding artabilir → önlem: **Port Security, 802.1X**, izleme. (Yanlış genelleme: "her dolu tablo switch'i hub'a çevirir".)

**Port Security CLI:**
```
Switch(config)# interface fastEthernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 1
Switch(config-if)# switchport port-security mac-address sticky
Switch(config-if)# switchport port-security violation shutdown
```
İhlalde port **err-disabled** olur; geri almak için `shutdown` + `no shutdown`. Kontrol: `show port-security interface fa0/1`, `show mac address-table (dynamic)`, `clear mac address-table dynamic`.
**Lab 1:** PC0 .10 Fa0/1, PC1 .11 Fa0/2, PC2 .12 Fa0/3 (/24) — başlangıçta tablonun boş olması beklenmez.
""",
            "concepts": [
                ("OUI", "MAC'in ilk 24 biti; üreticiyi tanımlar."), ("BIA", "Burned-In Address — NIC'e üretici tarafından yazılan MAC."),
                ("Flooding", "Hedef bilinmediğinde/broadcast'te çerçevenin diğer tüm portlara gönderilmesi."),
                ("Collision domain", "Olası çakışmanın kapsamı; switch'te her port ayrı."), ("Broadcast domain", "Yayın çerçevesinin ulaştığı L2 alanı; router ayırır."),
                ("Sticky MAC", "Port Security'de görülen MAC'in otomatik güvenli listeye eklenmesi."), ("err-disabled", "Port Security ihlalinde portun kapandığı durum."),
            ],
            "must": ["Ethernet II alan sırası ve boyutları; min 64 / max 1518 B", "EtherType 0x0800 / 0x0806 / 0x86DD", "MAC 48 bit = 6 bayt = 12 hex; OUI ilk 24 bit",
                     "Switch: öğren (kaynak) → ilet/flood (hedef)", "Bilinmeyen unicast ve broadcast flood edilir; geldiği porta geri gitmez",
                     "Tek VLAN'lı switch = 1 broadcast domain; her port ayrı collision domain", "Store-and-forward vs cut-through", "Port Security komutları, violation shutdown → err-disabled"],
            "cheat": [{"title": "Ethernet II çerçevesi", "columns": ["Alan", "Boyut", "Görev"], "rows": [
                ["Preamble + SFD", "8 B", "Senkronizasyon (sayıma girmez)"], ["Hedef MAC", "6 B", "Alıcı"], ["Kaynak MAC", "6 B", "Gönderen"],
                ["EtherType", "2 B", "Taşınan protokol"], ["Payload", "46–1500 B", "Üst katman verisi (+padding)"], ["FCS", "4 B", "CRC-32 hata saptama"]]},
                      {"title": "Switch kararları", "columns": ["Trafik", "Hedef MAC", "Switch ne yapar?"], "rows": [
                ["Bilinen unicast", "Tabloda var", "Tek hedef porta iletir"], ["Bilinmeyen unicast", "Tabloda yok", "Aynı VLAN'da flood"],
                ["Broadcast", "FF:FF:FF:FF:FF:FF", "Aynı VLAN'da flood"]]}],
            "images": [("ag_ethernet_cerceve.jpg", "Ethernet II çerçevesi: alanların sırası (Erişim Katmanı, slayt 13)"),
                       ("ag_64_bayt.jpg", "64 bayt sınırı hesabı (slayt 15)"), ("ag_ethertype.jpg", "EtherType değerleri (slayt 16)"),
                       ("ag_mac_vs_ip.jpg", "MAC ve IP adresi karşılaştırması (slayt 22)"), ("ag_switch_davranis.jpg", "MAC adres tablosu (slayt 27)"),
                       ("ag_broadcast_unknown_unicast.jpg", "Broadcast ve unknown unicast farkı (slayt 30)"), ("ag_arp_ping.jpg", "Ping öncesi ARP (slayt 31)")],
            "templates": [],
        },
        {
            "id": "ag-h5",
            "title": "5. Hafta — IPv4/IPv6 Adresleme ve Subnetting",
            "sources": ["hafta_5_ipv4_ipv6_ve_subnetting.pdf (metin + görsel sayfalar)"],
            "summary": """
**IPv4:** **32 bit**, 8'er bitlik **4 oktet**, noktalı onluk (192.168.1.10 = 11000000.10101000.00000001.00001010); 2³² ≈ **4,3 milyar** adres.
**Ağ kısmı** (posta kodu gibi; router sadece buna bakar) + **Host kısmı** (kapı numarası). **Subnet mask:** 1 bitleri ağ, 0 bitleri host; 255.255.255.0 = **/24** (CIDR).

**Sınıflar:** A 1.0.0.0–127.255.255.255 /8 (16 milyon+ host) · B 128–191 /16 (**65.534** host) · C 192–223 /24 (**254** host) · **D 224–239 multicast** · E 240–255 deneysel.
**RFC 1918 özel IP:** **10.0.0.0/8** · **172.16.0.0 – 172.31.255.255 /12** · **192.168.0.0/16** — internette yönlendirilemez, **NAT gerekir**.
Özel adresler: **127.0.0.1 loopback** (kendi TCP/IP yığınını test) · **169.254.0.0/16 APIPA** (DHCP'ye ulaşılamayınca Windows) · **255.255.255.255** yerel broadcast · **0.0.0.0/0** varsayılan rota.

**AND işlemi** (1 AND 1 = 1, diğerleri 0): Kaynak IP AND mask = kaynak ağ; Hedef IP AND mask = hedef ağ. **Eşitse yerel** (ARP ile MAC bul, doğrudan gönder) · **farklıysa uzak** (Default Gateway'e teslim).
Örn. 192.168.1.130 AND 255.255.255.0 = **192.168.1.0**.

**İletim türleri:** Unicast bire-bir (HTTP, SMTP, FTP) · **Broadcast** bire-hepsi, hedef IP 255.255.255.255 / MAC FF:FF:FF:FF:FF:FF (DHCP Discover, ARP); **router broadcast'i geçirmez** · **Multicast** bire-grup, D sınıfı 224.0.0.0–239.255.255.255 (IPTV, borsa, routing güncellemeleri).

**Adres türleri (/24):** **Ağ adresi** host bitleri tümü 0 (192.168.1.0, cihaza atanamaz) · İlk host son bit 1 (.1, genelde gateway) · Son host (.254) · **Broadcast** host bitleri tümü 1 (.255).

**Subnetting:** büyük broadcast domain → yoğunluk + güvenlik zafiyeti; broadcast alanını yalnızca L3 cihaz böler. Host bitlerinden **bit ödünç alma** →
**alt ağ sayısı = 2ⁿ** (n ödünç bit), **kullanılabilir host = 2ʰ − 2** (h kalan host biti; −2 ağ + broadcast). Faydalar: performans, departman güvenliği (ACL), IP israfını önleme (P2P WAN linkine /30), yönetilebilirlik.

**Örnek: 192.168.1.0/24 → 4 alt ağ:** 2ⁿ=4 → n=2 → **/26**, mask **255.255.255.192**, h=6 → **62 host**, blok (magic number) **256−192 = 64**.

| Alt ağ | Ağ adresi | İlk host | Son host | Broadcast |
|---|---|---|---|---|
| 1 (00) | 192.168.1.0 | .1 | .62 | .63 |
| 2 (01) | 192.168.1.64 | .65 | .126 | .127 |
| 3 (10) | 192.168.1.128 | .129 | .190 | .191 |
| 4 (11) | 192.168.1.192 | .193 | .254 | .255 |

**Vaka – yanlış mask:** 172.16.10.15'e /24 yerine **/16** girildi → hem kendi ağı hem sunucu (172.16.20.50) AND sonucu 172.16.0.0 → sunucuyu yerel sandı, ARP attı, gateway'e göndermedi.
Düzeltme /24 → sunucu 172.16.20.0 farklı ağda → router'a gitti. Ders: DHCP insan hatasını önler.

**IPv6:** **128 bit** (2¹²⁸ ≈ 3,4×10³⁸, 340 undesilyon); **8 hekstet** × 16 bit, hex; sabit **40 bayt başlık**; dahili **IPsec**; **broadcast yok** (multicast + anycast); NAT bağımlılığı kalkar.
Kısaltma: **Kural 1** her hekstetteki **baştaki** sıfırlar atılır (sondakiler atılamaz) · **Kural 2** ardışık sıfır hekstetleri **`::`** ile — **yalnızca bir kez**.
2001:0db8:0000:0000:0008:0800:200c:417a → 2001:db8:0:0:8:800:200c:417a → **2001:db8::8:800:200c:417a**.
Geçiş: **Dual Stack** (eşzamanlı), **Tunneling** (IPv6'yı IPv4 içinde kapsülleme), **NAT64** (çeviri).

**Lab 1:** aynı subnet (192.168.1.10 ↔ .20) ping başarılı; PC1 192.168.2.20 yapılınca ağ adresleri farklı ve router yok → **Request Timed Out**.
**Lab 2:** Simulation Mode; unicast sadece PC1'e; `ping 192.168.1.255` subnet broadcast → switch geldiği port hariç tüm portlara çoğaltır.
""",
            "concepts": [
                ("CIDR", "Eğik çizgi gösterimi; /24 = 24 adet 1 biti."), ("APIPA", "169.254.0.0/16; DHCP yoksa Windows'un atadığı adres."),
                ("Loopback", "127.0.0.1; kendi TCP/IP yığınını test."), ("Magic number", "256 − maskenin ilgili okteti = blok boyutu."),
                ("Hekstet", "IPv6'da 16 bitlik grup (8 adet)."), ("Dual Stack", "IPv4 ve IPv6'nın aynı cihazda eşzamanlı çalışması."),
            ],
            "must": ["RFC 1918: 10/8, 172.16/12, 192.168/16", "AND ile yerel/uzak kararı", "2ⁿ alt ağ, 2ʰ−2 host",
                     "/26 = 255.255.255.192, 62 host, blok 64", "Ağ adresi host bitleri 0, broadcast host bitleri 1",
                     "IPv6 128 bit, 8 hekstet, '::' bir kez, broadcast yok", "Sınıf D = multicast; router broadcast geçirmez"],
            "cheat": [{"title": "Prefix tablosu (son oktet)", "columns": ["Prefix", "Mask", "Blok", "Host"], "rows": [
                ["/24", "255.255.255.0", "256", "254"], ["/25", "255.255.255.128", "128", "126"], ["/26", "255.255.255.192", "64", "62"],
                ["/27", "255.255.255.224", "32", "30"], ["/28", "255.255.255.240", "16", "14"], ["/29", "255.255.255.248", "8", "6"],
                ["/30", "255.255.255.252", "4", "2"]]},
                      {"title": "Özel adresler", "columns": ["Adres", "Anlam"], "rows": [
                ["10.0.0.0/8", "A sınıfı özel"], ["172.16.0.0/12", "B sınıfı özel (172.16–172.31)"], ["192.168.0.0/16", "C sınıfı özel"],
                ["127.0.0.1", "Loopback"], ["169.254.0.0/16", "APIPA / link-local"], ["255.255.255.255", "Yerel broadcast"], ["0.0.0.0/0", "Varsayılan rota"]]}],
            "images": [("ag_and_islemi.jpg", "Bitsel VE (AND) işlemi ve cihazın karar süreci (hafta 5, s.9)"),
                       ("ag_network_host_broadcast.jpg", "Network, host ve yayın adresleri (s.10)"),
                       ("ag_subnetting_26.jpg", "192.168.1.0/24 ağının 4 alt ağa bölünmesi (s.24)"),
                       ("ag_ipv6_kisaltma.jpg", "IPv6 hekstet yapısı ve kısaltma kuralları (s.21)"),
                       ("ag_ipv4_ipv6_gecis.jpg", "IPv4 → IPv6 geçiş: Dual-Stack, Tunneling, NAT64 (s.22)")],
            "templates": ["c_subnet_hesap"],
        },
        {
            "id": "ag-h6",
            "title": "6. Hafta — DHCP ve NAT/PAT ile Ağ Adresleme",
            "sources": ["Hafta6_DHCP_ve_NAT_ile_Ağ_Adresleme v1.pdf (görsel)", "Hafta6_bilgisayar_aglari_dhcp_nat_sunumu_V2.pdf"],
            "summary": """
Cihazın 4 parametresi: **IP, Subnet Mask, Default Gateway, DNS**.
**Statik:** elle girilir, asla değişmez → sunucular, ağ yazıcıları, router/switch yönetim arabirimleri, IP kamera/NVR; büyük ağda zaman alır, **IP çakışması** riski.
**Dinamik (DHCP):** belirli süreyle **kiralama**, merkezi yönetim, tak-çalıştır, çakışmayı önler; ayrılan cihazın IP'si havuza döner → PC, telefon, Wi‑Fi istemcileri.
**Public** IP: küresel benzersiz, IANA/RIPE/ARIN, ISP'den ücretli · **Private** IP: LAN içinde benzersiz, ücretsiz, internette yönlendirilemez (ISP sınırda düşürür) → NAT.

**DHCPv4 bileşenleri:** İstemci **UDP 68** · Sunucu **UDP 67** · **Relay Agent** – farklı alt ağdaki sunucuya router üzerinden `ip helper-address` ile broadcast'i unicast iletir.

**DORA:**
1. **DISCOVER** – istemci → **broadcast**; kaynak IP **0.0.0.0**, hedef **255.255.255.255**, hedef MAC FF:FF:FF:FF:FF:FF, port 68→67. Router broadcast'i geçirmez. Yanıt yoksa tekrar; hiç yoksa **APIPA 169.254.x.x**.
2. **OFFER** – sunucu → teklif: IP (örn. 192.168.1.50), mask, gateway, DNS, lease. Sunucu önce ICMP ping ile çakışma kontrol edebilir; birden çok sunucu varsa istemci genelde **ilk gelen** teklifi alır.
3. **REQUEST** – istemci → **broadcast** (diğer sunuculara "X'i seçtim" demek için); kaynak IP hâlâ 0.0.0.0. Yenilemede (T1) **unicast**.
4. **ACK** – sunucu onaylar, MAC–IP **binding table**'a yazar; istemci **Gratuitous ARP** ile son çakışma kontrolü yapar. **DHCPNAK** → istemci DORA'ya baştan başlar.

**Zamanlayıcılar:** Lease (Cisco varsayılan **1 gün**, Windows Server **8 gün**) · **T1 = %50** unicast REQUEST ile yenileme · **T2 = %87,5** herhangi bir sunucuya broadcast REQUEST (rebinding) · %100 → IP bırakılır, DORA baştan.
**Havuz parametreleri:** Pool (örn. 192.168.10.1–254) · **Exclusion** (`ip dhcp excluded-address`, statik cihazlar) · **MAC rezervasyonu** (hep aynı IP).

**Default Gateway:** kendi alt ağında olmayan hedefler için ilk router arabirimi. AND sonucu farklıysa paket gateway'in MAC'ine çerçevelenir. **Gateway yoksa yerel ağda haberleşir ama İNTERNETE ÇIKAMAZ.**
Router: L3 başlığını açar, routing table'a bakar (next-hop), yeni L2 başlığıyla **yeniden çerçeveler**. **Sınır router'ı:** inside (özel IP) ↔ outside (public IP), NAT yapar.
**Kablosuz router çift rol:** iç ağa **DHCP Server** (192.168.1.x dağıtır, gateway 192.168.1.1) · ISP'ye karşı **DHCP Client** (WAN'dan tek public IP alır, örn. 203.0.113.45).

**NAT neden?** IPv4 tasarrufu (binlerce cihaz tek public IP) · güvenlik (iç IP'ler gizli, dışarıdan başlatılan erişim engellenir) · ISP değişim esnekliği.
**Terimler:** **Inside Local** iç cihazın özel IP'si (192.168.1.10) · **Inside Global** iç cihazın dışarıdaki public IP'si (203.0.113.1) · Outside Local (genelde Outside Global ile aynı) · **Outside Global** hedefin gerçek public IP'si (198.51.100.5).

| | Statik NAT | Dinamik NAT | PAT (NAT Overload) |
|---|---|---|---|
| Oran | **1:1** | **M:N** (havuz) | **M:1** |
| Public IP | Her iç cihaza 1 | Eşzamanlı aktif cihaz kadar | **Tek IP yeter** |
| Dışarıdan erişim | **Evet** (sürekli) | Hayır | Hayır (port forwarding ile) |
| Kullanım | Web/mail/VPN sunucuları | Özel kurumsal | Evler, şirketler, internetin **%99**'u |

Dinamik NAT: havuz bitince sonraki cihazlar engellenir, pahalı. **PAT:** **soket çifti** (IP + **kaynak port**) ile ayırt eder; teorik **65.535** oturum/IP.
Örnek tablo: 192.168.1.10:1554 → 203.0.113.1:**8001** · 192.168.1.11:1554 → 203.0.113.1:**8002** (aynı iç port, router dışarıda farklı port atar).

**Vaka (çağrı merkezi, 150 kişi):** bazı PC'ler 192.168.0.x aldı → çalışanın getirdiği modem = **Rogue DHCP** (hatalı gateway); ayrıca PAT **65.535 port sınırı** doldu →
çözüm: access switch'lerde **DHCP Snooping**, NAT translation timeout optimizasyonu.
**Sorun giderme:** `ipconfig /all` (APIPA? gateway?) · `ip helper-address` eksik mi? · **inside/outside yönlerinin unutulması en sık NAT hatası** · ACL iç bloğu kapsıyor mu, komut sonunda `overload` var mı?

**Lab 1 – DHCP:**
```
Router(config)# ip dhcp excluded-address 192.168.10.1 192.168.10.10
Router(config)# ip dhcp pool MYO_LAN_POOL
Router(dhcp-config)# network 192.168.10.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.10.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# lease 2
```
Doğrulama: PC'de IP Configuration → DHCP; `ipconfig /all`; router'da **`show ip dhcp binding`**; Simulation'da DORA (broadcast mavi, unicast turuncu).

**Lab 2 – PAT:**
```
Router(config)# access-list 1 permit 192.168.10.0 0.0.0.255
Router(config)# ip nat inside source list 1 interface GigabitEthernet0/0/1 overload
Router(config)# interface g0/0/0
Router(config-if)# ip nat inside
Router(config)# interface g0/0/1
Router(config-if)# ip nat outside
```
**`overload`** kelimesi dinamik NAT'ı PAT'a (M:1) çevirir. Doğrulama: **`show ip nat translations`** (aynı inside global, farklı portlar :1025, :1026), **`show ip nat statistics`** (hits/misses).
""",
            "concepts": [
                ("DORA", "Discover → Offer → Request → Acknowledgment."), ("Relay Agent", "ip helper-address ile DHCP broadcast'ini başka alt ağa unicast ileten router."),
                ("T1 / T2", "%50 yenileme (unicast) / %87,5 rebinding (broadcast)."), ("Inside Local", "İç cihazın özel IP'si."),
                ("Inside Global", "İç cihazın dış dünyada göründüğü public IP."), ("PAT", "NAT Overload; tek public IP + port numaralarıyla M:1."),
                ("Rogue DHCP", "Yetkisiz DHCP sunucusu; DHCP Snooping ile engellenir."),
            ],
            "must": ["DORA sırası; Discover & Request broadcast", "Discover: kaynak 0.0.0.0, hedef 255.255.255.255; UDP 68→67",
                     "T1 %50, T2 %87,5; Cisco 1 gün, Windows Server 8 gün", "ip helper-address = relay", "Gateway yoksa internete çıkılamaz",
                     "Inside Local / Inside Global / Outside Global", "Statik 1:1 – Dinamik M:N – PAT M:1; overload", "65.535 port; Rogue DHCP → DHCP Snooping",
                     "show ip dhcp binding · show ip nat translations · show ip nat statistics"],
            "cheat": [{"title": "DORA özeti", "columns": ["Adım", "Yön", "Tür", "Mesaj"], "rows": [
                ["Discover", "İstemci → ağ", "Broadcast", "DHCP sunucusu var mı?"], ["Offer", "Sunucu → istemci", "Unicast/Bcast", "Sana IP/Mask/GW/DNS teklifim"],
                ["Request", "İstemci → ağ", "Broadcast (yenilemede unicast)", "Teklifi kabul ettim"], ["Ack", "Sunucu → istemci", "Unicast/Bcast", "Kiralama onaylandı"]]},
                      {"title": "Cisco komutları", "columns": ["Amaç", "Komut"], "rows": [
                ["Havuzdan hariç tut", "ip dhcp excluded-address 192.168.10.1 192.168.10.10"], ["Havuz", "ip dhcp pool AD"], ["Gateway", "default-router 192.168.10.1"],
                ["Kiralamaları gör", "show ip dhcp binding"], ["Relay", "ip helper-address <DHCP-IP>"], ["PAT", "ip nat inside source list 1 interface g0/0/1 overload"],
                ["Statik NAT", "ip nat inside source static 192.168.10.254 203.0.113.10"], ["NAT tablosu", "show ip nat translations"]]}],
            "images": [("ag_dora.jpg", "4 adımlı DORA süreci (Hafta 6 v1, s.3)"), ("ag_dhcp_havuz.jpg", "DHCP sunucu parametreleri: havuz, opsiyonlar, lease, dışlama (s.4)"),
                       ("ag_nat_turleri.jpg", "Statik NAT, Dinamik NAT, PAT karşılaştırması (s.7)"), ("ag_pat_tablosu.jpg", "PAT soket seviyesinde dönüşüm (s.8)"),
                       ("ag_paket_yasam_dongusu.jpg", "Uçtan uca paket yaşam döngüsü: DHCP → Gateway → PAT → İnternet (s.9)"),
                       ("ag_dhcp_cli.jpg", "Cisco DHCPv4 yapılandırması (s.11)"), ("ag_pat_cli.jpg", "Cisco PAT (NAT Overload) yapılandırması (s.13)")],
            "templates": [],
        },
    ],
    "flashcards": [
        ("Bandwidth ile throughput farkı?", "Bandwidth teorik maksimum; throughput fiilen ölçülen gerçek hız."),
        ("NFC menzili?", "Yaklaşık 4 cm."), ("2.4 GHz'te çakışmayan kanallar?", "1, 6, 11."),
        ("SSID gizlemek güvenlik sağlar mı?", "Hayır; tarayıcı araçlarla tespit edilir."),
        ("WPA3'ün kimlik doğrulama yöntemi?", "SAE (Simultaneous Authentication of Equals)."),
        ("PDU sırası (yukarıdan aşağı)?", "Veri → Segment → Paket → Çerçeve → Bit."),
        ("Segment'e hangi bilgiler eklenir?", "Kaynak ve hedef port numaraları (TCP/UDP başlığı)."),
        ("Switch PDU'nun hangi katmanlarını açar?", "Sadece L1 ve L2 (hedef MAC'e bakar)."),
        ("Ethernet II minimum / maksimum çerçeve?", "64 bayt / 1518 bayt (preamble hariç)."),
        ("EtherType 0x0806?", "ARP."), ("EtherType 0x86DD?", "IPv6."),
        ("MAC adresi kaç bit, OUI kaç bit?", "48 bit; OUI ilk 24 bit."),
        ("Switch tabloya hangi adresi yazar?", "Gelen çerçevenin KAYNAK MAC adresini (ve portunu)."),
        ("Bilinmeyen unicast'te switch ne yapar?", "Aynı VLAN'daki diğer portlara flood eder."),
        ("Tek VLAN'lı 5 portlu switch'te broadcast domain sayısı?", "1."),
        ("Store-and-forward avantajı?", "FCS denetler, hatalı çerçeveyi iletmez."),
        ("RFC 1918 B sınıfı özel blok?", "172.16.0.0 – 172.31.255.255 (/12)."),
        ("APIPA aralığı?", "169.254.0.0/16."),
        ("/26 maskesi ve host sayısı?", "255.255.255.192 — 62 host, blok 64."),
        ("Kullanılabilir host formülü?", "2ʰ − 2."),
        ("IPv6'da '::' kaç kez kullanılabilir?", "Sadece bir kez."),
        ("IPv6'da broadcast var mı?", "Hayır; multicast ve anycast var."),
        ("DHCP istemci / sunucu portları?", "UDP 68 / UDP 67."),
        ("DHCPDISCOVER kaynak IP'si?", "0.0.0.0 (hedef 255.255.255.255)."),
        ("T1 ve T2 oranları?", "%50 ve %87,5."),
        ("Relay agent komutu?", "ip helper-address <DHCP-IP>."),
        ("Inside Local nedir?", "İç ağdaki cihazın RFC 1918 özel IP'si."),
        ("PAT'ı etkinleştiren anahtar kelime?", "overload."),
        ("Rogue DHCP'ye karşı switch özelliği?", "DHCP Snooping."),
    ],
}

QUESTIONS = [
    {"week": "ag-h1", "q": "100 Mbps fiber hattı olan bir ofiste yoğun saatlerde fiilen 65 Mbps ölçülüyor. 65 Mbps değeri neyi ifade eder?",
     "options": ["Bant genişliği (Bandwidth)", "Aktarım hızı (Throughput)", "Gecikme (Latency)", "Jitter"], "answer": 1,
     "explain": "Bandwidth teorik maksimumdur (100 Mbps); belirli anda fiilen aktarılan gerçek hız **throughput**'tur."},
    {"week": "ag-h1", "q": "Aşağıdakilerden hangisi bir 'ara cihaz' (intermediary device) DEĞİLDİR?",
     "options": ["Switch", "Router", "IP kamera", "Firewall"], "answer": 2,
     "explain": "IP kamera bir **uç cihazdır**. Ara cihazlar: switch, router, wireless access point, firewall."},
    {"week": "ag-h1", "q": "Mevcut bakır telefon hatlarını kullanarak yüksek frekansta dijital veri aktaran ISP bağlantı yöntemi hangisidir?",
     "options": ["Cable", "DSL (ADSL/VDSL)", "FTTH", "Uydu"], "answer": 1,
     "explain": "DSL telefon hattını kullanır; Cable TV koaksiyelini; FTTH eve kadar fiber çeker; uydu kırsal bölgeler içindir."},
    {"week": "ag-h1", "q": "Vaka çalışmasında 20 kişilik büroda VoIP ses kesilmelerinin kök nedeni ve çözümü neydi?",
     "options": ["Kablo arızası – kablo değişimi", "Kontrolsüz P2P/Torrent trafiği – P2P kısıtlama ve VoIP önceliklendiren QoS", "DHCP çakışması – statik IP", "Wi‑Fi paraziti – 5 GHz'e geçiş"], "answer": 1,
     "explain": "İki çalışanın torrent trafiği ev tipi router'ı boğdu, throughput 15 Mbps'e düştü. P2P kısıtlandı, QoS kuralları tanımlandı, kurumsal L2 switch'e geçildi."},
    {"week": "ag-h2", "q": "2.4 GHz bandında birbiriyle çakışmayan kanallar hangileridir?",
     "options": ["1, 5, 9", "1, 6, 11", "2, 7, 12", "36, 40, 44"], "answer": 1,
     "explain": "2.4 GHz'te sadece 3 çakışmayan kanal vardır: 1, 6, 11. 5 GHz'te 24+ çakışmayan kanal bulunur."},
    {"week": "ag-h2", "q": "Kablosuz ağ güvenliği için aşağıdaki ifadelerden hangisi YANLIŞTIR?",
     "options": ["WEP kullanılmamalıdır", "SSID broadcast'ini kapatmak ağı gerçekten gizler ve tek başına yeterli güvenlik sağlar", "WPS PIN açığı nedeniyle kapatılmalıdır", "WPA3 SAE ile brute-force'a karşı daha dayanıklıdır"], "answer": 1,
     "explain": "SSID gizlemek gerçek bir güvenlik sağlamaz; ağ adı tarayıcı araçlarla tespit edilebilir."},
    {"week": "ag-h2", "q": "Kafede müşterilerin birbirinin cihazına erişmesini engellemek için erişim noktasında hangi özellik açılmalıdır?",
     "options": ["MAC filtreleme", "SSID gizleme", "AP Client Isolation", "WPS"], "answer": 2,
     "explain": "Vaka çözümü: WPA2-AES şifreleme + **Client Isolation** + personel için ayrı VLAN/SSID."},
    {"week": "ag-h2", "q": "Yalnızca 5 GHz bandında çalışan Wi‑Fi standardı hangisidir?",
     "options": ["802.11n (Wi‑Fi 4)", "802.11ac (Wi‑Fi 5)", "802.11ax (Wi‑Fi 6)", "802.11g"], "answer": 1,
     "explain": "802.11n çift bant, **802.11ac yalnız 5 GHz**, 802.11ax 2.4/5/6 GHz."},
    {"week": "ag-h2", "q": "Bluetooth hangi IEEE standardı ve ağ türüyle ilişkilidir?",
     "options": ["802.11 – WLAN", "802.15.1 – PAN", "802.3 – LAN", "802.16 – MAN"], "answer": 1,
     "explain": "Bluetooth IEEE 802.15.1, kişisel alan ağı (PAN); düşük güç, eşleştirme (pairing)."},
    {"week": "ag-h3", "q": "Kapsülleme sürecinde Taşıma katmanında (L4) veriye eklenen bilgi ve oluşan PDU hangisidir?",
     "options": ["IP adresleri – Paket", "Port numaraları – Segment", "MAC adresleri – Çerçeve", "Sinyaller – Bit"], "answer": 1,
     "explain": "L4'te kaynak ve hedef port numaralarını içeren TCP/UDP başlığı eklenir → **Segment**."},
    {"week": "ag-h3", "q": "Veri bağlantısı katmanında çerçeveye eklenen ve hata kontrolü sağlayan kuyruk alanı hangisidir?",
     "options": ["TTL", "FCS", "SFD", "EtherType"], "answer": 1,
     "explain": "Çerçeve = MAC başlığı + paket + **FCS** (Frame Check Sequence, CRC-32 ile hata saptar)."},
    {"week": "ag-h3", "q": "OSI modelinin Oturum, Sunum ve Uygulama katmanları TCP/IP modelinde hangi katmana karşılık gelir?",
     "options": ["Taşıma", "İnternet", "Uygulama", "Ağ Erişimi"], "answer": 2,
     "explain": "OSI 5-6-7 → TCP/IP Uygulama · OSI 4 → Taşıma · OSI 3 → İnternet · OSI 1-2 → Ağ Erişimi."},
    {"week": "ag-h3", "q": "Packet Tracer PDU uygulamasında PC1'den Server1'e HTTP isteği giderken TCP başlığındaki hedef port hangisidir?",
     "options": ["1025", "443", "80", "53"], "answer": 2,
     "explain": "Kaynak port rastgele istemci portu (1025), **hedef port 80 (HTTP varsayılan)**."},
    {"week": "ag-h3", "q": "Simülasyonda paket switch'e geldiğinde PDU penceresinde hangi katmanların aktif olduğu görülür?",
     "options": ["Sadece L1 ve L2", "L1–L3", "L1–L4", "Tüm 7 katman"], "answer": 0,
     "explain": "Switch bir Katman 2 cihazıdır; IP veya HTTP katmanlarını açmaz, yalnızca hedef MAC'e bakarak porta iletir."},
    {"week": "ag-h3", "q": "Otomotiv fabrikasında robotların elektromanyetik paraziti nedeniyle UTP bağlantıları kopuyordu. Uygulanan mühendislik çözümü neydi?",
     "options": ["Kablosuz ağa geçmek", "Cat6 UTP kullanmak", "Kritik omurgayı fiber optiğe dönüştürmek", "Koaksiyel kablo kullanmak"], "answer": 2,
     "explain": "Fiber ışık kullanır; manyetik alanlar ışığı bükemez → EMI %100 engellendi."},
    {"week": "ag-h3", "q": "Alıcı cihazda dekapsülleme sırasında veri bağlantısı katmanında hangi kontrol yapılır?",
     "options": ["Hedef port kontrol edilir", "Hedef IP doğrulanır", "Cihaz kendi MAC adresini doğrularsa çerçeve sökülür", "Bitler sinyale çevrilir"], "answer": 2,
     "explain": "L2'de hedef MAC kendi MAC'iyle eşleşirse çerçeve başlığı ve FCS sökülür, paket L3'e iletilir. Eşleşmezse paket düşürülür."},
    {"week": "ag-h3", "q": "Fiziksel ve veri bağlantısı katmanı standartlarını (802.3 Ethernet, 802.11 Wi‑Fi) yazan kuruluş hangisidir?",
     "options": ["IANA", "IETF", "IEEE", "ISO"], "answer": 2,
     "explain": "IEEE donanım kurallarını yazar; IANA/ICANN adresleme ve DNS; ISO/ITU-T OSI modelini tanımlar."},
    {"week": "ag-h4", "q": "Ethernet II çerçevesinin minimum boyutu (preamble/SFD hariç) kaç bayttır?",
     "options": ["46", "60", "64", "1518"], "answer": 2,
     "explain": "6 (hedef MAC) + 6 (kaynak MAC) + 2 (EtherType) + 46 (min payload) + 4 (FCS) = **64 bayt**. Maksimum 1518."},
    {"week": "ag-h4", "q": "Bir Ethernet çerçevesinde taşınacak veri 20 bayt ise kaç bayt padding eklenir?",
     "options": ["0", "20", "26", "44"], "answer": 2,
     "explain": "Minimum payload 46 bayt; 46 − 20 = **26 bayt padding**."},
    {"week": "ag-h4", "q": "EtherType alanında 0x0806 değeri neyi belirtir?",
     "options": ["IPv4", "IPv6", "ARP", "VLAN etiketi"], "answer": 2,
     "explain": "0x0800 IPv4 · **0x0806 ARP** · 0x86DD IPv6."},
    {"week": "ag-h4", "q": "MAC adresi 00:60:2F:AA:BB:CC için hangisi doğrudur?",
     "options": ["32 bit; ilk 16 bit üretici", "48 bit; ilk 24 bit (00:60:2F) OUI", "64 bit; son 24 bit OUI", "48 bit; tamamı IANA tarafından atanır"], "answer": 1,
     "explain": "MAC 48 bit = 6 bayt = 12 hex rakam. İlk 24 bit OUI (üretici), son 24 bit üreticinin atadığı kısım."},
    {"week": "ag-h4", "q": "Switch, dinamik MAC tablosuna hangi bilgiyi yazar?",
     "options": ["Hedef IP – port", "Kaynak MAC – giriş portu", "Hedef MAC – çıkış portu", "Kaynak IP – VLAN"], "answer": 1,
     "explain": "Öğrenme: gelen çerçevenin **kaynak MAC**'i ve giriş portu tabloya yazılır. Tablo IP değil MAC–port eşleşmesi tutar."},
    {"week": "ag-h4", "q": "PC-A, PC-B'ye ilk kez çerçeve gönderiyor ve switch PC-B'nin MAC'ini henüz bilmiyor. Switch ne yapar?",
     "options": ["Çerçeveyi düşürür", "Kaynağı öğrenir, çerçeveyi aynı VLAN'daki diğer portlara flood eder", "Router'a gönderir", "ARP isteği üretir"], "answer": 1,
     "explain": "Adım 1: ÖĞREN (Kaynak …:01 → Fa0/1), KARAR (hedef …:02 yok → Flood). Flood geldiği porta geri gönderilmez."},
    {"week": "ag-h4", "q": "Tek VLAN'lı 5 portlu bir switch'te kaç broadcast domain vardır?",
     "options": ["1", "5", "10", "0"], "answer": 0,
     "explain": "Tek VLAN'lı switch = 1 broadcast domain (her port ayrı collision domain'dir). Broadcast alanlarını farklı VLAN'lar ve router arayüzleri ayırır."},
    {"week": "ag-h4", "q": "Çerçevenin tamamını alıp FCS denetimi yaparak hatalı çerçeveleri iletmeden atan switch iletim yöntemi hangisidir?",
     "options": ["Cut-through", "Store-and-forward", "Fragment-free flooding", "Half-duplex"], "answer": 1,
     "explain": "Store-and-forward hata kontrolü yapar ama gecikme alma süresine bağlıdır; cut-through düşük gecikmeli ama hatalı çerçeveyi iletebilir."},
    {"week": "ag-h4", "q": "Port Security'de 'switchport port-security violation shutdown' yapılandırılmış bir porta izinsiz MAC'li cihaz bağlanırsa port ne olur?",
     "options": ["Sadece uyarı loglanır", "err-disabled durumuna geçer", "VLAN 1'e taşınır", "Hub moduna geçer"], "answer": 1,
     "explain": "İhlalde port err-disabled olur; izinli cihaza dönüp `shutdown` + `no shutdown` ile geri alınır."},
    {"week": "ag-h4", "q": "PC-A ile PC-B arasına bir router (R1) girdiğinde çerçeve başlıkları için hangisi doğrudur?",
     "options": ["MAC adresleri uçtan uca değişmez", "1. atlamada MAC A → Router MAC, 2. atlamada Router MAC → MAC B olur", "IP adresleri her atlamada değişir", "Router MAC başlığını açmaz"], "answer": 1,
     "explain": "Her Ethernet bağlantısında Layer 2 başlığı farklıdır; IP adresleri (NAT yoksa) uçtan uca aynı kalır."},
    {"week": "ag-h4", "q": "PC-A, aynı ağdaki 192.168.1.11'e ping atmadan önce simülasyonda neden ARP mesajı görülür?",
     "options": ["Gateway'i bulmak için", "Hedef IP'nin MAC adresini öğrenmek için broadcast ARP Request gönderir", "IP almak için", "DNS çözmek için"], "answer": 1,
     "explain": "PC-A hedefin MAC'ini bilmez → 'Kimde?' ARP Request (broadcast) → PC-B ARP Reply → sonra ICMP Echo Request."},
    {"week": "ag-h5", "q": "Aşağıdakilerden hangisi RFC 1918 özel (private) IP aralığında DEĞİLDİR?",
     "options": ["10.20.30.40", "172.20.1.1", "172.32.1.1", "192.168.50.5"], "answer": 2,
     "explain": "B sınıfı özel blok 172.16.0.0–**172.31**.255.255'tir. 172.32.1.1 bu aralığın dışındadır (public)."},
    {"week": "ag-h5", "q": "Bir Windows bilgisayar DHCP sunucusuna ulaşamazsa kendisine hangi aralıktan adres atar?",
     "options": ["127.0.0.0/8", "169.254.0.0/16", "192.168.0.0/16", "0.0.0.0/0"], "answer": 1,
     "explain": "APIPA / link-local: 169.254.0.0/16. 127.0.0.1 loopback'tir."},
    {"week": "ag-h5", "q": "192.168.1.0/24 ağı 4 eşit alt ağa bölünürse yeni alt ağ maskesi ve alt ağ başına kullanılabilir host sayısı nedir?",
     "options": ["255.255.255.128 – 126", "255.255.255.192 – 62", "255.255.255.224 – 30", "255.255.255.192 – 64"], "answer": 1,
     "explain": "2ⁿ = 4 → n = 2 bit ödünç → /26 = 255.255.255.192; h = 6 → 2⁶ − 2 = **62** (ağ ve broadcast adresleri çıkarılır)."},
    {"week": "ag-h5", "q": "192.168.1.0/24'ün /26 ile bölünmesinde 2. alt ağın (192.168.1.64) broadcast adresi nedir?",
     "options": ["192.168.1.126", "192.168.1.127", "192.168.1.128", "192.168.1.191"], "answer": 1,
     "explain": "Blok 64: 2. alt ağ .64–.127 → ilk host .65, son host .126, **broadcast .127**."},
    {"week": "ag-h5", "q": "IP adresi 192.168.1.130, maske 255.255.255.0 ise AND işlemi sonucu ağ adresi nedir?",
     "options": ["192.168.1.0", "192.168.1.128", "192.168.1.130", "192.168.0.0"], "answer": 0,
     "explain": "Son oktet: 10000010 AND 00000000 = 0 → **192.168.1.0** (slayttaki AND örneği)."},
    {"week": "ag-h5", "q": "Muhasebe PC'sine 172.16.10.15 IP'si /24 yerine yanlışlıkla 255.255.0.0 maskesiyle girildi. Sunucu 172.16.20.50'ye neden erişilemedi?",
     "options": ["IP çakışması oluştu", "PC sunucuyu yerel ağda sandı, ARP attı ve paketi gateway'e göndermedi", "DNS çalışmadı", "Switch portu kapandı"], "answer": 1,
     "explain": "/16 ile her iki adresin AND sonucu 172.16.0.0 çıktı → yerel sanıldı. /24 ile 172.16.10.0 ≠ 172.16.20.0 → router'a yönlendirilir."},
    {"week": "ag-h5", "q": "2001:0db8:0000:0000:0008:0800:200c:417a adresinin kurallara uygun en kısa yazımı hangisidir?",
     "options": ["2001:db8::8:800:200c:417a", "2001:db8::8:8:200c:417a", "2001:db8:0::8:800::417a", "2001:db8::0008:800:200c:417a"], "answer": 0,
     "explain": "Kural 1: baştaki sıfırlar atılır (0db8→db8, 0008→8, 0800→800 — sondaki sıfırlar atılamaz). Kural 2: ardışık sıfır hekstetleri bir kez '::'."},
    {"week": "ag-h5", "q": "IPv6 için hangisi YANLIŞTIR?",
     "options": ["128 bitliktir", "8 hekstetten oluşur", "Broadcast iletimi geliştirilmiştir", "'::' adreste yalnızca bir kez kullanılabilir"], "answer": 2,
     "explain": "IPv6'da **broadcast tamamen kaldırılmıştır**; yerine multicast ve anycast vardır."},
    {"week": "ag-h5", "q": "IPTV canlı yayınları ve yönlendirme protokol güncellemelerinde kullanılan, D sınıfı adreslerle yapılan iletim türü hangisidir?",
     "options": ["Unicast", "Broadcast", "Multicast", "Anycast"], "answer": 2,
     "explain": "Multicast (bire-grup): 224.0.0.0–239.255.255.255; sadece abone cihazlara gider, bant genişliğini korur."},
    {"week": "ag-h5", "q": "5 host biti kalan bir alt ağda kaç kullanılabilir host adresi vardır?",
     "options": ["32", "30", "31", "62"], "answer": 1,
     "explain": "2⁵ − 2 = 32 − 2 = **30** (/27)."},
    {"week": "ag-h6", "q": "DORA sürecinin doğru sırası hangisidir?",
     "options": ["Discover – Offer – Request – Acknowledgment", "Offer – Discover – Request – Ack", "Discover – Request – Offer – Ack", "Request – Offer – Discover – Ack"], "answer": 0,
     "explain": "Discover (istemci broadcast) → Offer (sunucu teklif) → Request (istemci broadcast kabul) → Ack (sunucu onay)."},
    {"week": "ag-h6", "q": "DHCPDISCOVER mesajında kaynak ve hedef IP adresleri nedir?",
     "options": ["192.168.1.1 → 192.168.1.255", "0.0.0.0 → 255.255.255.255", "169.254.1.1 → 0.0.0.0", "127.0.0.1 → 255.255.255.255"], "answer": 1,
     "explain": "İstemcinin henüz IP'si olmadığı için kaynak 0.0.0.0; hedef yerel broadcast 255.255.255.255; port 68 → 67."},
    {"week": "ag-h6", "q": "DHCP istemcisi kiralama süresinin %50'si dolduğunda ne yapar?",
     "options": ["IP'yi bırakır", "T1: kiraladığı sunucuya unicast DHCPREQUEST ile yenileme ister", "T2: herhangi bir sunucuya broadcast atar", "DHCPDISCOVER başlatır"], "answer": 1,
     "explain": "T1 (%50) → unicast yenileme; T2 (%87,5) → broadcast rebinding; %100 → IP düşer, DORA baştan."},
    {"week": "ag-h6", "q": "DHCP sunucusu farklı bir alt ağdaysa router arabiriminde hangi komut yapılandırılmalıdır?",
     "options": ["ip nat inside", "ip helper-address <DHCP-IP>", "ip dhcp excluded-address", "default-router"], "answer": 1,
     "explain": "Router broadcast'i geçirmez; relay agent `ip helper-address` ile broadcast'i unicast olarak sunucuya iletir."},
    {"week": "ag-h6", "q": "İç ağdaki cihazın kendi lokal ağındaki RFC 1918 özel IP adresine NAT terminolojisinde ne denir?",
     "options": ["Inside Global", "Inside Local", "Outside Local", "Outside Global"], "answer": 1,
     "explain": "Inside Local: iç cihazın özel IP'si (192.168.1.10). Inside Global: dışarıya çıkarken dönüştüğü public IP (203.0.113.1)."},
    {"week": "ag-h6", "q": "Binlerce iç cihazı TEK bir public IP üzerinden, kaynak port numaralarını değiştirerek internete çıkaran yöntem hangisidir?",
     "options": ["Statik NAT (1:1)", "Dinamik NAT (M:N)", "PAT / NAT Overload (M:1)", "DHCP Relay"], "answer": 2,
     "explain": "PAT soket çifti (IP + port) ile cihazları ayırır; internetin %99'u bunu kullanır; teorik sınır 65.535 port."},
    {"week": "ag-h6", "q": "Şirket içindeki web sunucusunun dışarıdan sürekli erişilebilir olması için en uygun NAT türü hangisidir?",
     "options": ["PAT", "Dinamik NAT", "Statik NAT", "NAT64"], "answer": 2,
     "explain": "Statik NAT 1:1 kalıcı eşleme yapar, dışarıdan başlatılan erişime izin verir: `ip nat inside source static 192.168.10.254 203.0.113.10`."},
    {"week": "ag-h6", "q": "'ip nat inside source list 1 interface GigabitEthernet0/0/1 overload' komutundaki 'overload' kelimesinin işlevi nedir?",
     "options": ["Statik NAT'ı etkinleştirir", "Dinamik NAT'ı PAT (M:1) dönüşümüne çevirir", "ACL'yi siler", "DHCP havuzunu genişletir"], "answer": 1,
     "explain": "overload, WAN arabiriminin tek public IP'si üzerinden port tabanlı (PAT) dönüşüm sağlar."},
    {"week": "ag-h6", "q": "Çağrı merkezinde bazı PC'lerin 192.168.0.x adresi alıp internete çıkamamasının nedeni ve switch tarafındaki çözüm hangisidir?",
     "options": ["IP çakışması – statik IP", "Rogue (sahte) DHCP sunucusu – DHCP Snooping", "Broadcast fırtınası – STP", "PAT – statik NAT"], "answer": 1,
     "explain": "Çalışanın getirdiği modem sahte DHCP olarak hatalı gateway dağıttı. Access switch'lerde DHCP Snooping yetkisiz DHCP yanıtlarını engeller."},
    {"week": "ag-h6", "q": "Router üzerinde hangi MAC adresine hangi IP'nin kiralandığını gösteren komut hangisidir?",
     "options": ["show ip nat translations", "show ip dhcp binding", "show mac address-table", "ipconfig /all"], "answer": 1,
     "explain": "`show ip dhcp binding` kiralama tablosunu gösterir. `show ip nat translations` NAT tablosudur."},
    {"week": "ag-h6", "q": "Bir istemcide default gateway tanımlanmamışsa ne olur?",
     "options": ["Hiçbir cihazla haberleşemez", "Yerel ağda haberleşir ama internete çıkamaz", "APIPA adresi alır", "DHCP sunucusu olur"], "answer": 1,
     "explain": "Gateway eksikliği riski: cihaz yerel ağda kusursuz haberleşir ama farklı ağlara/internete ASLA çıkamaz."},
]
