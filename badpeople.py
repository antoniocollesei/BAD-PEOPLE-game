import random
import tkinter as tk
from tkinter import simpledialog

# List of sentences
items = [
    "Most likely to be childhood friends with Hitler?",
    "Most likely to ask an overweight woman if she's pregnant?",
    "Most likely to burn down their home for the insurance money?",
    "Who will have the most divorces by the time they're 80?",
    "Who would be the best stripper?",
    "In their lifetime, who's most likely to perform sexual acts for money?",
    "Most likely to have a naked picture of themselves on the Internet?",
    "Who masturbates the most to former lovers?",
    "Who will be the most difficult old person to be around?",
    "Most likely to have a secret sexual fetish?",
    "Who has slept with someone in the shortest amount of time after meeting them?",
    "Most likely to secretly run a meth lab?",
    "Most likely to join a cult?",
    "If we were all in prison, who would rise to prison gang leader?",
    "Most likely to get too kinky on a first date hook-up?",
    "Most likely to impregnate someone (or get pregnant) tonight?",
    "Who would charge the most as a hitman?",
    "If we were all prostitutes, who would charge the most?",
    "If a private investigator did a background check on all of us, whose would be the most unsettling?",
    "If I decided to rob a bank, who's the last person I'd choose to help me?",
    "Least likely to give up their seat on the bus for an elderly person?",
    "Most likely to tip less than 10% at a restaurant?",
    "Who has the best chance of cheating a lie detector test?",
    "Most likely to gain weight after marriage?",
    "Who would I call if I needed help burying a dead body?",
    "In the event of a zombie apocalypse, who would sacrifice everyone here to save themselves?",
    "Who will be the next person to get punched in the face?",
    "Who would I trust the least with a newborn baby?",
    "If we were all on Survivor™, who would be the first person voted off the island?",
    "Most likely to want to build a wall between Mexico and the U.S.?",
    "Most likely to support polygamy?",
    "Most likely to become a liability after two drinks?",
    "Most likely to get a tattoo they will later regret?",
    "Most likely to steal from their employer?",
    "Whose funeral will have the smallest attendance?",
    "Most likely to get upset playing Bad People?",
    "If we were all stand-up comedians, who would get the least amount of laughs?",
    "Most likely to create a scam business?",
    "In their lifetime, who will have the least positive impact on the human species?",
    "Most likely to sell out their family and friends for fame?",
    "Most likely to commit a hit-and-run?",
    "Most likely to follow-through on a revenge plot?",
    "Whose face looks most like an animal's face?",
    "Who would be the worst reality TV show star?",
    "Who would be the worst phone sex operator?",
    "Who would _________ for the least amount of money?",
    "Most likely to appear on the 'NO FLY LIST'?",
    "Least likely to tell a new sexual partner that they have an STD?",
    "Most likely to marry for money?",
    "Who should be banned from creating offspring?",
    "Most likely to 'cock block' a friend?",
    "Most likely to purchase a mail-order wife/husband?",
    "Who's the last person I'd want to be trapped in an elevator with?",
    "Who thinks they're more attractive than they actually are?",
    "Most likely to accidentally shoot themselves?",
    "Most likely to Facebook® creep a new love interest for several hours?",
    "Most likely to RSVP 'yes' to a party but never show up?",
    "Most likely to give a drunk, train wreck speech at a wedding?",
    "Who has secretly done something VERY illegal and gotten away with it?",
    "Most likely to murder their spouse for the insurance money and get away with it?",
    "Who has probably successfully blackmailed someone?",
    "Most likely to turn up drunk to pre-drinks?",
    "Who takes the most 'sick days off' without actually being sick?",
    "If I decided to kidnap someone, who's the last person I'd ask to help me?",
    "Most likely to talk their way out of a speeding ticket?",
    "If I were on Who Wants to Be a Millionaire™, who's the last person I'd call as a lifeline?",
    "Least likely to be a target for identity theft?",
    "Who's least affected by 'save the children' ads?",
    "Most likely to enter as a contestant on The Bachelor®/The Bachelorette®?",
    "Least likely to be remembered at a party?",
    "Who would be the most successful serial killer?",
    "Most likely to have a midlife crisis?",
    "Most likely to pay for sex?",
    "Most likely to end up broke due to a gambling addiction?",
    "Least likely to shave their genital area?",
    "Most likely to appear as a guest on Maury®?",
    "In their lifetime, who's most likely to be committed to an insane asylum?",
    "Most likely to get fired for _________?",
    "Who's the most high maintenance in a relationship?",
    "Least likely to sacrifice their life for a family member?",
    "If we were all homeless panhandlers, who would make the least amount of money?",
    "In their lifetime, who will most likely need a liver transplant?",
    "If everyone committed _________, who would be the last person to get caught?",
    "Most likely to enjoy being dominated in the bedroom?",
    "Most likely to show up to an Emergency Room with a _________ up their ass?",
    "Most likely to go ________ with Donald Trump?",
    "Most likely to fall for a pyramid scheme?",
    "Who was the last person to piss on a sexual partner?",
    "If a big fire broke out right now, who would push everyone out of the way to get out first?",
    "Most likely to become a vegetarian because their partner wanted them to?",
    "Most likely to try ____________ with Charlie Sheen?",
    "Least likely to try ___________?",
    "Who will be the next person to have a threesome?",
    "Most likely to join ISIS?",
    "Most likely to break up with someone because _________?",
    "If we were all therapists, who would probably sleep with their patients?",
    "Who would be the worst person to work for?",
    "Who was the last person to masturbate?",
    "Least likely to end a relationship with someone if they _________?",
    "Most likely to become a liability after eating a pot brownie?",
    "Least likely to send a sext?",
    "Who has seen the most people in this room naked?",
    "Who has had a sexual dream about ____________?",
    "Who could never say no to ___________?",
    "In their lifetime, who's most likely to become a pimp or madam?",
    "Most likely to have had sex in the back of a taxi?",
    "Who has done the most 'walks of shame'?",
    "Least likely to believe in global warming?",
    "Who is most like their racial stereotype?",
    "Who would get the most enjoyment from being a member of the opposite sex for a day?",
    "Most likely to lie to someone to get something they want?",
    "Who would sell their soul for the least amount of money?",
    "Most likely to fake an orgasm?",
    "If I was the ruthless dictator of a country, who would I choose as my second-in-command?",
    "Most likely to convince the group to play strip poker?",
    "They say, 'You can't judge a book by its cover.' Who did I misread when we first met?",
    "Most likely to 'not get the joke'?",
    "Most likely to cheat while playing a board game?",
    "Who has the largest porn collection?",
    "Most likely to crack a beer during a eulogy?",
    "Most likely to laugh if they saw a blind person trip?",
    "Most likely to say, 'I'm not racist, but ...'?",
    "Most likely to fart and blame it on someone else?",
    "Most likely to shout the wrong name during sex?",
    "Who has had sex in the most random place?",
    "Who is the worst person to call for relationship advice?",
    "Most likely to have sex with a homeless guy because they thought he was a hipster?",
    "Tattoo a teardrop on their face for the least amount of money?",
    "Most likely to end up on the FBI's Most Wanted List?",
    "Most likely to steal from a tip jar?",
    "Most likely to create a fake social media account to spy on someone?",
    "Who has gone the longest without showering?",
    "Most likely to borrow something with no intention of returning it?",
    "Who is 'never the problem' in a relationship?",
    "Who really needs to start making New Year's resolutions?",
    "Who would be the easiest to kidnap?",
    "Most likely to lie on their resume?",
    "Who was the oldest person to lose their virginity?",
    "Most likely to leave a party by blowing glitter in your face and disappearing?",
    "Who would take the longest to be reported to the police as missing?",
    "Who has the worst 'game'?",
    "Most likely to shed the next drunken tear?",
    "Most likely to accidentally have drugs on them while going through airport security?",
    "Most likely to draw a dick on a passed out friend?",
    "Who was the last person to have a drink thrown in their face?",
    "Who was the last person to be drunk/high at work?",
    "Most likely to say 'I love you' too early?",
    "Most likely to wake up tomorrow not knowing where they are?",
    "Who has the worst poker face?",
    "If we were all police officers, who would be the dirty cop?",
    "Most likely to run into a former lover and not remember their name?",
    "Who can't go 10 minutes without looking at themselves in the mirror?",
    "Most likely to rat me out if they were under pressure from the cops?",
    "If we were all characters in a horror movie, who would get killed first?",
    "Most likely to sleep their way to the top?",
    "Most likely to puke and rally?",
    "Most likely to have a secret body piercing or tattoo?",
    "Most likely to have a secret sex tape?",
    "Most likely to sleep with a co-worker?"
]

# Create a Tkinter window
window = tk.Tk()

# Set the window title
window.title("BAD PEOPLE")

# Set the window size
window.geometry("1000x500")

# Define a list to store players and their scores
players = []

# Define a function to add a new player
def add_player():
    global players
    player_name = simpledialog.askstring("Add Player", "Enter player name:")
    if player_name:
        # Prompt the user for the player's initial score
        player_score = simpledialog.askinteger("Add Player", f"Enter {player_name}'s score:", initialvalue=0)
        # Add the new player to the players list
        players.append({'name': player_name, 'score': player_score})
        # Update the players label
        update_players_label()

def assign_point(player_name):
    # Find the player in the players list and add 1 to their score
    for player in players:
        if player['name'] == player_name:
            player['score'] += 1
    # Update the players label
    update_players_label()

# Define a function to update the players label
def update_players_label():
    # Create a string to display all players and their scores
    players_str = "Players:\n"
    for player in players:
        players_str += f"{player['name']}: {player['score']}\n"
    # Update the players label with the new string
    players_label.config(text=players_str)

def select_item():
    global selected_item
    # Generate a new random item that is not the same as the previous one
    new_item = random.choice([item for item in items if item != selected_item])
    # Update the label with the new item
    label.config(text=f"{new_item}")
    # Update the selected_item variable
    selected_item = new_item
    # Prompt the user for the player who deserves a point
    player_names = [player['name'] for player in players]
    if player_names:
        point_window = tk.Toplevel(window)
        point_window.title("Assign Point")
        prompt_label = tk.Label(point_window, text="Who deserves a point?")
        prompt_label.pack()
        for player_name in player_names:
            player_button = tk.Button(point_window, text=player_name, command=lambda name=player_name: assign_point(name))
            player_button.pack()
    else:
        tk.messagebox.showerror("Error", "There are no players.")


# Select the first item from the list
selected_item = random.choice(items)

# Create a label with the selected item
label = tk.Label(window, text=f"{selected_item}", font=("Arial", 18))
label.pack(pady=20)

# Create a button to select a new item
button = tk.Button(window, text="Next Round", command=select_item)
button.pack()

# Create a button to add a new player
add_player_button = tk.Button(window, text="Add New Player", command=add_player)
add_player_button.pack()

# Create a label to display players and their scores
players_label = tk.Label(window, text="")
players_label.pack()

# Run the window loop
window.mainloop()
