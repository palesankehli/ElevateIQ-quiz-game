import json


def load_data():
    with open('questions.json', 'r') as file:
        return json.load(file)
    
BURGUNDY = '\033[38;2;128;0;32m'
GOLD = '\033[38;2;212;175;55m'
RESET = '\033[0m'
BOLD = '\033[1m'

def welcome_banner():
  
    print(f"\n{BURGUNDY}╔" + "═" * 80 + f"╗" )
    print(f"║" + " " * 30 + f"{GOLD}WELCOME TO ELEVATE IQ" + " " * 29 + f"{BURGUNDY}║")
    print(f"╚" + "═" *80 + f"╝{RESET}")

welcome_banner()
