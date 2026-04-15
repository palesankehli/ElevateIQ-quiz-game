import json

def main():
    welcome_banner()
    help_section()


def load_data():
    with open('questions.json', 'r') as file:
        return json.load(file)
    
BURGUNDY = '\033[38;2;128;0;32m'
GOLD = '\033[38;2;212;175;55m'
RESET = '\033[0m'
BOLD = '\033[1m'

def welcome_banner():
  
    print(f"\n{BURGUNDY}┏" + "━" * 80 + f"┓" )
    print(f"┃" + " " * 30 + f"{GOLD}{BOLD}WELCOME TO ELEVATE IQ" + " " * 29 + f"{BURGUNDY}┃")
    print(f"┗" + "━" *80 + f"┛{RESET}")
    print(f"""{BOLD}{GOLD}       
          A test of your knowledge across multiple categories,
                    Let's see how smart you are! 😉
          {RESET}""")

def help_section():
    print(f"\n{BURGUNDY}┏" + "━" * 80 + f"┓" )
    print(f"┃" + " " * 30 + f"{GOLD}{BOLD}•  GAME INSTRUCTIONS  •" + " " * 27 + f"{BURGUNDY}┃")
    print(f"┗" + "━" *80 + f"┛{RESET}")

    print(f"""   {GOLD}{BOLD}
          
    • Pick a category to test your specific knowledge(Science, History etc)
    • Choose between Easy, Medium, or Hard difficulty.
    • Choose the correct answer from the options provided and score points.
    • You get a hint after 2 tries.
    • If you get answer incorrectly after 3 attempts, answer will be displayed{RESET}

""")


if __name__ =="__main__":
    main()