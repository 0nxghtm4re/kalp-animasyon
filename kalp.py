import math
import time
import turtle

def setup():
    """Ekran ve pencere ayarlarını yapar."""
    turtle.setup(900, 700)
    turtle.bgcolor("black")
    turtle.title("Seni Seviyorum ❤️")
    turtle.tracer(0)

def main():
    setup()
    
    # 100 farklı dilde "Seni seviyorum" sözleri
    phrases = [
        "Seni seviyorum", "I love you", "Te amo", "Ti amo", "Je t'aime",
        "Ich liebe dich", "Kocham cię", "Aku cinta kau", "Я тебя люблю",
        "Ik hou van jou", "Jeg elsker dig", "Mahal kita", "Te quiero",
        "Minä rakastan sinua", "Σ' αγαπώ", "أنا بحبك", "ani ohev otach",
        "Volim te", "Milujem ťa", "Obicham te", "Te iubesc", "Szeretlek",
        "Ljubim te", "Jeg elsker deg", "Ég elska þig", "T'estimo",
        "Ma armastan sind", "Es mīlu tevi", "Tave myliu", "Saranghae",
        "Wo ai ni", "Aishiteru", "Phom rak khun", "Tôi yêu em",
        "Aloha wau ia oe", "Nakupenda", "Te quiero mucho", "Te amo tanto",
        "Gusto kita", "Mina amor", "Mi amor", "Mon amour", "Amore mio",
        "Vida mia", "Corazón mio", "Cinta", "Aşkım", "Canımın içi",
        "Gözümün bebeği", "Ruhum", "Bitanem", "Her şeyim", "Sen sevgilimsin",
        "Yüreğim", "Ömrüm", "Gönlüm", "Nefesim", "Tatlım", "Güzelim",
        "Sevdam", "Hasretim", "Yarim", "Cigerparem", "Papatyam",
        "Çiçeğim", "Yıldızım", "Güneşim", "Ay tanem", "Melek yüzlüm",
        "Kıymetlim", "Değerlim", "Birtaneciyim", "Gönül sultanım", "Huzurum",
        "Neşem", "Baharım", "Yazım", "Kışım", "Umut yaratanım",
        "Yol arkadaşım", "Dönüm noktam", "Kalbimin sahibi", "Ömrümün sebebi",
        "Al yazmalım", "Gönül dağım", "Göz nurum", "Alnımın yazısı", "Kaderim",
        "Yazgımsın", "Sevgi pıtırcığım", "Can özüm", "Gönül bahçem", "Tatlı belam",
        "Çılgınım", "Minik kuşum", "Papatya falım", "İlk aşkım", "Son aşkım"
    ]
    
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    
    red_colors = ["red", "crimson", "firebrick", "darkred", "indianred", "tomato"]
    
    # Kalp matrisini oluşturmak için matematiksel parametre (t) kullanalım
    # Adım sayısını 100 yaparak tam 100 farklı dilde kelime ile kalbi çizdiriyoruz
    steps = 100
    for i in range(steps):
        # Matematiksel kalp denklemi (Parametrik formül)
        # Bu formül doğrudan kalbin hatlarını çizer
        t.color(red_colors[i % len(red_colors)])
        
        # 0'dan 2*pi'ye kadar düzenli artarak kalbin etrafını sarar
        theta = (i / steps) * (2 * math.pi)
        
        # Kalp koordinat denklemleri
        x = 16 * (math.sin(theta) ** 3)
        y = 13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta)
        
        # Boyutu ekrana göre büyütelim
        scale = 22
        t.goto(x * scale, y * scale)
        
        # Listeden sıradaki dili alalım
        phrase = phrases[i % len(phrases)]
        
        # Kalbin hatları net ve okunabilir olsun diye sabit/uygun bir font boyutu
        t.write(phrase, align="center", font=("Arial", 9, "bold"))
        
        # Akıcı, gözü yormayan, tam kararında animasyon hızı
        turtle.update()
        time.sleep(0.08)
        
    turtle.done()

if __name__ == '__main__':
    main()
