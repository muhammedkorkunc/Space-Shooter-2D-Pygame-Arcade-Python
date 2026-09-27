# 🚀 Space Shooter 2D Arcade Game in Python (Pygame)

### 2D Uzay Savaşı Oyunu: Çarpışma Denetimi, Dinamik Sprite Yönetimi ve Ses Motoru

Bu depo; Bilgisayar Mühendisliği lisans programı bünyesinde Python ve Pygame kütüphanesi kullanılarak geliştirilen **2D Space Shooter (Uzay Savaşı)** arcade oyununun tam kaynak kodlarını, grafik/ses varlıklarını ve teknik proje raporunu barındırır.

---

## 🎮 Oyun Mekanikleri ve Sistem Mimarisi

| Modül / Varlık          | Dosya / Kaynak                   | Fonksiyonel Görev & Algoritma                                                                         |
| :---------------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **Ana Oyun Döngüsü**    | `Oyun2.py` / `FOR.py`            | FPS sabitleme (Clock tick), klavye olay dinleyicileri (Event Loop) ve durum güncellemeleri.           |
| **Oyuncu Kontrolü**     | `uzay_gemi.png`                  | X ve Y eksenlerinde sınırlandırılmış dinamik hareket ve sürekli mermi ateşleme mekaniği.              |
| **Düşman Yapay Zekası** | `uzayli.png`, `uzayli_mermi.png` | Rastgele x koordinatlarında doğan (spawn), aşağı yönlü mermi püskürten dalga algoritması.             |
| **Çarpışma Tespiti**    | Pygame `colliderect` / `mask`    | Oyuncu mermisi-uzaylı ve düşman mermisi-oyuncu arasındaki piksel/dikdörtgen hassasiyetli çarpışmalar. |
| **Ses & Müzik Hattı**   | `arka_plan_sarki.wav`, `.wav`    | Arka plan döngüsel müziği, ateşleme ve patlama ses efektlerinin mikser yönetimi.                      |

---

## 🕹️ Kontroller & Oynanış

- **Yön Tuşları / WASD:** Uzay gemisinin ekran sınırları içinde yönlendirilmesi.
- **Boşluk (Space):** Lazer mermisi ateşleme.
- **Hedef:** Belirlenen düşman dalgalarını yok ederek tebrik ekranına (`tebrikler.png`) ulaşmak ve can puanını korumak.

---

## 🔒 Copyright & License / Telif Hakkı Bildirimi

Bu oyun projesi, kaynak kodları, grafik/ses varlıkları ve beraberindeki proje raporu **Proprietary (Tescilli / Tüm Hakları Saklıdır)** lisansına tabidir.

```text
Copyright (c) 2026 Muhammed Emin Korkunç. All Rights Reserved.

Bu projedeki tüm Python kaynak kodları, oyun mantığı, grafik düzenlemeleri
ve rapor içerikleri Muhammed Emin Korkunç'a aittir. Yazarın açık yazılı izni
olmaksızın kısmen veya tamamen kopyalanması, paylaşılması veya ticari/akademik
amaçla izinsiz kullanımı kesinlikle yasaktır.
```

👨‍💻 Geliştirici / Author
Muhammed Emin Korkunç

GitHub: @muhammedkorkunc

LinkedIn: Muhammed Emin Korkunç

Email: muhammedemin.korkunc@gmail.com
