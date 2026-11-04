import math
import random
import turtle

def setup():
    """Ekran ve pencere ayarlarını yapar."""
    turtle.setup(900, 700)
    turtle.bgcolor("black")
    turtle.title("100 Dilde Kırmızı Kalp Animasyonu")
    turtle.tracer(2, 10) # Akıcı çizim için

def heart_x(k):
    """Kalp şeklinin X koordinatını hesaplar."""
    return 16 * math.sin(k) ** 3

def heart_y(k):
    """Kalp şeklinor Y koordinatını hesaplar."""
    return (13 * math.cos(k) - 5 * math.cos(2 * k) - 
            2 * math.cos(3 * k) - math.cos(4 * k))

def main():
    setup()
    
    # 100 farklı dilde "Seni seviyorum" sözleri
    phrases = [
        "Seni seviyorum", "I love you", "Te amo", "Ti amo", "Je t'aime",
        "Ich liebe dich", "Kocham cię", "Aku cinta kau", "Я тебя люблю",
        "Ik hou van jou", "Jeg elsker dig", "Mahal kita", "Te quiero",
        "Minä rakastan sinua", "Σ' αγαπώ", "أنا بحبك", "ani ohev otach",
        "Bho a bheil gràdh agam ort", "Mil te chamo", "Volim te",
        "Milujem ťa", "Љубим те", "Obicham te", "Te iubesc", "Szeretlek",
        "Ljubim te", "Jeg elsker deg", "Ég elska þig", "T'estimo",
        "T'estim", "Ma armastan sind", "Es mīlu tevi", "Tave myliu",
        "Mahal kita", "Gusto kita", "Saranghae", "Wo ai ni", "Aishiteru",
        "Phom rak khun", "Chan rak khun", "Tôi yêu em", "Empatiku",
        "Aloha wau ia oe", "Cinta kepada mu", "Asante", "Nakupenda",
        "Mbi gi", "Ndiku munhu", "Ina son ki", "Mina mohabbat karata",
        "Padmase", "Asante", "Ay lub yu", "Namaste", "Kem chho",
        "Rakh khun", "Tear o", "Mhor a bheil", "Ghajini", "Tora bhalobashi",
        "Me t'dua", "Te dua", "Tungjatjeta", "Kuv hlub koj", "Hau ol hov",
        "Niyikunda", "Ndagukunda", "Ndimunoda", "Mino rah", "E ratou",
        "Au thương em", "Mang a love", "Lethal", "Mina khwahish",
        "Nazdar", "Ahoj", "Zdorovo", "Privet", "Zdravstvuyte",
        "Namaskaram", "Vanakkam", "Namaskaar", "Sat Sri Akaal",
        "Khub bhalo", "Bhalo bashi", "Sata ki", "Me t'du",
        "Te quiero mucho", "Te amo tanto", "Je t'adore", "Ich mag dich",
        "C'est la vie", "Mon amour", "Mi amor", "Corazón mio",
        "Vida mia", "Ooh la la", "Amore mio", "Caro mio"
    ]
    
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    
    # Sadece kırmızı tonları
    red_colors = ["red", "crimson", "firebrick", "darkred", "indianred", "orangered"]
    
    for i in range(100):
        t.color(random.choice(red_colors))
        k = random.uniform(0, 2 * math.pi)
        
        scale = random.uniform(15, 22)
        x = heart_x(k) * scale
        y = heart_y(k) * scale
        
        t.goto(x, y)
        
        phrase = phrases[i % len(phrases)]
        font_size = random.randint(8, 12)
        t.write(phrase, align="center", font=("Arial", font_size, "bold"))
        
        turtle.update()
        
    turtle.done()

if __name__ == '__main__':
    main()
