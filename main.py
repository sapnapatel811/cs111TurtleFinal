#Game: Totally Lost in Translation, is created by Rere Sonoiki, Sapna Patel, and Rasika Pandav for CS 111 @UIC on 11/25/24 with Professor Dey
#Creators: Rere Sonoiki, Rasika Pandav, Sapna Patel
#For CS 111 Final Project @UIC, Professor Dey
#Due Date: 11/26/24
#Brief Description: This is a language-learning adventure game set in Paris, where players explore iconic locations and learn French. This game uses the 'turtle' module and blends education and fun for interactive gameplay. 

#imports required modules
import turtle
import random
from PIL import Image

#sets background color
turtle.Screen().bgcolor("black")

locations = ["Cafe de Flore", "Eiffel Tower", "Moulin Rouge", "Louvre", "Jardin des Tuileries"]
fireworks_colors = ["red", "white", "blue", "gold", "silver"]

#counter variables
num_mistakes = 0
locations_visited = 0

#turtle set-up
turtle_baguette = turtle.Turtle() #for score display
turtle_notebook = turtle.Turtle() #for notebook phrase display
turtle_rules = turtle.Turtle() #display game rules
turtle_character_selection_txt = turtle.Turtle() #displays txt that user should select a character
turtle_text = turtle.Turtle() #displays the scenario the character is in
turtle_display = turtle.Turtle() #displays end screen message

#button-related turtles
letsgo_button = turtle.Turtle()
begin_button = turtle.Turtle()
cat_button = turtle.Turtle()
fox_button = turtle.Turtle()
cat = turtle.Turtle()
fox = turtle.Turtle()
turtle_cafe_here_button = turtle.Turtle()
turtle_eiffel_tower_here_button = turtle.Turtle()
turtle_moulin_rouge_here_button = turtle.Turtle()
turtle_louvre_here_button = turtle.Turtle()
turtle_jardin_here_button = turtle.Turtle()
turtle_exit_button = turtle.Turtle()
turtle_user_choice = turtle.Turtle()

#fireworks turtle
fireworks = turtle.Screen()
fireworks.setup(width = 800, height = 600)
fire_turtle = turtle.Turtle()
fire_turtle.speed(0)
fire_turtle.hideturtle()

current_screen = ""
turtle_screen = turtle.Screen()
expanded = False
notebook_screen = turtle.Screen()

#resize letsgo_button
image1 = Image.open('intro_button.gif')
width1 = 120
height1 = 100
resized_image = image1.resize((width1, height1))
resized_image.save('resized_intro_button.gif') 

#resize begin_button
image2 = Image.open('begin_button.gif')
width2 = 100
height2 = 60
resized_image2 = image2.resize((width2, height2))
resized_image2.save('resized_begin_button.gif')

#resize cat button 
image3 = Image.open('cat_button.gif')
width3 = 120
height3 = 70
resized_image3 = image3.resize((width3, height3))
resized_image3.save('resized_cat_button.gif')

#resize fox button 
image4 = Image.open('fox_button.gif')
width4 = 120
height4 = 70
resized_image4 = image4.resize((width4, height4))
resized_image4.save('resized_fox_button.gif')

#notebook image
note_image = Image.open('notebook.gif')
note_width = 180
note_height = 210
small_note_image = note_image.resize((note_width, note_height))
small_note_image.save("small_notebook.gif")

#resize fox character
image5 = Image.open('fox_icon.gif')
width5 = 100
height5 = 150
resized_image5 = image5.resize((width5, height5))
resized_image5.save('resized_fox_icon.gif')

#resize cat character
image6 = Image.open('cat_icon.gif')
width6 = 100
height6 = 150
resized_image6 = image6.resize((width6, height6))
resized_image6.save('resized_cat_icon.gif')

#here cafe button
here_cafe_button = Image.open('here_icon.gif')
width7 = 60
height7 = 60
resized_here_cafe_button = here_cafe_button.resize((width7, height7))
resized_here_cafe_button.save('resized_here_icon.gif')

#here eiffel button
here_eiffel_button = Image.open('here_eiffel.gif')
width7 = 60
height7 = 60
resized_here_cafe_button = here_cafe_button.resize((width7, height7))
resized_here_cafe_button.save('resized_eiffel_icon.gif')

#here moulin rouge button
here_moulin_button = Image.open('here_moulin.gif')
width8 = 60
height8 = 60
resized_here_cafe_button = here_cafe_button.resize((width8, height8))
resized_here_cafe_button.save('resized_moulin_icon.gif')

#here louvre button
here_louvre_button = Image.open('here_louvre.gif')
width9 = 60
height9 = 60
resized_louvre_button = here_louvre_button.resize((width9, height9))
resized_louvre_button.save('resized_louvre_icon.gif')

#here jardin button
here_jardin_button = Image.open('here_jardin.gif')
width10 = 60
height10 = 60
resized_jardin_button = here_louvre_button.resize((width10, height10))
resized_jardin_button.save('resized_jardin_icon.gif')

#resize exit button 
image11 = Image.open('exit_button.gif')
width11 = 100
height11 = 130
resized_image11 = image11.resize((width11, height11))
resized_image11.save('resized_exit_button.gif')

#resize end_screen
image12 = Image.open('game_end_screen.gif')
width12 = 800
height12 = 600
resized_image12 = image12.resize((width12, height12))
resized_image12.save('resized_game_end_screen.gif')

#displays intro screen with a let's go button
def intro_screen(resized_image): 
    global letsgo_button
    letsgo_button.showturtle()
    turtle_screen.bgpic("game_intro_screen.gif")
    turtle_screen.setup(width = 800, height = 600)
    turtle_screen.addshape("resized_intro_button.gif")
    letsgo_button.penup()
    letsgo_button.shape("resized_intro_button.gif")
    button_loc = letsgo_button.goto(200,-250)
    turtle_screen.onclick(lets_go_button)

#displays lets go button on intro screen 
def lets_go_button(x,y):
    if letsgo_button.distance(x,y) < 50:
        rules_screen()

#displays the rules from a text file
def display_rules():
    letsgo_button.hideturtle()
    turtle_screen.bgpic("rules_bg.gif")

    file = open("rules.txt")
    game_rules = file.readlines()
    file.close()

    turtle_rules.speed(100)
    turtle_rules.penup()
    turtle_rules.goto(0,250)
    
    line_spacing = 33
    for line in game_rules:
        clean_line = line.strip()
        turtle_rules.write(clean_line, align = "center", font = ("Arial", 11, "bold"))
        turtle_rules.sety(turtle_rules.ycor() - line_spacing)

#displays the rules screen with a begin button
def rules_screen():
    global begin_button
    turtle_screen.bgpic("rules_bg.gif")
    display_rules()
    turtle_screen.setup(width = 800, height = 600)
    turtle_screen.addshape("resized_begin_button.gif")
    begin_button.penup()
    begin_button.shape("resized_begin_button.gif")
    begin_button.goto(0,-260)
    turtle_screen.onclick(check_begin_button_click)

#displays begin button on rules screen 
def check_begin_button_click(x,y):
    if begin_button.distance(x,y) < 50:
        character_selection_screen()

#allows user to select a character for their adventure
def character_selection_screen():
    begin_button.hideturtle()
    turtle_rules.clear()
    turtle_screen.bgpic("character_selection.gif")
    turtle_screen.setup(width = 800, height = 600)
    turtle_screen.addshape("resized_cat_button.gif")
    turtle_screen.addshape("resized_fox_button.gif")

    cat_button.penup()
    cat_button.shape("resized_cat_button.gif")
    cat_button.goto(150,80)
    cat_button.showturtle()

    fox_button.penup()
    fox_button.shape("resized_fox_button.gif")
    fox_button.goto(-140,80)
    fox_button.showturtle()

    #text that tells user to pick character
    turtle_character_selection_txt.penup()
    turtle_character_selection_txt.goto(0,220)
    turtle_character_selection_txt.color("#D11D61")
    turtle_character_selection_txt.write("Time to pick your Parisian adventurer! Who will you be?", align = "center", font=("Arial",16,"bold"))
    turtle_character_selection_txt.goto(0,170)
    turtle_character_selection_txt.color("#D11D61")
    turtle_character_selection_txt.write("Choose wisely from the characters below and let the fun begin!", align = "center", font=("Arial",16,"bold"))
    turtle_character_selection_txt.hideturtle()

    turtle_screen.onscreenclick(character_choice)

#checks which character is chosen for the game
def character_choice(x,y):
    if cat_button.distance(x,y) < 50:
        map_screen(x,y)
        turtle_user_choice.penup()
        turtle_screen.addshape("resized_cat_icon.gif")
        turtle_user_choice.shape("resized_cat_icon.gif")
        turtle_user_choice.goto(-270, 20)
    elif fox_button.distance(x,y) < 50:
        map_screen(x,y)
        turtle_user_choice.penup()
        turtle_screen.addshape("resized_fox_icon.gif")
        turtle_user_choice.shape("resized_fox_icon.gif")
        turtle_user_choice.goto(-270,20)

#displays the map screen with the locations to choose from
def map_screen(x,y):
    global current_screen
    show_here_turtles()
    turtle_user_choice.showturtle()
    cat_button.hideturtle()
    fox_button.hideturtle()
    turtle_character_selection_txt.clear()

    current_screen = "map_screen.gif"   
    turtle_screen.bgpic("map_screen.gif")
    baguette_scoreboard()
    note_screen()
    exit()
    turtle_notebook.onclick(expand_note)

    #here cafe display
    turtle_cafe_here_button.penup()
    turtle_cafe_here_button.goto(-250,-70)
    turtle_screen.addshape('resized_here_icon.gif')
    turtle_cafe_here_button.shape('resized_here_icon.gif')
    turtle_cafe_here_button.showturtle()

    #here eiffel display
    turtle_eiffel_tower_here_button.penup()
    turtle_eiffel_tower_here_button.goto(0,0)
    turtle_screen.addshape('resized_eiffel_icon.gif')
    turtle_eiffel_tower_here_button.shape('resized_eiffel_icon.gif')
    turtle_eiffel_tower_here_button.showturtle()

    #here moulin display
    turtle_moulin_rouge_here_button.penup()
    turtle_moulin_rouge_here_button.goto(200,0)
    turtle_screen.addshape('resized_moulin_icon.gif')
    turtle_moulin_rouge_here_button.shape('resized_moulin_icon.gif')
    turtle_moulin_rouge_here_button.showturtle()

    #here louvre display
    turtle_louvre_here_button.penup()
    turtle_louvre_here_button.goto(100,150)
    turtle_screen.addshape('resized_louvre_icon.gif')
    turtle_louvre_here_button.shape('resized_louvre_icon.gif')
    turtle_louvre_here_button.showturtle()

    #here jardin display
    turtle_jardin_here_button.penup()
    turtle_jardin_here_button.goto(0,-250)
    turtle_screen.addshape('resized_jardin_icon.gif')
    turtle_jardin_here_button.shape('resized_jardin_icon.gif')
    turtle_jardin_here_button.showturtle()

    #handles all the clicks for the locations
    def handle_click(x,y):
        if turtle_cafe_here_button.distance(x,y) < 50:
            make_character_move_cafe()
            here_cafe(x,y)
        elif turtle_eiffel_tower_here_button.distance(x,y) < 50:
            make_character_move_eiffel()
            here_effiel(x,y)
        elif turtle_moulin_rouge_here_button.distance(x,y) < 50:
            make_character_move_moulin()
            here_moulin(x,y)
        elif turtle_louvre_here_button.distance(x,y) < 50:
            make_character_move_louver()
            here_louvre(x,y)
        elif turtle_jardin_here_button.distance(x,y) < 50:
            make_character_move_jardin()
            here_jardin(x,y)  
    turtle_screen.onscreenclick(handle_click)

#event-driven function to move character to each of the five locations
def make_character_move_cafe():
    turtle_user_choice.penup()
    turtle_user_choice.goto(-250,-70)
    turtle_user_choice.speed(1)
    turtle_user_choice.hideturtle()

def make_character_move_eiffel():
    turtle_user_choice.penup()
    turtle_user_choice.goto(0,0)
    turtle_user_choice.speed(1)
    turtle_user_choice.hideturtle()

def make_character_move_moulin():
    turtle_user_choice.penup()
    turtle_user_choice.goto(200,0)
    turtle_user_choice.speed(1)
    turtle_user_choice.hideturtle()

def make_character_move_louver():
    turtle_user_choice.penup()
    turtle_user_choice.goto(100,150)
    turtle_user_choice.speed(1)
    turtle_user_choice.hideturtle()

def make_character_move_jardin():
    turtle_user_choice.penup()
    turtle_user_choice.goto(0,-250)
    turtle_user_choice.speed(1)
    turtle_user_choice.hideturtle()

#draws the baguette scoreboard
def baguette_scoreboard():
    turtle_baguette.speed(1000)
    turtle_baguette.penup()
    turtle_baguette.goto(640,300)
    turtle_baguette.pendown()
    turtle_baguette.color("tan")
    turtle_baguette.begin_fill()
    turtle_baguette.circle(30,180)
    turtle_baguette.forward(200)
    turtle_baguette.circle(30,180)
    turtle_baguette.end_fill()

    turtle_baguette.penup()
    turtle_baguette.color("white")
    for sprinkle in range(25): #draws the white sprinkles on the baguette for a more realistic French look
        turtle_baguette.goto(550 + random.randint(-50,150), 350 + random.randint(-50,0))
        turtle_baguette.dot(7)

    turtle_baguette.goto(550,305)
    turtle_baguette.color("black")
    message = f'Mistakes: {num_mistakes}\nLocations Visited: {locations_visited}'
    turtle_baguette.write(message, align = "center", font = ("Arial", 16, "bold"))

#displays the notebook
def note_screen():
    turtle_screen.addshape("small_notebook.gif")
    turtle_notebook.shape("small_notebook.gif")
    turtle_notebook.penup()
    turtle_notebook.goto(550,150)

#expands and closes notebook
def expand_note(x,y):
    global expanded, current_screen
    if expanded == False:
        turtle_screen.addshape('notebook.gif')
        turtle_screen.bgpic("notebook.gif")
        hide_here_turtles()
        expanded = True   
    else:      
        if current_screen == "map_screen.gif":
            turtle_screen.bgpic("map_screen.gif")
            show_here_turtles()
        if current_screen == "cafe.gif":
            turtle_screen.bgpic("cafe.gif")
        if current_screen == "eiffel.gif":
            turtle_screen.bgpic("eiffel.gif")
        if current_screen == "moulin.gif":
            turtle_screen.bgpic("moulin.gif")
        if current_screen == "louvre.gif":
            turtle_screen.bgpic("louvre.gif")
        if current_screen == "jardin.gif":
            turtle_screen.bgpic("jardin.gif")
        expanded = False

#hides the here turtles
def hide_here_turtles():
    turtle_cafe_here_button.hideturtle()
    turtle_eiffel_tower_here_button.hideturtle()
    turtle_moulin_rouge_here_button.hideturtle()
    turtle_louvre_here_button.hideturtle()
    turtle_jardin_here_button.hideturtle()

#shows the here turtles
def show_here_turtles():
    turtle_cafe_here_button.showturtle()
    turtle_eiffel_tower_here_button.showturtle()
    turtle_moulin_rouge_here_button.showturtle()
    turtle_louvre_here_button.showturtle()
    turtle_jardin_here_button.showturtle()

#handles all the five location backgrounds and input validation
def here_cafe(x,y):
    cafe_screen()
    
def cafe_screen():
    turtle_screen.bgpic("cafe.gif")
    turtle_screen.setup(width = 800, height = 600)
    turtle_cafe_here_button.hideturtle()
    cafe_de_flore()

def cafe_de_flore():
    global num_mistakes, locations_visited
    hide_here_turtles()
    turtle_text.hideturtle()
    turtle_text.penup()
    turtle_text.color("#8b0000")
    turtle_text.goto(-70, 160)
    turtle_text.write("You are thirsty from the long travel to Paris,\nso you want to order a coffee with steamed milk.",align = "center", font = ("Arial", 18, "bold"))
    turtle_text.penup()
    turtle_text.color("black")
    turtle_text.goto(-15,110)
    turtle_text.write("Vous avez choisi ?", align = "center", font = ("Arial", 16, "bold"))
    answer = turtle.textinput("Enter response: ", '')
    if (answer != "Oui. Je voudrais un cafe au lait, s'il vous plait.") and (answer != "Oui. Je voudrais un café au lait, s'il vous plaît."):
        turtle_text.color("black")
        turtle_text.goto(-30,50)
        turtle_text.write("Je reviens dans un moment\n(I will come back later)", align = "center", font = ("Arial", 16, "bold")) 
        num_mistakes = num_mistakes + 1
        update_scoreboard()
        check_win()
    else:
        turtle_text.color("black")
        turtle_text.goto(-130,60)
        turtle_text.write("Très bien, je vous apporte ça tout de suite.\n(Very well, I will bring it right away.)", align = "center", font = ("Arial", 16, "bold"))
        locations_visited = locations_visited + 1
        update_scoreboard()
        turtle_text.clear()
        check_win()
    turtle_text.clear()
    turtle_notebook.onclick(expand_note)
    turtle_exit_button.onclick(map_screen)

def here_effiel(x,y):
    eiffel_screen() 

def eiffel_screen():
    turtle_screen.bgpic("eiffel.gif")
    turtle_text.clear()
    turtle_screen.setup(width = 800, height = 600)
    turtle_eiffel_tower_here_button.hideturtle()
    eiffel_tower()

def eiffel_tower():
    global num_mistakes, locations_visited
    hide_here_turtles()
    turtle_text.hideturtle()
    turtle_text.penup()
    turtle_text.color("red")
    turtle_text.goto(-15, 200)
    turtle_text.write("You're determined\nto see the Eiffel Tower but\nParis is a maze. Ask a local!",align = "center", font = ("Arial", 18, "bold"))
    answer = turtle.textinput('Enter question: ', '')
    if (answer != "Excusez-moi, où est la tour Eiffel ?") and (answer != "Excusez-moi, ou est la tour Eiffel ?"):
        turtle_text.hideturtle()
        turtle_text.penup()
        turtle_text.color("black")
        turtle_text.goto(75,-25)
        turtle_text.write("J’ai pas le temps !\n(I don't have time for this!)",  align = "center", font = ("Arial", 16, "bold"))
        num_mistakes = num_mistakes + 1
        update_scoreboard()
        check_win()
    else:
        turtle_text.hideturtle()
        turtle_text.penup()
        turtle_text.color("black")
        turtle_text.goto(-100,20)
        turtle_text.write("Tournez à droit et vous verrez la Tour Eiffel.\n(Turn right and you will see the Eiffel Tower.)", align = "center", font = ("Arial", 16, "bold"))
        locations_visited = locations_visited + 1
        update_scoreboard()
        turtle_text.clear()
        check_win()
    turtle_text.clear()
    turtle_notebook.onclick(expand_note)
    turtle_exit_button.onclick(map_screen)

def here_moulin(x,y):
    moulin_screen() 

def moulin_screen():
    turtle_screen.bgpic("moulin.gif")
    turtle_screen.setup(width = 800, height = 600)
    turtle_moulin_rouge_here_button.hideturtle()
    moulin_rouge()

def moulin_rouge(): 
    global num_mistakes, locations_visited
    hide_here_turtles()
    turtle_text.hideturtle()
    turtle_text.penup()
    turtle_text.goto(0, 150)
    turtle_text.color("#FAF9F6")
    turtle_text.write("The Moulin Rouge is everything you imagined:\nGlitter and Glam!!\nWaiting for the show to start, you don't have a watch,\nso you ask someone for the time.", align = "center", font = ("Arial", 16, "bold"))
    answer = turtle.textinput('Enter question: ', '')
    if (answer != "Quelle heure est-il ?"):
        turtle_text.goto(-50, 50 )
        turtle_text.color("yellow") 
        turtle_text.write("Je ne sais pas.\n(I don't know.)", align = "center", font = ("Arial", 16, "bold"))
        num_mistakes = num_mistakes + 1
        update_scoreboard()
        check_win()
    else:
        turtle_text.goto(-50, 50)
        turtle_text.color("yellow")
        turtle_text.write("Il est 20h30.\n(It is 8:30 pm.)", align = "center", font = ("Arial", 16, "bold"))
        locations_visited = locations_visited + 1
        update_scoreboard()
        turtle_text.clear()
        check_win()
    turtle_text.clear()
    turtle_notebook.onclick(expand_note)
    turtle_exit_button.onclick(map_screen)

def here_louvre(x,y):
    louvre_screen() 

def louvre_screen():
    turtle_screen.bgpic("louvre.gif")
    turtle_screen.setup(width = 800, height = 600)
    turtle_louvre_here_button.hideturtle()
    louvre()

def louvre():
    global num_mistakes, locations_visited
    hide_here_turtles()
    turtle_text.hideturtle()
    turtle_text.penup()
    turtle_text.goto(0, 200)
    turtle_text.color("#8b0000")
    turtle_text.write("You want to see the painting, The Coronation of Napoleon,\nbut the museum is enourmous. Go ask for help!", align = "center", font = ("Arial", 18, "bold"))
    answer = turtle.textinput('Enter question: ', '')
    if (answer != "Excusez-moi, où se trouve le tableau Le Sacre de Napoléon ?") and (answer != "Excusez-moi, ou se trouve le tableau Le Sacre de Napoleon ?"):
        turtle_text.penup()
        turtle_text.goto(0,50)
        turtle_text.color("black")
        turtle_text.write("Demandez à un autre employé.\n(Ask another employee)", align = "center", font = ("Arial", 16, "bold"))
        num_mistakes = num_mistakes + 1
        update_scoreboard()
        turtle_text.clear()
        check_win()
    else:
        turtle_text.penup()
        turtle_text.goto(0,50)
        turtle_text.color("black")
        turtle_text.write("Le tableau se trouve\ndans l’aile Denon,\nau deuxième étage, salle 75.\n(The Coronation of Napoleon is in the Denon Wing,\non the second floor in room 75.)" , align = "center", font = ("Arial", 16, "bold"))
        locations_visited = locations_visited + 1
        update_scoreboard()
        turtle_text.clear()
        check_win()
    turtle_text.clear()
    turtle_notebook.onclick(expand_note)
    turtle_exit_button.onclick(map_screen)

def here_jardin(x,y):
    jardin_screen() 

def jardin_screen():
    turtle_screen.bgpic("jardin.gif")
    turtle_screen.setup(width = 800, height = 600)
    turtle_jardin_here_button.hideturtle()
    jardin()

def jardin():
    global num_mistakes, locations_visited
    hide_here_turtles()
    turtle_text.hideturtle()
    turtle_text.penup()
    turtle_text.goto(125,175)
    turtle_text.color("#ff748c")
    turtle_text.write('Strolling through the Tuileries Garden,\nwhile looking at one of the flowerbeds,\nyou see a pretty flower.\nYou do not know the name of it\nso you ask another person for its name.', align = "center", font = ("Arial", 16, "bold"))
    answer = turtle.textinput('Enter question: ', '')
    if answer != "Excusez-moi, quel est le nom de la fleur ?":
        turtle_text.goto(30,50)
        turtle_text.color('black')
        turtle_text.write("Débrouille-toi !\n(Figure it out yourself!)", align = "center", font = ("Arial", 16, "bold"))
        num_mistakes = num_mistakes + 1
        update_scoreboard()
        check_win()
    else:
        turtle_text.goto(50,50)
        turtle_text.color('black')
        turtle_text.write("C’est une digitale pourpre.\n(This is a lady's glove)", align = "center", font = ("Arial", 16, "bold"))
        locations_visited = locations_visited + 1
        update_scoreboard()
        turtle_text.clear()
        check_win()
    turtle_text.clear()
    turtle_notebook.onclick(expand_note)
    turtle_exit_button.onclick(map_screen)

#updates scoreboard everytime mistake or correct answer inputted
def update_scoreboard():
    turtle_baguette.clear()
    baguette_scoreboard()

#checks if win or loss and disaplys corresponding screen
def check_win():
    global num_mistakes, locations_visited
    if locations_visited == 3:
        win_screen()
    elif num_mistakes == 3:
        loss_screen()

#draws fireworks if game won
def win_fireworks(turtle):
    turtle.width(1)
    for i in range(36):
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.color(random.choice(fireworks_colors))
        size = random.randint(20,100)
        turtle.speed(0)
        for i in range(36):
            turtle.forward(size)
            turtle.backward(size)
            turtle.right(10)
            turtle.speed(0)

#displays win screen with fireworks :)
def win_screen():
    hide_here_turtles()
    turtle_screen.bgpic("resized_game_end_screen.gif")
    turtle_display.goto(0,0)
    turtle_text.color("#fefec8")
    turtle_display.write("Bravo!\nYou have explored Paris in style.\nThe City of Light applauds your linguisic skills!\nWhat a magnificent journey! Bon voyage until next time!", align = "center", font = ("Arial", 16, "bold"))
    for f in range(10):
        win_fireworks(fire_turtle)

#displays loss screen :(
def loss_screen():
    hide_here_turtles()
    turtle_screen.bgpic("resized_game_end_screen.gif")
    turtle_display.goto(0,0)
    turtle_text.color("#fefec8")
    turtle_display.write("Sorry!\nEvery explorer faces a few setbacks.\nBut do not worry—Paris will still be waiting for you.\nKeep practicing your French; your next adventure awaits!", align = "center", font = ("Arial", 16, "bold"))

#exit button
def exit():
    turtle_screen.addshape("resized_exit_button.gif")
    turtle_exit_button.penup()
    turtle_exit_button.goto(300,-300)
    turtle_exit_button.shape("resized_exit_button.gif")
    turtle_exit_button.showturtle()

#main game play loop which calls necessary functions to organize and run game
game_loop = True
while game_loop:
    intro_screen(resized_image)
    turtle_exit_button.onclick(map_screen)
    turtle_screen.listen()
    turtle_screen.mainloop()