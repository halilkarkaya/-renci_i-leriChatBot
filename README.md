# RAG (Retrieval-Augmented Generation) Projesi

Bu proje, Google Generative AI ve LangChain kullanarak geliştirilmiş bir RAG (Retrieval-Augmented Generation) uygulamasıdır. Proje, Excel dosyasından alınan soru-cevap verilerini kullanarak kullanıcı sorularına yanıt vermektedir.

## Özellikler

- Excel dosyasından veri yükleme
- Google Generative AI ile metin üretimi
- ChromaDB ile vektör tabanlı arama
- Türkçe dil desteği
- Hızlı ve etkili yanıt sistemi

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/rag.git
cd rag
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
.\venv\Scripts\activate  # Windows
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. `.env` dosyası oluşturun ve Google API anahtarınızı ekleyin:
```
GOOGLE_API_KEY=your_api_key_here
```

## Kullanım

1. Excel dosyanızı `myproject/soru_cevaplar.xlsx` konumuna yerleştirin.

2. Uygulamayı başlatın:
```bash
python main.py
```

## Proje Yapısı

```
rag/
├── myproject/
│   ├── myapp/
│   │   └── rag_utils.py
│   └── soru_cevaplar.xlsx
├── main.py
├── requirements.txt
└── README.md
```

## Gereksinimler

- Python 3.8+
- Google API anahtarı
- Excel dosyası (soru-cevap verileri)

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. 