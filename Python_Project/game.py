import turtle
import random
import time
import pickle
import operator
import os

turtle.setup(width=1200, height=800, startx=None, starty=None)  # Set screen height/width
scores = {}  # Dictionary to keep track of player scores

def show_circle(a_turtle, color):

    """
    This method will draw a python turtle circle and its
    color will be based on the color that is passed in
    from our list of potential colors.
    """
    a_turtle.color(color)   # Set the color
    a_turtle.speed(100)     # Set base speed so circles are drawn instantly
    a_turtle.begin_fill()  # Start filling
    a_turtle.circle(100)   # Draw circle
    a_turtle.end_fill()   # Finish filling

def new_game():

    """
    This method will set up a game of simon says.
    It requires a helper function "show_circle()", which
    draws the pattern as it gets larger.
    """

    # Stores the colors for the circles
    simon_colors = ["blue", "green", "red", "yellow"]
    scores_turtle = turtle.Turtle()

    try:
        with open("scores.txt", "rb") as myFile:  # Open file and store data in dictionary
            scores = pickle.load(myFile)
    except EOFError:  # If empty file give empty dictionary
        scores = {}

    shape_turtle = turtle.Turtle()  # Turtle that draws the circles

    while True:
        # Clears screen before each new game
        turtle.clearscreen()
        turtle.clear()
        turtle.reset()
        scores_turtle.clear()
        scores_turtle.reset()
        scores_turtle.hideturtle()

        # Prompts user to enter his/her name
        name = turtle.textinput("Simon Says game", "Enter your name and then press OK:")

        # Displays start screen instructions
        turtle.write("Hello " + name + " and welcome to Simon Says!\n\nA series of circles will"
        " be displayed on the screen.\nYour task, should you choose to accept, is to guess the pattern.\nEnter your guess in the text box."
        "\n\n(ex: if the pattern is blue red, enter br)\n\nHave fun!\n\n", align="center", font=("Arial", 14, "bold"))

        # Waits for 1 second so user can read instructions
        time.sleep(1)

        # User can enter anything here to start game
        # Game will only end here if the user clicks cancel
        instructions_input = turtle.textinput("Ready to play?", "Press OK to continue.")

        # Clears screen once user hits OK button
        if instructions_input.strip() == "":
            turtle.clear()
        else:
            turtle.clear()

        correct = True  # Checks if the answer is correct
        score = 0  # Stores user score
        answer = []  # Stores the correct answer pattern with each color
        answer_string = ""   # Stores the correct answer pattern with each starting letter

        # Keeps going while the answer is correct
        while correct:
            rand = random.randint(0, 3)  # Random number to generate a random color
            answer.append(simon_colors[rand])  # Adds the color to the answer list
            answer_string += answer[score][0]  # Adds the first letter of each color to answer_string

            # Draws the sequence of circles
            for i in range(0, len(answer)):
                show_circle(shape_turtle, [answer[i]])

                # Decreases sleep time as score goes up, stops at .3 seconds
                if score == 0:
                    time.sleep(1.5)
                elif score < 10:
                    time.sleep(1.5 - ((score + 1) * .1))
                else:
                    time.sleep(.3)

                shape_turtle.hideturtle()
                shape_turtle.clear()

            # Prompt user to guess
            user_guess = turtle.textinput("Answer", "Enter your guess:")
            user_guess = user_guess.strip().lower()  # Remove unnecessary white spaces and convert to lower case

            # If answer is not equal to the answer_string, stops game
            if user_guess != answer_string:
                correct = False
                scores[name] = score
                sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))
                turtle.write("TOP SCORES\n\n", align="center", font=("Arial", 14, "bold"))
                for key, val in sorted_scores:
                    scores_turtle.write("\n")
                    scores_turtle.write(str(key) + ".    " + str(val), align="center", font=("Arial", 10))

            # Adds to user score each round they get one correct
            else:
                score += 1

        # Asks user if he/she wants to play again
        if not correct:
            continue_option = turtle.textinput("GAME OVER!", "Press OK to play again. Enter q and hit OK to quit:")
        # User quits the game
        if continue_option.strip() == "q" or continue_option.strip() == "Q":
            break

# Main game loop
new_game()
