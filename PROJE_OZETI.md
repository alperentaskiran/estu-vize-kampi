# ESTÜ Vize Kampı — Proje Özeti

> Bu dosya, projeyi ilk kez gören bir yapay zekâ asistanının (ör. Gemini) ya da geliştiricinin sistemi hızlıca anlaması için yazıldı.
> Ne yapıldığını, sistemin nasıl çalıştığını, hangi modüllerin olduğunu ve yeni içeriğin nasıl ekleneceğini anlatır.

## 1. Proje nedir?

**ESTÜ Vize Kampı**, Eskişehir Teknik Üniversitesi (ESTÜ) **Bulut Bilişim Operatörlüğü** programı için hazırlanmış bir **vize (ara sınav) çalışma platformudur**.
Vizeler **9 Kasım 2026**'da başlar. Uygulama, Canvas'tan indirilen ders materyallerinin (PDF, PPTX, DOCX, PNG) tamamından derlenmiş içerikle şunları sunar:

- hafta hafta konu özetleri, "🎯 Sınavda Kesin Çıkar" kutuları, kavram kartları ve ders diyagramları,
- hızlı tekrar (cheat sheet) tabloları ve ezber kartları (flashcard),
- açıklamalı çoktan seçmeli vize provası soruları, aralarında C/C# kod çıktısı ve hata bulma soruları,
- derslerde anlatılan C / C# kodlarının salt-okunur bir kod editörü görünümünde arşivi,
- sınav simülatörü, yanlış cevapların biriktiği "Tekrar Çözülecekler" havuzu ve ilerleme istatistikleri.

| | |
|---|---|
| **Canlı uygulama** | https://estu-vize-kampi.streamlit.app |
| **Kaynak kod** | https://github.com/alperentaskiran/estu-vize-kampi (herkese açık repo, `main` dalı) |
| **Teknoloji** | Python · Streamlit 1.5x · pandas (sadece iki bağımlılık: `requirements.txt`) |
| **Tema** | Koyu tema (`.streamlit/config.toml`), mobil ve masaüstü uyumlu |
| **Dağıtım** | Streamlit Community Cloud; `main` dalına her push'ta otomatik yeniden yayınlanır |

## 2. İçerik envanteri (güncel)

| Ders | `id` | Hafta | Soru | Ezber kartı | Diyagram | Kod şablonu |
|---|---|---|---|---|---|---|
| 🖥️ Bilgi Teknolojileri | `bt` | 4 | 39 | 25 | 7 | 0 |
| 🧮 BTP239 · Bilgisayar Donanımı | `donanim` | 4 | 78 | 37 | 6 | 3 |
| 🌐 Bilgisayar Ağları (Cisco BNET) | `ag` | 7 | 74 | 41 | 26 | 3 |
| ⚙️ İşletim Sistemleri ve Güvenliği (C) | `c` | 3 | 62 | 30 | 13 | 35 |
| 🟣 Programlama 1 (C#) | `cs` | 3 | 29 | 16 | 2 | 18 |
| **Toplam** | | **21** | **282** | **149** | **54** | **59** |

Soruların 35'inde kod parçası vardır (kod çıktısı / derleme hatası soruları). Kod şablonu sütunu, şablonun `course` alanındaki derse göre sayılmıştır.

**Ders kapsamı (özet):**
- **Bilgi Teknolojileri:** BT'ye giriş, donanım-yazılım, yazılım ve işletim sistemleri, ağ temelleri (topoloji, OSI, kablolar, kablosuz).
- **Bilgisayar Donanımı:** bilgisayarın tarihçesi/sınıflandırması, sayı sistemleri ve dönüşümler; kasa türleri, güç kaynağı, konnektörler, UPS; anakart (form faktörü, yonga seti, veri yolları ISA/PCI/AGP/PCIe, USB, portlar, IRQ/DMA).
- **Bilgisayar Ağları:** ağ dünyası, kablosuz/ev ağı, katmanlı modeller ve kapsülleme, erişim katmanı/Ethernet/MAC/switch, IPv4/IPv6 ve subnetting, DHCP ve NAT/PAT, ARP ve ağlar arası yönlendirme (routing).
- **İşletim Sistemleri (C):** C'ye giriş I-II (değişken, döngü, fonksiyon, dizi, string, pointer, struct, getpid); işletim sistemine giriş (kernel, user/kernel mode, system call) ve derleme zinciri (gcc -E/-S/-c, ELF, ldd, nm, strace).
- **Programlama 1 (C#):** değişkenler, while → for döngüleri, veri türleri ve operatörler.

## 3. Klasör yapısı

```
estü canvas/
├── app.py                  # Giriş noktası: sayfa ayarı, başlık (hero), sekme seçici, sayfa yönlendirme
├── requirements.txt        # streamlit, pandas
├── README.md               # Kısa kullanıcı/kurulum dokümanı
├── PROJE_OZETI.md          # Bu dosya
├── .streamlit/config.toml  # Koyu tema, toolbar, istatistik kapatma
├── data/                   # TÜM ders içeriği (saf Python veri yapıları)
│   ├── course_bt.py        # Her ders dosyası: COURSE sözlüğü + QUESTIONS listesi
│   ├── course_donanim.py
│   ├── course_ag.py
│   ├── course_c.py         # c_prog() yardımcı: main gövdesini tam C programına çevirir
│   ├── course_cs.py        # cs_prog() yardımcı: C# Main gövdesini tam programa çevirir
│   ├── code_templates.py   # TEMPLATES: derslerdeki 59 C/C# kodu
│   └── curriculum.py       # Dersleri birleştirir, id atar, arama sözlüklerini kurar
├── modules/                # Arayüz ve durum yönetimi
│   ├── state.py            # Sayfa sabitleri, oturum durumu, sınav motoru, sekme takibi
│   ├── progress.py         # Kalıcı ilerleme (JSON dosyası)
│   ├── ui.py               # CSS ve ortak HTML bileşenleri
│   ├── page_cockpit.py     # 📊 Vize Kokpiti
│   ├── page_notes.py       # 📚 Ders Özetleri
│   ├── page_lab.py         # 💻 Ders Kodları
│   └── page_exam.py        # 📝 Sınav & Yanlışlarım
├── assets/                 # Ders PDF'lerinden kırpılmış 54 diyagram (jpg/png)
├── tests/
│   ├── test_app.py         # Streamlit AppTest ile arayüz testleri (7 test)
│   ├── verify_content.py   # Veri bütünlüğü + kod sorularını gerçek derleyicide doğrulama
│   └── code_runner.py      # Yalnızca testlerde kullanılan C/C# derleme-çalıştırma motoru
└── canvas_materyalleri/    # Ham Canvas dosyaları (PDF/PPTX/DOCX/PNG) — .gitignore'da, repoya girmez
```

`.gitignore` ayrıca `.progress/` (yerel ilerleme), `.streamlit/secrets.toml`, Python önbellekleri ve `.claude/` klasörünü dışlar.

## 4. Sistem nasıl çalışır?

### 4.1 Veri katmanı (`data/`)

İçerik veritabanı yoktur; her şey **Python modüllerinde sabit veri** olarak durur. Bu sayede uygulama hafiftir ve içerik Git ile sürümlenir.

**Her ders dosyası** iki şey dışa aktarır:

```python
COURSE = {
    "id": "ag", "name": "Bilgisayar Ağları (Cisco BNET)", "short": "AĞ", "icon": "🌐", "color": "#…",
    "teacher": "", "sources": [...],          # kaynak dosya adları
    "weeks": [
        {
            "id": "ag-h7",                    # benzersiz hafta kimliği
            "title": "7. Hafta — ARP ...",
            "sources": ["hafta_7_arp_ve_routing.pdf"],
            "summary": """Markdown konu anlatımı (tablo içerebilir)""",
            "concepts": [("Terim", "Tanım"), ...],          # kavram kartları
            "must": ["Sınavda kesin çıkar maddesi", ...],    # 🎯 kutusu
            "cheat": [{"title": ..., "columns": [...], "rows": [[...], ...]}],  # cheat sheet tabloları
            "images": [("ag_arp_routing_topoloji.jpg", "Açıklama")],         # assets/ içindeki görseller
            "templates": ["c_arp_hedefi", ...],              # code_templates.py kimlikleri
        },
    ],
    "flashcards": [("Soru", "Cevap"), ...],
}

QUESTIONS = [
    {"week": "ag-h7", "q": "Soru metni", "options": [4 şık], "answer": 1, "explain": "Detaylı çözüm",
     # isteğe bağlı kod sorusu alanları:
     "code": "ekranda gösterilen kod", "lang": "c" | "csharp", "stdin": "...",
     "run": "derlenebilir tam program", "expect": "beklenen çıktı", "expect_error": True},
]
```

**`code_templates.py`** → `TEMPLATES` listesi: `{"id", "lang", "course", "title", "source", "code", "stdin"?}`.
Başlığı `⚠️ Hatalı kod` ile başlayan şablonlar bilerek derlenmeyen örneklerdir (derleme/bağlama hatasını okumayı öğretir).

**`curriculum.py`** bütün dersleri birleştirir:
- `COURSES` (sıralı ders listesi), her soruya `{ders}-{sıra:03d}` biçiminde kimlik atar (ör. `ag-074`), `course` alanını ekler, `run` olan sorularda `lang`'i çıkarır,
- `EXAM_START = date(2026, 11, 9)`,
- arama sözlükleri: `COURSE_BY_ID`, `QUESTION_BY_ID`, `WEEK_BY_ID`, `TEMPLATES_BY_ID`,
- yardımcılar: `questions_for(course_ids, week_ids)`, `templates_for(...)`.

Başlıktaki "X ders · Y soru · Z ders kodu" sayaçları bu listelerin uzunluğundan hesaplandığı için yeni içerik eklendiğinde **otomatik güncellenir**.

### 4.2 Uygulama akışı (`app.py`)

1. `st.set_page_config` (geniş düzen, kenar çubuğu kapalı).
2. `state.init()` oturum değişkenlerini hazırlar, `ui.inject_css()` özel CSS'i ekler.
3. `ui.hero()` başlığı ve vizeye kalan gün sayacını çizer.
4. `st.segmented_control(key="nav")` ile 4 sekme seçilir; `state.track_navigation()` geçerli sayfayı döndürür.
5. İlgili sayfanın `render()` fonksiyonu çağrılır.

### 4.3 Sayfalar

| Sekme | Modül | Ne yapar? |
|---|---|---|
| 📊 **Vize Kokpiti** | `page_cockpit.py` | Geri sayım, genel metrikler, ders kartları (konu ilerlemesi, son başarı, havuzdaki yanlış), hafta bazlı "konuyu bitirdim" işaretleri, deneme istatistik grafikleri, en çok yanlış yapılan sorular, **💾 İlerleme yedeği** (JSON indir / yükle / sıfırla). |
| 📚 **Ders Özetleri** | `page_notes.py` | Ders seçimi (`pills`), üç görünüm: **Konu Anlatımı** (hafta sekmeleri: özet, 🎯 kutusu, kavram ızgarası, diyagramlar, ilgili kodlar ve "💻 Editörde Aç"), **Cheat Sheet** (tüm tablolar), **Ezber Kartları** (çevir, ileri/geri, karıştır, "biliyorum" işareti). |
| 💻 **Ders Kodları** | `page_lab.py` | Derslerdeki 59 kodun **salt-okunur** arşivi. Ortalanmış, VS Code benzeri editör görünümü (dosya sekmesi, satır numarası, renklendirme, durum çubuğu: kaynak + hafta + örnek stdin). Filtre (Tümü / C / C# / Diğer), kod seçici, Önceki/Sonraki, dosyayı indir, "📚 Konu özetine git". **Kod çalıştırma bilerek yoktur** (uygulama hafif kalsın diye). |
| 📝 **Sınav & Yanlışlarım** | `page_exam.py` | Ders/hafta/soru sayısı seçerek deneme oluşturma (isteğe bağlı "önce hiç çözmediklerim"), şıkları her denemede karıştırılan sorular, anında doğru/yanlış + çözüm, deneme sonu özeti ve ders bazlı tablo. **Tekrar Çözülecekler** havuzu: yanlışlar buraya eklenir; havuz modunda doğru çözülen soru havuzdan çıkar. |

### 4.4 Durum yönetimi (`modules/state.py`)

- Sayfa sabitleri: `PAGE_COCKPIT`, `PAGE_NOTES`, `PAGE_LAB`, `PAGE_EXAM`, `PAGES`.
- `track_navigation()`: kullanıcı **sınav sekmesinden ayrılıp geri dönerse** aktif deneme `reset_exam_state(keep_questions=True)` ile **Soru 1'e sıfırlanır** (cevaplar silinir, sorular aynı kalır) ve bilgi mesajı gösterilir. Bu, isteğin bilinçli bir kuralıdır.
- `open_in_lab(template_id)`: "💻 Editörde Aç" düğmelerinin callback'i; kodu seçip Ders Kodları sekmesine geçer.
- `new_exam(...)`: soru kimlikleri, her soru için rastgele şık sırası, `nonce` (widget anahtarlarını tazelemek için), `retry` (havuz modu) bilgisini tutan `exam` sözlüğü oluşturur.

### 4.5 Kalıcı ilerleme (`modules/progress.py`)

- İlerleme `.progress/progress.json` dosyasında tutulur (`ESTU_PROGRESS_DIR` ortam değişkeniyle klasör değiştirilebilir; testler geçici klasör kullanır).
- Alanlar: `topics_done` (bitirilen haftalar), `wrong_pool` (yanlış soru kimliği → sayaç/tarih), `answered`, `attempts` (deneme geçmişi), `flash_known` (bilinen kartlar).
- Fonksiyonlar: `record_answer`, `set_topic`, `add_attempt`, `toggle_flash`, `remove_wrong`, `clear_wrong`, `export_json`, `import_json`, `reset_all`.
- ⚠️ Streamlit Cloud'da dosya sistemi kalıcı değildir (uygulama yeniden başlayınca sıfırlanabilir) ve tüm ziyaretçiler aynı dosyayı paylaşır. Bu yüzden Kokpit'te **JSON yedek indir/yükle** özelliği vardır.

### 4.6 Arayüz yardımcıları (`modules/ui.py`)

Tek bir CSS bloğu (kartlar, başlık, 🎯 kutusu, kavram ızgarası, soru kartı, kod editörü sekmesi ve durum çubuğu, mobil kırılımlar) ve HTML üreten yardımcılar: `hero`, `progress_bar`, `must_box`, `concept_grid`, `table_md`, `esc` (HTML kaçışlama).
Kod yazı tipinde **ligatürler kapalıdır** (`<=` gibi operatörler `≤` olarak görünmesin diye).

## 5. Test ve doğrulama

| Komut | Ne yapar? |
|---|---|
| `python -m pytest tests/test_app.py -q` | Streamlit **AppTest** ile 7 arayüz testi: tüm sayfalar ve tüm ders görünümleri hatasız açılıyor mu, "Editörde Aç" geçişi, Ders Kodları sayfasının salt-okunur olması ve gezinmesi, sekme değişince sınavın Soru 1'e sıfırlanması, yanlışlar havuzu, deneme kaydı. |
| `python tests/verify_content.py --offline` | Yapısal kontrol: her derste ≥25 soru ve ≥10 kart, her haftada özet/must/cheat, görsel dosyaları ve şablon kimlikleri mevcut mu, soru kimlikleri benzersiz mi, 4 farklı şık, geçerli cevap indeksi, çözüm açıklaması. |
| `python tests/verify_content.py` | Yukarıdakine ek olarak **tüm kod sorularını ve tüm şablonları gerçek derleyicide** çalıştırır; `expect` çıktısını ve `expect_error` (derleme/bağlama hatası) beklentisini doğrular. Ağ gerekir, sıralı çalışır (birkaç dakika sürer). |

`tests/code_runner.py` (yalnızca test aracı, uygulamaya yüklenmez): sırasıyla **yerel gcc / mcs+mono**, **Piston** (`PISTON_URL` / `PISTON_TOKEN` ile; herkese açık Piston API'si 15.02.2026'dan beri yalnızca izinli kullanıcılara açık) ve **Wandbox** (gcc-13.2.0-c, mono-6.12.0.199) motorlarını dener. Sonsuz döngülere karşı zamanlayıcı, mono'da UTF-8 konsol, HTTP 429/5xx ve geçici "OCI runtime error" için yeniden deneme içerir; gcc ve `ld` (undefined reference / multiple definition) hatalarını ayrıştırır.

## 6. Yeni ders materyali ekleme iş akışı

Bu projede yeni bir Canvas PDF'i geldiğinde izlenen adımlar:

1. Dosya `canvas_materyalleri/` klasörüne konur; daha önce işlenmemiş dosya, değiştirilme tarihine ve ders dosyalarındaki `sources` alanlarına bakılarak bulunur.
2. Metin `pypdf` ile çıkarılır; metni olmayan ya da diyagram içeren slaytlar `pymupdf` ile görüntüye çevrilip **görsel olarak okunur**.
3. Önemli diyagramlar slayt başlığı atılıp kırpılarak `assets/` klasörüne kaydedilir (`{ders}_{konu}.jpg`).
4. İlgili `data/course_*.py` dosyasında `weeks` listesinin **sonuna** yeni hafta eklenir (eski içerik silinmez); `flashcards` ve `QUESTIONS` listelerine ekleme yapılır; `sources` ve dosya başındaki açıklama güncellenir. Yeni bir ders ise yeni `course_*.py` oluşturulup `curriculum.py`'ye eklenir.
5. PDF'te kod varsa (ya da konu hesaplamaya uygunsa) `code_templates.py`'ye şablon eklenir ve haftanın `templates` listesine yazılır.
6. `verify_content.py` (önce `--offline`, sonra derleyicili) ve `pytest` çalıştırılır; README'deki sayılar güncellenir.
7. Commit + `git push origin main` → Streamlit Cloud otomatik yeniden yayınlar.

## 7. Bilinen tuzaklar ve tasarım kararları

- **Callback'ler:** Düğmeler `st.rerun()` yerine `on_click` callback'leri kullanır; AppTest'te eskimiş eleman hatalarını ve çift tıklama sorunlarını önler.
- **Widget anahtarları:** Bir widget'ın değeri koddan değiştirilecekse, anahtar **aynı çalıştırmada ve widget oluşturulmadan önce** atanmalıdır; aksi hâlde tarayıcıda boş görünebilir (Ders Kodları sayfası bu kalıbı kullanır).
- **`<pre>` blokları:** `st.markdown` HTML içindeki satır sonlarını birleştirdiği için çok satırlı HTML `st.html` ile basılır.
- **Kod çalıştırma kaldırıldı:** Önceden uygulamada derleyici (Kod Lab) vardı; kullanıcının isteğiyle salt-okunur "Ders Kodları" arşivine dönüştürüldü. Derleme motoru yalnızca içerik doğrulama için `tests/` altında kaldı. Bu yüzden `packages.txt` yoktur.
- **Hafta numaraları:** Bazı PDF'lerin slayt üst bilgisi dosya adından farklı hafta numarası taşır (ör. `hafta_7_arp_ve_routing.pdf` slaytlarında "8. Hafta"); uygulamada dosya adı sırası esas alınır ve `sources` alanında not düşülür.
- **Streamlit Cloud:** Ücretsiz çalışma alanında yalnızca bir özel uygulama hakkı olduğu için repo herkese açık yapıldı. Push sırasında GitHub hata verirse otomatik yeniden yayın tetiklenmeyebilir; yeni bir push ya da Streamlit panelinden "Reboot app" gerekir.

## 8. Proje geçmişi (özet)

1. Tüm Canvas materyallerinden 5 derslik platform kuruldu (Kokpit, Ders Özetleri, Kod Lab, Sınav & Yanlışlarım), testler yazıldı.
2. Git deposu oluşturuldu, GitHub'a gönderildi, Streamlit Community Cloud'a yayınlandı.
3. Kod yazı tipi ligatürleri kapatıldı; BTP239 dersinin adı "Bilgisayar Donanımı" olarak düzeltildi.
4. Kod Lab, kod çalıştırmayan, ortalanmış ve geniş **💻 Ders Kodları** arşivine dönüştürüldü.
5. Yeni materyaller eklendi: `Hafta03_OS.pdf` (C dersi 3. hafta), `BTP239_Hafta02.pdf` ve `BTP239_Hafta03.pdf` (Donanım 2–3. hafta), `hafta_7_arp_ve_routing.pdf` (Ağlar 7. hafta). Soru sayısı 185'ten 282'ye, kod sayısı 50'den 59'a çıktı.

## 9. Yerelde çalıştırma

```bash
pip install -r requirements.txt
streamlit run app.py
```
