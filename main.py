import customtkinter as ctk
import subprocess
import pygame
import messagebox

# Initialize Pygame Mixer for Sound
pygame.mixer.init()
sound_on = True  # Sound starts ON

# Create Main Window
window = ctk.CTk()
window.geometry("700x700")
window.resizable(False, False)
window.title("Line Score Game")
window.iconbitmap("Data/icon.ico")
window.configure(background="black")

# Function to Start the Game
def start_game():
    window.destroy()
    subprocess.run(["python", "main_game.py"])


# Function to Toggle Sound
def show_rules():
    rules_win = ctk.CTkToplevel(window)
    rules_win.geometry("500x300")
    rules_win.title("Game Rules")
    rules_win.configure(background="black")

    # Rules text
    rules_text = (
        "🔹 Control your paddle to hit the ball.\n"
        "🔹 Use W/S for Player 1 (Left paddle).\n"
        "🔹 Use UP/DOWN arrows for Player 2 (Right paddle).\n"
        "🔹 Prevent the ball from touching the wall behind you.\n"
        "🔹 Each goal increases the opponent’s score.\n"
        "🔹 First player to reach a certain score wins!\n"
        "🔹 player who is score 5 points first he will win\n"
        "🔹 Good Luck *\n"
    )

    ctk.CTkLabel(rules_win, text="Game Rules", font=ctk.CTkFont("Arial", 20), text_color="white").pack(pady=10)
    ctk.CTkLabel(rules_win, text=rules_text, font=ctk.CTkFont("Arial", 16), text_color="gray", wraplength=450, justify="left").pack(pady=10)

# Function to Show Credits
def show_credits():
    messagebox.showinfo("Credits", "Created by Yossef Ibrahim\nVersion 25.0")
# Function to Exit
def exit_game():
    window.destroy()

# Title Label
ctk.CTkLabel(window, text="Line Score Game", font=ctk.CTkFont("Arial", 35, "bold"), text_color="white").place(relx=0.5, rely=0.1, anchor="center")
ctk.CTkLabel(window, text="_________________", font=ctk.CTkFont("Arial", 35, "bold"), text_color="white").place(relx=0.5, rely=0.15, anchor="center")

# Start Button
ctk.CTkButton(window, text="Start", font=ctk.CTkFont("Arial", 30), border_width=3, fg_color="green",
              text_color="white", width=200, command=start_game).place(relx=0.35, rely=0.3)

# Option Button (Sound Toggle)
option_btn = ctk.CTkButton(window, text=" Rules ", font=ctk.CTkFont("Arial", 30), border_width=3, fg_color="blue",
                           text_color="white", width=200, command=show_rules)
option_btn.place(relx=0.35, rely=0.45)

# Credits Button
ctk.CTkButton(window, text="Credits", font=ctk.CTkFont("Arial", 30), border_width=3, fg_color="purple",
              text_color="white", width=200, command=show_credits).place(relx=0.35, rely=0.6)

# Exit Button
ctk.CTkButton(window, text="Exit", font=ctk.CTkFont("Arial", 30), border_width=3, fg_color="red",
              text_color="white", width=200, command=exit_game).place(relx=0.35, rely=0.75)

# Run Main Loop
window.mainloop()
