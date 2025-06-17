# **Word2Vec**

Word2Vec, kelimeleri anlam benzerliklerine göre sayısal vektörlere dönüştüren bir wprd embedding tekniğidir. **CBOW** ve **Skip-gram**olarak iki mimarisi vardır. Benzer kelimeler vektör uzayında birbirine yakın olur.

- Anlamsal benzerlikleri sayısal olarak ifade eder. Yani *“king - man + woman ≈ queen”* gibi ilişkileri kurabilir.

- **CBOW:** Etrafındaki kelimelerden ortadaki kelimeyi bulmaya çalışıyor.
- **SKIP-GRAM:** Ortadaki kelimelerden etrafındaki kelimeleri bulmaya çalışıyor.

![alt text](../images/word2vec1.png)

Sayısal değerler daha hızlı anlayabilmek için renklendirilmiştir.

![alt text](../images/word2vec2.png)

Kelimeler arasındaki ilişkilerin yakalanması.

![alt text](../images/word2vec3.png)

Kelimler vektörleri üzerinde lineer cebir yapılabilir.