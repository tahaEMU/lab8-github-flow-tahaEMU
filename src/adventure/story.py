from adventure.utils import read_events_from_file
import random

# --- Rich formatting setup (optional) ---
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt
    from rich.rule import Rule
    console = Console()
    _RICH_AVAILABLE = True
except Exception:
    console = None
    _RICH_AVAILABLE = False
# ----------------------------------------


def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."


def left_path(event):
    return "You walk left. " + event


def right_path(event):
    return "You walk right. " + event


if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    # Fancy intro using Rich (if available)
    if _RICH_AVAILABLE:
        console.print(Panel.fit("🌲 Welcome to the Adventure! 🌲", subtitle="Choose wisely...", style="bold cyan"))
        console.print(Rule(style="dim"))
        console.print("You wake up in a dark forest. You can go [green]left[/] or [magenta]right[/].")
    else:
        print("You wake up in a dark forest. You can go left or right.")

    while True:
        if _RICH_AVAILABLE:
            choice = Prompt.ask("Which direction do you choose? (left/right/exit)").strip().lower()
        else:
            choice = input("Which direction do you choose? (left/right/exit): ").strip().lower()

        if choice == 'exit':
            if _RICH_AVAILABLE:
                console.print(Panel.fit("Goodbye, adventurer! See you next time.", style="bold cyan"))
            else:
                print("Goodbye, adventurer!")
            break

        outcome = step(choice, events)

        if _RICH_AVAILABLE:
            console.print(Panel.fit(outcome, style="bold green"))
        else:
            print(outcome)