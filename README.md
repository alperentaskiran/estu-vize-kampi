# 🎓 ESTÜ Vize Kampı — Bulut Bilişim Operatörlüğü

9 Kasım vizeleri için Streamlit çalışma platformu + gömülü C / C# derleyici laboratuvarı.
İçerik, `canvas_materyalleri/` klasöründeki tüm PDF, PPTX, DOCX ve PNG dosyalarından (görüntü tabanlı slaytlar dahil) derlenmiştir.

| Ders | Kaynak | Hafta | Soru | Kart |
|---|---|---|---|---|
| 🖥️ Bilgi Teknolojileri (Erkut Bölükbaş) | 1–4.hafta PDF | 4 | 39 | 25 |
| 🧮 BTP239 · Bilgisayar Temelleri & Sayı Sistemleri | BTP239_Hafta01, dönüşümler | 2 | 33 | 17 |
| 🌐 Bilgisayar Ağları (Cisco BNET) | hafta_1…6, Erişim Katmanı, PDU docx, kapsülleme PNG | 6 | 49 | 29 |
| ⚙️ İşletim Sistemleri ve Güvenliği (C) | Hafta01/02_C_Giris | 2 | 35 | 18 |
| 🟣 Programlama 1 (C#) | Degiskenler, Whiledan_Fora, veri türleri & operatör PNG'leri | 3 | 29 | 16 |

## Sekmeler
- **📊 Vize Kokpiti** — geri sayım, ders kartları, konu tamamlama takibi, deneme istatistikleri, motor durumu, ilerleme yedeği.
- **📚 Ders Özetleri** — hafta bazlı konu anlatımı, "🎯 Sınavda Kesin Çıkar" kutuları, kavram kartları, ders diyagramları (`assets/`),
  cheat sheet tabloları, ezber kartları ve her örnek kod için **💻 Editörde Aç**.
- **💻 Kod Lab (C/C#)** — dil seçici, 50 ders şablonu, editör, **Program Girdisi (Stdin)**, ▶️ Derle ve Çalıştır, terminal,
  satır/sütun numaralı derleyici hataları ve hatalı satırı vurgulayan kod görünümü.
- **📝 Sınav & Yanlışlarım** — ders/hafta filtreli deneme, anında çözüm açıklaması, kalıcı **Tekrar Çözülecekler** havuzu.
  Sınav sekmesinden ayrılıp dönünce aktif deneme otomatik **Soru 1'e sıfırlanır** (`reset_exam_state`).

## Derleyici katmanları (`modules/code_sandbox.py`)
1. **Yerel**: `gcc` / `mcs + mono` varsa geçici dizinde derler, 5 sn zaman aşımı. Streamlit Cloud'da `packages.txt` kurar.
2. **Piston API**: genel sunucu (emkc.org) 15.02.2026'dan beri **whitelist'e kapalı**. Kendi Piston sunucunuz veya token'ınız varsa
   `.streamlit/secrets.toml` içine ekleyin:
   ```toml
   PISTON_URL = "https://sizin-piston-sunucunuz/api/v2/execute"
   PISTON_TOKEN = "..."
   ```
3. **Wandbox API**: anahtarsız, ücretsiz son yedek (yerel Windows'ta derleyici yoksa otomatik kullanılır). Uzak çalıştırmada 5 sn sınırı,
   satır numaralarını değiştirmeyen bir watchdog ile uygulanır.

## Çalıştırma
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Testler
```bash
python tests/verify_content.py          # veri bütünlüğü + tüm kod soruları/şablonlar gerçek derleyicide
python -m pytest tests/test_app.py -q   # 4 sayfa, Editörde Aç, sınav sıfırlama, yanlışlar havuzu
```

## Streamlit Cloud'a yayınlama
Repoyu GitHub'a gönderin (`canvas_materyalleri/` `.gitignore` ile dışarıda kalır), share.streamlit.io'da `app.py`'yi seçin.
`requirements.txt` Python paketlerini, `packages.txt` (`gcc`, `g++`, `mono-mcs`, `mono-runtime`) sistem derleyicilerini kurar.
İlerleme `.progress/progress.json`'da tutulur; Cloud yeniden başlatılınca silinebileceği için Kokpit'teki **İlerlemeyi indir/yükle** ile yedekleyin.
