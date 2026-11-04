import math
import random
import time
import turtle

def setup():
    """Ekran ve pencere ayarlarını yapar."""
    turtle.setup(900, 700)
    turtle.bgcolor("black")
    turtle.title("Seni Seviyorum ❤️")
    turtle.tracer(0) # Animasyonu manuel kontrol etmek için tracer'ı kapatıyoruz

def heart_x(k):
    return 16 * math.sin(k) ** 3

def heart_y(k):
    return (13 * math.cos(k) - 5 * math.cos(2 * k) - 
            2 * math.cos(3 * k) - math.cos(4 * k))

def main():
    setup()
    
    phrases = [
        "Seni seviyorum", "I love you", "Te amo", "Ti amo", "Je t'aime",
        "Ich liebe dich", "Kocham cię", "Aku cinta kau", "Я тебя люблю",
        "Ik hou van jou", "Jeg elsker dig", "Mahal kita", "Te quiero",
        "Minä rakastan sinua", "Σ' αγαπώ", "أنا بحبك", "ani ohev otach",
        "Volim te", "Milujem ťa", "Obicham te", "Te iubesc", "Szeretlek",
        "Ljubim te", "Jeg elsker deg", "Ég elska þig", "T'estimo",
        "Ma armastan sind", "Es mīlu tevi", "Tave myliu", "Saranghae",
        "Wo ai ni", "Aishiteru", "Phom rak khun", "Tôi yêu em",
        "Aloha wau ia oe", "Nakupenda", "Te quiero mucho", "Te amo tanto"
    ]
    
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    
    red_colors = ["red", "crimson", "firebrick", "darkred", "indianred", "tomato"]
    
    # Kelimeleri tek tek, yavaş ve smooth bir şekilde ekrana basalım
    for i in range(70):
        t.color(random.choice(red_colors))
        k = random.uniform(0, 2 * math.pi)
        
        scale = random.uniform(15, 22)
        x = heart_x(k) * scale
        y = heart_y(k) * scale
        
        t.goto(x, y)
        
        phrase = phrases[i % len(phrases)]
        font_size = random.randint(9, 13)
        
        t.write(phrase, align="center", font=("Arial", font_size, "bold"))
        
        # Her kelimeden sonra ekranı güncelt ve minik bir bekleme koy (Smooth etki için)
        turtle.update()
        time.sleep(0.05) # Bu süre yazının akış hızını belirler
        
    turtle.done()

if __name__ == '__main__':
    main()
