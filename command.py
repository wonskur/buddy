import time
import actions
def play(frames, fps=4, loops=1):
    for _ in range(loops):
        for frame in frames:
            print("\033[H\033[J", end="")
            print("\n".join(frame))
            time.sleep(1 / fps)

def calc(string, ): # Без безопасности сами виноваты если чо то будет
    play(actions.thinking, loops=2)
    string = string.strip()
    if not string.startswith("calc"):
        return "Error: the command must start with 'calc'"
    expression = string[4:].strip()
    if not expression:
        return "Error: the command must start with 'calc'"
    try:
        return eval(expression)
    except Exception as e:
        return f"Calculation error: {e}"
    play(actions.standing, loops=2)