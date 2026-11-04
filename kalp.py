import math
import time
import turtle

def setup():
    """Ekran ve pencere ayarlarını yapar."""
    turtle.setup(900, 700)
    turtle.bgcolor("black")
    turtle.title("100 Dilde Seni Seviyorum ❤️")
    turtle.tracer(0)

def main():
    setup()
    
    # Sol taraftaki Türkçe iltifatlar çıkarıldı, tamamen farklı dünya dilleri eklendi
    phrases = [
        "Seni seviyorum", "I love you", "Te amo", "Ti amo", "Je t'aime",
        "Ich liebe dich", "Kocham cię", "Aku cinta kau", "Я тебя люблю",
        "Ik hou van jou", "Jeg elsker dig", "Mahal kita", "Te quiero",
        "Minä rakastan sinua", "Σ' αγαπώ", "أنا بحبك", "ani ohev otach",
        "Volim te", "Milujem ťa", "Љубим те", "Obicham te", "Te iubesc",
        "Szeretlek", "Ljubim te", "Jeg elsker deg", "Ég elska þig", "T'estimo",
        "Ma armastan sind", "Es mīlu tevi", "Tave myliu", "Saranghae",
        "Wo ai ni", "Aishiteru", "Phom rak khun", "Tôi yêu em",
        "Aloha wau ia oe", "Nakupenda", "Gusto kita", "Cinta kepada mu",
        "Namaste", "Te quiero mucho", "Te amo tanto", "Je t'adore",
        "Mon amour", "Mi amor", "Amore mio", "Vida mia", "Corazón mio",
        "Bho a bheil gràdh agam ort", "Mil te chamo", "T'estim",
        "Ghajini", "Tora bhalobashi", "Me t'dua", "Te dua", "Tungjatjeta",
        "Kuv hlub koj", "Hau ol hov", "Niyikunda", "Ndagukunda", "Ndimunoda",
        "Au thương em", "Zdorovo", "Privet", "Zdravstvuyte", "Namaskaram",
        "Vanakkam", "Sat Sri Akaal", "Khub bhalo", "Bhalo bashi",
        "C'est la vie", "Carissimo", "Te stim", "Eu te amo", "Seni yaxshi ko'raman",
        "Men seni sevaman", "Min yхylyaman", "Azizam", "Mən səni sevirəm",
        "Ez ji te hezkirim", "Min hezkır dikim", "Seni yoldashim", "Ty kohayesh",
        "Ya vas lubil", "Obicham te mnogo", "Ljubim te iz srca", "Te quiero mi vida",
        "Querido mio", "Ooh la la", "Amore grande", "Un amore così grande",
        "Te amo mi amor", "Forever my love", "Te quiero tanto", "All my love",
        "True love", "Te amo para siempre", "Hlub tshav puam"
    ]
    
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    
    # Sadece kırmızı ve tonları
    red_colors = ["red", "crimson", "firebrick", "darkred", "indianred", "tomato"]
    
    steps = 100
    for i in range(steps):
        t.color(red_colors[i % len(red_colors)])
        
        # Matematiksel kalp konturu
        theta = (i / steps) * (2 * math.pi)
        x = 16 * (math.sin(theta) ** 3)
        y = 13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta)
        
        scale = 22
        t.goto(x * scale, y * scale)
        
        phrase = phrases[i % len(phrases)]
        t.write(phrase, align="center", font=("Arial", 9, "bold"))
        
        turtle.update()
        time.sleep(0.08)
        
    turtle.done()

if __name__ == '__main__':
    main()
