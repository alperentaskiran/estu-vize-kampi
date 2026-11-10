"""İşletim Sistemleri ve Güvenliği — C ile Giriş (Hafta 1 & 2) + İşletim Sistemine Giriş ve Derleme Zinciri (Hafta 3) + Process (Hafta 4).

Kaynaklar: Hafta01_C_Giris.pdf, Hafta02_C_Giris_II.pdf, Hafta03_OS.pdf, Process.pdf, C_Programlamaya_Giris_Kapsamli.pdf (çalışma fasikülü),
output.pdf (Hafta 1–2 kapsamlı ders notu) (diyagram sayfaları görsel olarak okundu).
Kod soruları `run` alanında tam program ve `expect` alanında beklenen çıktıyla saklanır;
tests/verify_questions.py bunları gerçek derleyicide doğrular.
"""


def c_prog(body, includes=("stdio.h",)):
    """Bir main() gövdesini derlenebilir tam programa çevirir."""
    head = "".join(f"#include <{h}>\n" for h in includes)
    lines = "\n".join("    " + ln if ln else "" for ln in body.strip("\n").split("\n"))
    return f"{head}\nint main() {{\n{lines}\n    return 0;\n}}\n"


COURSE = {
    "id": "c",
    "name": "İşletim Sistemleri ve Güvenliği (C)",
    "short": "C",
    "icon": "⚙️",
    "color": "#f59e0b",
    "teacher": "",
    "sources": ["Hafta01_C_Giris.pdf", "Hafta02_C_Giris_II.pdf", "Hafta03_OS.pdf", "Process.pdf", "C_Programlamaya_Giris_Kapsamli.pdf", "output.pdf"],
    "weeks": [
        {
            "id": "c-h1",
            "title": "Hafta 1 — C Programlamaya Giriş I",
            "sources": ["Hafta01_C_Giris.pdf", "C_Programlamaya_Giris_Kapsamli.pdf", "output.pdf (Hafta 1–2 kapsamlı ders notu)"],
            "summary": """
#### 1. Bu ders neden C ile işleniyor?
İşletim sistemi; donanım (CPU, RAM, disk) ile kullanıcı uygulamaları arasındaki **köprüdür**. Linux çekirdeği, Windows kernel'i ve macOS'un büyük kısmı **C** ile yazılmıştır. Bunun üç nedeni vardır:

| Neden | Açıklama | Bu derse etkisi |
|---|---|---|
| **Düşük seviye bellek kontrolü** | C doğrudan bellek adresleriyle çalışır (`&`, `*`). | Process, stack, heap gibi OS kavramları "görünür" olur. |
| **POSIX API desteği** | OS'in ortak arayüzü C fonksiyonlarıdır: `fork()`, `pthread_create()`, `sem_wait()`. | İleriki haftalarda process/thread/semafor bu fonksiyonlarla yazılacak. |
| **Sistem seviyesi performans** | Python, Java gibi üst seviye diller de arka planda bu C çağrılarını kullanır. | C öğrenmek, tüm dillerin altındaki katmanı anlamaktır. |

> *Bu ders bir C programlama dersi değildir; C'yi işletim sistemini anlamak ve yönetmek için bir **araç** olarak kullanma dersidir.*

#### 2. Bir C programının anatomisi
```c
#include <stdio.h>      // 1) Ön işlemci direktifi: printf/scanf'in bildirimlerini koda ekler
                        //    (# ile başlayan satırlar derlemeden ÖNCE işlenir)
int main() {            // 2) Başlangıç noktası: OS programı çalıştırınca main'i çağırır
    printf("Merhaba\\n");  // 3) İfade (komut) — her ifade ';' ile biter
    return 0;           // 4) Çıkış durumu (exit status): 0 = "başarıyla bitti" bilgisi OS'e gider
}                       // 5) Blok kapanışı
```
**Neden-sonuç:** `#include <stdio.h>` yazılmazsa derleyici `printf`'in ne olduğunu bilmez → **`implicit declaration of function 'printf'`** uyarısı/hatası.
`return 0` kabuğa (bash) programın başarıyla bittiğini söyler; `echo $?` komutu bu değeri gösterir.

#### 3. printf, kaçış dizileri ve format belirteçleri
`printf` ilk argümandaki metni yazar; metindeki her **format belirteci** sıradaki argümanın **nasıl yorumlanacağını** söyler.

| Belirteç | Tip | Örnek | Çıktı |
|---|---|---|---|
| `%d` (veya `%i`) | `int` | `printf("%d", 42)` | `42` |
| `%ld` | `long` | `printf("%ld", fakt)` | `720` |
| `%f` | `float` / `double` (printf'te) | `printf("%f", 3.14)` | `3.140000` (varsayılan 6 basamak) |
| `%.2f` | ondalık, 2 basamak | `printf("%.2f", 3.14159)` | `3.14` |
| `%lf` | `double` (**scanf** ile okurken şart) | `scanf("%lf", &d)` | — |
| `%c` | `char` | `printf("%c", 'A')` | `A` |
| `%s` | string (`char[]`) | `printf("%s", "OS")` | `OS` |
| `%p` | adres (pointer) | `printf("%p", (void*)&x)` | `0x7ffc…` |
| `%%` | yüzde işaretinin kendisi | `printf("%%50")` | `%50` |

Kaçış dizileri: `\\n` yeni satır · `\\t` sekme · `\\\\` ters bölü · `\\"` çift tırnak · `\\0` null karakter.
**Tuzak:** `printf("%d\\n", 3.14);` → `%d` bir **int** bekler ama argüman **double**'dır; bellekteki bitler yanlış yorumlanır → **tanımsız davranış**, ekrana anlamsız bir sayı basılır (gcc `-Wall` ile `format '%d' expects argument of type 'int'` uyarısı verir). Derleyici sayıyı **otomatik çevirmez**.

#### 4. Değişkenler ve veri tipleri
Değişken, RAM'de değer saklayan **isimli bir kutudur**. C'de her değişkenin bir **tipi** vardır ve **kullanılmadan önce tanımlanmalıdır** (yoksa `undeclared identifier` hatası).

| Tip | Ne tutar? | Boyut (tipik, 64-bit Linux) | Belirteç | Örnek |
|---|---|---|---|---|
| `char` | tek karakter (aslında 1 baytlık sayı, ASCII) | 1 bayt | `%c` | `char harf = 'A';` (`'A'` = 65) |
| `int` | tam sayı | 4 bayt (≈ ±2,1 milyar) | `%d` | `int yas = 20;` |
| `long` | büyük tam sayı | 8 bayt | `%ld` | `long fakt = 1;` |
| `float` | ondalık (≈ 6-7 basamak hassasiyet) | 4 bayt | `%f` | `float boy = 1.75;` |
| `double` | ondalık (≈ 15-16 basamak, daha hassas) | 8 bayt | `%f` / scanf `%lf` | `double pi = 3.14159265;` |

```c
int sayi;            // tanımlama (declaration) — değeri henüz belirsiz (çöp değer!)
sayi = 10;           // atama (assignment)
int x = 5;           // tanımlama + ilk değer verme (initialization)
int a = 3, b = 4;    // aynı satırda birden fazla
int toplam = a + b;  // 7
```
**Dikkat:** `char` **tek** karakter tutar ve **tek tırnak** kullanır (`'A'`). Metin (string) için **`char[]` dizisi** ve **çift tırnak** gerekir (`"Ali"`) → 2. hafta.
Boyutlar `sizeof` ile öğrenilir: `sizeof(int)` → 4, `sizeof(char)` → 1 (C standardı `char`'ı her zaman 1 bayt tanımlar).

#### 5. Operatörler
**Aritmetik:** `+ - * / %`

| İfade | Sonuç | Neden? |
|---|---|---|
| `10 / 3` | **3** | **int / int → int**: ondalık kısım **atılır** (yuvarlanmaz, kesilir) |
| `10 / 3.0` | 3.333333 | Bir taraf ondalık olunca işlem ondalık yapılır |
| `(float)10 / 3` | 3.333333 | **Tür dönüşümü (type casting)** bölmeden ÖNCE yapılır |
| `(float)(10 / 3)` | 3.000000 | Bölme önce int olarak yapılır (3), sonra çevrilir → **yanlış!** |
| `10 % 3` | 1 | Mod = bölümden kalan (sadece tam sayılarda) |
| `15 % 4` | 3 | 15 = 4·3 + **3** |

**Klasik ortalama tuzağı:** `int a = 10, b = 3; float ort = (a + b) / 2;` → `13 / 2` int bölmesi = **6** → `ort` **6.0** olur (6.5 değil!). Doğrusu: `(a + b) / 2.0` veya `(float)(a + b) / 2`.

**Karşılaştırma:** `==  !=  <  >  <=  >=` → sonuç **1 (doğru)** veya **0 (yanlış)**'dır (`printf("%d", 3 == 3)` → `1`).
**`=` atama, `==` karşılaştırma!** `if (x = 5)` yazılırsa x'e 5 **atanır**, ifadenin değeri 5 (sıfırdan farklı = doğru) olur → koşul **her zaman doğru** sayılır ve x'in eski değeri kaybolur.

**Mantık:** `&&` VE (iki koşul da doğruysa) · `||` VEYA (en az biri doğruysa) · `!` DEĞİL.
Aralık kontrolü: `if (yas >= 18 && yas <= 65)` (18 ve 65 dahil). `||` ile yazılırsa (`yas >= 18 || yas <= 65`) **her sayı** koşulu sağlar → mantık hatası.
**`&` ≠ `&&`:** tek `&` **bitwise AND**'dir, bitleri tek tek karşılaştırır: `6 & 3` → `110 & 011 = 010` → **2**. (Ayrıca `&x` biçiminde "adresini al" anlamına gelir.)

#### 6. Kontrol yapıları
```c
if (not >= 90)       printf("AA\\n");
else if (not >= 80)  printf("BA\\n");   // buraya gelindiyse not < 90 demektir
else if (not >= 70)  printf("BB\\n");
else if (not >= 60)  printf("CC\\n");
else                 printf("FF\\n");
```
Koşullar **yukarıdan aşağı** denenir; **ilk doğru koşulun bloğu çalışır, zincirin kalanı atlanır**. Bu yüzden **en dar / en yüksek koşul en başa** yazılır.
Sıra ters olsaydı (`if (not >= 60)` en üstte) 95 alan öğrenci de "CC" alırdı.

**Mini alıştırma (x = 15):** `if (x > 10) printf("A");` ve ayrı bir `if (x > 20) printf("B"); else printf("C");` → iki **bağımsız** if vardır.
İlki "A" basar; ikincide 15 > 20 yanlış olduğu için else çalışır, "C" basar → çıktı **AC**. *(else her zaman kendisine en yakın if'e aittir.)*

#### 7. Döngüler
```
for ( başlangıç ;  koşul  ;  artış )
        ①            ②↺        ④↺        ① bir kez çalışır
      i = 1        i <= 5     i++        ② her turdan ÖNCE kontrol edilir (yanlışsa çıkılır)
                                         ③ gövde çalışır
                                         ④ her turdan SONRA çalışır, sonra tekrar ②
```
| Döngü | Koşul nerede kontrol edilir? | En az kaç kez çalışır? | Ne zaman kullanılır? |
|---|---|---|---|
| `for` | turun **başında** | 0 | Tekrar sayısı önceden belli (sayaçlı) |
| `while` | turun **başında** | 0 | Tekrar sayısı belirsiz, koşula bağlı |
| `do-while` | turun **sonunda** | **1** | Gövde en az bir kez çalışmalı (ör. menü) |

* `for (int i = 0; i < n; i++)` → **n tur** (0 … n−1) · `for (int i = 1; i <= n; i++)` → **n tur** (1 … n) · `for (int i = 0; i <= n; i++)` → **n+1 tur**.
* **İç içe döngü:** dış döngünün **her bir** turu için iç döngü baştan sona döner → toplam = dış × iç (3 × 4 = **12** kez).
* `while` içinde sayaç güncellenmezse (`i++` unutulursa) koşul hep doğru kalır → **sonsuz döngü**.
* `do { printf("%d\\n", i); i++; } while (i <= 5);` (i = 10) → koşul yanlış olsa da gövde bir kez çalışır → **10** basılır.
* **`break`** döngüyü **tamamen** bitirir: `if (i == 5) break;` → `1 2 3 4` · **`continue`** sadece **o turu atlar**: `if (i == 3) continue;` → `1 2 4 5`.

#### 8. Fonksiyonlar, prototip ve kapsam
```c
int kare(int x);              // PROTOTİP: dönüş tipi + ad + parametreler (gövde yok, ';' ile biter)

int main() {
    printf("%d\\n", kare(4));  // 16 — derleyici kare'yi prototipten tanıyor
    return 0;
}

int kare(int x) {             // TANIM (gövde)
    return x * x;
}
```
* Fonksiyon: belirli bir işi yapan, **bir kez yazılıp defalarca çağrılan** blok. Parametre alır, `return` ile değer döndürür; **`void`** fonksiyon değer döndürmez.
* **Neden prototip?** C derleyicisi dosyayı **yukarıdan aşağı** okur. `main` içinde, henüz görmediği bir fonksiyon çağrılırsa ne döndürdüğünü bilemez → uyarı/hata. Prototip, fonksiyonun **imzasını** önceden bildirir.
* **Kapsam (scope):** **global** değişken tüm fonksiyonların dışında tanımlanır, her yerden erişilir · **yerel (local)** değişken yalnızca tanımlandığı `{ }` bloğunda yaşar; blok bitince yok olur.

#### 9. scanf: neden `&`?
```c
int yas;
scanf("%d", &yas);   // "klavyeden okunan sayıyı yas'ın ADRESİNE yaz"
```
C'de fonksiyonlara değişkenin **kopyası** gider (2. haftada "değer ile aktarım"). scanf'in değeri **asıl değişkene** yazabilmesi için değişkenin **bellek adresini** (`&yas`) alması gerekir.
`scanf("%d", yas);` yazılırsa scanf, yas'ın içindeki **çöp değeri adres sanıp** oraya yazmaya çalışır → genellikle **Segmentation fault**.

#### 10. GCC ile derleme ve hata okuma
```bash
nano merhaba.c                     # kodu yaz (Ctrl+O kaydet, Ctrl+X çık)
gcc merhaba.c -o merhaba           # derle; -o çıktı dosyasının adı
gcc merhaba.c                      # -o yoksa çıktı: a.out
gcc -Wall merhaba.c -o merhaba     # Warnings ALL: şüpheli durumları raporla
gcc -g merhaba.c -o merhaba        # hata ayıklayıcı (gdb) bilgisi ekle
./merhaba                          # ./ = "bulunduğum dizindeki" dosyayı çalıştır
```
Aşamalar (3. haftada ayrıntılı): **Ön işleme → Derleme → Assembly → Bağlama**.

**Hata mesajı okuma:** `merhaba.c:3:22: error: expected ';' before '}' token` → **dosya** merhaba.c · **satır 3** · **sütun 22** · sorun: noktalı virgül eksik.
Derleyici eksikliği genellikle **bir sonraki** token'da fark eder; bu yüzden hatayı **gösterilen satırda veya bir üstünde** ara. **İlk hatayı düzelt, tekrar derle** — tek bir eksik `;` onlarca zincirleme hataya yol açabilir.

| Hata / uyarı | Anlamı | Çözüm |
|---|---|---|
| `expected ';' before …` | Noktalı virgül eksik | Gösterilen satırın veya bir üstünün sonuna `;` |
| `'x' undeclared` | Değişken tanımlanmamış | Kullanmadan önce `int x;` |
| `implicit declaration of function 'printf'` | Başlık dosyası eksik | `#include <stdio.h>` |
| `format '%d' expects argument of type 'int'` | Belirteç ile tip uyuşmuyor | Doğru belirteci kullan (`%f`, `%ld` …) |

#### 11. Yorumlar ve kodlama stili
`// tek satır` · `/* çok satırlı */` — yorumlar **ön işleme aşamasında silinir**, derleyici görmez. Anlamlı isimler (`x` yerine `yas`), tutarlı girinti (4 boşluk) ve boşluk kullanımı okunabilirliği artırır.

#### ⚠️ Sınav Tuzakları & Dikkat Edilecekler
| Tuzak | Hatalı | Doğru / sonuç |
|---|---|---|
| Atama ile karşılaştırma | `if (x = 5)` → her zaman doğru | `if (x == 5)` |
| int bölmesi | `float c = 5 / 2;` → **2.0** | `5 / 2.0` veya `(float)5 / 2` → 2.5 |
| Cast'in yeri | `(float)(a + b) / 2` doğru, `(float)((a + b) / 2)` yanlış | Önce çevir, sonra böl |
| scanf'te `&` | `scanf("%d", yas);` → çökme | `scanf("%d", &yas);` |
| Sonsuz döngü | `while (i <= 5) { printf(…); }` | Gövdede `i++` |
| Tur sayısı | `i <= n` ile `i < n` farkı | 0'dan başlayıp `<= n` → n+1 tur |
| do-while | "koşul yanlışsa hiç çalışmaz" sanmak | En az **1** kez çalışır |
| Yanlış belirteç | `printf("%d", 3.14)` | Tanımsız davranış; `%f` kullan |
| Taşma | `int` ile 13! hesaplamak | 13! > 2,1 milyar → `long` + `%ld` |
| `-o` yok | — | Çıktı `a.out` olur |
| `./` yok | `merhaba` → command not found | `./merhaba` |
""",
            "concepts": [
                ('%d / %f / %c / %s / %p', "int / ondalık / karakter / string / adres format belirteçleri; %ld long, scanf'te double için %lf."),
                ('int / int', 'Sonuç tam sayıdır, ondalık kısım kesilir: 10/3 = 3. Ondalık için 10/3.0 veya (float)10/3.'),
                ('Tür dönüşümü (cast)', '(float)a / b — değeri işlemden önce geçici olarak başka tipe çevirir.'),
                ('= ve ==', '= atama yapar, == karşılaştırır (sonuç 1/0). if (x = 5) her zaman doğrudur.'),
                ('&& ve &', '&& mantıksal VE; & bitwise AND (6 & 3 = 2) ya da adres operatörü.'),
                ('else if zinciri', 'İlk doğru koşul çalışır, kalanı atlanır; en dar koşul en başa.'),
                ('do-while', 'Koşul sonda kontrol edilir; gövde en az bir kez çalışır.'),
                ('break / continue', 'break döngüyü bitirir; continue yalnızca o turu atlar.'),
                ('Prototip', "int kare(int x); — fonksiyonun imzası main'den önce derleyiciye bildirilir."),
                ('Kapsam (scope)', 'Global her yerden erişilir; yerel yalnızca tanımlandığı { } bloğunda yaşar.'),
                ('&değişken', 'Değişkenin bellek adresi; scanf değeri bu adrese yazar.'),
                ('-Wall / -g / -o', 'Tüm uyarılar / hata ayıklama bilgisi / çıktı dosyasının adı (yoksa a.out).'),
            ],
            "must": [
                'Format belirteçleri: %d int, %ld long, %f float/double, %c char, %s string, %p adres',
                'printf("%d", 3.14) → tanımsız davranış (otomatik çevrilmez)',
                'int / int → int: 10/3 = 3, 10 % 3 = 1, 15 % 4 = 3; (float)a/b ile ondalık',
                '(a + b) / 2 tuzağı: 13/2 = 6 → 6.0; doğrusu (a + b) / 2.0',
                '= atama, == karşılaştırma; if (x = 5) her zaman doğru',
                'Aralık: yas >= 18 && yas <= 65 (|| ile yazmak mantık hatası)',
                'Mini alıştırma x = 15 → AC',
                'for/while başta kontrol (0 tur olabilir), do-while sonda (en az 1 tur)',
                'break → 1 2 3 4 · continue → 1 2 4 5 · iç içe 3×4 = 12',
                "Prototip main'den önce; global/yerel kapsam",
                'scanf("%d", &yas) — & adres verir',
                'gcc -o (yoksa a.out), -Wall uyarılar, -g gdb; ./program ile çalıştır',
                'Hata mesajı dosya:satır:sütun; ilk hatayı düzelt, implicit declaration → #include eksik',
            ],
            "cheat": [
                {"title": 'Format belirteçleri', "columns": ['Belirteç', 'Tip', 'Örnek'], "rows": [
                    ['%d / %i', 'int', 'printf("%d", 42)'],
                    ['%ld', 'long', 'printf("%ld", fakt)'],
                    ['%f / %.2f', 'float / double', 'printf("%.2f", 3.14159) → 3.14'],
                    ['%lf', 'double (scanf)', 'scanf("%lf", &d)'],
                    ['%c', 'char', 'printf("%c", \'A\')'],
                    ['%s', 'string (char[])', 'printf("%s", "OS")'],
                    ['%p', 'adres', 'printf("%p", (void*)&x)'],
                    ['%%', '% karakteri', 'printf("%%")'],
                ]},
                {"title": 'Veri tipleri', "columns": ['Tip', 'Boyut', 'Belirteç', 'Not'], "rows": [
                    ['char', '1 bayt', '%c', 'Tek karakter, tek tırnak'],
                    ['int', '4 bayt', '%d', '≈ ±2,1 milyar'],
                    ['long', '8 bayt', '%ld', '13! ve üzeri'],
                    ['float', '4 bayt', '%f', '≈ 6-7 basamak'],
                    ['double', '8 bayt', '%f (scanf: %lf)', '≈ 15-16 basamak'],
                ]},
                {"title": 'Bölme ve tür dönüşümü', "columns": ['İfade', 'Sonuç'], "rows": [
                    ['10 / 3', '3'],
                    ['10 / 3.0', '3.333333'],
                    ['(float)10 / 3', '3.333333'],
                    ['(float)(10 / 3)', '3.000000'],
                    ['10 % 3', '1'],
                    ['(10 + 3) / 2', '6'],
                    ['(10 + 3) / 2.0', '6.5'],
                ]},
                {"title": 'Döngü karşılaştırması', "columns": ['Döngü', 'Kontrol', 'En az', 'Kullanım'], "rows": [
                    ['for', 'Başta', '0', 'Tekrar sayısı belli'],
                    ['while', 'Başta', '0', 'Koşula bağlı'],
                    ['do-while', 'Sonda', '1', 'En az bir kez çalışmalı'],
                ]},
                {"title": 'GCC', "columns": ['Komut', 'Anlam'], "rows": [
                    ['gcc a.c -o a', 'Derle, çıktı adı a'],
                    ['gcc a.c', 'Çıktı a.out'],
                    ['gcc -Wall a.c -o a', 'Tüm uyarılar'],
                    ['gcc -g a.c -o a', 'Hata ayıklama (gdb) bilgisi'],
                    ['./a', 'Çalıştır'],
                    ['echo $?', 'Son programın return değeri'],
                ]},
                {"title": 'Derleme hataları', "columns": ['Mesaj', 'Çözüm'], "rows": [
                    ["expected ';' before …", 'Satır sonuna ;'],
                    ["'x' undeclared", 'Değişkeni tanımla'],
                    ["implicit declaration of 'printf'", '#include <stdio.h>'],
                    ["format '%d' expects 'int'", 'Doğru belirteç'],
                ]},
            ],
            "images": [("c_program_yapisi.jpg", "Bir C programının yapısı (Hafta01 s.4)"), ("c_for_anatomi.jpg", "for döngüsünün üç parçası (s.18)"),
                       ("c_derleme_asamalari.jpg", "Kaynak koddan çalıştırılabilir dosyaya: ön işleme → derleme → assembly → bağlama (s.30)"),
                       ("c_if_else_akisi.jpg", "if / else karar akışı (Hafta01 s.14)"), ("c_dongu_secimi.jpg", "Döngü tipi seçimi: for / while / do-while (s.23)")],
            "templates": ["c_merhaba", "c_printf", "c_operatorler", "c_mini_alistirma", "c_harf_notu", "c_for", "c_ic_ice_for", "c_while",
                          "c_do_while", "c_break_continue", "c_fonksiyon", "c_prototip", "c_scope", "c_toplam_n", "c_faktoriyel", "c_hatali_noktali_virgul",
                          "c_tur_donusumu", "c_atama_tuzagi"],
        },
        {
            "id": "c-h2",
            "title": "Hafta 2 — C Programlamaya Giriş II (Dizi, String, Pointer, struct, getpid)",
            "sources": ["Hafta02_C_Giris_II.pdf", "output.pdf (Hafta 1–2 kapsamlı ders notu)"],
            "summary": """
#### 1. Diziler (arrays): bellekte yan yana duran kutular
Dizi, **aynı tipteki** birden çok değeri bellekte **ardışık (contiguous)** olarak tutar. İndeks **0'dan** başlar, boyut tanımlanırken **sabittir**.
```c
int a[5];                    // 5 eleman, değer atanmamış (yerel dizide ÇÖP değerler)
int b[5] = {1, 2, 3, 4, 5};  // hepsi atanmış
int c[5] = {1, 2};           // c[2], c[3], c[4] → 0 (eksik kalanlar sıfırlanır)
int d[] = {10, 20, 30};      // boyutu derleyici sayar → 3
```
`int sayilar[5] = {10, 20, 30, 40, 50};` bellekte şöyle durur (int = 4 bayt, başlangıç adresi örnek: 1000):
```
 indeks :   [0]     [1]     [2]     [3]     [4]   |  [5] ← DİZİNİN DIŞI!
 değer  :   10      20      30      40      50    |  ??   (başka bir değişkenin alanı)
 adres  :  1000    1004    1008    1012    1016   |  1020
            ↑
     sayilar (dizinin adı) = &sayilar[0] = 1000
```
* `i`. elemanın adresi = **başlangıç + i × sizeof(tip)** → bu yüzden indeksleme çok hızlıdır.
* Tüm elemanları gezmek: `for (int i = 0; i < 5; i++)` — **`i < 5`**, `i <= 5` değil!
* Ortalama: `toplam / 5.0` (int/int'ten kaçınmak için) ve `%.2f` → `150 / 5.0 = 30.00`.
* **C sınır kontrolü YAPMAZ:** `a[5] = 99;` derlenir, çoğu zaman uyarı bile vermez; ama 1020 adresindeki **başka bir veriyi ezer** → **tanımsız davranış (undefined behavior)**: program çökebilir, yanlış sonuç verebilir ya da "çalışıyor gibi" görünebilir.
* Eleman sayısı: `sizeof(dizi) / sizeof(dizi[0])` → `20 / 4 = 5` (yalnızca dizinin tanımlandığı yerde çalışır).

#### 2. String = char dizisi + `'\\0'`
C'de ayrı bir **string tipi yoktur**. String, sonunda **`'\\0'` (null terminator, ASCII 0)** bulunan bir `char` dizisidir. `printf("%s")`, `strlen` gibi fonksiyonlar **`'\\0'` görene kadar** okumaya devam eder; `'\\0'` yoksa nerede duracaklarını bilemezler.
```c
char isim[] = "Ali";          // derleyici '\\0' ekler → 4 bayt
```
```
 indeks :  [0]   [1]   [2]   [3]
 içerik :  'A'   'l'   'i'   '\\0'
            ↑ isim[0] → printf("%c", isim[0]) = A
```
| İfade | Değer | Neden? |
|---|---|---|
| `strlen("Ali")` | **3** | `'\\0'` **sayılmaz** |
| `sizeof(isim)` (`char isim[] = "Ali"`) | **4** | Dizinin bellekte kapladığı bayt, `'\\0'` **dahil** |
| `char sehir[20] = "Ankara"; sizeof(sehir)` | **20** | Dizinin boyutu (kullanılan kısım değil) |
| `strlen(sehir)` | **6** | Sadece "Ankara" |
| `strlen("Merhaba")` | **7** | 7 harf |

**string.h fonksiyonları:**
* **`strlen(s)`** → uzunluk (`'\\0'` hariç). Dönüş tipi `size_t`; `%zu` ile (ya da `(int)` cast ile `%d`) yazdırılır.
* **`strcpy(hedef, kaynak)`** → kaynağı `'\\0'` dahil hedefe kopyalar. **Hedef yeterince büyük olmalı**, yoksa taşar.
* **`strcmp(a, b)`** → **0 = eşit**; negatif: a sözlükte önce, pozitif: a sonra (`strcmp("abc", "abd") < 0`). `if (a == b)` iki **adresi** karşılaştırır, içeriği değil → string karşılaştırmada **strcmp** kullan.
* Bir diziye **`=` ile metin atanamaz**: `isim = "Veli";` **derleme hatası** → `strcpy(isim, "Veli");`. (İlk tanımda `char isim[] = "Ali";` serbesttir; bu atama değil **ilk değer verme**dir.)
* Kapasite: `char s[5] = "Merhaba";` → 7 harf + `'\\0'` = **8 bayt** gerekir, 5'e sığmaz · `char s[4] = "Test";` → 4 harf + `'\\0'` = 5 bayt gerekir → `'\\0'` için yer kalmaz, string bozulur.

#### 3. Pointer: adres tutan değişken
Normal değişken bir **değer** tutar; pointer bir değerin **bellekteki adresini** tutar.
```c
int x = 42;
int *p = &x;     // p, "int işaret eden pointer"; içinde x'in ADRESİ var
```
```
   değişken      adres       içerik
   ┌──────┐
   │  x   │      0x1000      42        ← x'in kendisi
   └──────┘
   ┌──────┐
   │  p   │      0x2000      0x1000    ← p'nin içinde x'in adresi var
   └──────┘                    │
                               └────────► 0x1000 adresindeki değer = *p = 42
```
| İfade | Anlamı | Örnek değer |
|---|---|---|
| `x` | x'in değeri | 42 |
| `&x` | x'in **adresi** ("adresini al") | 0x1000 |
| `p` | p'nin içindeki değer = x'in adresi | 0x1000 |
| `*p` | p'nin **gösterdiği adresteki değer** (dereference) | 42 |
| `&p` | p'nin kendi adresi | 0x2000 |
| `*p = 100;` | 0x1000'e 100 yaz → **x de 100 olur** | x = 100 |

* `*` **iki farklı yerde** kullanılır: tanımda (`int *p`) "p bir pointer'dır" demektir; ifadede (`*p`) "p'nin gösterdiği yerdeki değer" demektir.
* Adres yazdırma: `printf("%p", (void*)&x);` → adresler her çalıştırmada değişebilir.
* Neden önemli? `dizi[i] ≡ *(dizi+i)` · parametre aktarımı · OS API'leri pointer alır (`fork`, `pthread_create`) · `malloc()` pointer döndürür · string'ler `char*`.

**Pointer aritmetiği:** pointer'a 1 eklemek adresi **1 bayt değil, 1 eleman** (sizeof(tip) kadar) ilerletir.
```c
int a[5] = {10, 20, 30, 40, 50};
int *p = a;              // p → a[0]   (a tek başına &a[0] gibidir)
```
| İfade | Adres (a = 1000) | Değer |
|---|---|---|
| `p` | 1000 | — |
| `*p` | 1000 | 10 |
| `p + 1` | **1004** (int 4 bayt) | — |
| `*(p + 1)` | 1004 | 20 |
| `*(a + 2)` ≡ `a[2]` | 1008 | 30 |
| `*p + 1` | — | **11** (önce `*p`=10, sonra +1) |
| `p++` sonrası `*p` | 1004 | 20 |
| `(p + 2) - p` | — | **2** (iki pointer farkı eleman sayısıdır) |

`char *` pointer'da `+1` 1 bayt, `int *`'da 4 bayt, `double *`'da 8 bayt ilerler.

#### 4. Fonksiyonlara parametre aktarımı
C **varsayılan olarak değeri KOPYALAR** (pass by value).
```
DEĞER İLE: arttir(a)                       ADRES İLE: arttir(&a)
main:  a = 10  ──kopya──►  x = 10          main:  a = 10 (adres 0x1000)
                           x = 11                      ▲
main:  a = 10  (DEĞİŞMEDİ)                 fonksiyon: x = 0x1000 → *x = *x + 1
                                           main:  a = 11  (DEĞİŞTİ)
```
| Özellik | Değer ile (`void f(int x)`) | Adres ile (`void f(int *x)`) |
|---|---|---|
| Fonksiyona giden | Değişkenin **kopyası** | Değişkenin **adresi** (`&a`) |
| Parametre | Normal değişken | Pointer |
| Orijinale etkisi | **Etkilemez** (içeride 11, dışarıda 10) | **Doğrudan değiştirir** (11) |
| Kullanım | Hesaplama, sadece okuma | `swap()`, `scanf()`, birden çok sonuç döndürme |

**swap:** `void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }` → `swap(&x, &y);` ile x=3, y=7 → **x=7 y=3**. Pointersız (`swap(int a, int b)`) yazılsaydı sadece kopyalar yer değiştirir, x ve y aynı kalırdı.
*scanf'te `&` kullanmamızın nedeni budur: scanf değeri değişkenin adresine yazar.*

#### 5. struct: kendi veri tipini tanımlamak
`struct`, **farklı tipteki** verileri tek çatı altında toplar.
```c
struct Ogrenci {
    int   no;        // 4 bayt
    char  ad[20];    // 20 bayt
    float ort;       // 4 bayt
};                   // ← noktalı virgül şart!

struct Ogrenci o1;
o1.no = 12345;
strcpy(o1.ad, "Ali");    // o1.ad = "Ali";  → DERLEME HATASI (dizi atanamaz)
o1.ort = 3.45;
struct Ogrenci o2 = {12345, "Ali", 3.45};   // tanımda ilk değer vermek serbest
```
| Erişim | Ne zaman? | Örnek |
|---|---|---|
| `.` (nokta) | Elimizde struct **değişkeninin kendisi** varsa | `o1.no` |
| `->` (ok) | Elimizde struct'ın **adresi (pointer)** varsa | `p->no` |
| `(*p).no` | `->`'nun açık yazımı (parantez **şart**: `*p.no` yanlış okunur) | `(*p).no` |

* `struct Ogrenci sinif[3];` → struct dizisi: `sinif[0].no = 101; strcpy(sinif[1].ad, "Ayşe");`
* `p.no` (p pointer iken) **hatalıdır** → `p->no`.
* **OS'te her şey struct'tır:** **PCB (Process Control Block)** process bilgileri, thread yapıları, dosya tanımlayıcıları, ağ paketleri.

#### 6. İşletim sistemiyle ilk bağlantı: process ve getpid()
**Program ≠ Process:** program diskte duran çalıştırılabilir **dosyadır**; process o programın **çalışan** hâlidir. Aynı program iki kez çalıştırılırsa **iki ayrı process** (iki farklı PID) oluşur.
* **PID** (Process ID): OS'in her process'e verdiği **benzersiz** numara. **PID 1 = init / systemd**; küçük PID'ler (1–1000) genelde sistem, kullanıcı process'leri 1000+.
* Her process'in bir **parent**'ı vardır: terminalden çalıştırılan programın parent'ı genellikle **bash**'tir.
```c
#include <stdio.h>
#include <unistd.h>      // getpid, getppid, sleep — POSIX başlığı
#include <sys/types.h>   // pid_t

int main() {
    pid_t pid = getpid();     // bu process'in PID'i
    pid_t ppid = getppid();   // parent'ın (çoğunlukla bash) PID'i
    printf("PID: %d  Parent PID: %d\\n", (int)pid, (int)ppid);
    return 0;
}
```
* **`pid_t`**: POSIX'in PID tipi; Linux'ta `int` gibidir → `%d`; taşınabilirlik için `(int)` cast daha güvenli.
* `sleep(1)` → 1 saniye bekle (unistd.h). Bekleme sırasında başka terminalde `ps -ef | grep pid` ile process görülebilir.
* **`/proc/<PID>/`**: çalışan process'in bilgileri → `status`, `cmdline`, `fd/` (açık dosyalar), `maps` (bellek haritası).

**`./pid` yazınca ne olur?** 1) bash komutu okur → 2) dosyayı diskte bulur → 3) OS yeni process yaratır (**fork + exec**) → 4) bellek ayrılır, kod yüklenir → 5) `main()` başlar → 6) printf çıktısı terminale gider → 7) `return 0` → process biter → 8) bash yeniden komut bekler.

**Bir process'in bellek haritası** (yüksek adresten düşüğe):
```
 yüksek adres ┌──────────────────────────┐
              │ Stack  ↓  yerel değişken, │  fonksiyon çağrıları, dönüş adresleri
              │          fonksiyon param. │
              ├──────────────────────────┤
              │        (boş alan)         │
              ├──────────────────────────┤
              │ Heap   ↑  malloc()        │  dinamik bellek
              ├──────────────────────────┤
              │ Veri: .data / .bss        │  global ve static değişkenler
              ├──────────────────────────┤
 düşük adres  │ Kod: .text                │  makine kodu (main, fonksiyonlar)
              └──────────────────────────┘
```

#### 7. Güvenlik: buffer overflow
C dizi sınırlarını kontrol etmediği için bir arabelleğe (buffer) **kapasitesinden fazla veri** yazılabilir. Stack'teki bir dizi taşarsa yanındaki değişkenler ve hatta **fonksiyonun dönüş adresi (return address)** ezilir. Saldırgan bu adrese kendi kodunun adresini yazarak **programın akışını ele geçirebilir** → OS güvenliğindeki en klasik zafiyet. `strcpy` ve sınır kontrolsüz `scanf("%s")` bu yüzden risklidir.

#### ⚠️ Sınav Tuzakları & Dikkat Edilecekler
| Tuzak | Hatalı | Neden / doğru |
|---|---|---|
| Sınır aşımı | `int a[5]; a[5] = 99;` | Son indeks 4; C kontrol etmez → tanımsız davranış |
| Döngü sınırı | `for (i = 0; i <= 5; i++) a[i]` | 6. tur dizi dışı → `i < 5` |
| Kısmi ilk değer | "`int c[5] = {1,2}` kalanı çöp" sanmak | Kalanlar **0** |
| `sizeof` vs `strlen` | `"Ali"` için ikisini aynı sanmak | sizeof 4 (`'\\0'` dahil), strlen 3 |
| Kapasite | `char s[4] = "Test";` | `'\\0'` için 5 bayt gerekir |
| Diziye atama | `o.ad = "Ali";` / `isim = "Veli";` | `strcpy(o.ad, "Ali");` |
| String karşılaştırma | `if (s1 == s2)` | Adresleri karşılaştırır → `strcmp(s1, s2) == 0` |
| Başlatılmamış pointer | `int *p; *p = 5;` | Rastgele adrese yazar → Segmentation fault; `int *p = &x;` |
| `*p + 1` vs `*(p + 1)` | — | Değer+1 (11) ile sonraki eleman (20) farklıdır |
| Pointer aritmetiği | `p + 1` = adres+1 sanmak | adres + **sizeof(tip)** |
| struct pointer | `p.no` | `p->no` veya `(*p).no` |
| Değer ile aktarım | `void arttir(int x)` ile a'yı değiştirmeyi beklemek | Kopya değişir; `int *x` + `arttir(&a)` |
| unistd.h | getpid/sleep'i başlıksız kullanmak | `#include <unistd.h>` |
""",
            "concepts": [
                ('Dizi', "Aynı tipte elemanlar bellekte ardışık; indeks 0'dan, boyut sabit; C sınır kontrolü yapmaz."),
                ("'\\0'", 'String sonlandırıcı (null terminator); "Ali" bellekte 4 bayt.'),
                ('sizeof / strlen', "sizeof: bellekte kaplanan bayt ('\\0' dahil); strlen: karakter sayısı ('\\0' hariç)."),
                ('strcpy / strcmp', 'Kopyalama (diziye = ile metin atanamaz) / karşılaştırma (eşitse 0).'),
                ('&x', "x'in bellek adresi (adresini al operatörü)."),
                ('*p', "p'nin gösterdiği adresteki değer (dereference); *p = 100 → x de değişir."),
                ('Pointer aritmetiği', 'p + 1 adresi sizeof(tip) kadar ilerletir; dizi[i] ≡ *(dizi + i).'),
                ('Değer / adres ile aktarım', 'Kopya gider, orijinal değişmez / adres gider, orijinal değişir (swap, scanf).'),
                ('->', 'Pointer üzerinden struct alanına erişim: p->no ≡ (*p).no.'),
                ('PID / PPID', "Process'in benzersiz numarası / parent'ının numarası; getpid(), getppid() — unistd.h."),
                ('pid_t', "POSIX PID tipi; Linux'ta int gibi, (int) cast ile %d."),
                ('Buffer overflow', 'Sınır dışına yazılan veri komşu alanları ve dönüş adresini ezer; klasik güvenlik zafiyeti.'),
            ],
            "must": [
                'int c[5] = {1,2} → kalanlar 0; int d[] = {10,20,30} → boyut 3',
                'C sınır kontrolü yapmaz: a[5] → undefined behavior / buffer overflow',
                '"Ali" 4 bayt; strlen 3, sizeof 4; char s[5] = "Merhaba" sığmaz (8 bayt)',
                'strcpy ile kopyala, strcmp eşitse 0; dizilere = ile metin atanamaz',
                '&x adres, *p adresteki değer; *p = 100 → x = 100',
                "dizi[i] ≡ *(dizi + i); a ≡ &a[0]; p + 1 → bir sonraki eleman (int'te +4 bayt)",
                '*p + 1 (değer + 1) ≠ *(p + 1) (sonraki eleman)',
                'Değer ile: içeride 11, dışarıda 10 · adres ile: 11 · swap → x=7 y=3',
                'struct: nokta (o1.no) / ok (p->no ≡ (*p).no)',
                'int *p; *p = 5 → başlatılmamış pointer (segfault)',
                'Program ≠ Process; PID 1 = init/systemd; getpid/getppid → unistd.h',
                'Bellek haritası: Stack (yerel) · Heap (malloc) · Veri (.data/.bss) · Kod (.text)',
            ],
            "cheat": [
                {"title": 'Pointer hızlı tablo', "columns": ['İfade', 'Anlam'], "rows": [
                    ['int *p = &x;', "p, x'in adresini tutar"],
                    ['*p', 'Adresteki değer'],
                    ['*p = 10;', "x'i 10 yapar"],
                    ['&p', "p'nin kendi adresi"],
                    ['p + 1', 'Bir sonraki elemanın adresi (+sizeof)'],
                    ['a[i] ≡ *(a+i)', 'Dizi erişimi'],
                    ['*p + 1', 'Değer + 1'],
                    ['p->alan ≡ (*p).alan', 'struct pointer erişimi'],
                ]},
                {"title": 'string.h ve boyutlar', "columns": ['İfade', 'Sonuç', 'Not'], "rows": [
                    ['strlen("Merhaba")', '7', "'\\0' hariç"],
                    ['sizeof("Ali") / char s[] = "Ali"', '4', "'\\0' dahil"],
                    ['char t[20] = "Ankara"; sizeof(t)', '20', 'Dizinin tamamı'],
                    ['strcpy(d, s)', 'Kopyala', 'Hedef yeterince büyük olmalı'],
                    ['strcmp(a, b)', '0 → eşit', '<0 önce, >0 sonra'],
                ]},
                {"title": 'Parametre aktarımı', "columns": ['Özellik', 'Değer ile', 'Adres ile'], "rows": [
                    ['Giden', 'Kopya', 'Adres (&a)'],
                    ['Parametre', 'int x', 'int *x'],
                    ['Orijinal', 'Değişmez', 'Değişir'],
                    ['Örnek', 'kare(x)', 'swap, scanf'],
                ]},
                {"title": 'struct erişimi', "columns": ['Operatör', 'Ne zaman?', 'Örnek'], "rows": [
                    ['.', 'struct değişkeni', 'o1.no'],
                    ['->', 'struct pointer', 'p->no'],
                    ['(*p).', '-> ile aynı', '(*p).no'],
                ]},
                {"title": 'Process bellek haritası', "columns": ['Bölge', 'İçerik'], "rows": [
                    ['Stack', 'Yerel değişkenler, fonksiyon çağrıları, dönüş adresi'],
                    ['Heap', 'malloc ile ayrılan dinamik bellek'],
                    ['Veri (.data / .bss)', 'Başlatılmış / başlatılmamış global ve static'],
                    ['Kod (.text)', 'Makine kodu'],
                ]},
                {"title": 'Process komutları', "columns": ['Komut / fonksiyon', 'İş'], "rows": [
                    ['getpid()', 'Kendi PID'],
                    ['getppid()', 'Parent PID'],
                    ['sleep(n)', 'n saniye bekle'],
                    ['ps -ef', "Tüm process'ler"],
                    ['cat /proc/<PID>/status', 'Process durumu'],
                    ['ls /proc/<PID>/fd', 'Açık dosyalar'],
                ]},
            ],
            "images": [("c_pointer_mantigi.jpg", "Pointer = adres tutan değişken (Hafta02 s.12)"), ("c_ampersand_yildiz.jpg", "& ve * işlemleri özeti (s.15)"),
                       ("c_parametre_aktarimi.jpg", "Değer ile (kopya) ve adres ile (pointer) aktarım (s.18)"), ("c_bellek_haritasi.jpg", "Bir process'in bellek haritası (s.34)")],
            "templates": ["c_dizi", "c_dizi_tuzak", "c_string", "c_pointer", "c_dizi_pointer", "c_deger_aktarim", "c_adres_aktarim", "c_swap",
                          "c_struct", "c_struct_dizi", "c_struct_pointer", "c_getpid", "c_process_sleep", "c_kod_okuma",
                          "c_sizeof_strlen", "c_pointer_aritmetigi"],
        },
        {
            "id": "c-h3",
            "title": "Hafta 3 — İşletim Sistemine Giriş + Derleme Zinciri (Kernel, User/Kernel Mode, System Call, gcc -E/-S/-c)",
            "sources": ["Hafta03_OS.pdf"],
            "summary": """
### Bölüm A — İşletim Sistemine Giriş

#### 1. İşletim sistemi nedir, ne yapar?
İşletim sistemi (OS), **donanım ile uygulama arasındaki aracıdır**. Uygulamalar diske, ekrana, ağa doğrudan değil, **OS üzerinden** ulaşır.
* **Kaynakları yönetir:** CPU, bellek, disk, ağ.
* **Hizmet verir:** process oluşturma, dosya açma, ağ bağlantısı.
* **Güvenlik ve izolasyon sağlar:** process'ler birbirinin belleğine karışmaz.
* **Arayüz sunar:** kabuk (bash) veya grafik arayüz (GUI).

| Görev | Ne yapar? | Örnek |
|---|---|---|
| Process yönetimi | Oluşturma, sonlandırma, senkronizasyon | `fork()`, `exit()` |
| Bellek yönetimi | Tahsis, serbest bırakma, koruma | `malloc` → `brk`/`mmap` |
| Dosya sistemi | Dosya, klasör, izin | `open()`, `chmod` |
| G/Ç (I/O) yönetimi | Klavye, ekran, disk, ağ | `read()`, `write()` |
| CPU zamanlaması | Hangi process ne zaman çalışacak? | Zamanlayıcı (scheduler) |
| Güvenlik ve koruma | Yetkisiz erişimi engelleme | Kullanıcı/izin denetimi |

**Katmanlar** (yukarıdan aşağı; her katman yalnızca altındakiyle konuşur):
```
 ┌───────────────────────────────┐
 │ Kullanıcı uygulamaları        │  ./merhaba, firefox, bash
 ├───────────────────────────────┤
 │ Kütüphaneler (libc, pthread)  │  printf, malloc, pthread_create
 ├───────────────────────────────┤  ← USER MODE
 │ Sistem çağrıları (syscall)    │  write, read, fork, brk  ← kontrollü kapı
 ├───────────────────────────────┤  ← KERNEL MODE
 │ Çekirdek (kernel)             │  zamanlayıcı, bellek, sürücüler
 ├───────────────────────────────┤
 │ Donanım (CPU, RAM, disk)      │
 └───────────────────────────────┘
```

#### 2. Kernel (çekirdek)
* OS'in çekirdeğidir; bilgisayar açılırken **ilk yüklenen** yazılımdır ve **sürekli bellekte** kalır.
* **Donanıma doğrudan erişebilen tek yazılımdır**; tüm kritik kararlar burada verilir. Linux'ta kernel dosyası **`vmlinuz`**'dur.
* Görevleri: process zamanlaması · bellek yönetimi (sanal bellek, paging, koruma) · dosya sistemi · **cihaz sürücüleri** · **sistem çağrılarını işleme** · **kesmeleri (interrupt) yönetme**.

#### 3. User mode ve kernel mode
CPU iki yetki seviyesinde çalışır:

| | User mode (kısıtlı) | Kernel mode (yetkili) |
|---|---|---|
| Kim çalışır? | Uygulama programları | Çekirdek |
| Donanım erişimi | **Doğrudan erişemez** | Tam erişim |
| Bellek | Sadece kendi alanı | Tüm bellek |
| Hata olursa | Sadece o process çöker | Tüm sistem etkilenebilir |
| Diğer moda geçiş | **Sadece syscall ile** | — |

**Neden iki mod?** **Güvenlik** (uygulama kernel'i bozamaz) · **Kararlılık** (uygulama çökse bile kernel ayakta kalır) · **İzolasyon** (process'ler birbirinin belleğine erişemez) · **Yetkilendirme** (kritik işlemler sadece kernel'da).

#### 4. Sistem çağrısı (system call)
Uygulamanın kernel'dan hizmet istemesinin **tek yolu**; user mode'dan kernel mode'a **kontrollü bir kapı**dır. Uygulama "şu dosyaya yaz" der; işi kernel yapar, sonucu döndürür. **libc** bu çağrıları sarmalar; syscall = uygulama ile kernel arasındaki **sözleşme**.

| Syscall | Görev | Syscall | Görev |
|---|---|---|---|
| `open()` | Dosya aç | `fork()` | **Yeni process oluştur** |
| `read()` | Dosyadan oku | `exec()` | **Çalışan programı değiştir** |
| `write()` | Dosyaya yaz | `wait()` | Child process'i bekle |
| `close()` | Dosya kapat | `exit()` | Process'i sonlandır |
| `brk()` | **Heap büyüt** | `mmap()` | Bellek haritala |
| `socket()` | Ağ soketi aç | `bind()` / `listen()` | Porta bağla / bağlantı bekle |

**`printf("Merhaba\\n")` arka planda adım adım:**
```
 [user mode]   main()  ──►  printf()  (libc: metni biçimlendir, tampona koy)
                                │
                                ▼
                        write(1, "Merhaba\\n", 8)     ← sistem çağrısı
 ───────────────────────────── mod geçişi ─────────────────────────────
 [kernel mode]          kernel write()  ──►  terminal sürücüsü  ──►  ekran
```
`write(fd, veri, n)`: **fd 1 = stdout**, 2 = stderr, 0 = stdin; **n = yazılacak bayt sayısı**; dönüş değeri yazılan bayt sayısıdır. `write(1, "Merhaba\\n", 3)` sadece **"Mer"** yazar.
**Tamponlama tuzağı:** printf çıktıyı önce libc tamponunda biriktirir; write ise doğrudan kernel'a gider. Çıktı bir dosyaya/boruya yönlendirilmişse printf ile write'ın sırası **karışabilir** → `fflush(stdout)` tamponu hemen boşaltır.

#### 5. Kernel mimarileri
| Mimari | Yapı | Örnek | Artı | Eksi |
|---|---|---|---|---|
| **Monolithic** | Tüm servisler (sürücü, dosya sistemi…) **aynı adres alanında**, kernel içinde | **Linux** | Hızlı (servisler arası çağrı ucuz) | Bir sürücü hatası **tüm sistemi** çökertebilir |
| **Microkernel** | Minimal kernel; servisler **ayrı process'lerde** (user mode) | **Minix** | Güvenli, hata izole | Daha yavaş (mesajlaşma maliyeti) |
| **Hybrid** | Karma yaklaşım | **Windows, macOS** | Denge | — |

### Bölüm B — Derleme Zinciri: kaynak koddan çalıştırılabilir dosyaya

#### 6. Dört adım ve ürettikleri dosyalar
```
 merhaba.c ──gcc -E──► merhaba.i ──gcc -S──► merhaba.s ──gcc -c──► merhaba.o ──gcc──► merhaba
  kaynak kod    cpp      ön işlenmiş   cc1     assembly      as      obje (ELF      ld    çalıştırılabilir
  (5-7 satır)            (800+ satır)          (metin)               relocatable)        (ELF executable)
```
| Adım | Komut | Araç | Girdi → Çıktı | Ne olur? | Çıktı insan okuyabilir mi? |
|---|---|---|---|---|---|
| 1. Ön işleme | `gcc -E merhaba.c -o merhaba.i` | **cpp** | `.c` → **`.i`** | `#include` dosyaları **kopyalanır**, `#define` makroları yerleştirilir, **yorumlar silinir** | Evet (C kodu) |
| 2. Derleme | `gcc -S merhaba.i -o merhaba.s` | **cc1** | `.i` → **`.s`** | C kodu **assembly**'ye çevrilir; sözdizimi hataları burada yakalanır | Evet (assembly) |
| 3. Assembly | `gcc -c merhaba.s -o merhaba.o` | **as** | `.s` → **`.o`** | Assembly **makine koduna** çevrilir | Hayır (ikili) |
| 4. Bağlama | `gcc merhaba.o -o merhaba` | **ld** | `.o` + kütüphaneler → **çalıştırılabilir** | Tanımsız semboller (printf/puts) çözülür, başlangıç kodu (crt) eklenir | Hayır (ikili) |

Tek adımda: `gcc merhaba.c -o merhaba` (dört adımı arka planda yapar, ara dosyaları siler). Kısa yol: `gcc -c merhaba.c` doğrudan `.o` üretir.
**Hangi hata hangi aşamada?** Eksik `;` veya yanlış tip → **derleme** (cc1) · `#include <yok.h>` bulunamadı → **ön işleme** · `undefined reference` / `multiple definition` → **bağlama** (ld).

#### 7. Assembly'yi okumak
```
  int x = 5;           movl  $5, -4(%rbp)      # x stack'te rbp-4 adresinde; oraya 5 yaz
  x = x + 3;           movl  -4(%rbp), %eax    # eax = x        (bellekten register'a)
                       addl  $3, %eax          # eax += 3
                       movl  %eax, -4(%rbp)    # x = eax        (register'dan belleğe)
```
`$5` sabit sayı · `%eax` register · `-4(%rbp)` stack'teki yerel değişken · `movl` taşı, `addl` topla (`l` = 32 bit).
`printf("Merhaba!\\n")` assembly'de **`call puts@PLT`** olur: metin sabit, **format belirteci yok ve `\\n` ile bitiyor** → gcc daha basit ve hızlı **puts**'u seçer (puts zaten satır sonu ekler). `@PLT` = fonksiyon çalışma anında paylaşımlı kütüphaneden bulunacak.

#### 8. Obje dosyası ve nm çıktısını okumak
```
$ file merhaba.o
merhaba.o: ELF 64-bit LSB relocatable, x86-64       ← "relocatable" = obje, henüz adresleri kesin değil
$ nm merhaba.o
                 U puts                              ← U = Undefined: burada YOK, bağlamada aranacak
0000000000000000 T main                              ← T = Text: .text bölümünde TANIMLI fonksiyon
```
| nm harfi | Anlamı |
|---|---|
| **T** / t | `.text`'te tanımlı fonksiyon (global / yerel-static) |
| **U** | **Tanımsız** — başka bir dosyadan/kütüphaneden gelecek |
| **D** / d | `.data`'da başlatılmış global / static değişken |
| **B** / b | `.bss`'te başlatılmamış global / static değişken |
| R | `.rodata` salt-okunur veri (string sabitleri) |

Obje dosyası = makine kodu + semboller (main) + **tanımsız semboller** (printf) + yeniden konumlandırma bilgisi → **çalıştırılabilir DEĞİLDİR** (`./merhaba.o` → `cannot execute binary file`).

#### 9. Bağlama (linking), linker hataları, statik ve dinamik bağlama
Linker (**ld**) `merhaba.o` + **libc.so** + başlangıç kodu (**crt0.o** / crt1.o: `_start`, main'i çağıran kod) dosyalarını birleştirir.
```c
int topla(int a, int b);   // sadece prototip
int main() { return topla(2, 3); }
```
→ derleme **geçer** (prototip yeterli) ama bağlamada: **`undefined reference to 'topla'`** → tanım yok ya da kütüphane eksik (pthread fonksiyonları için **`-pthread`**).
`gcc a.c b.c -o prog` → **`multiple definition of 'yardimci'`** → aynı fonksiyon iki dosyada tanımlı; birinde tanım, diğerinde sadece prototip olmalı.

| | Dinamik bağlama (varsayılan) | Statik bağlama (`gcc -static`) |
|---|---|---|
| Kütüphane kodu | Çalıştırılabilire **kopyalanmaz**; çalışırken `libc.so.6` yüklenir | Çalıştırılabilirin **içine kopyalanır** (`libc.a`) |
| Dosya boyutu | Küçük | Büyük |
| `ldd` çıktısı | Kütüphane listesi | `not a dynamic executable` |
| Güncelleme | libc güncellenince tüm programlar faydalanır | Yeniden derlemek gerekir |
| `nm` | `U puts@GLIBC_2.2.5` | puts tanımlı (T) |

#### 10. ELF formatı
Linux'un çalıştırılabilir/obje dosya biçimi **ELF**'tir (Executable and Linkable Format).
```
 ┌──────────────────────┐
 │ ELF Header           │  mimari (x86-64), tip (relocatable / executable), giriş noktası
 ├──────────────────────┤
 │ .text                │  makine kodu (main, fonksiyonlar)
 │ .rodata              │  salt-okunur sabitler ("Merhaba!")
 │ .data                │  BAŞLATILMIŞ global/static:   int sayac = 5;
 │ .bss                 │  BAŞLATILMAMIŞ global/static: int toplam;  (dosyada yer kaplamaz, 0 ile başlar)
 ├──────────────────────┤
 │ Sembol tablosu       │  main, printf … gibi isim → adres eşleşmeleri
 └──────────────────────┘
```
Yerel (fonksiyon içi) değişkenler ELF'te değil, çalışma anında **stack**'te oluşur.

#### 11. Loader: dosyadan process'e
```
  Disk: ./program (ELF)  ──exec()──►  RAM: kod yüklendi, veri hazır  ──►  Process (PID, çalışıyor)
```
Kabuk `fork()` ile kendini kopyalar, kopya **`execve()`** ile yerine programı yükler; **loader** ELF bölümlerini belleğe yerleştirir, dinamik bağlayıcı (`ld-linux-x86-64.so.2`) paylaşımlı kütüphaneleri bağlar, `_start` → `main` çağrılır.

#### 12. ldd ve strace çıktılarını okumak
```
$ ldd merhaba
    linux-vdso.so.1                                     ← kernel'in sağladığı sanal kütüphane (hızlı syscall)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6        ← C kütüphanesi (printf burada)
    /lib64/ld-linux-x86-64.so.2                         ← dinamik bağlayıcı/yükleyici
```
```
$ strace ./merhaba
execve("./merhaba", ...) = 0           ← program belleğe yüklendi (exec)
brk(NULL)              = 0x55a4...     ← heap sınırı soruldu
mmap(NULL, 8192, ...)  = 0x7f3c...     ← bellek haritalandı (libc yükleniyor)
write(1, "Merhaba, dünya!\\n", 17) = 17 ← printf'in asıl işi: fd 1'e 17 bayt yazıldı
exit_group(0)          = ?             ← return 0 → process bitti
+++ exited with 0 +++
```
Her satır: **`syscall_adı(argümanlar) = dönüş değeri`**. "Merhaba, dünya!\\n" 17 bayttır çünkü UTF-8'de **'ü' 2 bayt**tır. → *"Bir program çalıştırmak, bir dizi sistem çağrısı yapmaktır."*

#### 13. Linux gözlem komutları
| Komut | Ne gösterir? | Çıktıda bak |
|---|---|---|
| `uname -a` | Kernel ve sistem bilgisi | Kernel sürümü (5.15.0), mimari (x86_64) |
| `ps -ef` | Tüm process'ler (**anlık, statik** liste) | UID, **PID**, **PPID**, CMD — PID 1 `/sbin/init` |
| `top` | **Canlı** process izleme | %CPU, %MEM, Tasks (running/sleeping) |
| `free -h` | Bellek kullanımı | Mem total/used/free, Swap |
| `df -h` | Disk kullanımı | Size, Used, Avail, Use%, **Mounted on** (bağlandığı yer) |
| `lsblk` | Blok cihazlar (diskler, bölümler) | sda, sda1 … |
| `uptime` | Sistem ne kadar süredir açık | up 2 days |

#### 14. Yaygın hatalar
| Mesaj | Neden | Çözüm |
|---|---|---|
| `command not found: gcc` | Derleyici kurulu değil | `sudo apt install build-essential` |
| `undefined reference to X` | Fonksiyon tanımlı değil / kütüphane eksik | Tanımı ekle; pthread için `-pthread` |
| `cannot execute binary file` | Yanlış mimari ya da **.o dosyası** çalıştırılıyor | Önce bağla (`gcc x.o -o x`) |
| `No such file or directory` / `command not found` | `./` olmadan çalıştırılıyor | `./program` |

**Neden önemli?** Hata ayıklama (derleme mi, linker mı?) · performans (gereksiz include derlemeyi uzatır) · güvenlik (çalıştırılabilir format bilinmeli) · process kavramı (loader → process) · bağımlılıklar (ldd) · sistem yöneticiliği (paketler, .so dosyaları).

#### ⚠️ Sınav Tuzakları & Dikkat Edilecekler
| Tuzak | Doğrusu |
|---|---|
| `-S`'i obje sanmak | `-E` → .i · **`-S` → .s (assembly)** · **`-c` → .o (obje)** |
| `.o` dosyasını çalıştırmak | Relocatable; bağlanmadan çalışmaz |
| `U` harfini "unused" sanmak | **U = Undefined** (bağlamada çözülecek) |
| "Prototip varsa link de geçer" | Prototip derlemeyi geçirir; **tanım yoksa bağlama** hatası |
| `.data` / `.bss` karıştırmak | `int a = 5;` → .data · `int b;` → .bss (global için) |
| Yerel değişkeni ELF bölümü sanmak | Yerel değişken stack'te, çalışma anında |
| printf'i "doğrudan ekrana yazar" sanmak | printf → libc → **write** syscall → kernel |
| `write(1, s, 3)` | Sadece ilk **3 bayt** yazılır |
| strace'teki 1 | PID değil, **stdout dosya tanımlayıcısı** |
| Kernel mimarisi örnekleri | Monolithic = Linux · Microkernel = Minix · Hybrid = Windows/macOS |
| `fork` / `exec` | fork **yeni process** yaratır; exec mevcut process'in **programını değiştirir** |
| `ps -ef` / `top` | ps anlık liste, top canlı |
| Statik / dinamik | Dinamik: ldd kütüphaneleri listeler · Statik (`-static`): kütüphane dosyanın içinde, ldd "not a dynamic executable" |
""",
            "concepts": [
                ('Kernel', "Donanıma doğrudan erişebilen tek yazılım; açılışta ilk yüklenir, bellekte kalır; Linux'ta vmlinuz."),
                ('User / Kernel mode', 'Kısıtlı uygulama modu / donanıma tam erişimli yetkili mod; geçiş yalnızca syscall ile.'),
                ('System call', "User mode'dan kernel mode'a kontrollü kapı (open, read, write, fork, exec, brk…)."),
                ('libc', "printf, malloc gibi fonksiyonlarla syscall'ları sarmalayan C kütüphanesi (libc.so.6)."),
                ('fork / exec', "Yeni process oluştur / mevcut process'in çalıştırdığı programı değiştir."),
                ('Monolithic / Microkernel', "Tüm servisler kernel'de, hızlı (Linux) / minimal kernel, güvenli ama yavaş (Minix)."),
                ('cpp → cc1 → as → ld', 'Ön işleme (.i) → derleme (.s) → assembly (.o) → bağlama (çalıştırılabilir).'),
                ('.o (obje)', 'ELF relocatable; tanımsız semboller içerir, tek başına çalışmaz.'),
                ('nm: U / T', "U tanımsız sembol (bağlamada çözülür) / T .text'te tanımlı fonksiyon."),
                ('ld (linker)', "Obje dosyalarını, libc'yi ve crt başlangıç kodunu birleştirir; undefined reference burada çıkar."),
                ('Statik / dinamik bağlama', 'Kütüphane dosyaya kopyalanır (-static) / çalışırken .so olarak yüklenir (varsayılan).'),
                ('ELF', 'Header, .text, .rodata, .data (başlatılmış), .bss (başlatılmamış), sembol tablosu.'),
                ('Loader', "exec ile ELF'i belleğe yükleyip process'e dönüştüren mekanizma."),
                ('ldd / strace', 'Paylaşımlı kütüphaneleri listeler / programın sistem çağrılarını izler.'),
            ],
            "must": [
                "Kernel = donanıma doğrudan erişen tek yazılım; Linux'ta vmlinuz",
                "User mode donanıma erişemez → syscall ile kernel'a istek; iki mod: güvenlik, kararlılık, izolasyon, yetkilendirme",
                'printf → libc → write syscall → kernel → ekran; write(1, s, n): fd 1 stdout, n bayt',
                "fork = yeni process · exec = programı değiştir · wait = child'ı bekle · brk = heap büyüt · mmap = bellek haritala",
                'Monolithic (Linux) · Microkernel (Minix) · Hybrid (Windows, macOS)',
                'gcc -E → .i (cpp, 800+ satır) · -S → .s (cc1, assembly) · -c → .o (as, obje) · gcc → çalıştırılabilir (ld)',
                'printf("…\\n") → assembly\'de call puts@PLT',
                'nm: U = tanımsız, T = .text, D = .data, B = .bss',
                'undefined reference / multiple definition = linker (bağlama) hatası',
                ".data başlatılmış, .bss başlatılmamış global; yerel değişken stack'te",
                'Dinamik bağlama varsayılan (ldd → libc.so.6); -static ile kütüphane dosyaya gömülür',
                'strace: execve → brk → mmap → write(1, …, 17) = 17 → exit_group(0)',
                'uname -a · ps -ef (statik) · top (canlı) · free -h (bellek) · df -h (disk) · lsblk · uptime',
            ],
            "cheat": [
                {"title": 'Derleme zinciri', "columns": ['Adım', 'Komut', 'Araç', 'Çıktı'], "rows": [
                    ['1. Ön işleme', 'gcc -E merhaba.c -o merhaba.i', 'cpp', '.i (800+ satır)'],
                    ['2. Derleme', 'gcc -S merhaba.i -o merhaba.s', 'cc1', '.s (assembly)'],
                    ['3. Assembly', 'gcc -c merhaba.s -o merhaba.o', 'as', '.o (ELF relocatable)'],
                    ['4. Bağlama', 'gcc merhaba.o -o merhaba', 'ld', 'ELF executable'],
                ]},
                {"title": 'Hata hangi aşamada?', "columns": ['Hata', 'Aşama'], "rows": [
                    ['yok.h: No such file', 'Ön işleme'],
                    ["expected ';' / tip hatası", 'Derleme'],
                    ['undefined reference to X', 'Bağlama'],
                    ['multiple definition of X', 'Bağlama'],
                    ['cannot execute binary file', 'Çalıştırma (.o çalıştırıldı)'],
                ]},
                {"title": 'Yaygın sistem çağrıları', "columns": ['Syscall', 'İş'], "rows": [
                    ['open / close', 'Dosya aç / kapat'],
                    ['read / write', 'Oku / yaz'],
                    ['fork', 'Yeni process'],
                    ['exec', 'Programı değiştir'],
                    ['wait', "Child'ı bekle"],
                    ['exit', 'Sonlandır'],
                    ['brk', 'Heap büyüt'],
                    ['mmap', 'Bellek haritala'],
                    ['socket / bind / listen', 'Soket aç / porta bağla / bağlantı bekle'],
                ]},
                {"title": 'nm harfleri ve ELF bölümleri', "columns": ['Harf / bölüm', 'Anlam'], "rows": [
                    ['T / .text', 'Fonksiyon kodu'],
                    ['U', 'Tanımsız (bağlamada çözülecek)'],
                    ['D / .data', 'Başlatılmış global/static'],
                    ['B / .bss', 'Başlatılmamış global/static'],
                    ['R / .rodata', 'Salt-okunur sabitler'],
                ]},
                {"title": 'İnceleme ve gözlem komutları', "columns": ['Komut', 'Ne gösterir?'], "rows": [
                    ['file', 'Dosya türü (relocatable / executable)'],
                    ['nm', 'Semboller'],
                    ['ldd', 'Paylaşımlı kütüphaneler'],
                    ['objdump -d', 'Makine kodunu assembly olarak'],
                    ['strace', 'Sistem çağrıları'],
                    ['uname -a', 'Kernel bilgisi'],
                    ['ps -ef / top', "Process'ler (statik / canlı)"],
                    ['free -h / df -h', 'Bellek / disk'],
                    ['lsblk / uptime', 'Blok cihazlar / açık kalma süresi'],
                ]},
                {"title": 'Kernel mimarileri', "columns": ['Mimari', 'Örnek', 'Artı / eksi'], "rows": [
                    ['Monolithic', 'Linux', 'Hızlı / bir hata tüm sistemi çökertebilir'],
                    ['Microkernel', 'Minix', 'Güvenli / daha yavaş'],
                    ['Hybrid', 'Windows, macOS', 'Karma'],
                ]},
                {"title": 'Yaygın hatalar', "columns": ['Mesaj', 'Çözüm'], "rows": [
                    ['command not found: gcc', 'sudo apt install build-essential'],
                    ['undefined reference to X', 'Tanım / kütüphane ekle (-pthread)'],
                    ['cannot execute binary file', 'Yanlış mimari ya da .o çalıştırılıyor'],
                    ['No such file or directory', './program'],
                ]},
            ],
            "images": [("c_os_katmanlari.jpg", "İşletim sistemi katmanları (Hafta03 s.4)"),
                       ("c_user_kernel_mode.jpg", "User mode (kısıtlı) ve kernel mode (yetkili); syscall geçişi (s.8)"),
                       ("c_printf_syscall.jpg", "printf çağrısı arka planda: libc → write syscall → kernel → terminal (s.12)"),
                       ("c_derleme_zinciri.jpg", "Derleme zinciri: .c → .i → .s → .o → çalıştırılabilir (s.15)"),
                       ("c_elf_formati.jpg", "ELF dosya formatı: header, .text, .data, .bss, sembol tablosu (s.25)"),
                       ("c_strace.jpg", "strace ./merhaba çıktısı (s.28)")],
            "templates": ["c_derleme_zinciri", "c_assembly_karsilik", "c_write_syscall", "c_elf_bolumler", "c_linker_hata"],
        },
        {
            "id": "c-h4",
            "title": "Hafta 4 — Process (Program vs Process, PCB, Durumlar, fork / wait / exec, Zombi & Yetim)",
            "sources": ["Process.pdf"],
            "summary": """
**Geçen hafta:** OS'in görevleri, kernel ve user/kernel mode, system call, derleme zinciri (.c → .i → .s → .o → binary), ELF ve loader, strace.
**Bu hafta:** program vs process · PCB · process durumları · `fork()` · `getpid()/getppid()` · `wait()` · `exec()` · zombi ve yetim process.

#### 1. Program ≠ Process
* **Program:** diskte duran dosya (`./merhaba`) — **statik**.
* **Process:** çalışan program, OS'teki canlı karşılığı (PID: 4521) — **dinamik**. Aynı program iki kez çalıştırılırsa **iki ayrı process** (iki PID) olur.

**Her process'in kendine ait olanları:** PID · bellek alanı (**kod, veri, heap, stack**) · program counter (**PC** — hangi komutta kaldı?) ·
CPU register'ları · açık dosyaları (stdin, stdout, dosyalar) · bir **parent**'ı (kendisini yaratan process) · bir **durumu**.

#### 2. PCB — Process Control Block
Kernel her process için bir PCB tutar; process'i durdurup sonra kaldığı yerden devam ettirebilmek (**context switch**) için gereken her şey buradadır:

| Alan | Örnek |
|---|---|
| Process ID (PID) | 4521 |
| Process State | RUNNING |
| Program Counter | 0x4005A0 |
| CPU Registers | rax, rbx, rcx… |
| Memory Info | text, data, heap, stack |
| Open Files | stdin, stdout, fd=3… |
| Parent PID (PPID) | 3120 |
| Scheduling Info | priority, time slice |

#### 3. Process durumları (state diagram)
**NEW → (admitted) → READY → (dispatch) → RUNNING → (exit) → TERMINATED**
* RUNNING → **(interrupt)** → READY: zaman dilimi bitti, CPU başkasına verildi
* RUNNING → **(I/O wait)** → WAITING: disk/klavye/ağ bekleniyor
* WAITING → **(I/O done)** → READY: beklenen olay gerçekleşti (doğrudan RUNNING'e değil!)

**Tek çekirdekli CPU'da bir anda SADECE 1 process çalışır**; birden fazlası READY olabilir. OS saniyede yüzlerce kez değiştirir →
kullanıcı **paralel** sanır ama bu **eşzamanlılıktır (concurrency)**. Gerçek paralellik çok çekirdekli CPU'da mümkündür.

#### 4. fork() — yeni process yaratma
`fork()` çağıran process'in (**parent**) **kopyası** olan yeni bir process (**child**) yaratır. İkisi de `fork()`'tan **sonraki satırdan** devam eder.
```c
printf("fork'tan önce\\n");
pid_t pid = fork();
printf("fork'tan sonra\\n");   // iki kez yazılır: parent + child
```
**Dönüş değeri — aynı kod, farklı davranış:**
* **Parent'ta:** child'ın PID'i (**> 0**) · **Child'da:** **0** · **Hata:** **−1** (< 0)
```c
pid_t pid = fork();
if (pid < 0)       { printf("fork başarısız!\\n"); return 1; }
else if (pid == 0) { printf("CHILD: PID=%d, Parent=%d\\n", getpid(), getppid()); }
else               { printf("PARENT: PID=%d, Child=%d\\n", getpid(), pid); }
```
Gerekli başlıklar: `<unistd.h>` (fork, getpid, getppid, exec, sleep), `<sys/types.h>` (pid_t), `<sys/wait.h>` (wait, WIFEXITED, WEXITSTATUS).

**fork sonrası bellek:** child, parent'ın kod/veri/heap/stack'inin **kopyasını** alır; **ayrı bellek alanları** vardır.
`int x = 100;` → fork → child `x = 200` yapar → child **200**, parent hâlâ **100** yazar. Biri değişince diğeri etkilenmez.

**Process ağacı:** her process'in bir parent'ı vardır: `init/systemd (PID 1) → sshd → bash (3120) → ./program (4521), ps (4522)`.
`ps -ef --forest` ağacı girintili gösterir (PPID sütunu parent'ın PID'i).

#### 5. wait() — child process'i bekleme
`wait(&status)` parent'ı **child bitene kadar bloke eder**; child bitince parent devam eder ve child'ın **çıkış durumunu** alır,
biten child **toplanır (reap)** — kaynakları serbest kalır.
```c
int status;
wait(&status);
if (WIFEXITED(status))                       // normal mi bitti?
    printf("child %d ile bitti\\n", WEXITSTATUS(status));   // return 42 → 42
```
**wait vs sleep:** `sleep(n)` kör bekleme — süreye bağlı, çocuk erken bitse de beklersin · `wait` akıllı bekleme — duruma bağlı, çocuk biter bitmez devam eder ve
**çıkış kodunu verir**. Doğrusu `wait` veya `waitpid` kullanmak.

#### 6. Zombi ve yetim process
| | **Zombi (zombie)** | **Yetim (orphan)** |
|---|---|---|
| Durum | Çocuk öldü ama parent **wait() çağırmadı** | **Parent öldü**, çocuk yaşıyor |
| Sonuç | Kaynak yok, sadece PID (süreç tablosu girdisi) kalır | **init (PID 1) evlat edinir** |
| Gözlem | `ps`'te **`<defunct>`** görünür | Yeni **PPID = 1**, sistem çalışmaya devam eder |

#### 7. exec() — program değiştirme
`exec` ailesi (`execl`, `execv`, `execvp`…) mevcut process'in **programını tamamen değiştirir**: kod, veri, bellek yenisiyle değişir, **PID aynı kalır**.
**Başarılı olursa geri DÖNMEZ** — exec'ten sonraki satır sadece exec **başarısız** olursa çalışır.
```c
printf("exec öncesi\\n");
execl("/bin/ls", "ls", "-l", NULL);   // argüman listesi NULL ile biter
printf("exec başarısız!\\n");          // sadece hata durumunda
```
Önce: PID 4521, çalışan bash → exec → Sonra: PID 4521, çalışan ls.

#### 8. fork + exec + wait = klasik shell modeli
Shell bir komutu şöyle çalıştırır: **parent fork() → child exec(ls) → parent wait(&status) → ls biter → parent devam eder.**
```c
pid_t pid = fork();
if (pid == 0) { execl("/bin/ls", "ls", "-l", NULL); perror("exec başarısız"); return 1; }
else          { int status; wait(&status); printf("Komut bitti, çıkış kodu: %d\\n", WEXITSTATUS(status)); }
```
**fork nerelerde kullanılır?** shell komutları (en yaygın) · sunucular — her bağlantı için bir child (Apache, nginx fork modu) · paralel veri işleme · test araçları (izole ortam).
Web sunucusu: `accept` → `fork()`; child `close(server)`, `handle_client`, `exit(0)`; parent `close(client)` ve zombi kalmasın diye `waitpid(-1, NULL, WNOHANG)`.

#### 9. Yaygın fork hataları
1. **Dönüş değerini kontrol etmemek** — parent/child ayrımı yapılmazsa iki process aynı kodu çalıştırır.
2. **Child'da exec'i unutmak** — child aynı programı çalıştırmaya devam eder.
3. **Parent'ta wait'i unutmak** — **zombi process** oluşur.
4. **Döngü içinde fork** — `for (int i = 0; i < 3; i++) fork();` → her turda process sayısı ikiye katlanır: **2³ = 8 process** (1 orijinal + 7 yeni).

**Kod okuma alıştırması:** `printf("A"); fork(); printf("B"); fork(); printf("C");` → **1 A, 2 B, 4 C** (n fork → 2ⁿ process).
*Not:* çıktı terminal yerine dosyaya/boruya yönlendirilirse printf tamponu fork'la kopyalandığından satırlar tekrar görünebilir; `fflush(stdout)` bunu önler.

**Uygulama görevleri:** 1) parent/child PID karşılaştır · 2) fork sonrası bellek izolasyonu · 3) wait ile çıkış kodu · 4) exec ile başka program ·
5) mini shell (fork + exec + wait) · 6) fork döngüsü kaç process yaratır?
""",
            "concepts": [
                ("Process", "Çalışan program; kendi PID'i, belleği, PC'si, register'ları ve açık dosyaları vardır."),
                ("PCB", "Kernel'in her process için tuttuğu kayıt: PID, durum, PC, register'lar, bellek, dosyalar, PPID, zamanlama."),
                ("Concurrency", "Tek çekirdekte hızlı geçişlerle eşzamanlılık; gerçek paralellik çok çekirdekte."),
                ("fork()", "Çağıranın kopyası olan child'ı yaratır; parent'ta child PID, child'da 0, hatada −1 döner."),
                ("wait()", "Parent'ı child bitene kadar bloke eder; çıkış durumunu alır ve child'ı toplar."),
                ("exec()", "Process'in programını değiştirir, PID aynı kalır; başarılıysa geri dönmez."),
                ("Zombi", "Bitmiş ama parent'ı wait() yapmamış process; ps'te <defunct>."),
                ("Yetim", "Parent'ı ölmüş process; init (PID 1) evlat edinir."),
                ("WEXITSTATUS", "wait'ten gelen status içinden child'ın çıkış kodunu çıkarır."),
            ],
            "must": [
                "Program statik (diskte), process dinamik (çalışan, PID'li)",
                "PCB: PID, state, PC, register'lar, memory info, open files, PPID, scheduling info",
                "Durumlar: new → ready → running → waiting / terminated; I/O done → READY'ye döner",
                "Tek çekirdekte aynı anda 1 process çalışır (concurrency ≠ parallelism)",
                "fork() dönüşü: parent'ta child PID (> 0), child'da 0, hata −1",
                "fork sonrası bellek kopyadır: child'daki değişiklik parent'ı etkilemez",
                "wait(&status) + WIFEXITED / WEXITSTATUS → çıkış kodu; wait yoksa zombi",
                "Zombi: child öldü, parent wait yapmadı (<defunct>) · Yetim: parent öldü, PPID = 1",
                "exec başarılıysa geri dönmez, PID değişmez",
                "Shell modeli: fork + exec + wait · n kez fork → 2ⁿ process (for i<3 → 8)",
            ],
            "cheat": [
                {"title": "Sistem çağrıları", "columns": ["Çağrı", "Ne yapar?", "Dönüş / not"], "rows": [
                    ["fork()", "Çağıranın kopyası child'ı yaratır", "Parent: child PID · Child: 0 · Hata: −1"],
                    ["getpid() / getppid()", "Kendi PID'i / parent'ın PID'i", "<unistd.h>"],
                    ["wait(&status)", "Child bitene kadar bekler", "Biten child'ın PID'i; WEXITSTATUS(status) çıkış kodu"],
                    ["waitpid(-1, NULL, WNOHANG)", "Beklemeden biten child'ları toplar", "Sunucularda zombi önleme"],
                    ["execl(yol, ad, arg…, NULL)", "Programı değiştirir", "Başarılıysa dönmez; PID aynı"],
                    ["sleep(n)", "n saniye kör bekleme", "Çıkış kodu vermez"]]},
                {"title": "Process durum geçişleri", "columns": ["Geçiş", "Olay"], "rows": [
                    ["NEW → READY", "admitted"], ["READY → RUNNING", "dispatch (zamanlayıcı seçti)"], ["RUNNING → READY", "interrupt (zaman dilimi bitti)"],
                    ["RUNNING → WAITING", "I/O wait"], ["WAITING → READY", "I/O done"], ["RUNNING → TERMINATED", "exit"]]},
                {"title": "Zombi vs yetim", "columns": ["", "Zombi", "Yetim"], "rows": [
                    ["Kim öldü?", "Child", "Parent"], ["Neden?", "Parent wait() çağırmadı", "Parent child'dan önce bitti"],
                    ["Belirti", "ps'te `<defunct>`", "PPID = 1 (init evlat edinir)"]]},
                {"title": "fork sayma", "columns": ["Kod", "Process sayısı"], "rows": [
                    ["fork(); (1 kez)", "2"], ["fork(); fork(); (2 kez)", "4 → A×1, B×2, C×4"], ["for (i = 0; i < 3; i++) fork();", "2³ = 8"],
                    ["n kez fork", "2ⁿ (2ⁿ − 1 yeni)"]]},
            ],
            "images": [("c_program_process.jpg", "Program (statik) ≠ Process (dinamik) (Process.pdf s.4)"),
                       ("c_pcb.jpg", "PCB — Process Control Block alanları (s.6)"),
                       ("c_process_durumlari.jpg", "Process durum diyagramı (s.7)"),
                       ("c_fork_bellek.jpg", "fork sonrası parent ve child'ın ayrı bellek kopyaları (s.13)"),
                       ("c_wait_zaman.jpg", "wait(): parent child bitene kadar bloke olur (s.17)"),
                       ("c_zombi_yetim.jpg", "Zombi ve yetim process (s.19)"),
                       ("c_shell_modeli.jpg", "fork + exec + wait: klasik shell modeli (s.23)")],
            "templates": ["c_fork_basit", "c_fork_pid", "c_fork_bellek", "c_wait", "c_exec", "c_fork_exec_wait", "c_fork_sayma"],
        },
    ],
    "flashcards": [
        ("int/int sonucu?", "int — ondalık kısım atılır (10/3 = 3)."),
        ("= ile == farkı?", "= atama, == karşılaştırma."),
        ("do-while kaç kez çalışır?", "Koşul yanlış olsa bile en az bir kez."),
        ("gcc'de -o verilmezse çıktı adı?", "a.out"),
        ("'implicit declaration of printf' hatası?", "#include <stdio.h> eksik."),
        ("scanf'te neden & kullanılır?", "scanf değeri değişkenin ADRESİNE yazar."),
        ("Fonksiyon prototipi neden gerekir?", "main'den sonra tanımlanan fonksiyonu derleyicinin önceden tanıması için."),
        ("Derleme aşamaları?", "Ön işleme → Derleme → Assembly → Bağlama."),
        ("int c[5] = {1, 2}; c[3] = ?", "0 — atanmayan elemanlar 0 olur."),
        ("char isim[] = \"Ali\"; kaç bayt?", "4 ('A','l','i','\\0')."),
        ("strcmp eşit stringlerde ne döndürür?", "0"),
        ("dizi[i] neye eşittir?", "*(dizi + i)"),
        ("p->no neye eşittir?", "(*p).no"),
        ("Struct'taki char ad[20]'ye string nasıl atanır?", "strcpy(o.ad, \"Ali\");"),
        ("getpid() hangi başlıkta?", "<unistd.h>"),
        ("PID 1 kimdir?", "init / systemd."),
        ("Program ile process farkı?", "Program diskteki dosya; process çalışan programın OS'teki karşılığı."),
        ("Buffer overflow neden olur?", "C dizi sınırlarını kontrol etmediği için sınır dışına yazılır."),
        ("Donanıma doğrudan erişebilen tek yazılım?", "Kernel (Linux'ta vmlinuz)."),
        ("User mode'daki uygulama donanıma nasıl erişir?", "Doğrudan erişemez; sistem çağrısı (syscall) ile kernel'dan ister."),
        ("printf arka planda hangi syscall'a dönüşür?", "write (printf → libc → write → kernel → ekran)."),
        ("fork / exec / wait?", "Yeni process oluştur / programı değiştir / child'ı bekle."),
        ("Monolithic, microkernel, hybrid örnekleri?", "Linux · Minix · Windows/macOS."),
        ("gcc -E / -S / -c çıktıları?", ".i (ön işlenmiş) · .s (assembly) · .o (obje)."),
        ("nm çıktısında 'U puts' ne demek?", "puts tanımsız (undefined) sembol; bağlamada libc'den çözülür."),
        ("'undefined reference to topla' hangi aşamanın hatası?", "Bağlama (linker); topla tanımlı değil ya da kütüphane eksik."),
        (".data ile .bss farkı?", ".data başlatılmış, .bss başlatılmamış global değişkenler."),
        ("ldd ne gösterir?", "Programın bağlı olduğu paylaşımlı kütüphaneler (libc.so.6 …)."),
        ("strace'te write(1, …) içindeki 1?", "Dosya tanımlayıcı 1 = stdout (standart çıktı)."),
        ("Bellek / disk kullanımını gösteren komutlar?", "free -h / df -h."),
        ("(float)(10 / 3) ile (float)10 / 3 farkı?", "İlki 3.000000 (bölme önce int yapılır); ikincisi 3.333333 (önce çevrilir)."),
        ("int a = 10, b = 3; float ort = (a + b) / 2; → ort?", "6.0 — 13/2 int bölmesi 6; doğrusu (a + b) / 2.0 → 6.5."),
        ("if (x = 5) neden her zaman doğrudur?", "x'e 5 atanır; ifadenin değeri 5 (sıfırdan farklı) → doğru."),
        ("long ve double için format belirteçleri?", "long: %ld · double: printf'te %f, scanf'te %lf."),
        ("char / int / long / float / double boyutları?", "1 / 4 / 8 / 4 / 8 bayt (tipik 64-bit Linux)."),
        ("İç içe döngü: dış 3, iç 4 tur → iç gövde kaç kez?", "12 (3 × 4)."),
        ("char isim[] = \"Ali\"; sizeof ve strlen?", "sizeof 4 ('\\0' dahil), strlen 3."),
        ("char s[4] = \"Test\"; neden sorunlu?", "4 harf + '\\0' = 5 bayt gerekir; '\\0' sığmaz, string bozulur."),
        ("*p + 1 ile *(p + 1) farkı?", "Gösterilen değer + 1 / bir sonraki elemanın değeri."),
        ("int *p için p + 1 adresi kaç bayt ilerletir?", "sizeof(int) = 4 bayt (bir eleman)."),
        ("İki string nasıl karşılaştırılır?", "strcmp(a, b) == 0; a == b adresleri karşılaştırır."),
        ("Buffer overflow neyi ezebilir?", "Komşu değişkenleri ve fonksiyonun dönüş adresini (return address)."),
        ("Hangi hata hangi aşamada: expected ';' / undefined reference?", "Derleme (cc1) / bağlama (ld)."),
        ("Statik ve dinamik bağlama farkı?", "Statik (-static): kütüphane dosyaya kopyalanır; dinamik: çalışırken libc.so.6 yüklenir (ldd listeler)."),
        ("nm'de D ve B harfleri?", "D: .data (başlatılmış global) · B: .bss (başlatılmamış global)."),
        ("fork ile exec farkı?", "fork yeni process yaratır; exec mevcut process'in programını değiştirir."),
        ("PCB'de neler tutulur?", "PID, durum, program counter, CPU register'ları, bellek bilgisi, açık dosyalar, PPID, zamanlama bilgisi."),
        ("Process durumları?", "new, ready, running, waiting, terminated."),
        ("WAITING durumundaki process I/O bitince nereye geçer?", "READY (doğrudan RUNNING'e değil)."),
        ("Tek çekirdekte aynı anda kaç process çalışır?", "1 — diğerleri READY; hızlı geçişle eşzamanlılık (concurrency)."),
        ("fork() parent'ta, child'da ve hatada ne döndürür?", "Parent: child'ın PID'i (> 0) · Child: 0 · Hata: −1."),
        ("fork'tan sonra child x'i değiştirirse parent'taki x?", "Değişmez — bellek kopyalanır, alanlar ayrıdır."),
        ("wait(&status) ne yapar?", "Child bitene kadar parent'ı bekletir, çıkış durumunu alır, child'ı toplar."),
        ("Child'ın çıkış kodunu hangi makro verir?", "WEXITSTATUS(status) (önce WIFEXITED ile kontrol)."),
        ("Zombi process?", "Bitmiş ama parent'ı wait() çağırmamış child; ps'te <defunct>."),
        ("Yetim process?", "Parent'ı ölmüş child; init (PID 1) evlat edinir, PPID = 1."),
        ("exec başarılı olursa ne olur?", "Program değişir, PID aynı kalır, exec'ten geri dönülmez."),
        ("Shell bir komutu nasıl çalıştırır?", "fork + exec + wait."),
        ("for (i = 0; i < 3; i++) fork(); kaç process?", "2³ = 8."),
        ("printf A; fork; printf B; fork; printf C → kaç A/B/C?", "1 A, 2 B, 4 C."),
        ("wait ile sleep farkı?", "sleep süreye bağlı kör bekleme; wait child bitince döner ve çıkış kodunu verir."),
        ("Parent'ta wait'i unutmanın sonucu?", "Zombi process."),
        ("Process ağacını gösteren komut?", "ps -ef --forest (veya pstree)."),
    ],
}

QUESTIONS = [
    {"week": "c-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int a = 10, b = 3;\nprintf(\"%d %d\\n\", a / b, a % b);",
     "options": ["3 1", "3.33 1", "3 0", "4 1"], "answer": 0,
     "explain": "int / int → int: 10/3 = **3** (ondalık atılır); 10 % 3 = **1** (kalan).",
     "run": c_prog('int a = 10, b = 3;\nprintf("%d %d\\n", a / b, a % b);'), "expect": "3 1"},
    {"week": "c-h1", "q": "Ders slaytındaki mini alıştırmanın çıktısı nedir?", "lang": "c",
     "code": "int x = 15;\nif (x > 10)\n    printf(\"A\");\nif (x > 20)\n    printf(\"B\");\nelse\n    printf(\"C\");",
     "options": ["A", "AB", "AC", "C"], "answer": 2,
     "explain": "İki ayrı if vardır. 15 > 10 → 'A'. İkinci if'te 15 > 20 yanlış → else → 'C'. Çıktı **AC**.",
     "run": c_prog('int x = 15;\nif (x > 10)\n    printf("A");\nif (x > 20)\n    printf("B");\nelse\n    printf("C");\nprintf("\\n");'), "expect": "AC"},
    {"week": "c-h1", "q": "Aşağıdaki do-while döngüsünün çıktısı nedir?", "lang": "c",
     "code": "int i = 10;\ndo {\n    printf(\"%d\\n\", i);\n    i++;\n} while (i <= 5);",
     "options": ["Hiçbir şey yazmaz", "10", "10 11 12 ... sonsuz", "5"], "answer": 1,
     "explain": "do-while gövdeyi koşulu kontrol etmeden **en az bir kez** çalıştırır: 10 yazılır, i=11 olur, 11<=5 yanlış → biter.",
     "run": c_prog('int i = 10;\ndo {\n    printf("%d\\n", i);\n    i++;\n} while (i <= 5);'), "expect": "10"},
    {"week": "c-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "for (int i = 1; i <= 10; i++) {\n    if (i == 5) break;\n    printf(\"%d \", i);\n}",
     "options": ["1 2 3 4", "1 2 3 4 5", "5 6 7 8 9 10", "1 2 3 4 6 7 8 9 10"], "answer": 0,
     "explain": "i == 5 olduğunda **break** döngüden tamamen çıkar; 5 yazılmaz.",
     "run": c_prog('for (int i = 1; i <= 10; i++) {\n    if (i == 5) break;\n    printf("%d ", i);\n}\nprintf("\\n");'), "expect": "1 2 3 4"},
    {"week": "c-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "for (int i = 1; i <= 5; i++) {\n    if (i == 3) continue;\n    printf(\"%d \", i);\n}",
     "options": ["1 2", "1 2 4 5", "1 2 3 4 5", "3"], "answer": 1,
     "explain": "**continue** sadece o turu atlar; 3 yazılmaz ama döngü devam eder.",
     "run": c_prog('for (int i = 1; i <= 5; i++) {\n    if (i == 3) continue;\n    printf("%d ", i);\n}\nprintf("\\n");'), "expect": "1 2 4 5"},
    {"week": "c-h1", "q": "Slayttaki iç içe for döngüsünün çıktısı nedir?", "lang": "c",
     "code": "for (int i = 1; i <= 3; i++) {\n    for (int j = 1; j <= 3; j++) {\n        printf(\"%d%d \", i, j);\n    }\n    printf(\"\\n\");\n}",
     "options": ["11 22 33", "11 12 13 / 21 22 23 / 31 32 33 (üç satır)", "11 21 31 / 12 22 32 / 13 23 33", "123 123 123"], "answer": 1,
     "explain": "Dış döngü satırı (i), iç döngü sütunu (j) belirler; her satır sonunda \\n. Toplam 3×3 = 9 çıktı.",
     "run": c_prog('for (int i = 1; i <= 3; i++) {\n    for (int j = 1; j <= 3; j++) {\n        printf("%d%d ", i, j);\n    }\n    printf("\\n");\n}'),
     "expect": "11 12 13 \n21 22 23 \n31 32 33"},
    {"week": "c-h1", "q": "`for (int i = 0; i < 5; i++)` döngüsü kaç kez döner?",
     "options": ["4", "5", "6", "Sonsuz"], "answer": 1,
     "explain": "i = 0, 1, 2, 3, 4 → **5 tur**. `i <= 5` olsaydı 6 tur dönerdi (i <= n vs i < n farkı)."},
    {"week": "c-h1", "q": "Aşağıdaki while döngüsünde `i++;` satırı unutulursa ne olur?", "lang": "c",
     "code": "int i = 1;\nwhile (i <= 5) {\n    printf(\"%d\\n\", i);\n}",
     "options": ["1'den 5'e kadar yazar", "Hiçbir şey yazmaz", "Sonsuz döngü: sürekli 1 yazar", "Derleme hatası verir"], "answer": 2,
     "explain": "i hiç artmadığı için koşul hep doğrudur → **sonsuz döngü**. Sık hatalar: 'Sonsuz döngü → i++ unutmayın'."},
    {"week": "c-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int kare(int x) {\n    return x * x;\n}\nint main() {\n    int sonuc = kare(5);\n    printf(\"%d\\n\", sonuc);\n    return 0;\n}",
     "options": ["5", "10", "25", "x*x"], "answer": 2,
     "explain": "kare(5) = 5 × 5 = 25.",
     "run": "#include <stdio.h>\n\nint kare(int x) {\n    return x * x;\n}\n\nint main() {\n    int sonuc = kare(5);\n    printf(\"%d\\n\", sonuc);\n    return 0;\n}\n", "expect": "25"},
    {"week": "c-h1", "q": "`int kare(int x);` satırının main'den önce yazılmasının (fonksiyon prototipi) amacı nedir?",
     "options": ["Fonksiyonu iki kez tanımlamak", "main'den sonra tanımlanan fonksiyonu derleyicinin önceden tanıması", "Fonksiyonu global değişken yapmak", "Programı hızlandırmak"], "answer": 1,
     "explain": "Derleyici kodu yukarıdan aşağı okur; prototip, gövdesi daha aşağıda olan fonksiyonun imzasını önceden bildirir."},
    {"week": "c-h1", "q": "Derleyici şu hatayı verdi: `merhaba.c:3:22: error: expected ';' before '}' token`. Bu mesajdan ne anlaşılır?",
     "options": ["22. satır 3. sütunda tanımsız değişken", "3. satır 22. sütun civarında noktalı virgül eksik", "merhaba.c dosyası bulunamadı", "Bağlama (link) hatası"], "answer": 1,
     "explain": "Biçim: **dosya:satır:sütun: error: mesaj** → dosya merhaba.c, satır 3, sütun 22, noktalı virgül eksik."},
    {"week": "c-h1", "q": "Derleme sırasında `warning: implicit declaration of function 'printf'` uyarısı alınıyorsa sebebi nedir?",
     "options": ["printf yanlış yazılmış", "#include <stdio.h> eksik", "main fonksiyonu yok", "Noktalı virgül eksik"], "answer": 1,
     "explain": "Yaygın başlangıç hataları listesi: implicit declaration of printf → **#include <stdio.h> eksik**."},
    {"week": "c-h1", "q": "Aşağıdaki programda hangi satırda sözdizimi (syntax) hatası vardır?", "lang": "c",
     "code": "1  #include <stdio.h>\n2  int main() {\n3      int not = 75\n4      if (not >= 70) printf(\"BB\\n\");\n5      return 0;\n6  }",
     "options": ["1. satır", "3. satır (noktalı virgül eksik)", "4. satır (if parantezi)", "5. satır"], "answer": 1,
     "explain": "3. satırın sonunda `;` yok. gcc hatayı genelde bir sonraki satırı gösterir (`4:5: error: expected ',' or ';' before 'if'`) — hata mesajı satırının bir öncesine de bak!",
     "run": "#include <stdio.h>\nint main() {\n    int not = 75\n    if (not >= 70) printf(\"BB\\n\");\n    return 0;\n}\n", "expect_error": True},
    {"week": "c-h1", "q": "Aşağıdaki kodda mantık hatası vardır. yas = 15 iken çıktı ne olur ve neden?", "lang": "c",
     "code": "int yas = 15;\nif (yas = 18) {\n    printf(\"Yetiskin\\n\");\n} else {\n    printf(\"Cocuk\\n\");\n}",
     "options": ["Cocuk — koşul yanlış", "Yetiskin — '=' atama yapar, 18 doğru (sıfır olmayan) sayılır", "Derleme hatası", "Hiçbir şey"], "answer": 1,
     "explain": "`yas = 18` karşılaştırma değil **atamadır**; ifadenin değeri 18 ≠ 0 → doğru. Doğrusu `yas == 18` (veya `>=`).",
     "run": c_prog('int yas = 15;\nif (yas = 18) {\n    printf("Yetiskin\\n");\n} else {\n    printf("Cocuk\\n");\n}'), "expect": "Yetiskin"},
    {"week": "c-h1", "q": "`scanf(\"%d\", &yas);` ifadesinde `&` işaretinin görevi nedir?",
     "options": ["Mantıksal VE", "yas değişkeninin bellek adresini verir; scanf okunan değeri o adrese yazar", "Bitwise AND", "yas'ı sabit yapar"], "answer": 1,
     "explain": "& = adresini al. scanf değeri değiştirebilmek için değişkenin adresine ihtiyaç duyar (adres ile aktarım)."},
    {"week": "c-h1", "q": "gcc ile kaynak koddan çalıştırılabilir dosyaya giden aşamaların doğru sırası hangisidir?",
     "options": ["Derleme → Ön işleme → Bağlama → Assembly", "Ön işleme → Derleme → Assembly → Bağlama", "Bağlama → Derleme → Ön işleme → Assembly", "Assembly → Derleme → Bağlama → Ön işleme"], "answer": 1,
     "explain": "merhaba.c → Ön işleme (#include) → Derleme → Assembly → Bağlama → merhaba."},
    {"week": "c-h1", "q": "Faktöriyel örneğinde `fakt` değişkeni neden `long` tanımlanmıştır?",
     "options": ["Ondalık sonuç için", "int'in sığmayacağı büyük sonuçlar için (13! üzeri)", "Negatif sayılar için", "scanf ile okunabilmesi için"], "answer": 1,
     "explain": "Slayt notu: long → daha büyük sayı (13! üzeri için şart). 13! = 6.227.020.800 > int sınırı (2.147.483.647)."},
    {"week": "c-h1", "q": "Kullanıcı 4 girerse çıktı nedir?", "lang": "c", "stdin": "4",
     "code": "int n, toplam = 0;\nscanf(\"%d\", &n);\nfor (int i = 1; i <= n; i++) {\n    toplam += i;\n}\nprintf(\"Toplam: %d\\n\", toplam);",
     "options": ["Toplam: 4", "Toplam: 6", "Toplam: 10", "Toplam: 24"], "answer": 2,
     "explain": "1 + 2 + 3 + 4 = **10**. (24 olsaydı faktöriyel olurdu.)",
     "run": c_prog('int n, toplam = 0;\nscanf("%d", &n);\nfor (int i = 1; i <= n; i++) {\n    toplam += i;\n}\nprintf("Toplam: %d\\n", toplam);'), "expect": "Toplam: 10"},
    {"week": "c-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int c[5] = {1, 2};\nprintf(\"%d %d\\n\", c[1], c[3]);",
     "options": ["2 0", "1 0", "2 çöp değer", "Derleme hatası"], "answer": 0,
     "explain": "Kısmi başlatmada atanmayan elemanlar **0** olur: c = {1, 2, 0, 0, 0}. c[1] = 2, c[3] = 0.",
     "run": c_prog('int c[5] = {1, 2};\nprintf("%d %d\\n", c[1], c[3]);'), "expect": "2 0"},
    {"week": "c-h2", "q": "`int a[5];` tanımından sonra `a[5] = 99;` yazılırsa ne olur?",
     "options": ["Derleyici hata verip derlemez", "Dizi otomatik 6 elemana büyür", "Dizinin dışına yazılır; C sınır kontrolü yapmaz → tanımsız davranış (buffer overflow riski)", "a[0]'a yazılır"], "answer": 2,
     "explain": "Geçerli indeksler 0–4'tür. C sınır kontrolü YAPMAZ; program çökmezse bile undefined behavior. Saldırganların kullandığı buffer overflow'un temeli."},
    {"week": "c-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "char isim[] = \"Ali\";\nprintf(\"%d %d\\n\", (int)sizeof(isim), (int)strlen(isim));",
     "options": ["3 3", "4 3", "3 4", "4 4"], "answer": 1,
     "explain": "sizeof '\\0' dahil 4 bayt ('A','l','i','\\0'); strlen '\\0' hariç 3.",
     "run": c_prog('char isim[] = "Ali";\nprintf("%d %d\\n", (int)sizeof(isim), (int)strlen(isim));', ("stdio.h", "string.h")), "expect": "4 3"},
    {"week": "c-h2", "q": "`strcmp(\"abc\", \"abc\")` ifadesi ne döndürür?",
     "options": ["1", "0", "-1", "true"], "answer": 1,
     "explain": "strcmp eşit stringlerde **0** döndürür; farklıysa pozitif/negatif bir değer.",
     "run": c_prog('printf("%d\\n", strcmp("abc", "abc"));', ("stdio.h", "string.h")), "expect": "0"},
    {"week": "c-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int x = 42;\nint *p = &x;\n*p = 100;\nprintf(\"%d\\n\", x);",
     "options": ["42", "100", "x'in adresi", "Derleme hatası"], "answer": 1,
     "explain": "p, x'in adresini tutar; `*p = 100` o adresteki değeri yani **x'i** değiştirir.",
     "run": c_prog('int x = 42;\nint *p = &x;\n*p = 100;\nprintf("%d\\n", x);'), "expect": "100"},
    {"week": "c-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int a[5] = {10, 20, 30, 40, 50};\nint *p = a;\nprintf(\"%d %d %d\\n\", a[2], *(a+2), *(p+1));",
     "options": ["30 30 20", "20 30 20", "30 32 11", "30 30 10"], "answer": 0,
     "explain": "a[2] ≡ *(a+2) = 30. p = a → p, a[0]'ı gösterir; *(p+1) = a[1] = 20.",
     "run": c_prog('int a[5] = {10, 20, 30, 40, 50};\nint *p = a;\nprintf("%d %d %d\\n", a[2], *(a+2), *(p+1));'), "expect": "30 30 20"},
    {"week": "c-h2", "q": "Aşağıdaki programın çıktısı nedir?", "lang": "c",
     "code": "void arttir(int x) {\n    x = x + 1;\n    printf(\"Iceride: %d\\n\", x);\n}\nint main() {\n    int a = 10;\n    arttir(a);\n    printf(\"Disarida: %d\\n\", a);\n}",
     "options": ["Iceride: 11 / Disarida: 11", "Iceride: 11 / Disarida: 10", "Iceride: 10 / Disarida: 10", "Iceride: 10 / Disarida: 11"], "answer": 1,
     "explain": "C varsayılan olarak **değeri kopyalar**; fonksiyondaki x, a'nın kopyasıdır. a değişmez.",
     "run": "#include <stdio.h>\n\nvoid arttir(int x) {\n    x = x + 1;\n    printf(\"Iceride: %d\\n\", x);\n}\n\nint main() {\n    int a = 10;\n    arttir(a);\n    printf(\"Disarida: %d\\n\", a);\n    return 0;\n}\n",
     "expect": "Iceride: 11\nDisarida: 10"},
    {"week": "c-h2", "q": "Aşağıdaki swap programının çıktısı nedir?", "lang": "c",
     "code": "void swap(int *a, int *b) {\n    int t = *a;\n    *a = *b;\n    *b = t;\n}\nint main() {\n    int x = 3, y = 7;\n    swap(&x, &y);\n    printf(\"x=%d y=%d\\n\", x, y);\n}",
     "options": ["x=3 y=7", "x=7 y=3", "x=7 y=7", "x=3 y=3"], "answer": 1,
     "explain": "Adresler aktarıldığı için fonksiyon orijinal değişkenleri değiştirir → x=7 y=3.",
     "run": "#include <stdio.h>\n\nvoid swap(int *a, int *b) {\n    int t = *a;\n    *a = *b;\n    *b = t;\n}\n\nint main() {\n    int x = 3, y = 7;\n    swap(&x, &y);\n    printf(\"x=%d y=%d\\n\", x, y);\n    return 0;\n}\n",
     "expect": "x=7 y=3"},
    {"week": "c-h2", "q": "`struct Ogrenci *p = &o1;` tanımında `p->no` ifadesi hangisine eşittir?",
     "options": ["*p.no", "(*p).no", "&p.no", "p.no"], "answer": 1,
     "explain": "-> operatörü 'pointer üzerinden alan erişimi'dir: p->no ≡ (*p).no ≡ o1.no. (*p.no yanlış; nokta önceliklidir.)"},
    {"week": "c-h2", "q": "Aşağıdaki kodun hangi satırı derleme hatasına yol açar?", "lang": "c",
     "code": "1  struct Ogrenci { int no; char ad[20]; float ort; };\n2  struct Ogrenci o;\n3  o.no = 12345;\n4  o.ad = \"Ali\";\n5  o.ort = 3.45;",
     "options": ["1. satır", "3. satır", "4. satır — char[] atamayla kopyalanamaz, strcpy(o.ad, \"Ali\") kullanılmalı", "5. satır"], "answer": 2,
     "explain": "Diziler `=` ile atanamaz (error: assignment to expression with array type). Doğrusu `strcpy(o.ad, \"Ali\");`.",
     "run": c_prog('struct Ogrenci { int no; char ad[20]; float ort; };\nstruct Ogrenci o;\no.no = 12345;\no.ad = "Ali";\no.ort = 3.45;'), "expect_error": True},
    {"week": "c-h2", "q": "`int *p; *p = 5;` kodunun sorunu nedir?",
     "options": ["Sorun yok, p 5 olur", "p initialize edilmemiş; rastgele bir adrese yazılır (tanımsız davranış)", "Derleyici p'yi otomatik NULL yapar", "*p yerine &p yazılmalı"], "answer": 1,
     "explain": "Yaygın hata: initialize edilmemiş pointer. p bir adres göstermediği için *p = 5 bilinmeyen belleğe yazar; çökme/güvenlik açığı."},
    {"week": "c-h2", "q": "`char s[5] = \"Merhaba\";` tanımının sorunu nedir?",
     "options": ["Sorun yoktur", "\"Merhaba\" '\\0' ile 8 karakterdir, 5 elemanlık diziye sığmaz", "char dizisine string atanamaz", "s büyük harfle yazılmalı"], "answer": 1,
     "explain": "7 harf + '\\0' = 8 karakter. Yaygın hatalar slaytında: 'char s[5] = \"Merhaba\"; // 8 karakter sığmaz!'"},
    {"week": "c-h2", "q": "getpid() ve getppid() fonksiyonlarını kullanmak için hangi POSIX başlık dosyası eklenmelidir?",
     "options": ["<stdlib.h>", "<unistd.h>", "<string.h>", "<process.h>"], "answer": 1,
     "explain": "unistd.h POSIX başlık dosyasıdır; getpid, getppid ve sleep burada tanımlıdır. pid_t için <sys/types.h>."},
    {"week": "c-h2", "q": "Linux'ta genellikle PID'i 1 olan process hangisidir?",
     "options": ["bash", "init / systemd", "kernel thread 0", "ilk açılan kullanıcı programı"], "answer": 1,
     "explain": "1 numaralı PID genelde init/systemd'dir; küçük PID'ler (1–1000) sistem process'leri, kullanıcı process'leri genelde 1000+."},
    {"week": "c-h2", "q": "Program ve process kavramları için hangisi doğrudur?",
     "options": ["İkisi aynı şeydir", "Program diskteki çalıştırılabilir dosya; process onun çalışan hâli; her çalıştırma yeni bir process yaratır", "Process diskte, program bellekte durur", "Bir programın yalnızca bir process'i olabilir"], "answer": 1,
     "explain": "Program ≠ Process. Her çalıştırma yeni PID'li bir process yaratır; her process'in bir parent'ı vardır."},
    {"week": "c-h2", "q": "Kod okuma alıştırması: çıktı nedir?", "lang": "c",
     "code": "int a[3] = {1, 2, 3};\nint *p = a;\nprintf(\"%d\\n\", *p);\nprintf(\"%d\\n\", *(p+1));\nprintf(\"%d\\n\", a[2]);",
     "options": ["1 2 3 (alt alta)", "0 1 2", "1 1 1", "adres adres 3"], "answer": 0,
     "explain": "Slayttaki cevaplar: 1, 2, 3.",
     "run": c_prog('int a[3] = {1, 2, 3};\nint *p = a;\nprintf("%d\\n", *p);\nprintf("%d\\n", *(p+1));\nprintf("%d\\n", a[2]);'), "expect": "1\n2\n3"},
    {"week": "c-h2", "q": "Bir process'in bellek haritasında `malloc` ile ayrılan alan hangi bölgededir?",
     "options": ["Stack", "Heap", "Kod (.text)", "Veri (.data/.bss)"], "answer": 1,
     "explain": "Stack: yerel değişkenler ve fonksiyon çağrıları · **Heap: malloc/new** · Veri: global/static · Kod: makine kodu."},
    # ───────────────────────── Hafta 3 · İşletim Sistemine Giriş + Derleme Zinciri ─────────────────────────
    {"week": "c-h3", "q": "Aşağıdakilerden hangisi işletim sisteminin görevlerinden biri DEĞİLDİR?",
     "options": ["Process yönetimi", "Bellek yönetimi", "Kaynak kodu makine koduna derlemek", "G/Ç (I/O) yönetimi"], "answer": 2,
     "explain": "OS görevleri: process, bellek, dosya sistemi, G/Ç, CPU zamanlaması, güvenlik. Derleme işini gcc gibi derleyiciler yapar, OS değil."},
    {"week": "c-h3", "q": "Kernel (çekirdek) için hangisi YANLIŞTIR?",
     "options": ["Bilgisayar açılırken yüklenen ilk yazılımdır", "Sürekli bellekte kalır", "Donanıma doğrudan erişebilen tek yazılımdır", "Kullanıcı uygulamaları gibi user mode'da çalışır"], "answer": 3,
     "explain": "Kernel **kernel mode**'da (yetkili) çalışır. Uygulamalar user mode'dadır. Linux'ta kernel dosyası `vmlinuz`'dur."},
    {"week": "c-h3", "q": "Linux'ta kernel hangi dosyadır?",
     "options": ["/sbin/init", "vmlinuz", "libc.so.6", "a.out"], "answer": 1,
     "explain": "Slayt: \"Linux'ta 'vmlinuz' dosyasıdır\". /sbin/init PID 1'dir, libc.so.6 C kütüphanesidir."},
    {"week": "c-h3", "q": "User mode'da çalışan bir uygulama diske yazmak istediğinde ne olur?",
     "options": ["Disk denetleyicisine doğrudan yazar", "Sistem çağrısı (syscall) ile kernel'dan ister; kernel kernel mode'da yazar", "BIOS'u çağırır", "Önce root kullanıcısına geçer"], "answer": 1,
     "explain": "User mode donanıma doğrudan erişemez. Syscall user mode → kernel mode geçişini sağlayan kontrollü kapıdır."},
    {"week": "c-h3", "q": "\"Bir uygulama çökse bile kernel ayakta kalır\" ifadesi iki mod (user/kernel) kullanmanın hangi gerekçesidir?",
     "options": ["Güvenlik", "Kararlılık", "İzolasyon", "Yetkilendirme"], "answer": 1,
     "explain": "Güvenlik: uygulama kernel'i bozamaz · **Kararlılık: uygulama çökse bile kernel ayakta** · İzolasyon: process'ler birbirinin belleğine erişemez · Yetkilendirme: kritik işler sadece kernel'da."},
    {"week": "c-h3", "q": "Yeni bir process oluşturan sistem çağrısı hangisidir?",
     "options": ["exec()", "fork()", "wait()", "brk()"], "answer": 1,
     "explain": "fork yeni process oluşturur · exec çalışan programı değiştirir · wait child'ı bekler · brk heap'i büyütür."},
    {"week": "c-h3", "q": "Heap alanını büyütmek için kullanılan sistem çağrısı hangisidir?",
     "options": ["mmap()", "brk()", "socket()", "exit()"], "answer": 1,
     "explain": "brk() heap büyütür; mmap() bellek haritalar. (malloc arka planda bunları kullanır.)"},
    {"week": "c-h3", "q": "printf(\"Merhaba\") çağrısının arka plandaki sırası hangisidir?",
     "options": ["printf → kernel → libc → write → ekran", "printf → libc → write syscall → kernel (mod geçişi) → ekran", "printf → BIOS → ekran kartı", "printf → write → libc → ekran"], "answer": 1,
     "explain": "Uygulama printf() → kütüphane libc → syscall (write) → kernel mod geçişi → kernel write() → terminale yaz."},
    {"week": "c-h3", "q": "Tüm servislerin aynı adres alanında çalıştığı, hızlı ama bir hatada tüm sistemin çökebildiği kernel mimarisi ve örneği hangisidir?",
     "options": ["Microkernel – Minix", "Monolithic – Linux", "Hybrid – Windows", "Exokernel – macOS"], "answer": 1,
     "explain": "Monolithic (Linux) hızlı ama kırılgan · Microkernel (Minix) güvenli ama yavaş · Hybrid (Windows, macOS) karma."},
    {"week": "c-h3", "q": "Microkernel mimarisi için hangisi doğrudur?",
     "options": ["Tüm servisler kernel içindedir", "Minimal kernel; servisler ayrı process'lerde çalışır, güvenli ama daha yavaştır", "Windows ve macOS microkernel'dir", "En hızlı mimaridir"], "answer": 1,
     "explain": "Microkernel: minimal kernel, servisler ayrı process'te (Minix). Güvenli ama daha yavaş."},
    {"week": "c-h3", "q": "`gcc -E merhaba.c -o merhaba.i` komutu hangi adımı yapar ve neden çıktı 800+ satırdır?",
     "options": ["Derleme; assembly kodu uzundur", "Ön işleme; #include <stdio.h> içeriği dosyaya eklenir", "Bağlama; libc eklenir", "Assembly; makine kodu üretilir"], "answer": 1,
     "explain": "-E sadece ön işlemciyi (cpp) çalıştırır: #include'lar açılır, makrolar yerleşir. 5 satırlık kod 800+ satıra çıkar."},
    {"week": "c-h3", "q": "Derleme zincirinin doğru sırası hangisidir?",
     "options": [".c → .s → .i → .o → çalıştırılabilir", ".c → .i → .s → .o → çalıştırılabilir", ".c → .o → .i → .s → çalıştırılabilir", ".c → .i → .o → .s → çalıştırılabilir"], "answer": 1,
     "explain": "Ön işleme (.i) → derleme (.s, assembly) → assembly (.o, obje) → bağlama (ELF çalıştırılabilir). Tek adımda: gcc merhaba.c -o merhaba."},
    {"week": "c-h3", "q": "Assembly (.s) dosyası üreten gcc seçeneği hangisidir?",
     "options": ["-E", "-S", "-c", "-o"], "answer": 1,
     "explain": "-E → .i · **-S → .s** · -c → .o · -o çıktı dosyasının adını belirler."},
    {"week": "c-h3", "q": "`file merhaba.o` komutu \"ELF 64-bit LSB relocatable\" çıktısı veriyor. Bu dosya için hangisi doğrudur?",
     "options": ["Doğrudan ./merhaba.o ile çalıştırılabilir", "Obje dosyasıdır; printf gibi semboller henüz bağlanmamıştır, çalıştırılabilir değildir", "Ön işlenmiş C kodudur", "Paylaşımlı kütüphanedir"], "answer": 1,
     "explain": "Obje dosyası: makine kodu + semboller + tanımsız semboller + yeniden konumlandırma bilgisi. Linker (ld) bağlamadan çalışmaz."},
    {"week": "c-h3", "q": "`nm merhaba.o` çıktısındaki \"U puts\" satırı ne anlama gelir?",
     "options": ["puts kullanılmamış (unused)", "puts tanımsız (undefined) sembol; bağlama aşamasında libc'den çözülecek", "puts kullanıcı (user) fonksiyonudur", "puts .text bölümünde tanımlı"], "answer": 1,
     "explain": "nm'de **U = undefined**, **T = text** (kodda tanımlı, örn. `T main`). puts libc'dedir; linker bağlar."},
    {"week": "c-h3", "q": "Kodda `printf(\"Merhaba!\\n\");` yazılmasına rağmen assembly'de neden `call puts@PLT` görülür?",
     "options": ["printf ve puts aynı fonksiyondur", "Sabit, format belirteci olmayan ve \\n ile biten metni derleyici daha basit olan puts'a çevirir", "Ön işlemci printf'i siler", "Linker printf'i puts ile değiştirir"], "answer": 1,
     "explain": "gcc optimizasyonu: biçimlendirme gerektirmeyen ve satır sonu ile biten printf çağrısını puts ile değiştirir (puts zaten \\n ekler)."},
    {"week": "c-h3", "q": "Assembly'deki `addl $3, %eax` satırı C'deki hangi işleme karşılık gelir?",
     "options": ["x = 3", "eax register'ına 3 ekler (x = x + 3'ün toplama adımı)", "eax'i 3 ile çarpar", "3'ü belleğe yazar"], "answer": 1,
     "explain": "`int x = 5; x = x + 3;` → movl $5,-4(%rbp) (x=5) · movl -4(%rbp),%eax (eax=x) · **addl $3,%eax (eax+=3)** · movl %eax,-4(%rbp) (x=eax)."},
    {"week": "c-h3", "q": "Aşağıdaki kod derlenmeye (`gcc main.c -o main`) çalışıldığında ne olur?", "lang": "c",
     "code": "#include <stdio.h>\n\nint topla(int a, int b);   // sadece prototip\n\nint main() {\n    printf(\"%d\\n\", topla(2, 3));\n    return 0;\n}",
     "options": ["5 yazar", "Derleme aşaması geçer ama bağlamada 'undefined reference to topla' hatası alınır", "Ön işleme hatası alınır", "Çalışma zamanında segmentation fault olur"], "answer": 1,
     "explain": "Prototip derleyiciyi tatmin eder ama topla'nın **tanımı** hiçbir obje dosyasında yok → linker (ld) hatası: undefined reference to 'topla'.",
     "run": "#include <stdio.h>\n\nint topla(int a, int b);\n\nint main() {\n    printf(\"%d\\n\", topla(2, 3));\n    return 0;\n}\n", "expect_error": True},
    {"week": "c-h3", "q": "`gcc a.c b.c -o prog` komutunda \"b.o: multiple definition of 'yardimci'\" hatası alınıyor. Neden?",
     "options": ["yardimci hiç tanımlanmamış", "yardimci fonksiyonu hem a.c'de hem b.c'de tanımlanmış (çift tanım)", "b.c'de noktalı virgül eksik", "-pthread unutulmuş"], "answer": 1,
     "explain": "Linker aynı sembolün iki tanımını birleştiremez. Çözüm: tanımı tek dosyada bırak, diğerinde yalnızca prototip kullan."},
    {"week": "c-h3", "q": "ELF dosyasında başlatılmamış global değişkenler hangi bölümde tutulur?",
     "options": [".text", ".data", ".bss", "ELF Header"], "answer": 2,
     "explain": ".text makine kodu · .data **başlatılmış** globaller · **.bss başlatılmamış** globaller · sembol tablosu main/printf gibi semboller."},
    {"week": "c-h3", "q": "Bir programın bağlı olduğu paylaşımlı kütüphaneleri (libc.so.6 vb.) listeleyen komut hangisidir?",
     "options": ["nm", "ldd", "file", "strace"], "answer": 1,
     "explain": "ldd → linux-vdso.so.1, libc.so.6, ld-linux-x86-64.so.2. nm semboller, file dosya türü, strace sistem çağrıları."},
    {"week": "c-h3", "q": "strace çıktısındaki `write(1, \"Merhaba, dünya!\\n\", 17) = 17` satırında 1 ve sondaki 17 neyi ifade eder?",
     "options": ["1 = PID, 17 = süre", "1 = stdout dosya tanımlayıcısı, 17 = yazılan bayt sayısı", "1 = satır numarası, 17 = karakter kodu", "1 = başarı, 17 = hata kodu"], "answer": 1,
     "explain": "fd 1 standart çıktıdır. \"Merhaba, dünya!\\n\" UTF-8'de 17 bayttır ('ü' 2 bayt). Syscall yazılan bayt sayısını döndürür."},
    {"week": "c-h3", "q": "Aşağıdaki programın çıktısı nedir?", "lang": "c",
     "code": "#include <unistd.h>\n\nint main() {\n    write(1, \"Merhaba\\n\", 3);\n    write(1, \"\\n\", 1);\n    return 0;\n}",
     "options": ["Merhaba", "Mer", "Merhaba\\n\\n", "Derleme hatası (printf yok)"], "answer": 1,
     "explain": "write'ın üçüncü parametresi yazılacak bayt sayısıdır: yalnızca ilk 3 bayt (\"Mer\") yazılır, ardından satır sonu.",
     "run": "#include <unistd.h>\n\nint main() {\n    write(1, \"Merhaba\\n\", 3);\n    write(1, \"\\n\", 1);\n    return 0;\n}\n", "expect": "Mer"},
    {"week": "c-h3", "q": "Çalıştırılabilir dosyayı diskten belleğe yükleyip process hâline getiren mekanizma hangisidir?",
     "options": ["Linker – ld", "Loader – exec()", "Ön işlemci – cpp", "Assembler – as"], "answer": 1,
     "explain": "Loader: Disk (./program, ELF) → exec() → RAM (kod yüklendi, veri hazır) → Process (PID, çalışıyor)."},
    {"week": "c-h3", "q": "Linux'ta canlı (sürekli güncellenen) process izleme için kullanılan komut hangisidir?",
     "options": ["ps -ef", "top", "df -h", "uname -a"], "answer": 1,
     "explain": "top canlı izler; ps -ef statik liste verir; df -h disk, free -h bellek, uname -a kernel bilgisi."},
    {"week": "c-h3", "q": "Disk kullanımını ve dosya sistemlerinin bağlandığı yeri (Mounted on) gösteren komut hangisidir?",
     "options": ["free -h", "df -h", "lsblk", "uptime"], "answer": 1,
     "explain": "df -h: Filesystem, Size, Used, Avail, Use%, Mounted on. free -h bellek kullanımını gösterir."},
    {"week": "c-h3", "q": "`gcc merhaba.c -o merhaba` başarılı oldu ama `merhaba` yazınca program çalışmıyor. Slayttaki çözüm nedir?",
     "options": ["sudo apt install build-essential", "Programı ./merhaba şeklinde çalıştırmak", "-pthread eklemek", "merhaba.o dosyasını çalıştırmak"], "answer": 1,
     "explain": "Bulunduğun dizin PATH'te değildir; çalıştırılabilir dosya `./program` ile çağrılır. 'command not found: gcc' ise build-essential kurulumu gerektirir."},
    # ───────────── Hafta 1–2 ek sorular (C_Programlamaya_Giris_Kapsamli.pdf, output.pdf) — id'ler kaymasın diye sona eklendi ─────────────
    {"week": "c-h1", "q": "İşletim sistemi çekirdeklerinin (Linux, macOS vb.) ağırlıklı olarak C ile yazılmasının en temel sebebi hangisidir?",
     "options": ["Öğrenilmesi en kolay dil olması", "Web uygulamaları için ideal olması", "Düşük seviye bellek kontrolüne imkân verip OS kavramlarını görünür kılması", "Nesne yönelimli bir dil olması"], "answer": 2,
     "explain": "C doğrudan bellek adresleriyle çalışır ve POSIX API'leri (fork, pthread_create, sem_wait) C ile çağrılır. C nesne yönelimli değildir."},
    {"week": "c-h1", "q": "Ondalıklı bir float değeri printf ile yazdırmak için hangi format belirteci kullanılır?",
     "options": ["%d", "%s", "%c", "%f"], "answer": 3,
     "explain": "%f float/double · %d int · %s string · %c char. Basamak sınırı için %.2f."},
    {"week": "c-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int a = 10, b = 3;\nfloat ort = (a + b) / 2;\nprintf(\"%.1f\\n\", ort);",
     "options": ["6.5", "6.0", "7.0", "Derleme hatası"], "answer": 1,
     "explain": "(a + b) / 2 → 13 / 2 iki int'in bölümüdür = **6**; sonra float'a 6.0 olarak atanır. Doğrusu: (a + b) / 2.0 veya (float)(a + b) / 2 → 6.5.",
     "run": c_prog('int a = 10, b = 3;\nfloat ort = (a + b) / 2;\nprintf("%.1f\\n", ort);'), "expect": "6.0"},
    {"week": "c-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int a = 10, b = 4;\nprintf(\"%.2f %.2f\\n\", (float)a / b, (float)(a / b));",
     "options": ["2.50 2.50", "2.50 2.00", "2.00 2.50", "2.00 2.00"], "answer": 1,
     "explain": "(float)a / b: önce a float'a çevrilir, bölme ondalık yapılır → 2.50. (float)(a / b): önce int bölmesi 10/4 = 2, sonra çevrilir → 2.00.",
     "run": c_prog('int a = 10, b = 4;\nprintf("%.2f %.2f\\n", (float)a / b, (float)(a / b));'), "expect": "2.50 2.00"},
    {"week": "c-h1", "q": "`gcc -Wall program.c -o program` komutundaki -Wall seçeneğinin görevi nedir?",
     "options": ["Hata ayıklama bilgisi ekler", "Şüpheli durumlar için tüm yaygın uyarıları açar", "Kodu optimize eder", "Çıktı dosyasının adını belirler"], "answer": 1,
     "explain": "-Wall (Warnings All) uyarıları açar · -g gdb için hata ayıklama bilgisi · -O3 optimizasyon · -o çıktı adı."},
    {"week": "c-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int x = 3;\nif (x = 5)\n    printf(\"A %d\\n\", x);\nelse\n    printf(\"B %d\\n\", x);",
     "options": ["B 3", "A 5", "A 3", "Derleme hatası"], "answer": 1,
     "explain": "`x = 5` bir **atamadır**: x 5 olur ve ifadenin değeri 5 (sıfırdan farklı = doğru) → if bloğu çalışır: \"A 5\". Karşılaştırma için `==` gerekir (gcc -Wall uyarı verir).",
     "run": c_prog('int x = 3;\nif (x = 5)\n    printf("A %d\\n", x);\nelse\n    printf("B %d\\n", x);'), "expect": "A 5"},
    {"week": "c-h1", "q": "yas değişkeni 18 ile 65 arasında (ikisi de dahil) ise doğru olan ifade hangisidir?",
     "options": ["yas >= 18 || yas <= 65", "yas > 18 && yas < 65", "yas >= 18 && yas <= 65", "yas == 18 && yas == 65"], "answer": 2,
     "explain": "İki koşul birlikte sağlanmalı → &&; uçlar dahil → >= ve <=. || ile yazılırsa her sayı koşulu sağlar."},
    {"week": "c-h1", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "printf(\"%d %d %d\\n\", 15 % 4, 6 & 3, 6 && 3);",
     "options": ["3 2 1", "3 1 1", "3.75 2 1", "1 2 6"], "answer": 0,
     "explain": "15 % 4 = 3 (kalan) · 6 & 3: 110 & 011 = 010 = 2 (bitwise) · 6 && 3: iki taraf da sıfırdan farklı → 1 (mantıksal).",
     "run": c_prog('printf("%d %d %d\\n", 15 % 4, 6 & 3, 6 && 3);'), "expect": "3 2 1"},
    {"week": "c-h1", "q": "Dış döngü 3 kez, iç döngü 4 kez dönecek şekilde iç içe iki for yazılmıştır. İç döngünün gövdesi toplam kaç kez çalışır?",
     "options": ["7", "3", "4", "12"], "answer": 3,
     "explain": "Dış döngünün her turu için iç döngü baştan sona döner: 3 × 4 = 12."},
    {"week": "c-h1", "q": "`for (int i = 0; i <= 10; i++)` döngüsü kaç kez döner?",
     "options": ["10", "11", "9", "Sonsuz"], "answer": 1,
     "explain": "i = 0, 1, …, 10 → 11 tur. 0'dan başlayıp `<= n` kullanmak n+1 tur verir; n tur için `i < n`."},
    {"week": "c-h1", "q": "Tüm fonksiyonların dışında, dosyanın en üstünde tanımlanan ve her fonksiyondan erişilebilen değişkene ne denir?",
     "options": ["Küresel (global) değişken", "Yerel (local) değişken", "Parametre", "Prototipli değişken"], "answer": 0,
     "explain": "Global değişken her yerden erişilir; yerel değişken yalnızca tanımlandığı { } bloğunda yaşar."},
    {"week": "c-h1", "q": "double tipindeki bir değişkene scanf ile değer okurken hangi belirteç kullanılmalıdır?",
     "options": ["%d", "%f", "%lf", "%ld"], "answer": 2,
     "explain": "scanf'te double için %lf şarttır (%f float içindir). %ld long tam sayı belirtecidir."},
    {"week": "c-h1", "q": "`scanf(\"%d\", yas);` (& unutulmuş) satırı çalıştığında genellikle ne olur?",
     "options": ["Sorunsuz çalışır", "yas'ın içindeki çöp değer adres sanılıp oraya yazılmaya çalışılır → çökme (Segmentation fault)", "Derleyici & işaretini otomatik ekler", "yas 0 olur"], "answer": 1,
     "explain": "scanf değeri yazacağı ADRESİ bekler; &yas yerine yas verilince rastgele bir adrese yazmaya çalışır. gcc -Wall bunun için uyarı verir."},
    {"week": "c-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "void arttir(int *x) {\n    *x = *x + 5;\n}\n\nint main() {\n    int a = 10;\n    arttir(&a);\n    printf(\"a = %d\\n\", a);\n    return 0;\n}",
     "options": ["a = 10", "a = 15", "a = 5", "Adres değeri yazılır"], "answer": 1,
     "explain": "Adres ile aktarım: fonksiyon a'nın adresini alır, *x = *x + 5 doğrudan a'yı değiştirir → 15.",
     "run": "#include <stdio.h>\n\nvoid arttir(int *x) {\n    *x = *x + 5;\n}\n\nint main() {\n    int a = 10;\n    arttir(&a);\n    printf(\"a = %d\\n\", a);\n    return 0;\n}\n", "expect": "a = 15"},
    {"week": "c-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "char isim[] = \"Ali\";\nprintf(\"%d %d\\n\", (int)sizeof(isim), (int)strlen(isim));",
     "options": ["3 3", "4 3", "3 4", "4 4"], "answer": 1,
     "explain": "sizeof dizinin bellekte kapladığı bayttır ('\\0' dahil) = 4; strlen karakter sayısıdır ('\\0' hariç) = 3.",
     "run": c_prog('char isim[] = "Ali";\nprintf("%d %d\\n", (int)sizeof(isim), (int)strlen(isim));', ("stdio.h", "string.h")), "expect": "4 3"},
    {"week": "c-h2", "q": "`char s[4] = \"Test\";` tanımının sorunu nedir?",
     "options": ["Sorun yoktur", "\"Test\" 4 harf + '\\0' = 5 bayt gerektirir; '\\0' sığmaz, string bozulur", "char dizisine ilk değer verilemez", "Dizinin adı s olamaz"], "answer": 1,
     "explain": "String'in sonunda '\\0' olmalıdır; olmazsa printf(\"%s\") ve strlen nerede duracağını bilemez, bellekte okumaya devam eder."},
    {"week": "c-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int a[5] = {10, 20, 30, 40, 50};\nint *p = a;\nprintf(\"%d %d\\n\", *p + 1, *(p + 1));",
     "options": ["11 20", "20 20", "11 11", "20 11"], "answer": 0,
     "explain": "*p + 1: önce *p = 10, sonra +1 → 11. *(p + 1): bir sonraki elemanın değeri → 20.",
     "run": c_prog('int a[5] = {10, 20, 30, 40, 50};\nint *p = a;\nprintf("%d %d\\n", *p + 1, *(p + 1));'), "expect": "11 20"},
    {"week": "c-h2", "q": "`int *p` bir int dizisini gösteriyor ve int 4 bayttır. p'nin adresi 1000 ise `p + 1` hangi adresi gösterir?",
     "options": ["1001", "1004", "1008", "2000"], "answer": 1,
     "explain": "Pointer aritmetiği eleman bazındadır: p + 1 = adres + sizeof(int) = 1004. char* olsaydı 1001 olurdu."},
    {"week": "c-h2", "q": "Aşağıdaki kodun çıktısı nedir?", "lang": "c",
     "code": "int a[5] = {1, 2};\nprintf(\"%d %d\\n\", a[1], a[4]);",
     "options": ["2 0", "2 çöp değer", "1 2", "Derleme hatası"], "answer": 0,
     "explain": "Kısmi ilk değer verilen dizide eksik kalan elemanlar 0 ile doldurulur: a = {1, 2, 0, 0, 0}.",
     "run": c_prog('int a[5] = {1, 2};\nprintf("%d %d\\n", a[1], a[4]);'), "expect": "2 0"},
    {"week": "c-h2", "q": "İki string'in içeriğinin aynı olup olmadığını doğru şekilde kontrol eden ifade hangisidir?",
     "options": ["if (s1 == s2)", "if (strcmp(s1, s2) == 0)", "if (strcpy(s1, s2))", "if (strlen(s1) == strlen(s2))"], "answer": 1,
     "explain": "== iki dizinin ADRESLERİNİ karşılaştırır. strcmp içerikleri karşılaştırır, eşitse 0 döndürür. Uzunluk eşitliği içerik eşitliği değildir."},
    {"week": "c-h2", "q": "`struct Ogrenci *p = &o1;` iken aşağıdakilerden hangisi HATALIDIR?",
     "options": ["p->no = 5;", "(*p).no = 5;", "p.no = 5;", "o1.no = 5;"], "answer": 2,
     "explain": "p bir pointer olduğu için nokta ile erişilemez; p->no ya da (*p).no yazılmalıdır. o1.no doğrudan struct değişkeni üzerinden erişimdir."},
    {"week": "c-h2", "q": "Buffer overflow (arabellek taşması) neden OS güvenliğinde tehlikelidir?",
     "options": ["Programı sadece yavaşlatır", "Taşan veri komşu alanları ve fonksiyonun dönüş adresini ezerek saldırganın programın akışını değiştirmesine izin verebilir", "Sadece derleme sırasında oluşur", "Diski doldurur"], "answer": 1,
     "explain": "C dizilerde sınır kontrolü yapmaz; stack'te taşan veri dönüş adresine ulaşırsa saldırgan kendi kodunu çalıştırabilir."},
    {"week": "c-h2", "q": "Aynı program terminalden art arda iki kez çalıştırılıyor. Hangisi doğrudur?",
     "options": ["İki çalıştırma aynı PID'i alır", "Her çalıştırma farklı PID'li yeni bir process'tir; parent'ları genellikle bash'tir", "İkinci çalıştırma birincinin devamıdır", "PID her zaman 1'dir"], "answer": 1,
     "explain": "Program ≠ process: her çalıştırma yeni process (fork + exec) ve yeni PID demektir; getppid() çağıran kabuğun PID'ini verir."},
    {"week": "c-h3", "q": "Aşağıdaki hata mesajlarından hangisi BAĞLAMA (linking) aşamasında ortaya çıkar?",
     "options": ["expected ';' before '}' token", "stdio.h: No such file or directory", "undefined reference to 'topla'", "'x' undeclared"], "answer": 2,
     "explain": "undefined reference / multiple definition → ld (bağlama). Eksik ; ve tanımsız değişken → derleme (cc1). Bulunamayan başlık dosyası → ön işleme (cpp)."},
    {"week": "c-h3", "q": "Statik bağlama (`gcc -static`) ile derlenmiş bir program için hangisi doğrudur?",
     "options": ["Dosya boyutu dinamik derlemeden daha küçüktür", "libc kodu çalıştırılabilir dosyanın içine kopyalanır; ldd 'not a dynamic executable' der", "Çalışırken libc.so.6'ya ihtiyaç duyar", "Bağlama aşaması atlanır"], "answer": 1,
     "explain": "Varsayılan dinamik bağlamada kütüphane çalışırken yüklenir (ldd libc.so.6'yı listeler, dosya küçük). Statik bağlamada kütüphane koda gömülür, dosya büyür."},
    {"week": "c-h3", "q": "`int sayac = 5;` ve `int toplam;` global değişkenleri ELF dosyasında sırasıyla hangi bölümlerde tutulur?",
     "options": [".text – .data", ".data – .bss", ".bss – .data", ".rodata – .text"], "answer": 1,
     "explain": "Başlatılmış global → .data (nm'de D) · başlatılmamış global → .bss (nm'de B, 0 ile başlar). Fonksiyon kodu .text'tedir."},
    # ── Hafta 4: Process ──
    {"week": "c-h4", "q": "Program ile process arasındaki fark hangisinde doğru verilmiştir?",
     "options": ["Program çalışan koddur, process diskteki dosyadır", "Program diskteki statik dosyadır, process onun çalışan dinamik hâlidir",
                 "İkisi aynı şeydir", "Process sadece kernel'da çalışan programdır"], "answer": 1,
     "explain": "Program diskte duran dosya (./merhaba, statik); process çalışan program (PID'li, dinamik). Aynı program iki kez çalışırsa iki process olur."},
    {"week": "c-h4", "q": "Aşağıdakilerden hangisi PCB (Process Control Block) içinde tutulan bilgilerden DEĞİLDİR?",
     "options": ["Program Counter", "Parent PID (PPID)", "Programın kaynak kodu (.c dosyası)", "Açık dosyalar (stdin, stdout, fd)"], "answer": 2,
     "explain": "PCB: PID, state, PC, CPU register'ları, bellek bilgisi, açık dosyalar, PPID, zamanlama bilgisi. Kaynak kod PCB'de yer almaz."},
    {"week": "c-h4", "q": "Disk okuması bekleyen (WAITING) bir process'in okuma bittiğinde geçtiği durum hangisidir?",
     "options": ["RUNNING", "READY", "NEW", "TERMINATED"], "answer": 1,
     "explain": "I/O done → READY. CPU'ya tekrar zamanlayıcı (dispatch) ile geçer; doğrudan RUNNING'e gitmez."},
    {"week": "c-h4", "q": "Çalışan (RUNNING) bir process'in zaman dilimi dolduğunda (interrupt) geçtiği durum hangisidir?",
     "options": ["WAITING", "READY", "TERMINATED", "NEW"], "answer": 1,
     "explain": "interrupt: RUNNING → READY. RUNNING → WAITING ise I/O beklerken olur."},
    {"week": "c-h4", "q": "Tek çekirdekli bir CPU'da birden çok programın 'aynı anda' çalışıyor görünmesi nasıl açıklanır?",
     "options": ["Gerçek paralellik (parallelism)", "Eşzamanlılık (concurrency): OS process'ler arasında hızla geçiş yapar",
                 "Her process ayrı bir CPU'da çalışır", "Process'ler sırayla, biri bitmeden diğeri başlamaz"], "answer": 1,
     "explain": "Tek çekirdekte bir anda yalnız 1 process çalışır; OS saniyede yüzlerce kez değiştirir. Gerçek paralellik çok çekirdekte mümkündür."},
    {"week": "c-h4", "q": "pid_t pid = fork(); satırından sonra CHILD process'te pid değişkeninin değeri nedir?",
     "options": ["Child'ın kendi PID'i", "Parent'ın PID'i", "0", "−1"], "answer": 2,
     "explain": "fork child'da 0, parent'ta child'ın PID'ini (> 0), hata durumunda −1 döndürür. Child kendi PID'ini getpid() ile öğrenir."},
    {"week": "c-h4", "q": "fork() çağrısı −1 döndürürse bu ne anlama gelir?",
     "options": ["Child process oluşturuldu", "Kod child'da çalışıyor", "fork başarısız oldu, yeni process oluşmadı", "Parent sonlandı"], "answer": 2,
     "explain": "pid < 0 → hata (örn. process sınırı). Bu yüzden slayttaki örnek önce if (pid < 0) kontrol eder."},
    {"week": "c-h4", "q": "Aşağıdaki kod çalıştırıldığında ekrana kaç satır 'fork'tan sonra' yazılır?", "lang": "c",
     "code": "printf(\"fork'tan önce\\n\");\npid_t pid = fork();\nprintf(\"fork'tan sonra\\n\");",
     "options": ["1", "2", "3", "4"], "answer": 1,
     "explain": "fork'tan sonra iki process (parent + child) vardır ve ikisi de sonraki satırdan devam eder → 2 kez."},
    {"week": "c-h4", "q": "int x = 100; fork sonrası child x = 200 yapıp yazdırıyor, parent 1 saniye bekleyip x'i yazdırıyor. Çıktı nedir?",
     "options": ["CHILD: x=200, PARENT: x=200", "CHILD: x=200, PARENT: x=100", "CHILD: x=100, PARENT: x=100", "CHILD: x=100, PARENT: x=200"], "answer": 1,
     "explain": "fork belleği kopyalar; child kendi kopyasını değiştirir. Parent'taki x 100 kalır (ayrı bellek alanları)."},
    {"week": "c-h4", "q": "Aşağıdaki programın çıktısı nedir?", "lang": "c",
     "code": "pid_t pid = fork();\nif (pid == 0) {\n    return 42;\n} else {\n    int status;\n    wait(&status);\n    if (WIFEXITED(status))\n        printf(\"%d\\n\", WEXITSTATUS(status));\n}",
     "options": ["0", "42", "Child'ın PID'i", "Hiçbir şey"], "answer": 1,
     "explain": "Child 42 ile çıkar; parent wait ile bekler ve WEXITSTATUS(status) çıkış kodunu (42) verir.",
     "run": c_prog('pid_t pid = fork();\nif (pid == 0) {\n    return 42;\n} else {\n    int status;\n    wait(&status);\n    if (WIFEXITED(status))\n        printf("%d\\n", WEXITSTATUS(status));\n}', ("stdio.h", "unistd.h", "sys/wait.h")), "expect": "42"},
    {"week": "c-h4", "q": "Aşağıdaki programın çıktısı nedir? (child önce yazar, parent wait ile bekler)", "lang": "c",
     "code": "int x = 100;\npid_t pid = fork();\nif (pid == 0) {\n    x = 200;\n    printf(\"C %d\\n\", x);\n    return 0;\n}\nwait(NULL);\nprintf(\"P %d\\n\", x);",
     "options": ["C 200 / P 200", "C 200 / P 100", "P 100 / C 200", "C 100 / P 100"], "answer": 1,
     "explain": "wait, parent'ı child bitene kadar bekletir → önce 'C 200'. Bellek kopyalandığı için parent'taki x 100 kalır.",
     "run": c_prog('int x = 100;\npid_t pid = fork();\nif (pid == 0) {\n    x = 200;\n    printf("C %d\\n", x);\n    return 0;\n}\nwait(NULL);\nprintf("P %d\\n", x);', ("stdio.h", "unistd.h", "sys/wait.h")), "expect": "C 200\nP 100"},
    {"week": "c-h4", "q": "Child process bitmiş ancak parent wait() çağırmamışsa child hangi duruma düşer?",
     "options": ["Yetim (orphan)", "Zombi (zombie)", "READY", "Daemon"], "answer": 1,
     "explain": "Zombi: kaynakları yok, sadece PID/süreç tablosu girdisi kalır; ps'te <defunct> görünür. Önlemek için wait/waitpid."},
    {"week": "c-h4", "q": "Parent process child'dan önce sonlanırsa child için ne olur?",
     "options": ["Child da hemen sonlanır", "Zombi olur", "Yetim olur ve init (PID 1) tarafından evlat edinilir", "PID'i 0 olur"], "answer": 2,
     "explain": "Yetim (orphan): child çalışmaya devam eder, yeni PPID = 1 (init/systemd)."},
    {"week": "c-h4", "q": "execl(\"/bin/ls\", \"ls\", \"-l\", NULL); başarılı olursa aşağıdakilerden hangisi doğrudur?",
     "options": ["Yeni bir PID ile yeni process oluşur", "exec'ten sonraki printf satırı çalışır",
                 "Process'in programı ls ile değişir, PID aynı kalır ve exec geri dönmez", "Parent process sonlanır"], "answer": 2,
     "explain": "exec mevcut process'in kod/veri/belleğini yeni programla değiştirir; PID değişmez. Sonraki satıra sadece exec başarısız olursa gelinir."},
    {"week": "c-h4", "q": "Bir shell (bash) kullanıcının yazdığı komutu çalıştırmak için hangi üçlüyü kullanır?",
     "options": ["fork + exec + wait", "exec + fork + sleep", "getpid + exec + exit", "wait + fork + kill"], "answer": 0,
     "explain": "Parent fork() eder, child exec ile komutu yükler, parent wait ile bitmesini bekler ve çıkış kodunu alır."},
    {"week": "c-h4", "q": "for (int i = 0; i < 3; i++) fork(); kodu sonunda toplam kaç process olur (orijinal dahil)?",
     "options": ["3", "4", "6", "8"], "answer": 3,
     "explain": "Her fork process sayısını ikiye katlar: 2³ = 8 (1 orijinal + 7 yeni)."},
    {"week": "c-h4", "q": "printf(\"A\"); fork(); printf(\"B\"); fork(); printf(\"C\"); kodunda (terminale yazarken) kaç A, B, C yazılır?",
     "options": ["1 A, 2 B, 3 C", "1 A, 2 B, 4 C", "2 A, 2 B, 4 C", "1 A, 1 B, 1 C"], "answer": 1,
     "explain": "A fork'tan önce (1 process), B ilk fork'tan sonra (2 process), C ikinci fork'tan sonra (4 process)."},
    {"week": "c-h4", "q": "wait() ile sleep() karşılaştırmasında hangisi doğrudur?",
     "options": ["sleep child bitince döner ve çıkış kodunu verir", "wait süreye bağlıdır, sleep duruma bağlıdır",
                 "wait child biter bitmez döner ve çıkış kodunu almayı sağlar; sleep kör beklemedir", "İkisi de aynı işi yapar"], "answer": 2,
     "explain": "sleep(n) n saniye bekler (çocuk erken bitse bile); wait duruma bağlıdır ve status ile çıkış kodunu verir. Doğrusu wait/waitpid."},
    {"week": "c-h4", "q": "fork tabanlı bir web sunucusunda parent'ın döngüde waitpid(-1, NULL, WNOHANG) çağırmasının amacı nedir?",
     "options": ["Yeni istemci kabul etmek", "Biten child'ları bloke olmadan toplayıp zombi oluşmasını önlemek", "Child'ı öldürmek", "Socket'i kapatmak"], "answer": 1,
     "explain": "WNOHANG beklemeden döner; biten child'lar toplanır (reap), zombi birikmez."},
    {"week": "c-h4", "q": "wait() ve WEXITSTATUS makrosu hangi başlık dosyasında tanımlıdır?",
     "options": ["<stdio.h>", "<unistd.h>", "<sys/wait.h>", "<string.h>"], "answer": 2,
     "explain": "wait/waitpid, WIFEXITED, WEXITSTATUS → <sys/wait.h>. fork, getpid, exec, sleep → <unistd.h>; pid_t → <sys/types.h>."},
]
