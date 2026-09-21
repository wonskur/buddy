import time
import actions
import os
import sys
def play(frames, fps=4, loops=1):
    for _ in range(loops):
        for frame in frames:
            print("\033[H\033[J", end="")
            print("\n".join(frame))
            time.sleep(1 / fps)
#def pretty(string):
#    c = len(string)
#    return "─" + "─"*c + "─" + "\n" + " " + string + "\n" + "─" + "─"*c + "─"
import os

def pretty(string):
    try:
        line_length = os.get_terminal_size().columns
    except OSError as e:
        print(f"Error: {e}")
        line_length = 80 
    border = "─" * line_length
    return border + "\n" + string + "\n" + border

def calc(string):
    play(actions.thinking, loops=2)
    string = string.strip()
    if not string.startswith("calc"):
        play(actions.dontknow, loops=2)
        return pretty("Error: the command must start with 'calc'")
    expression = string[4:].strip()
    if not expression:
        play(actions.standing, loops=2)
        return pretty("Error: the command must start with 'calc'")
    try:
        result = eval(expression)
        play(actions.standing, loops=2)
        return pretty(str(result))
    except Exception as e:
        play(actions.standing, loops=2)
        return pretty(f"Calculation error: {e}")
def read(file_name, target_words):
    target_words = [w.lower() for w in target_words]
    found_lines = []
    
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            if any(word in line.lower() for word in target_words):
                found_lines.append(line.strip())
                
    return "\n".join(found_lines)

def make(string):# Fingers crossed it actually works lol
    cmd, _, arg = string.partition(" ")
    arg = arg.strip()
    play(actions.standing, loops=1)
    match cmd:
        case "say":
            return pretty(arg)
        case "time":
            return pretty(time.strftime("%H:%M"))
        case "date":
            return pretty(time.strftime("%Y-%m-%d"))
        case "read":
            parts = arg.split()
            if len(parts) < 2:
                return pretty("Error: enter file name AND at least one word for search")
            file_name = parts[0]
            target_words = parts[1:]
            try:
                return pretty(read(file_name, target_words))
            except FileNotFoundError:
                return pretty(f"Error: File '{file_name}' not found")

        case "calc":
            return calc(string)
        case "quit":
            return None
        case _:
            play(actions.dontknow,loops=1)
            return pretty(f"Unknown command: {cmd}")