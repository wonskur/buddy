import actions
import command

command.play(actions.greeting,loops=1)
while True:
    cmd = input("\n> ")
    result = command.make(cmd)
    if result is None:
        print(command.pretty("Bye!"))
        break
    print(result)