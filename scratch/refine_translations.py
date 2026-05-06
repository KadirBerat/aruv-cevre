import os
import re

def translate_homepage_and_common(directory):
    replacements = [
        # Subtitles
        (r'<div class="subtitle wow fadeInUp" data-wow-delay=".0s">Arüv Çevre Müh. Müş. Hiz. İnş. San. ve Tic. A.Ş.</div>', 
         r'<div class="subtitle wow fadeInUp" data-wow-delay=".0s">ARÜV ÇEVRE Müh. Müş. Hiz. İnş. San. ve Tic. A.Ş.</div>'),
        
        # Section Titles
        (r'Why Arüv Çevre\?', r'Neden Arüv Çevre?'),
        (r'Our Solar Projects', r'Projelerimiz'),
        (r'Powering a Brighter Future', r'Daha Parlak Bir Gelecek İnşa Ediyoruz'),
        (r'What Our Clients Say', r'Müşterilerimiz Ne Diyor?'),
        (r'Latest News', r'Güncel Haberler'),
        (r'Get in Touch', r'İletişime Geçin'),
        (r'Years of Experience', r'Yıllık Deneyim'),
        
        # Small labels
        (r'happy customers', r'mutlu müşteri'),
        (r'Solar Panels Installed', r'Kurulu Güneş Paneli'),
        (r'Homes Powered', r'Aydınlatılan Evler'),
        (r'Years of Solar Expertise', r'Yıllık Uzmanlık'),
        
        # Navigation
        (r'<span>Read More</span>', r'<span>Devamını Oku</span>'),
        (r'<span>View All Projects</span>', r'<span>Tüm Projeleri Gör</span>'),
        (r'<span>Contact Us</span>', r'<span>İletişim</span>'),
        
        # Breadcrumbs / Meta
        (r'Legal Information', r'Yasal Bilgilendirme'),
        (r'Solar Energy HTML Template', r'Çevre ve Mühendislik Çözümleri'),
        (r'Ecology &amp; Solar Energy HTML Template', r'Çevre, Mühendislik ve Müşavirlik Hizmetleri'),
        
        # Feature list items
        (r'Professional Team', r'Profesyonel Ekip'),
        (r'Customized Solutions', r'Size Özel Çözümler'),
        (r'Affordable Plans', r'Uygun Maliyetli Planlar'),
        (r'Ongoing Support', r'Kesintisiz Destek'),
        (r'Top-Tier Equipment', r'Üst Düzey Ekipman'),
        (r'Fast Installation', r'Hızlı Kurulum')
    ]

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                original_content = content
                for pattern, repl in replacements:
                    content = re.sub(pattern, repl, content, flags=re.IGNORECASE)

                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Refined translations in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    translate_homepage_and_common(".")
