def print_message( *, message, level="INFO",):
    print(f"{level} {message}")

print_message(message="estamos locos??")
print_message(level="FYI", message="estamos locos??")
print_message("***", message="estamos locos??") #TyperError, keyworkd only arguments