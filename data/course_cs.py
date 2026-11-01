"""Programlama 1 (C#) — Değişkenler, while → for, veri türleri, operatörler.

Kaynaklar: Degiskenler_.pptx, Whiledan_Fora.pptx, C-ile-Veri-Turleri-ve-Degiskenler...png (aslında C# tip tablosu),
operatorler.png.
"""


def cs_prog(body, usings=("System",)):
    """Main gövdesini mono/mcs ile derlenebilir tam C# programına çevirir."""
    head = "".join(f"using {u};\n" for u in usings)
    lines = "\n".join("        " + ln if ln else "" for ln in body.strip("\n").split("\n"))
    return f"{head}\nclass Program\n{{\n    static void Main()\n    {{\n{lines}\n    }}\n}}\n"


COURSE = {
    "id": "cs",
    "name": "Programlama 1 (C#)",
    "short": "C#",
    "icon": "🟣",
    "color": "#f472b6",
    "teacher": "",
    "sources": ["Degiskenler_.pptx", "Whiledan_Fora.pptx", "C-ile-Veri-Turleri-ve-Degiskenler-Nelerdir-Temel-Bilgilerog.png", "operatorler.png"],
    "weeks": [
        {
            "id": "cs-h1",
            "title": "Değişkenler — Program bilgiyi nasıl hatırlar? (Kek tarifinden C#'a)",
            "sources": ["Degiskenler_.pptx"],
            "summary": """
**Algoritma** yapılacak işlemleri ve sıralarını belirler (kek: ölç → karıştır → kalıba dök → pişir). **Değişkenler** ise adımlarda kullanılan bilgileri tutar
(kaç yumurta? ne kadar şeker? fırın ısındı mı?). *Algoritma, değişkenlerde tuttuğumuz bilgileri kullanır.*

```csharp
int yumurtaSayisi = 3;
double sekerBardagi = 1.5;
int pisirmeSuresi = 35;
string kekCesidi = "Kakaolu";
bool firinIsindi = false;
```

**Değişken = isim verilmiş saklama alanı:** değeri saklarız, ismiyle ulaşırız, gerektiğinde değiştiririz.
**Üç özellik:** `int puan = 20;` → **veri tipi** (int, tam sayı) · **isim** (puan, değere erişim adı) · **değer** (20, şu anki içerik).

**Atama:** `puan = puan + 5;` → 1) mevcut değeri al (10) 2) işlemi yap (15) 3) sonucu puan'a yaz. **Yeni değer eskisinin yerini alır.**
Tarifi iki katına çıkarmak: `yumurtaSayisi = yumurtaSayisi * 2;` (6) · `sekerBardagi = sekerBardagi * 2;` (3) — her değişken ayrı güncellenir.
Pişirme süresi de iki katına çıkmalı mı? **Hayır** — hangi değişkenin nasıl güncelleneceğine problemin kurallarına göre karar verilir.

**Bilgiye uygun veri tipi:** `int yas = 18;` tam sayı · `double ortalama = 72.5;` ondalık · `string ad = "Ayşe";` metin · `bool dersiGecti = true;` doğru/yanlış.
**Telefon numarası → string:** `"05321234567"` — baştaki sıfırı koruruz, telefon numaralarıyla hesap yapmayız; bu bir **tanımlayıcıdır**.

**Atama anında değer kopyalanır:** `int a = 5; int b = a; a = 9;` → **a = 9, b = 5** (b, atama sırasında a'nın değeri olan 5'i aldı).
**Stok takibi:** `stok = 12; satilan = 3; stok = stok - satilan; satilan = 5;` → **stok 9** (satilan sonradan değişse de stok yeniden hesaplanmaz).

**Kafe siparişi:** `string urunAdi = "Çay"; int adet = 2; decimal birimFiyat = 25m; bool odendi = false;`
Anlamlı isim kullan (birimFiyat). **Para tutarlarında `decimal`** kullanılır (literal sonuna `m`).
Çıkış soruları: değişkene neden ihtiyaç duyarız? · `int x = 4; x = x + 2;` → **6** · "Ödeme yapıldı mı?" → **bool**.
""",
            "concepts": [
                ("Değişken", "İsim verilmiş saklama alanı: tip + isim + değer."), ("Atama (=)", "Sağdaki ifadenin sonucunu soldaki değişkene yazar."),
                ("decimal", "Para tutarları için; literal sonuna m eklenir (25m)."), ("bool", "true / false; 'Ödeme yapıldı mı?'"),
                ("string", "Metin; telefon numarası gibi tanımlayıcılar için de kullanılır."),
            ],
            "must": ["Değişkenin 3 özelliği: veri tipi, isim, değer", "int b = a; a = 9; → b değişmez (değer kopyalanır)", "stok = 9 sorusu",
                     "Telefon numarası string (baştaki 0, hesap yapılmaz)", "Para → decimal (25m)", "Evet/Hayır bilgisi → bool"],
            "cheat": [{"title": "Hangi bilgi hangi tip?", "columns": ["Bilgi", "Tip", "Örnek"], "rows": [
                ["Yaş, adet, puan", "int", "int adet = 2;"], ["Ortalama, ölçü", "double", "double ortalama = 72.5;"], ["Para", "decimal", "decimal birimFiyat = 25m;"],
                ["İsim, telefon", "string", 'string telefon = "05321234567";'], ["Evet/Hayır", "bool", "bool odendi = false;"]]}],
            "images": [],
            "templates": ["cs_kek_tarifi", "cs_atama", "cs_kopyalama", "cs_stok", "cs_kafe"],
        },
        {
            "id": "cs-h2",
            "title": "While'dan For'a — Döngüleri düzenli yazmak",
            "sources": ["Whiledan_Fora.pptx"],
            "summary": """
**if ≠ while:** aynı gövde, `int i = 1;` başlangıcıyla → **if** koşulu **bir defa** değerlendirir → çıktı **1** · **while** koşulu **her turda** yeniden değerlendirir → **1 2 3 4 5**.

**Sayma döngüsünün 3 parçası:** 1) **Başlangıç** `int i = 1` 2) **Koşul** `i <= 5` 3) **Değişim/Artış** `i++`.
**for** sayaçla ilgili bu üç bilgiyi **aynı yerde toplar**: `for (int i = 1; i <= 5; i++) { Console.WriteLine(i); }` — while sürümüyle **aynı çıktı**.

**for çalışma sırası:** 1) Başlat (`int i = 1`, **bir kez**) → 2) Koşul doğru mu? → 3) Gövde → 4) Değiştir (`i++`) ve koşula dön. **Koşul YANLIŞ olunca biter.**
İzleme (i <= 3): i=1 ✔ yaz 1 · i=2 ✔ yaz 2 · i=3 ✔ yaz 3 · i=4 ✘ biter.

**Kaç kez?** `for (int i = 0; i < 5; i++)` → **5 tekrar**, çıktı **0 1 2 3 4**; sayaç sıfırdan başlar. **`i < 5` ile `i <= 5` aynı değildir!**
**Adım:** `for (int i = 2; i <= 10; i += 2)` → **2 4 6 8 10**. 10'dan 1'e: `for (int i = 10; i >= 1; i--)`.

**Hangisini seçersin?** 1'den 100'e say → **for** · Doğru parola girilene kadar sor → **while** · 20 kez yıldız → **for** · Kullanıcı 0 girene kadar sayı al → **while**.
(Kesin kural değil; ikisi de çoğu işi yapabilir.)

**Aynı problem iki yol:** 1'den 10'a toplam → while ve for ikisi de **55**.
**while → for:** `int sayac = 3; while (sayac <= 15) { Console.WriteLine(sayac); sayac += 3; }` →
`for (int sayac = 3; sayac <= 15; sayac += 3)` → **3 6 9 12 15**.

**Hata bul:** `for (int i = 1; i <= 5; i--)` → i azalır, `i <= 5` hep doğru → **durmaz** (koşulun bir gün yanlış olması gerekir).
**Çıkış bileti:** for'un 3 bölümü (başlangıç, koşul, artış) · `for (int i = 1; i < 4; i++)` **3 kez** döner · for, while'ın sayaç bilgilerini tek satırda toplayan hâlidir.
**Ödev:** 1'den N'ye kadar çift sayıların toplamını hem while hem for ile yaz.

**Özet:** **if** koşul doğruysa bir kez · **while** koşul doğru kaldıkça tekrar · **for** başlangıç, koşul ve değişimi aynı yerde toplar.
""",
            "concepts": [
                ("for", "for (başlangıç; koşul; artış) — sayaçlı döngü."), ("while", "Koşul doğru kaldıkça tekrar; tekrar sayısı belli değilse."),
                ("i += 2", "Sayacı ikişer artırır."), ("Sonsuz döngü", "Koşul hiç yanlış olmazsa döngü durmaz (i-- ile i <= 5)."),
            ],
            "must": ["if bir kez, while her turda kontrol", "for'un 3 parçası ve çalışma sırası", "i < 5 → 5 tur (0..4); i < 4 → 3 tur",
                     "i += 2 → 2 4 6 8 10", "while ↔ for dönüşümü (sayac 3..15)", "i-- hatası → sonsuz döngü", "Toplam 1..10 = 55"],
            "cheat": [{"title": "while ↔ for", "columns": ["while", "for"], "rows": [
                ["int i = 1;\nwhile (i <= 5)\n{\n    Console.WriteLine(i);\n    i++;\n}", "for (int i = 1; i <= 5; i++)\n{\n    Console.WriteLine(i);\n}"]]},
                      {"title": "Döngü seçimi", "columns": ["Durum", "Döngü"], "rows": [
                ["1'den 100'e say", "for"], ["Doğru parola girilene kadar sor", "while"], ["20 kez yıldız çiz", "for"], ["Kullanıcı 0 girene kadar sayı al", "while"]]}],
            "images": [],
            "templates": ["cs_if_vs_while", "cs_while_say", "cs_for_say", "cs_for_sifirdan", "cs_for_ikiser", "cs_geri_say", "cs_toplam",
                          "cs_while_to_for", "cs_hatali_for", "cs_cift_toplam_odev"],
        },
        {
            "id": "cs-h3",
            "title": "Veri Türleri ve Operatörler (görsel tablolar)",
            "sources": ["C-ile-Veri-Turleri-ve-Degiskenler-Nelerdir-Temel-Bilgilerog.png", "operatorler.png"],
            "summary": """
Görseldeki tablo C# yerleşik veri türlerini listeler (dosya adı "C ile" olsa da `sbyte`, `decimal`, `object`, `string` gibi tipler C#'a aittir):

| Ad | Boyut (bayt) | Aralık |
|---|---|---|
| byte | 1 | 0 – 255 |
| short | 2 | −32.768 – 32.767 |
| int | 4 | −2.147.483.648 – 2.147.483.647 |
| long | 8 | −9.223.372.036.854.775.808 – 9.223.372.036.854.775.807 |
| sbyte | 1 | −128 – 127 |
| ushort | 2 | 0 – 65.535 |
| uint | 4 | 0 – 4.294.967.295 |
| ulong | 8 | 0 – 18.446.744.073.709.551.615 |
| float | 4 | ±1,5×10⁻⁴⁵ – ±3,4×10³⁸ |
| double | 8 | ±5,0×10⁻³²⁴ – ±1,7×10³⁰⁸ |
| object | — | — |
| char | 2 | Bir Unicode karakter |
| string | — | Karakterlerin tümü |
| decimal | 16 | ±1,0×10⁻²⁸ – ±7,9×10²⁸ |
| bool | 2 (görselde) | true veya false |

> ⚠️ Görselde `int` alt sınırı "−2.147.483.628" yazılmış; doğrusu **−2.147.483.648**. `bool` için görselde 2 bayt yazıyor; C#'ta `sizeof(bool)` **1** döndürür (Kod Lab'da `cs_sizeof` şablonuyla deneyebilirsin).
> İşaretsiz (u…) tipler negatif tutamaz; `sbyte` işaretli `byte`'tır.

**Karşılaştırma ve mantık operatörleri** (operatorler.png):

| Operatör | Anlam |
|---|---|
| `>` | Greater Than (büyüktür) |
| `<` | Less Than (küçüktür) |
| `>=` | Greater Than or Equal To |
| `<=` | Less Than or Equal To |
| `!=` | Not Equal To (eşit değil) |
| `!` | Not (değil) |
| `&&` | And (ve) — iki taraf da doğruysa true |
| `\\|\\|` | Or (veya) — en az biri doğruysa true |

Karşılaştırmaların sonucu **bool**'dur: `Console.WriteLine(5 > 3 && 2 > 4);` → **False**.
""",
            "concepts": [
                ("sbyte / byte", "1 bayt; işaretli −128..127 / işaretsiz 0..255."), ("decimal", "16 bayt; para ve hassas ondalık."),
                ("char", "2 bayt; bir Unicode karakter."), ("&& / ||", "Ve / veya; sonuç bool."), ("!=", "Eşit değil."),
            ],
            "must": ["byte 0–255, sbyte −128–127", "short 2, int 4, long 8, decimal 16, char 2 bayt", "ushort 0–65.535",
                     "float 4, double 8 bayt", "&&, ||, !, != anlamları ve bool sonucu"],
            "cheat": [{"title": "Tamsayı tipleri", "columns": ["İşaretli", "İşaretsiz", "Bayt"], "rows": [
                ["sbyte", "byte", "1"], ["short", "ushort", "2"], ["int", "uint", "4"], ["long", "ulong", "8"]]}],
            "images": [("cs_veri_turleri.jpg", "C# veri türleri, boyutları ve aralıkları (orijinal görsel)"), ("cs_operatorler.png", "Karşılaştırma ve mantık operatörleri (orijinal görsel)")],
            "templates": ["cs_sizeof", "cs_operatorler", "cs_tip_hatasi"],
        },
    ],
    "flashcards": [
        ("Değişkenin üç özelliği?", "Veri tipi, isim, değer."),
        ("int a = 5; int b = a; a = 9; → b?", "5 — atama anındaki değer kopyalanır."),
        ("Telefon numarası hangi tipte?", "string — baştaki sıfır korunur, hesap yapılmaz."),
        ("Para tutarı hangi tipte?", "decimal (örn. 25m)."),
        ("'Ödeme yapıldı mı?' hangi tipte?", "bool."),
        ("if ile while farkı?", "if koşulu bir kez, while her turda değerlendirir."),
        ("for'un üç bölümü?", "Başlangıç; koşul; artış (değişim)."),
        ("for (int i = 0; i < 5; i++) kaç kez?", "5 kez (0, 1, 2, 3, 4)."),
        ("for (int i = 1; i < 4; i++) kaç kez?", "3 kez."),
        ("for (int i = 1; i <= 5; i--) neden durmaz?", "i azaldıkça i <= 5 hep doğru kalır."),
        ("Doğru parola girilene kadar sormak için?", "while."),
        ("byte aralığı?", "0 – 255 (1 bayt)."), ("sbyte aralığı?", "−128 – 127."),
        ("decimal kaç bayt?", "16."), ("char kaç bayt?", "2 (Unicode)."),
        ("&& ne zaman true?", "İki taraf da true ise."),
    ],
}

QUESTIONS = [
    {"week": "cs-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "csharp",
     "code": "int a = 5;\nint b = a;\na = 9;\nConsole.WriteLine(a + \" \" + b);",
     "options": ["9 9", "5 5", "9 5", "5 9"], "answer": 2,
     "explain": "b, atama sırasında a'nın değeri olan 5'i aldı. a'nın sonradan 9 olması b'yi değiştirmez.",
     "run": cs_prog('int a = 5;\nint b = a;\na = 9;\nConsole.WriteLine(a + " " + b);'), "expect": "9 5"},
    {"week": "cs-h1", "q": "'Sıra sizde: stok takibi' — son durumda stok kaçtır?", "lang": "csharp",
     "code": "int stok = 12;\nint satilan = 3;\nstok = stok - satilan;\nsatilan = 5;\nConsole.WriteLine(stok);",
     "options": ["7", "9", "12", "4"], "answer": 1,
     "explain": "stok = 12 − 3 = 9 olarak hesaplanıp yazıldı. satilan'ın sonradan 5 olması stok'u yeniden hesaplatmaz.",
     "run": cs_prog('int stok = 12;\nint satilan = 3;\nstok = stok - satilan;\nsatilan = 5;\nConsole.WriteLine(stok);'), "expect": "9"},
    {"week": "cs-h1", "q": "`int x = 4; x = x + 2;` sonrasında x'in değeri nedir?",
     "options": ["4", "2", "6", "42"], "answer": 2,
     "explain": "Mevcut değer (4) alınır, işlem yapılır (4 + 2 = 6), sonuç x'e yazılır.",
     "run": cs_prog("int x = 4;\nx = x + 2;\nConsole.WriteLine(x);"), "expect": "6"},
    {"week": "cs-h1", "q": "`int puan = 20;` ifadesinde `puan` değişkenin hangi özelliğidir?",
     "options": ["Veri tipi", "İsim", "Değer", "Operatör"], "answer": 1,
     "explain": "int → veri tipi, **puan → isim (değere erişim adı)**, 20 → değer."},
    {"week": "cs-h1", "q": "Telefon numarası \"05321234567\" hangi veri tipinde tutulmalıdır?",
     "options": ["int", "long", "string", "double"], "answer": 2,
     "explain": "Baştaki sıfırı korumak ve hesap yapılmayacağı için **string**; telefon numarası bir tanımlayıcıdır. (Ayrıca int'e sığmaz.)"},
    {"week": "cs-h1", "q": "Kafe sipariş programında 'ödeme yapıldı mı?' bilgisi için en uygun tanım hangisidir?",
     "options": ["string odendi = \"hayır\";", "bool odendi = false;", "int odendi = 0;", "decimal odendi = 0m;"], "answer": 1,
     "explain": "Doğru/yanlış bilgisi **bool** ile tutulur."},
    {"week": "cs-h1", "q": "C#'ta para tutarları için slaytta önerilen veri tipi ve doğru yazım hangisidir?",
     "options": ["double birimFiyat = 25;", "decimal birimFiyat = 25m;", "int birimFiyat = 25.0;", "float birimFiyat = 25m;"], "answer": 1,
     "explain": "Para için **decimal**; literal sonuna **m** eklenir: `decimal birimFiyat = 25m;`."},
    {"week": "cs-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "csharp",
     "code": "int yumurtaSayisi = 3;\ndouble sekerBardagi = 1.5;\nyumurtaSayisi = yumurtaSayisi * 2;\nsekerBardagi = sekerBardagi * 2;\nConsole.WriteLine(yumurtaSayisi + \" \" + sekerBardagi);",
     "options": ["3 1.5", "6 3", "6 3.0", "9 4.5"], "answer": 1,
     "explain": "6 yumurta, 3 bardak şeker. C#'ta double 3.0, string birleştirmede '3' olarak yazılır.",
     "run": cs_prog('int yumurtaSayisi = 3;\ndouble sekerBardagi = 1.5;\nyumurtaSayisi = yumurtaSayisi * 2;\nsekerBardagi = sekerBardagi * 2;\nConsole.WriteLine(yumurtaSayisi + " " + sekerBardagi);'), "expect": "6 3"},
    {"week": "cs-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "csharp",
     "code": "decimal birimFiyat = 25m;\nint adet = 2;\nConsole.WriteLine(birimFiyat * adet);",
     "options": ["50", "25", "252", "Derleme hatası"], "answer": 0,
     "explain": "decimal × int → decimal: 25 × 2 = 50.",
     "run": cs_prog("decimal birimFiyat = 25m;\nint adet = 2;\nConsole.WriteLine(birimFiyat * adet);"), "expect": "50"},
    {"week": "cs-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "csharp",
     "code": "int i = 1;\nif (i <= 5)\n{\n    Console.WriteLine(i);\n    i++;\n}",
     "options": ["1", "1 2 3 4 5", "Hiçbir şey", "Sonsuz döngü"], "answer": 0,
     "explain": "**if** koşulu yalnızca bir defa değerlendirir → 1 yazılır. while olsaydı 1 2 3 4 5 yazılırdı.",
     "run": cs_prog("int i = 1;\nif (i <= 5)\n{\n    Console.WriteLine(i);\n    i++;\n}"), "expect": "1"},
    {"week": "cs-h2", "q": "Aşağıdaki döngü kaç kez çalışır, ilk ve son yazdırılan sayı nedir?", "lang": "csharp",
     "code": "for (int i = 0; i < 5; i++)\n{\n    Console.WriteLine(i);\n}",
     "options": ["5 kez; 0 ve 4", "6 kez; 0 ve 5", "5 kez; 1 ve 5", "4 kez; 1 ve 4"], "answer": 0,
     "explain": "Çıktı 0 1 2 3 4 → 5 tekrar. i < 5 ile i <= 5 aynı değildir!",
     "run": cs_prog("for (int i = 0; i < 5; i++)\n{\n    Console.WriteLine(i);\n}"), "expect": "0\n1\n2\n3\n4"},
    {"week": "cs-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "csharp",
     "code": "for (int i = 2; i <= 10; i += 2)\n{\n    Console.Write(i + \" \");\n}",
     "options": ["2 4 6 8", "2 4 6 8 10", "1 3 5 7 9", "2 3 4 5 6 7 8 9 10"], "answer": 1,
     "explain": "i += 2 → ikişer artış: 2 → 4 → 6 → 8 → 10.",
     "run": cs_prog('for (int i = 2; i <= 10; i += 2)\n{\n    Console.Write(i + " ");\n}\nConsole.WriteLine();'), "expect": "2 4 6 8 10"},
    {"week": "cs-h2", "q": "`for (int i = 1; i < 4; i++)` döngüsü kaç kez döner?",
     "options": ["3", "4", "5", "2"], "answer": 0,
     "explain": "i = 1, 2, 3 → 3 kez (çıkış bileti sorusu 2)."},
    {"week": "cs-h2", "q": "for döngüsünün çalışma sırası hangisidir?",
     "options": ["Koşul → Başlat → Gövde → Değiştir", "Başlat (bir kez) → Koşul → Gövde → Değiştir → Koşula dön", "Başlat → Gövde → Koşul → Değiştir", "Gövde → Değiştir → Koşul"], "answer": 1,
     "explain": "Başlangıç bir kez çalışır; sonra her turda koşul → gövde → değişim. Koşul yanlış olunca biter."},
    {"week": "cs-h2", "q": "Aşağıdaki while döngüsünün for karşılığı hangisidir?", "lang": "csharp",
     "code": "int sayac = 3;\nwhile (sayac <= 15)\n{\n    Console.WriteLine(sayac);\n    sayac += 3;\n}",
     "options": ["for (int sayac = 0; sayac < 15; sayac++)", "for (int sayac = 3; sayac <= 15; sayac += 3)", "for (int sayac = 3; sayac < 15; sayac *= 3)", "for (sayac <= 15; sayac = 3; sayac += 3)"], "answer": 1,
     "explain": "Başlangıç int sayac = 3; koşul sayac <= 15; değişim sayac += 3 → çıktı 3 6 9 12 15."},
    {"week": "cs-h2", "q": "Aşağıdaki kod neden beklendiği gibi durmaz?", "lang": "csharp",
     "code": "for (int i = 1; i <= 5; i--)\n{\n    Console.WriteLine(i);\n}",
     "options": ["i++ yerine i-- yazıldığı için i küçülür ve i <= 5 koşulu hep doğru kalır", "Koşulda <= yerine < olmalı", "Console.WriteLine yanlış", "i 1'den başlayamaz"], "answer": 0,
     "explain": "İpucu: koşulun bir gün yanlış olması gerekir. i: 1, 0, −1, −2 … hep ≤ 5 → sonsuz döngü (int taşana kadar)."},
    {"week": "cs-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "csharp",
     "code": "int toplam = 0;\nfor (int i = 1; i <= 10; i++)\n{\n    toplam += i;\n}\nConsole.WriteLine(toplam);",
     "options": ["45", "55", "10", "100"], "answer": 1,
     "explain": "1 + 2 + … + 10 = 55. Aynı problem while ile de 55 verir.",
     "run": cs_prog("int toplam = 0;\nfor (int i = 1; i <= 10; i++)\n{\n    toplam += i;\n}\nConsole.WriteLine(toplam);"), "expect": "55"},
    {"week": "cs-h2", "q": "Slayttaki 'Hangi durumda hangisini seçersin?' tablosuna göre 'Doğru parola girilene kadar sor' için hangi döngü uygundur?",
     "options": ["for", "while", "if", "switch"], "answer": 1,
     "explain": "Kaç tekrar olacağı baştan bilinmiyor → while. 1'den 100'e say / 20 kez yıldız → for."},
    {"week": "cs-h2", "q": "10'dan 1'e geri saymak için for döngüsü nasıl yazılmalıdır?",
     "options": ["for (int i = 10; i <= 1; i++)", "for (int i = 10; i >= 1; i--)", "for (int i = 1; i >= 10; i--)", "for (int i = 10; i > 1; i++)"], "answer": 1,
     "explain": "Başlangıç 10, koşul i >= 1, değişim i-- → 10 9 … 1.",
     "run": cs_prog('for (int i = 10; i >= 1; i--)\n{\n    Console.Write(i + " ");\n}\nConsole.WriteLine();'), "expect": "10 9 8 7 6 5 4 3 2 1"},
    {"week": "cs-h2", "q": "Kullanıcı 6 girerse aşağıdaki program ne yazar? (Ödev: 1'den N'ye çift sayıların toplamı)", "lang": "csharp", "stdin": "6",
     "code": "int n = int.Parse(Console.ReadLine());\nint toplam = 0;\nfor (int i = 2; i <= n; i += 2)\n{\n    toplam += i;\n}\nConsole.WriteLine(toplam);",
     "options": ["12", "21", "6", "30"], "answer": 0,
     "explain": "2 + 4 + 6 = 12.",
     "run": cs_prog("int n = int.Parse(Console.ReadLine());\nint toplam = 0;\nfor (int i = 2; i <= n; i += 2)\n{\n    toplam += i;\n}\nConsole.WriteLine(toplam);"), "expect": "12"},
    {"week": "cs-h3", "q": "C# veri türleri tablosuna göre `byte` tipinin boyutu ve aralığı nedir?",
     "options": ["1 bayt, −128 – 127", "1 bayt, 0 – 255", "2 bayt, 0 – 65.535", "4 bayt, 0 – 255"], "answer": 1,
     "explain": "byte işaretsiz 1 bayt: 0–255. sbyte işaretli: −128–127."},
    {"week": "cs-h3", "q": "Hangi veri tipi 16 bayt yer kaplar?",
     "options": ["double", "long", "decimal", "ulong"], "answer": 2,
     "explain": "decimal 16 bayt (±1,0×10⁻²⁸ – ±7,9×10²⁸). double, long ve ulong 8 bayttır."},
    {"week": "cs-h3", "q": "`ushort` tipinin aralığı hangisidir?",
     "options": ["−32.768 – 32.767", "0 – 65.535", "0 – 255", "0 – 4.294.967.295"], "answer": 1,
     "explain": "ushort: 2 bayt, işaretsiz → 0–65.535. short: −32.768–32.767. uint: 0–4.294.967.295."},
    {"week": "cs-h3", "q": "C#'ta `char` tipi kaç bayttır ve ne tutar?",
     "options": ["1 bayt – ASCII karakter", "2 bayt – bir Unicode karakter", "4 bayt – metin", "Değişken boyut – karakterlerin tümü"], "answer": 1,
     "explain": "Tabloya göre char 2 bayt, bir Unicode karakter. Karakterlerin tümü = string."},
    {"week": "cs-h3", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "csharp",
     "code": "Console.WriteLine(5 > 3 && 2 > 4);",
     "options": ["True", "False", "1", "Derleme hatası"], "answer": 1,
     "explain": "&& (And) için iki taraf da doğru olmalı: true && false → **False**.",
     "run": cs_prog("Console.WriteLine(5 > 3 && 2 > 4);"), "expect": "False"},
    {"week": "cs-h3", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "csharp",
     "code": "int a = 7;\nConsole.WriteLine(a != 7 || !(a < 5));",
     "options": ["True", "False", "7", "Derleme hatası"], "answer": 0,
     "explain": "a != 7 → false; a < 5 → false, !(false) → true; false || true → **True**.",
     "run": cs_prog("int a = 7;\nConsole.WriteLine(a != 7 || !(a < 5));"), "expect": "True"},
    {"week": "cs-h3", "q": "Aşağıdaki programda hangi satırda derleme hatası vardır?", "lang": "csharp",
     "code": "1  int sayi = 5\n2  Console.WriteLine(sayi);",
     "options": ["1. satır — ';' eksik", "2. satır — WriteLine yanlış yazılmış", "Hata yok", "1. satır — int küçük harfle yazılamaz"], "answer": 0,
     "explain": "1. satırın sonunda `;` yok. Visual Studio (Roslyn) bunu `CS1002: ; expected` olarak 1. satırda gösterir; mono/mcs ise hatayı "
                "bir sonraki satırda `CS1525: Unexpected symbol 'Console'` diye bildirir — Kod Lab'da deneyip gör. Hata satırının bir öncesine de bak!",
     "run": cs_prog("int sayi = 5\nConsole.WriteLine(sayi);"), "expect_error": True},
    {"week": "cs-h3", "q": "`int x = 3.5;` satırı derlenirken ne olur?",
     "options": ["x = 3 olur", "x = 4 olur", "Derleme hatası: double örtük olarak int'e dönüştürülemez (CS0266)", "x = 3.5 olur"], "answer": 2,
     "explain": "3.5 bir double sabitidir; C# veri kaybına yol açan örtük dönüşüme izin vermez → CS0266. Açık cast gerekir: (int)3.5.",
     "run": cs_prog("int x = 3.5;\nConsole.WriteLine(x);"), "expect_error": True},
    {"week": "cs-h3", "q": "operatorler.png'deki `!=` operatörünün anlamı hangisidir?",
     "options": ["Not", "Not Equal To (eşit değil)", "Greater Than or Equal To", "Or"], "answer": 1,
     "explain": "!= Not Equal To · ! Not · && And · || Or · >= Greater Than or Equal To."},
]
