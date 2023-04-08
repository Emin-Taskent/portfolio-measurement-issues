# portfolio-measurement-issues

## AB Testing

### İş problemi
Facebook kısa süre önce mevcut **"maximumbidding"** adı verilen teklif verme türüne alternatif olarak yeni bir teklif türü olan **"average bidding"**’i tanıttı.

Müşterilerimizden biri olan xyz.com, bu yeni özelliği test etmeye karar verdi ve **average bidding'in maximumbidding'den daha fazla dönüşüm getirip getirmediğini** anlamak için bir A/B testi yapmak istiyor.

A/B testi 1 aydır devam ediyor ve xyz.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor. xyz.com için nihai başarı ölçütü **Purchase**'dır. Bu nedenle, istatistiksel testler için **Purchase** metriğine odaklanılmalıdır.

### Veri Seti Hikayesi

Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır. Kontrol ve Test grubu olmak üzere iki ayrı veri seti vardır. Kontrol grubuna **Maximum Bidding**, test grubuna **Average Bidding** uygulanmıştır.

## Rating Product & Sorting Reviews in Amazon

### İş problemi

E-ticaretteki en önemli problemlerden bir tanesi ürünlere satış sonrası verilen puanların doğru şekilde hesaplanmasıdır. Bu problemin çözümü e-ticaret sitesi için daha fazla müşteri memnuniyeti sağlamak, satıcılar için ürünün öne çıkması ve satın alanlar için sorunsuz bir alışveriş deneyimi demektir. Bir diğer problem ise ürünlere verilen yorumların doğru bir şekilde sıralanması olarak karşımıza çıkmaktadır. Yanıltıcı yorumların öne çıkması ürünün satışını doğrudan etkileyeceğinden dolayı hem maddi kayıp hem de müşteri kaybına neden olacaktır. Bu 2 temel problemin çözümünde e-ticaret sitesi ve satıcılar satışlarını arttırırken müşteriler ise satın alma yolculuğunu sorunsuz olarak tamamlayacaktır.

### Veri Seti Hikayesi

Amazon ürün verilerini içeren bu veri seti ürün kategorileri ile çeşitli metadataları içermektedir. Elektronik kategorisindeki en
fazla yorum alan ürünün kullanıcı puanları ve yorumları vardır.

    Değişkenler;

* reviewerID: Kullanıcı ID’si
* asin: Ürün ID’si
* reviewerName: Kullanıcı Adı
* helpful: Faydalı değerlendirme derecesi
* reviewText: Değerlendirme
* overall: Ürün rating’i
* summary: Değerlendirme özeti
* unixReviewTime: Değerlendirme zamanı
* reviewTime: Değerlendirme zamanı Raw
* day_diff: Değerlendirmeden itibaren geçen gün sayısı
* helpful_yes: Değerlendirmenin faydalı bulunma sayısı
* total_vote: Değerlendirmeye verilen oy sayısı
