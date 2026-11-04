import math
import random
import turtle

def setup():
    """Ekran ve pencere ayarlarını yapar."""
    turtle.setup(800, 600)
    turtle.bgcolor("black")
    turtle.title("I Love You - Heart Animation")
    turtle.tracer(2)

def heart_x(k):
    """Kalp şeklinin X koordinatını hesaplar."""
    return 15 * math.sin(k) ** 3

def heart_y(k):
    """Kalp şeklinin Y koordinatını hesaplar."""
    return (12 * math.cos(k) - 5 * math.cos(2 * k) - 
            2 * math.cos(3 * k) - math.cos(4 * k))

def main():
    setup()
    
    # Farklı dillerde "Seni seviyorum" sözleri
    phrases = [
        "I love you", "Te amo", "Ti amo",
        "Seni seviyorum", "Je t'aime",
        "Ich liebe dich", "Kocham cię",
        "Aku cinta kau", "Я тебя люблю",
        "Ik hou van jou", "Jeg elsker dig",
        "Mahal kita", "Te quiero"
    ]
    
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    
    # Kalp şeklinde rastgele noktalara farklı dillerde sözler yazdıralım
    for _ in range(50):
        t.color(random.choice(["red", "pink", "hotpink", "deeppink", "magenta"]))
        k = random.uniform(0, 2 * math.pi)
        x = heart_x(k) * 20
        y = heart_y(k) * 20
        t.goto(x, y)
        phrase = random.choice(phrases)
        t.write(phrase, align="center", font=("Arial", 10, "bold"))
        
    turtle.update()
    turtle.done()

if __name__ == '__main__':
    main()
