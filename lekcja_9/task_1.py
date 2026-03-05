def append_to_file(text: str):

    with open("lesson_9/dziennik2.txt", mode="a", encoding="utf-8") as f:
        f.write(f"{text} \n")

while True:
    user_input = input("Podaj tekst: ")

    if user_input == 'koniec':
        break
    else:
        append_to_file(user_input)