def interpret(command: str) -> str:
    command = command.replace('()', 'o').replace('(al)','al')
    print(command)


command = "(al)G(al)()()G"
# Output: "Goal"
interpret(command)
