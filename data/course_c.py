"""İşletim Sistemleri ve Güvenliği — C ile Giriş (Hafta 1 & 2).

Kaynaklar: Hafta01_C_Giris.pdf, Hafta02_C_Giris_II.pdf (diyagram sayfaları görsel olarak okundu).
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
    "sources": ["Hafta01_C_Giris.pdf", "Hafta02_C_Giris_II.pdf"],
    "weeks": [
        {
            "id": "c-h1",
            "title": "Hafta 1 — C Programlamaya Giriş I",
            "sources": ["Hafta01_C_Giris.pdf"],
            "summary": """
**Neden C?** Linux, Windows çekirdeği ve macOS büyük ölçüde C ile yazılmıştır; POSIX API'leri (`fork()`, `pthread_create()`, `sem_wait()`) C ile çağrılır;
düşük seviye bellek kontrolü OS kavramlarını görünür kılar. *Bu ders C programlama dersi değil, C'yi araç olarak kullanma dersidir.*

**Program yapısı:** `#include <stdio.h>` (kütüphane) → `int main() {` (başlangıç) → komutlar → `return 0;` (dönüş) → `}` (kapanış).

**printf:** `\\n` yeni satır · **`%d`** tam sayı · **`%f`** ondalık · **`%s`** string · **`%c`** karakter · `%p` adres · `%.2f` iki basamak.
Soru: `printf("%d\\n", 3.14);` → format double ile uyuşmaz → **tanımsız davranış** (gcc `-Wall` uyarı verir, anlamsız sayı basılır).

**Derleme:** `nano merhaba.c` → `gcc merhaba.c -o merhaba` → `./merhaba`. `-o` verilmezse çıktı **a.out** olur. `-Wall` uyarıları göster, `-g` hata ayıklama bilgisi.
Linux'ta çalıştırılabilir dosya **`./`** ile çağrılır. Aşamalar: **Ön işleme → Derleme → Assembly → Bağlama**.

**Veri tipleri:** `int` (42, −7) · `float` (3.14) · `double` (daha hassas) · `char` ('A' — tek karakter; string için `char[]`). Değişken kullanılmadan önce tanımlanmalıdır.

**Operatörler:** `+ - * / %` — **DİKKAT: int / int → int** (10/3 = 3), `10 % 3 = 1` · karşılaştırma `== != < > <= >=` (**`=` atama, `==` karşılaştırma!**) ·
mantık `&&` VE, `||` VEYA, `!` DEĞİL · `&` bitwise AND.

**Kontrol:** `if`, `if/else`, `else if` zinciri (**sıralama önemli, en yüksek koşul önce**).
Mini alıştırma `x = 15` → ilk if "A" basar; ikinci if/else'de x>20 yanlış → "C" → çıktı **AC**.

**Döngüler:** `for (başlangıç; koşul; artış)` — başlangıç bir kez, koşul her turda, artış her turdan sonra · `while` (koşula bağlı; `i++` unutulursa **sonsuz döngü**) ·
`do-while` (**en az bir kez** çalışır; i=10, koşul i<=5 → yine "10" basar). Seçim: **for** kaç kez belli, **while** koşula bağlı, **do-while** en az bir kez.
`i <= n` vs `i < n` → tur sayısı farkı. `break` döngüden çıkar (1 2 3 4), `continue` turu atlar (1 2 4 5).

**Fonksiyonlar:** bir kez yazılır, defalarca çağrılır; parametre alır, değer döndürür (`int kare(int x)`), `void` değer döndürmez.
**Prototip** (`int kare(int x);`) main'den önce yazılır → main'den sonra tanımlanan fonksiyonu derleyici önceden tanır.
**Kapsam:** global her yerden, yerel sadece tanımlandığı blokta.

**scanf:** `scanf("%d", &yas);` — **`&yas` değişkenin adresi** (scanf değeri o adrese yazar).

**Derleme hatalarını okuma:** `merhaba.c:3:22: error: expected ';' before '}' token` → dosya merhaba.c, **satır 3, sütun 22**, noktalı virgül eksik.
İlk hatayı düzelt, tekrar derle — zincirleme hatalar normaldir.
Yaygın: `expected ';'` · `undeclared identifier` (tanımsız değişken) · `implicit declaration of printf` (**#include <stdio.h> eksik**) · `format '%d' expects int`.

**Örnekler:** harf notu (else-if), 1'den N'e toplam, faktöriyel (`long` → 13! üzeri için şart, `%ld`).
**Sık hatalar:** `=` yerine `==` · `;` unutmak · sonsuz döngü · int bölmesi (ondalık için float) · scanf'te `&` unutmak.
""",
            "concepts": [
                ("%d / %f / %s / %c / %p", "Tam sayı / ondalık / string / karakter / adres format belirteçleri."),
                ("int / int", "Sonuç tam sayıdır; ondalık kısım atılır (10/3 = 3)."),
                ("do-while", "Koşul sonda kontrol edilir; gövde en az bir kez çalışır."),
                ("Prototip", "Fonksiyonun main'den önce bildirimi: int kare(int x);"),
                ("-Wall", "gcc'nin tüm yaygın uyarıları göstermesini sağlar."),
                ("&değişken", "Değişkenin bellek adresi; scanf için gerekli."),
            ],
            "must": ["printf format belirteçleri ve %d ile 3.14 tuzağı", "int bölmesi ve % mod", "= ile == farkı", "Mini alıştırma çıktısı: AC",
                     "do-while en az bir kez (i=10 → 10)", "break (1 2 3 4) / continue (1 2 4 5)", "Hata mesajı okuma: dosya:satır:sütun",
                     "implicit declaration of printf → #include <stdio.h> eksik", "Derleme aşamaları: Ön işleme → Derleme → Assembly → Bağlama"],
            "cheat": [{"title": "Format belirteçleri", "columns": ["Belirteç", "Tip", "Örnek"], "rows": [
                ["%d", "int", 'printf("%d", 42)'], ["%ld", "long", 'printf("%ld", fakt)'], ["%f / %.2f", "float/double", 'printf("%.2f", 3.14159) → 3.14'],
                ["%c", "char", "printf(\"%c\", 'A')"], ["%s", "string (char[])", 'printf("%s", "OS")'], ["%p", "adres", 'printf("%p", &x)']]},
                      {"title": "GCC", "columns": ["Komut", "Anlam"], "rows": [
                ["gcc a.c -o a", "Derle, çıktı adı a"], ["gcc a.c", "Çıktı a.out"], ["gcc -Wall a.c -o a", "Uyarıları göster"],
                ["gcc -g a.c -o a", "Hata ayıklama bilgisi"], ["./a", "Çalıştır"]]}],
            "images": [("c_program_yapisi.jpg", "Bir C programının yapısı (Hafta01 s.4)"), ("c_for_anatomi.jpg", "for döngüsünün üç parçası (s.18)"),
                       ("c_derleme_asamalari.jpg", "Kaynak koddan çalıştırılabilir dosyaya: ön işleme → derleme → assembly → bağlama (s.30)")],
            "templates": ["c_merhaba", "c_printf", "c_operatorler", "c_mini_alistirma", "c_harf_notu", "c_for", "c_ic_ice_for", "c_while",
                          "c_do_while", "c_break_continue", "c_fonksiyon", "c_prototip", "c_scope", "c_toplam_n", "c_faktoriyel", "c_hatali_noktali_virgul"],
        },
        {
            "id": "c-h2",
            "title": "Hafta 2 — C Programlamaya Giriş II (Dizi, String, Pointer, struct, getpid)",
            "sources": ["Hafta02_C_Giris_II.pdf"],
            "summary": """
**Dizi:** aynı tipte birden çok değer, indeks **0'dan** başlar, boyut sabit.
`int a[5];` (değer atanmamış) · `int b[5] = {1,2,3,4,5};` · `int c[5] = {1, 2};` (**kalanlar 0**) · `int d[] = {10,20,30};` (boyut otomatik 3).
**Tuzak:** `a[5] = 99;` → dizi dışı! **C sınır kontrolü YAPMAZ**; çökmese bile *undefined behavior*.
Ortalama için `toplam / 5.0` (int/int'ten kaçın) ve `%.2f`.

**String:** C'de ayrı tip DEĞİL → `char` dizisi + **`'\\0'` (null terminator)**. `char isim[] = "Ali";` → **4 karakter** ('A','l','i','\\0').
`string.h`: **`strlen`** (uzunluk, '\\0' hariç; "Merhaba" → 7) · **`strcpy(dst, src)`** kopyala · **`strcmp(a, b)`** → **0 = eşit**, pozitif/negatif fark.

**Pointer = adres tutan değişken.** `&x` → x'in adresi (`%p` ile yazdırılır) · `int *p = &x;` (int işaret eden pointer) · **`*p`** → adresteki değer;
`*p = 100;` → **x de 100 olur**. Önemi: `dizi[i] ≡ *(dizi+i)`, parametre aktarımı, OS API'leri (fork, pthread_create), `malloc()` pointer döner, string'ler `char*`.
Dizi–pointer: `a` tek başına `&a[0]` gibidir; `int *p = a;` → `*p` = 10, `*(p+1)` = 20.

**Parametre aktarımı:** **Değer ile (varsayılan)** — C değeri KOPYALAR; fonksiyon içindeki değişiklik dışarıyı etkilemez (içeride 11, dışarıda 10).
**Adres ile** — `void arttir(int *x) { *x = *x + 1; }` + `arttir(&a);` → a değişir (11). *scanf'te & kullanmamızın nedeni budur.*
**Swap:** `swap(&x, &y)` → x=7 y=3.

**struct:** farklı tipleri tek yapıda toplar (kendi veri tipin). `struct Ogrenci { int no; char ad[20]; float ort; };`
Erişim: `o1.no` (nokta) · pointer ile `p->no` ≡ `(*p).no`. **`o.ad = "Ali";` HATALI** → char[] atamayla kopyalanamaz, **`strcpy(o.ad, "Ali")`**.
OS'te her şey struct: **PCB** (Process Control Block), thread yapıları, dosya tanımlayıcıları, ağ paketleri.

**Program ≠ Process:** program diskte duran çalıştırılabilir dosya; process çalışan programın OS'teki karşılığı. Her çalıştırma **yeni process**; her process'in **PID**'i ve parent'ı vardır.
PID benzersizdir; **PID 1 = init/systemd**; küçük PID'ler (1–1000) sistem, kullanıcı process'leri genelde 1000+.
`getpid()` kendi PID, `getppid()` parent PID — **`<unistd.h>`** (POSIX başlığı), `<sys/types.h>`. **`pid_t`** POSIX PID tipi (Linux'ta int; `%d` veya `(int)` cast).
`/proc/<PID>/` → status, cmdline, fd/, maps. `sleep(1)` → 1 sn bekle (unistd.h).
Çalışma akışı: bash komutu okur → dosyayı bulur → OS yeni process yaratır (**fork + exec**) → bellek ayrılır, kod yüklenir → main() → printf terminale → return 0 → kabuk yeniden bekler.
**Bellek haritası:** Stack (yerel değişkenler, fonksiyon çağrıları) · boş alan · Heap (malloc) · Veri (.data/.bss, global/static) · Kod (.text).

**Yaygın hatalar:** `a[5]=99` sınır dışı · `char s[5] = "Merhaba";` (8 karakter sığmaz) · `int *p; *p = 5;` (**initialize edilmemiş pointer**) · `o.ad = "Ali"` · getpid'i (int) cast etmek daha güvenli.
**Güvenlik notu – Buffer Overflow:** dizi sınırı kontrol edilmezse saldırgan sınır dışına yazarak kodu değiştirebilir; OS güvenliğinde en klasik zafiyet.
""",
            "concepts": [
                ("'\\0'", "String sonlandırıcı (null terminator)."), ("strcmp", "Eşitse 0 döndürür."),
                ("*p", "p'nin gösterdiği adresteki değer (dereference)."), ("->", "Pointer üzerinden struct alanına erişim: p->no ≡ (*p).no."),
                ("PID", "İşletim sisteminin her process'e atadığı benzersiz numara."), ("Buffer overflow", "Dizi sınırının dışına yazılması; klasik güvenlik zafiyeti."),
            ],
            "must": ["int c[5] = {1,2} → kalanlar 0", "C sınır kontrolü yapmaz → undefined behavior / buffer overflow", "\"Ali\" 4 bayt ('\\0' dahil); strlen '\\0' hariç",
                     "& adres al, * değere eriş; *p = 100 → x değişir", "dizi[i] ≡ *(dizi+i)", "Değer ile aktarım kopyalar; adres ile orijinal değişir; swap",
                     "o.ad = \"Ali\" hatalı → strcpy", "getpid / getppid → unistd.h; PID 1 = init/systemd", "Program ≠ Process"],
            "cheat": [{"title": "Pointer hızlı tablo", "columns": ["İfade", "Anlam"], "rows": [
                ["int *p = &x;", "p, x'in adresini tutar"], ["*p", "Adresteki değer"], ["*p = 10;", "x'i 10 yapar"], ["p + 1", "Bir sonraki elemanın adresi"],
                ["a[i] ≡ *(a+i)", "Dizi erişimi"], ["p->alan ≡ (*p).alan", "struct pointer erişimi"]]},
                      {"title": "string.h", "columns": ["Fonksiyon", "İş", "Örnek"], "rows": [
                ["strlen(s)", "Uzunluk ('\\0' hariç)", 'strlen("Merhaba") = 7'], ["strcpy(d, s)", "Kopyala", 'strcpy(o.ad, "Ali")'],
                ["strcmp(a, b)", "Karşılaştır", '0 → eşit']]}],
            "images": [("c_pointer_mantigi.jpg", "Pointer = adres tutan değişken (Hafta02 s.12)"), ("c_ampersand_yildiz.jpg", "& ve * işlemleri özeti (s.15)"),
                       ("c_parametre_aktarimi.jpg", "Değer ile (kopya) ve adres ile (pointer) aktarım (s.18)"), ("c_bellek_haritasi.jpg", "Bir process'in bellek haritası (s.34)")],
            "templates": ["c_dizi", "c_dizi_tuzak", "c_string", "c_pointer", "c_dizi_pointer", "c_deger_aktarim", "c_adres_aktarim", "c_swap",
                          "c_struct", "c_struct_dizi", "c_struct_pointer", "c_getpid", "c_process_sleep", "c_kod_okuma"],
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
]
