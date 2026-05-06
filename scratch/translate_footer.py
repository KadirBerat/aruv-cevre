import os
import re

def translate_footer_blocks(directory):
    replacements = [
        # Footer description
        (r'<p>At Arüv Çevre, we’re committed to delivering reliable, efficient, and sustainable solar energy solutions\..*?protecting the planet\.</p>', 
         r'<p>Arüv Çevre olarak, sürdürülebilir bir gelecek için teknoloji odaklı ve çevreye duyarlı mühendislik çözümleri sunuyoruz. Sektördeki deneyimimizle projelerinizi güvenle hayata geçiriyoruz.</p>'),
        
        # Extra content description
        (r'<h5>Hakkımızda</h5>\s*<p>At Arüv Çevre, we’re committed to delivering reliable, efficient, and sustainable solar energy solutions\..*?protecting the planet\.</p>', 
         r'<h5>Hakkımızda</h5><p>Arüv Çevre olarak, sürdürülebilir bir gelecek için teknoloji odaklı ve çevreye duyarlı mühendislik çözümleri sunuyoruz. Sektördeki deneyimimizle projelerinizi güvenle hayata geçiriyoruz.</p>'),
        
        # Services titles in extra content
        (r'<li>Solar Panel Installation</li>', r'<li>Güneş Paneli Kurulumu</li>'),
        (r'<li>Panel Maintenance &amp; Repair</li>', r'<li>Panel Bakım ve Onarım</li>'),
        (r'<li>Custom System Design</li>', r'<li>Özel Sistem Tasarımı</li>'),
        (r'<li>Energy Storage Solutions</li>', r'<li>Enerji Depolama Çözümleri</li>'),
        (r'<li>System Monitoring Services</li>', r'<li>Sistem İzleme Hizmetleri</li>'),
        (r'<li>Panel Modernization</li>', r'<li>Panel Modernizasyonu</li>'),
        
        # Company/Contact titles
        (r'<h5>Our Services</h5>', r'<h5>Hizmetlerimiz</h5>'),
        (r'<h5>Company</h5>', r'<h5>Kurumsal</h5>'),
        (r'<h5>Contact Us</h5>', r'<h5>Bize Ulaşın</h5>'),
        (r'<h5>About Us</h5>', r'<h5>Hakkımızda</h5>'),
        
        # Placeholder contact labels
        (r'<span>Main Office</span>', r'<span>Merkez Ofis</span>'),
        (r'<span>Call Us</span>', r'<span>Bizi Arayın</span>'),
        (r'<span>Email Us</span>', r'<span>E-posta</span>'),
        (r'<span>Office Hours</span>', r'<span>Çalışma Saatleri</span>'),
        
        # Work labels in extra content
        (r'<div><i class="icofont-clock-time me-2 op-5"></i>Monday - Friday 08:00 - 17:00</div>',
         r'<div><i class="icofont-clock-time me-2 op-5"></i>Pazartesi - Cuma 08:00 - 17:00</div>')
    ]

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                original_content = content
                for pattern, repl in replacements:
                    content = re.sub(pattern, repl, content, flags=re.IGNORECASE | re.DOTALL)

                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Translated footer blocks in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    translate_footer_blocks(".")
