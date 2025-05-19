Resim Ödevi A

FER2013 isimli açık veri seti temel alınarak, çeşitli yüz ifadeleri dört sınıfa yeniden etiketlenmiştir:

- `healthy`: Mutlu (happy) ve nötr (neutral) yüz ifadeleri
- `depression`: Üzgün (sad) yüz ifadeleri
- `bipolar`: Kızgın (angry) ve korkmuş (fear) ifadeler
- `schizophrenia`: Tiksinme (disgust) ve sürpriz (surprise) ifadeleri

Bu sınıflandırma, yüz ifadesi ile zihinsel durum arasında anlamlı bağlantılar kurmak amacıyla yapılmıştır.

Klasör Yapısı

Aşağıda oluşturulan veri setinin genel klasör yapısı verilmiştir:

data/
├── fer2013.csv # Orijinal CSV dosyası (GitHub'a dahil edilmemiştir)
├── fer2013_images/ # CSV'den oluşturulan ham görseller
└── mental_dataset/ # Yeniden etiketlenmiş ve boyutlandırılmış son veri seti


Not: `data/` klasörü `.gitignore` dosyasıyla izleme dışı bırakılmıştır.

Kullanılan Scriptler

Python dilinde geliştirilmiş çeşitli scriptler `scripts/` klasörü içinde yer almaktadır:

- `csv_to_images.py`: `fer2013.csv` dosyasındaki piksel verilerinden 48x48 PNG görseller üretir
- `resize_images.py`: Tüm görselleri 224x224 boyutuna getirir
- `reorganize_fer2013.py`: Etiketleri `healthy`, `depression`, `bipolar`, `schizophrenia` olarak yeniden organize eder
- `split_data.py`: (isteğe bağlı) Eğitim, doğrulama ve test alt klasörlerine ayırmak için kullanılabilir
- `cnn_model.py`: (ileride kullanılmak üzere) CNN tabanlı sınıflandırma modeli için taslak yapı içerir

Veri Kaynağı

FER2013 veri seti, 35.000'den fazla yüz görüntüsünü içeren, ifadelere dayalı bir sınıflandırma veri setidir. Aşağıdaki bağlantıdan temin edilebilir:

- Kaggle bağlantısı: https://www.kaggle.com/datasets/msambare/fer2013

CSV dosyası büyük boyutlu olduğu için GitHub deposuna eklenmemiştir. Talep üzerine `.zip` formatında paylaşılabilir.

Lisans

Bu proje eğitim amaçlıdır. Görsel verilerin kaynağı olan FER2013 veri seti, ilgili lisans koşullarına tabidir.
