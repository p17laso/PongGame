# PongGame
# A fully integrated functional pong game written in Python.
# Code 

import turtle  # module για δημιουργία basic γραφικών
import winsound  # Για να προσθέσω ήχο στο παιχνίδι / αυτή η εντολή δουλεύει αποκλειστικά για υπολογιστή με Windows
from turtle import Screen, Turtle  # Για ευκολί αφήνω το module να δημιουργήσει το παράθυρο στο
# οποίο θα δουλέψω. Στη συνέχεια μπορώ να το επεξεργαστώ καλώντας τα methods του.
# Ουσαστικά αντί για screen = turtle.Screen() μπορώ να γράψω screen = Screen() για να δημιοργήσω παράθυρα
# και αντί για object = turtle.Turtle() --> object = Turtle() για να δημιουργήσω turtle objects

# Αρχική οθόνη έναρξης παιχνιδιού

start = False


# Function για το backbone της μετάβασης από την αρχική οθόνη στο παιχνίδι
def start_game():
    global start  # Αν δεν το έκανα global θα έκανε απλά ένα local start και θα περιοριζόταν σε αυτό το function
    start_message.clear()  # Για να αφαιρέσω τις "ζωγραφιές" του turtle από την οθόνη
    start = True
    pong_start()  # Μετάβαση στο επόμενο function


# Function για την έναρξη του παιχνιδιού μετά την εμφάνιση της αρχικής οθόνης
def pong_start():
    run_game()


#  Function για την μεάβαση του screen από την αρχική οθόνη στο παράθυρο του παιχνιδιού
def move_one_step():
    if start:
        screen.update()


screen = Screen()  # Δημιουργώ την αρχική οθόνη. Βy default είναι λευκή.
screen.bgcolor("black")  # Αλλάζω το χρώμα

start_message = Turtle()  # Δημιουργώ turtle object
start_message.hideturtle()  # Κρύβω τη χελώνα
start_message.penup()  # Το turtle όταν κινείται αφήνει πίσω του γραμμές οπότε κάνω penup
start_message.pencolor("white")  # Χρώμα
start_message.sety(75)  # Συντεταγμένες y
start_message.write("Press SPACE to start", align="center", font=("Courier", 20, "bold"))  # Μήνυμα έναρξης

screen.onkeypress(start_game, 'space')  # Όταν πατάς space ξεκινάει το παιχνίδι
screen.listen()  # Του λέω να ακούει για keyboard input
move_one_step()  # Καλώ το function για να με μεταβιβάσει από την αρχική --> παιχνίδι


#  Function για το παιχνίδι
def run_game():
    wn = Screen()  # Δημιουργώ window
    wn.title("Pong game")  # Τίτλος παραθύρου
    wn.bgpic("background.png")  # Background image
    wn.setup(width=960, height=720)  # Μέγεθος παραθύρου / έβαλα συντεταγμένες ίδιες με το μέγεθος της εικόνας
    wn.tracer(0)  # Σταματάει το παράθυρο από το να κάνει update. Τα update θα γίνονται χειροκίνητα. Με αυτόν τον τρόπο
    # επιταχύνεται το παιχνίδι.

    # Δημιουργία παραθύρου όπου οι παίκτες μπορούν να βάλουν τα ονόματα τους
    Player_A = wn.textinput("Player A", "Name of the player: ")
    Player_B = wn.textinput("Player B", "Name of the player: ")

    # Paddle A --> Φτιάχνω το πρώτο paddle
    paddle_a = turtle.Turtle()  # Τα paddle είναι turtle objects // turtle --> module name // Turtle --> class name
    paddle_a.speed(0)  # Ταχύτητα του animation. Αυτό κάνει την ταχύτητα τη μεγαλύτερη δυνατή ειδάλως όλα θα πήγαιναν
    # πάρα πολύ αργά
    paddle_a.shape("square")  # Σχήμα paddle
    paddle_a.color("blue")  # Χρώμα paddle
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Βy default το σχήμα είναι 20x20 pixels, για να το κάνω
    # ορθογώνιο το κάνω stretch
    paddle_a.penup()
    paddle_a.goto(-400, 0)  # Συντεταγμένες paddle // Θέλω να είναι στη μέση τέρμα αριστερά

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("red")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(400, 0)  # Συντεταγμένες paddle // Θέλω να είναι στη μέση τέρμα δεξιά

    # Ball // Σχεδιασμός μπάλας
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")  # Σχήμα μπάλας
    ball.color("white")  # Χρώμα
    ball.penup()
    ball.goto(0, 0)  # Συντεταγμένες μπάλας // Θέλω να είναι στη μέση
    ball.dx = 0.4  # Χωρίζω τις κινήσεις της μπάλας σε 2 τιμές και βάζω τιμές στις συντεταγμένες  x και y
    ball.dy = -0.4  # Με αυτές τις συντεταγμένες κινείται πάνω και διαγώνια

    # Pen --> turtle για να γράφει το σκορ
    pen = turtle.Turtle()
    pen.speed(0)  # animation speed
    pen.color("white")  # Χρώμα
    pen.penup()  # Για να μη βλέπουμε τις γραμμές που τραβάει το turtle
    pen.hideturtle()  # Για να μη βλέπουμε το turtle
    pen.goto(0, 300)  # Θέλω να ξεκινήσει να γράφει από το κέντρο πάνω πάνω
    pen.write(str(Player_A) + ": 0    " + str(Player_B) + ": 0", align="center", font=("Courier", 24, "bold"))
    # Το align είναι για να ευθυγραμμίσει τα γράμματα

    # Score
    score_a = 0  # Αρχικά το σκορ και των 2 είναι 0
    score_b = 0

    # Function για να κινούνται τα paddles πάνω - κάτω
    # Το y αυξάνεται όταν πάμε πάνω και μειώνεται όσο κατεβαίνουμε.
    def paddle_a_up():
        y = paddle_a.ycor()  # y coordinate του paddle_a
        y += 20  # Κάθε φορά προσθέτω 20
        paddle_a.sety(y)  # Το νέο y θα είναι y+20

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20  # Κάθε φορά αφαιρώ 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    # Keyboard binding --> "Δένω" τα κουμπιά με το function
    wn.listen()  # Λέει στο πρόγραμμα να ακούει για keyboard input
    wn.onkeypress(paddle_a_up, "w")  # Όταν ο χρήστης πατάει το "w" καλεί το function paddle_a_up
    # το w είναι lowercase αν είναι κεφαλαίο δε θα το δεχτεί. Επίσης δε θα το δεχτεί αν είναι ελληνικά.
    wn.onkeypress(paddle_a_down, "s")  # Όταν ο χρήστης πατάει το "s" καλεί το function paddle_a_down
    wn.onkeypress(paddle_b_up, "Up")  # Όταν ο χρήστης πατάει το πάνω βελάκι καλεί το function paddle_b_up
    wn.onkeypress(paddle_b_down, "Down")  # Όταν ο χρήστης πατάει το κάτω βελάκι καλεί το function paddle_b_down

    # Main game loop
    while True:
        wn.update()  # Κάθε φορά που τρέχει το loop κάνει update το screen

        # Για την κίνηση της μπάλας
        ball.setx(ball.xcor() + ball.dx)  # Θέλω την τωρινή συντεταγμένη x που είναι 0 + την μετατόπιση.
        ball.sety(ball.ycor() + ball.dy)  # Το ίδιο για την y από 0 γίνεται 1

        # Border checking --> Όταν φτάσει και ακουμπήσει κάποιο συγκεκριμένο σημείο θέλω να αναπηδήσει
        if ball.ycor() > 330:  # y = 350 είναι η καλύτερη δυνατή μεγαλύτερη τιμή που μπορεί να πάρει το y
            # Το παράθυρο είναι έχει 720 ύψος. Λόγω αξόνων: 720/2 = 360  το μεγαλύτερο ύψος.
            # Κατεβάζω λίγο για να μη χτυπάει ακριβώς στα όρια οπότε 330
            ball.sety(330)  # Αν y > 330 τότε y θα γίνει ξανα 330
            ball.dy *= -1  # και θα αντιστρέψω τη φορά
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            # Βάζω το SND_ASYNC για να μην κολλάει ο ήχος και για να σταματάει αυτόματα μόλις γίνει πρόσκρουση σε κάτι
            # άλλο ώστε να ξεκινάει κατευθείαν νέος ήχος
        if ball.ycor() < -330:
            ball.sety(-330)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # Τώρα ορίζω όρια για όταν η μπάλα πάει να φύγει από τα αριστερά. Το μέγεθος του παραθύρου στο x είναι 960. Για
        # διαμοιρασμό στον άξονα x 960/2 = 480 (-450 στα αριστερά και +450 στα δεξιά). Για ασφάλεια κατεβάζω άλλα 30.
        if ball.xcor() > 450:
            ball.goto(0, 0)  # Κάποιος χάνει οπότε πάει ξανά από την αρχή
            ball.dx *= -1
            score_a += 1  # Αν η μπάλα περάσει από τα αριστερά ο παίκρης Α κερδίζει πόντο
            pen.clear()  # Το χρησιμοποιώ για να μη γράφει το 1 σκορ πάνω από το άλλο.
            pen.write(str(Player_A) + ": {}    ".format(score_a) + str(Player_B) + ": {}".format(score_b),
                      align="center", font=("Courier", 24, "bold"))  # Γράφει τα ονόματα των παικτών και εμφανίζει το
            # αλλαγμένο σκορ κάθε φορά
            winsound.PlaySound("losesound.wav", winsound.SND_ASYNC)  # Ο ήχος που βγαίνει όταν χάνεις
        if ball.xcor() < -450:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write(str(Player_A) + ": {}    ".format(score_a) + str(Player_B) + ": {}".format(score_b),
                      align="center", font=("Courier", 24, "bold"))
            winsound.PlaySound("losesound.wav", winsound.SND_ASYNC)

        # Paddle and ball collisions
        # Για να γίνει αυτό συγκρίνουμε τις συντεταγμένες x και y του paddle και της μπάλας
        # Το x του κέντρου της ρακέτας είναι 400, η ρακέτα είναι 20 pixels wide Χ 100 pixels tall οπότε εμείς
        # Θέλουμε να ελέγξουμε αν η μπάλα χτυπάει στις συντεταγμένες που έχει το paddle για να γίνει σύγκρουση.
        if (ball.xcor() > 390 and ball.xcor() < 400) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            # Αν η x συντεταγμένη της μπάλας είναι > από 390 αυτό σημαίνει ότι οι γωνίες της μπάλας και της ρακέτας
            # ακουμπιούνται και ότι είναι μεταξύ του πάνω και κάτω μέρους του paddle. Συνολικά το πλάτος του paddle
            # είναι 100 αλλά υπολογίζω και το μέγεθος της μπάλας (για αυτό βάζω 40 πιο πάνω: 40+40+μέγεθος μπάλας=~100)
            ball.setx(390)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # ήχος μπάλας όταν χτυπάει στις ρακέτες
            # και τα τοιχώματα

        if (ball.xcor() < -390 and ball.xcor() > -400) and (
                ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-390)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # Τα paddle δε μπορούν να φεύγουν από την οθόνη
        # Μετά από δοκιμές αποφάσισα να βάλω την τιμή 310 γιατί οι ρακέτες φτάνουν ακριβώς στις άκρες.
        if paddle_a.ycor() >= 310:
            paddle_a_down()
        if paddle_a.ycor() <= -310:
            paddle_a_up()
        if paddle_b.ycor() >= 310:
            paddle_b_down()
        if paddle_b.ycor() <= -310:
            paddle_b_up()

        # Αν score >= 3 τότε κάποιος από τους 2 κερδίζει. Αν πατήσουν το y το παιχνίδι ξαναρχίζει.
        if score_a >= 3:
            restart = wn.textinput("Game result",
                                   "Well done " + Player_A + ", you won! \n Do you want to restart? (y/n)")
            if restart == "y":  # αν πατήσουν y το παιχνίδι ξαναρχίζει από την αρχή.
                wn.clearscreen()
                run_game()
            else: # αν πατήσουν οτιδήποτε άλλο εκτός από y το παιχνίδι τελειώνει
                exit()  # σταματάει το πρόγραμμα

        if score_b >= 3:
            restart = wn.textinput("Game result",
                                   "Well done " + Player_B + ", you won! \n Do you want to restart? (y/n)")
            if restart == "y":
                wn.clearscreen()
                run_game()
            else:
                exit()


screen.mainloop()  # This method listens for events, such as button clicks or keypresses, and blocks any code that
# comes after it from running until the window it's called on is closed.
