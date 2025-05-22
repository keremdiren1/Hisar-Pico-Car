## Nedir

Raspberry Pi Pico, Raspberry Pi Vakfı tarafından geliştirilen ve 2021 yılında piyasaya sürülen küçük, düşük maliyetli bir mikrodenetleyici kartıdır. Geniş çapta bilinen Raspberry Pi bilgisayarlarından farklı olarak, Pico bir mikrodenetleyici kartıdır; yani bir bilgisayar değil, belirli görevleri yerine getirmek için tasarlanmış gömülü sistem projelerinde kullanılır.

### Kullanım Alanları:
- Basit elektronik projeleri (LED yakma, buton kontrolü vs.)
- Robotik uygulamalar
- Sensör verisi okuma ve işleme
- Otomasyon sistemleri
- Eğitim amaçlı mikrodenetleyici programlama

## Nasıl Çalışıyor

- Raspberry Pi Pico, micro-USB kablo ile bilgisayara veya bir güç kaynağına bağlanarak çalışır. 1.8V - 5.5V arası giriş voltajlarını destekler, genelde USB'den gelen 5V yeterlidir.
- Çalıştırılmak istenlien kod yüklenir.
  1. Pico'nun üzerindeki BOOTSEL düğmesine basılı tutup USB ile bilgisayara bağlarsan,
  2. Bilgisayar onu bir USB diski gibi tanır.
  3. `.uf2` uzantılı program dosyasını bu diske sürüklersin.
  4. Dosya yüklendikten sonra Pico yeniden başlar ve programı çalıştırır.
  5. Yüklenen program, RP2040 üzerindeki flash hafızadan çalıştırılır.
  6. Program giriş/çıkış pinlerini (GPIO) kullanarak fiziksel dünyayla iletişim kurar.
  7. Örneğin: LED yakar, sensör verisi okur, motor kontrol eder.
- aa
