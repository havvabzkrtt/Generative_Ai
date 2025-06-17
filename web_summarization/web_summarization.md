# Webpage to Bullet Points Summarizer

## Amaç
Bu proje, bir web sayfasındaki metni otomatik olarak özetleyip madde işaretli (bullet points) şekilde sunmak için geliştirilmiştir. Kullanıcıdan alınan bir URL ile, sayfadaki metin çekilir ve Hugging Face Transformers kütüphanesindeki özetleme modeliyle kısa ve anlamlı bir özet oluşturulur.

## Çalışma Prensibi

1. **Web Sayfası İçeriğinin Çekilmesi:**  
   - Kullanıcıdan bir web sayfası URL’si alınır.
   - `requests` ile sayfa içeriği çekilir.
   - `BeautifulSoup` ile `<p>` etiketleri içindeki metinler birleştirilir.

2. **Özetleme:**  
   - Hugging Face Transformers kütüphanesinin `pipeline("summarization")` fonksiyonu ile önceden eğitilmiş bir özetleme modeli başlatılır.
   - Birleştirilen metin, bu modele gönderilerek özet alınır.

3. **Bullet Points Oluşturma:**  
   - Elde edilen özet cümlelere bölünür.
   - Her cümle bir madde işareti olarak kullanıcıya sunulur.

4. **Arayüz:**  
   - Streamlit ile basit ve etkileşimli bir web arayüzü sağlanır.

## Kullanım Alanları

- Haber, blog veya makale gibi uzun web içeriklerinin hızlıca özetlenmesi
- Bilgiye hızlı erişim ve içerik tarama
- Eğitim, araştırma ve içerik yönetimi uygulamaları

## Kullanılan Teknolojiler

- **Python 3.x**
- **Streamlit:** Web arayüzü için
- **requests:** Web sayfası içeriğini çekmek için
- **BeautifulSoup:** HTML’den metin ayıklamak için
- **transformers (Hugging Face):** Metin özetleme modeli için

## Kurulum ve Kullanım

1. Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install streamlit transformers requests beautifulsoup4
    ```

2. Uygulamayı başlatın:
    ```bash
    streamlit run webpagesummarizer.ipynb
    ```
    veya kodu bir `.py` dosyasına kopyalayıp çalıştırabilirsiniz.

3. Web arayüzünde bir URL girin ve özet ile bullet points çıktısını alın.

## Notlar

- Varsayılan olarak Hugging Face’in öntanımlı özetleme modeli kullanılır. Daha iyi sonuçlar için farklı modeller belirtilebilir.
- Uzun metinlerde modelin maksimum giriş uzunluğu sınırına dikkat edilmelidir.

