# Berkay AI - Sevgili Asistanı

Berkay AI, sevgilinizle doğal, samimi ve sevgi dolu sohbetler yapabilen, geçmiş konuşmaları hafızasında tutan bir yapay zeka sohbet uygulamasıdır. Hem frontend (React + Tailwind CSS) hem de backend (FastAPI + Agno Memory) ile Docker üzerinde kolayca çalıştırabilirsiniz.

## Özellikler
- Sevgili gibi davranan, insansı ve sıcak bir AI
- Tüm geçmiş konuşmaları kalıcı olarak hafızada tutar (Agno Memory V2 + SQLite)
- Kurallar dosyası (rules.txt) ile konuşma tarzı ve sınırları kolayca değiştirilebilir
- Basit ve modern bir web arayüzü
- Docker ile kolay kurulum ve çalıştırma

---

## Kurulum
    pip install -r requirements.txt

### 1. Gerekli Dosyalar
- `app.py` (Backend API)
- `frontend/` (React arayüzü)
- `rules.txt` (Konuşma kuralları)
- `requirements.txt` (Backend bağımlılıkları)
- `docker-compose.yml` (Tüm sistemi ayağa kaldırır)
- `.gitignore` (Gereksiz dosyaları git takibinden çıkarır)

### 2. Ortam Değişkenleri
- Google Gemini API anahtarınızı app.py dosyasında 72.satıra ekleyin:
  ```
  GEMINI_API_KEY=your_google_gemini_api_key
  ```
  (Varsayılan anahtar kodda örnek olarak gömülü.)

### 3. Docker ile Çalıştırma

Terminalde proje klasöründe:
```bash
docker-compose up --build
```
- Frontend: [http://localhost:2301](http://localhost:2301)
- Backend API: [http://localhost:2300](http://localhost:2300)

---

## Kullanım

1. Tarayıcıdan [http://localhost:2301](http://localhost:2301) adresine gidin.
2. Mesajınızı yazın, Berkay AI ile sohbet edin.
3. Tüm konuşmalar ve AI'nın hafızası `berkay_memory.db` dosyasında kalıcı olarak saklanır.

---

## Kurallar ve Özelleştirme

### Kurallar Dosyası: `rules.txt`
- Konuşma tarzı, hitap şekli, emoji kullanımı, pozitiflik gibi tüm kurallar burada tanımlı.
- **Düzenlemek için:**
  - `rules.txt` dosyasını açın.
  - Her satır bir kuraldır, istediğiniz gibi ekleyip çıkarabilirsiniz.
- Örnek:
  ```
  1. Nazik ve sevecen bir dil kullan
  2. Kısa ve öz cevaplar ver
  3. Kullanıcıya "aşkım" diye hitap et
  4. Her zaman pozitif ve destekleyici ol
  5. Gerektiğinde şakalar yap ve espritüel ol
  ```

### Hafıza/Memories
- Tüm geçmiş konuşmalar `berkay_memory.db` dosyasında saklanır.
- Silmek için bu dosyayı silebilirsiniz (veya yedekleyebilirsiniz).
- Her yeni konuşma ve cevap otomatik olarak hafızaya eklenir.

---

## Dosya ve Klasör Yapısı
```
.
├── app.py              # Backend API (FastAPI + Agno Memory)
├── requirements.txt    # Backend bağımlılıkları
├── rules.txt           # Konuşma kuralları
├── berkay_memory.db    # Kalıcı hafıza (otomatik oluşur)
├── docker-compose.yml  # Tüm sistemi başlatır
├── frontend/           # React + Tailwind arayüzü
│   ├── src/
│   ├── public/
│   └── ...
└── .gitignore
```

---

## Geliştirici Notları
- Backend kodunda (`app.py`) prompt ve memory yönetimi Agno'nun önerdiği şekilde yapılmıştır.
- Frontend arayüzü özelleştirmek için `frontend/src/App.js` dosyasını düzenleyebilirsiniz.
- Hafıza ve kurallar dosyası dışında başka bir veri saklanmaz.

---

## Sorun Giderme
- Eğer "500 Internal Server Error" alırsanız, backend loglarını kontrol edin.
- `berkay_memory.db` dosyasının yazılabilir olduğundan emin olun.
- API anahtarınızın geçerli olduğundan emin olun.

---

## Lisans
Bu proje tamamen kişisel kullanım ve sevgiliye özel AI deneyimi için tasarlanmıştır. 