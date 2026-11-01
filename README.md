# 🎓 ESTÜ Vize Kampı — Bulut Bilişim Operatörlüğü

9 Kasım vizeleri için Streamlit çalışma platformu + derslerdeki C / C# kodlarının arşivi.
İçerik, `canvas_materyalleri/` klasöründeki tüm PDF, PPTX, DOCX ve PNG dosyalarından (görüntü tabanlı slaytlar dahil) derlenmiştir.

| Ders | Kaynak | Hafta | Soru | Kart |
|---|---|---|---|---|
| 🖥️ Bilgi Teknolojileri (Erkut Bölükbaş) | 1–4.hafta PDF | 4 | 39 | 25 |
| 🧮 BTP239 · Bilgisayar Donanımı | BTP239_Hafta01, dönüşümler | 2 | 33 | 17 |
| 🌐 Bilgisayar Ağları (Cisco BNET) | hafta_1…6, Erişim Katmanı, PDU docx, kapsülleme PNG | 6 | 49 | 29 |
| ⚙️ İşletim Sistemleri ve Güvenliği (C) | Hafta01/02_C_Giris | 2 | 35 | 18 |
| 🟣 Programlama 1 (C#) | Degiskenler, Whiledan_Fora, veri türleri & operatör PNG'leri | 3 | 29 | 16 |

## Sekmeler
- **📊 Vize Kokpiti** — geri sayım, ders kartları, konu tamamlama takibi, deneme istatistikleri, ilerleme yedeği.
- **📚 Ders Özetleri** — hafta bazlı konu anlatımı, "🎯 Sınavda Kesin Çıkar" kutuları, kavram kartları, ders diyagramları (`assets/`),
  cheat sheet tabloları, ezber kartları ve her örnek kod için **💻 Editörde Aç**.
- **💻 Ders Kodları** — derslerde anlatılan 50 C / C# kodu, ortalanmış ve geniş salt-okunur kod editöründe
  (satır numaraları, sözdizimi renklendirme, kopyala/indir, önceki/sonraki, ilgili konu özetine dönüş).
  Uygulama hafif kalsın diye kod çalıştırma yoktur.
- **📝 Sınav & Yanlışlarım** — ders/hafta filtreli deneme, anında çözüm açıklaması, kalıcı **Tekrar Çözülecekler** havuzu.
  Sınav sekmesinden ayrılıp dönünce aktif deneme otomatik **Soru 1'e sıfırlanır** (`reset_exam_state`).

## Çalıştırma
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Testler
```bash
python tests/verify_content.py          # veri bütünlüğü + kod sorularının cevapları gerçek derleyicide (tests/code_runner.py, ağ gerekir)
python -m pytest tests/test_app.py -q   # 4 sayfa, Ders Kodları, sınav sıfırlama, yanlışlar havuzu
```

## Streamlit Cloud'a yayınlama
Repoyu GitHub'a gönderin (`canvas_materyalleri/` `.gitignore` ile dışarıda kalır), share.streamlit.io'da `app.py`'yi seçin.
`requirements.txt` yalnızca `streamlit` ve `pandas` kurar; sistem paketi gerekmez.
İlerleme `.progress/progress.json`'da tutulur; Cloud yeniden başlatılınca silinebileceği için Kokpit'teki **İlerlemeyi indir/yükle** ile yedekleyin.
