#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RASTGELE MAZERET ÜRETİCİ PRO v1.0
=================================
Bu yazılım, modern insanın en temel ihtiyacını karşılamak üzere
geliştirilmiştir: İnanılır, bilimsel ve tamamen saçma mazeretler.

Uyarı: Bu programın ürettiği mazeretler %100 gerçektir.
(Kanıt aranmamaktadır.)
"""

import random
import time
import sys

# Gizli parametre (sakın bakma - decode etme)
_gizli = "ZGVtb2tyYXNpIMO2bmVtbGlkaXIsIMO2emfDvHIgZMO8xZ/DvG4="  # base64, sakın decode etme

MAZERETLER = [
    "Kedim klavyenin üzerine oturdu ve tüm ödev dosyalarını 'sil' tuşuyla silmeyi öğrendi.",
    "Sabah kalktığımda evrenin genleşme hızı artmıştı, bu yüzden evden çıkmam 3 saat sürdü.",
    "Trafikte bir karınca konvoyu vardı, geçit vermek zorundaydım. Etik bir zorunluluktu.",
    "Bilgisayarım 'bugün çalışmayacağım' diye bir bildirim gönderdi. Saygı duydum.",
    "Rüyamda geç kaldığımı gördüm, uyanınca zaten geçmiştim. Kuantum tutarlılığı.",
    "Komşunun kedisi benim ayakkabılarımı rehin aldı. Pazarlık uzun sürdü.",
    "Güneş ışığı gözlerimi kamaştırdı, 47 dakika boyunca yönümü bulamadım.",
    "Telefonum 'acil sessizlik modu'na geçti ve beni uyandırmadı. Teknolojiye güvenemiyorum.",
    "Yolda bir sokak kedisi bana bakış attı. O bakışın anlamını çözmek 20 dakika sürdü.",
    "Kahve makinem 'bugün mola veriyorum' dedi. İnsan gibi davranan makinelere saygı duyarım.",
    "Zaman dilimi değişmişti ama kimse bana söylememişti. Küresel bir komplo olabilir.",
    "Aynada kendimi görünce 'bugün gitmesen de olur' dedim. Kendime kulak verdim.",
    "Bir kuş pencereye kondu ve bana uzun uzun baktı. O kuşun mesajını çözmek zorundaydım.",
    "Çoraplarımın biri kayboldu. Diğerini de aramak için tüm evi taradım. Hâlâ yok.",
    "İnternet bağlantım 'bugün seninle ilgilenmeyeceğim' mesajı verdi. Anlaştık.",
]

def dramatik_bekleme():
    """Ciddiyet katmak için gereksiz bekleme."""
    print("\n[SİSTEM] Mazeret veritabanı taranıyor...")
    for i in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n[SİSTEM] En uygun mazeret seçiliyor...")
    time.sleep(0.6)

def mazeret_uret(adet=1):
    """Belirtilen sayıda profesyonel mazeret üretir."""
    dramatik_bekleme()
    print("\n" + "="*50)
    print("  RASTGELE MAZERET ÜRETİCİ PRO - SONUÇ")
    print("="*50)
    for i in range(adet):
        mazeret = random.choice(MAZERETLER)
        print(f"\n{i+1}. MAZERET:\n   → {mazeret}")
    print("\n" + "="*50)
    print("Not: Bu mazeretler mahkemede geçerli değildir.")
    print("     (Ama denemeye değer.)")
    print("="*50)

def main():
    print("""
╔══════════════════════════════════════════════════════╗
║     RASTGELE MAZERET ÜRETİCİ PRO v1.0                ║
║     Ciddiyet Seviyesi: AŞIRI                         ║
║     Güvenilirlik: %0 (ama kaliteli)                  ║
╚══════════════════════════════════════════════════════╝
    """)
    
    while True:
        try:
            secim = input("\nKaç adet mazeret istersin? (1-5, q=çıkış): ").strip().lower()
            if secim == 'q':
                print("\n[SİSTEM] Mazeret üretimi sonlandırıldı. İyi bahaneler!")
                break
            adet = int(secim)
            if 1 <= adet <= 5:
                mazeret_uret(adet)
            else:
                print("[HATA] Lütfen 1 ile 5 arasında bir sayı gir.")
        except ValueError:
            print("[HATA] Geçerli bir sayı girmedin. Mazeret üretmek de bir sanattır.")
        except KeyboardInterrupt:
            print("\n\n[SİSTEM] Acil çıkış algılandı. Mazeretin: 'Program çöktü'.")
            sys.exit(0)

if __name__ == "__main__":
    main()
