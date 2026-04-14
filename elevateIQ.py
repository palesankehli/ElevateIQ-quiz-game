import json


def load_data():
    with open('questions.json', 'r') as file:
        return json.load(file)
    
BURGUNDY = '\033[38;2;128;0;32m'

def welcome_banner():
  
    print(f"\n{BURGUNDY}╔" + "═" * 80 + f"╗" )
    print("║" + " " * 30 + "WELCOME TO ELEVATE IQ" + " " * 29 + "║")
    print("╚" + "═" *80 + "╝")

welcome = welcome_banner()
print(welcome)
