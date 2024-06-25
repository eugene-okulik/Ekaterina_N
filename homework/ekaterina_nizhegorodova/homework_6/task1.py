text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
text_list = text.split()
fin_text = []
for word in text_list:
    if word.endswith(","):
        word = word.replace(",", "ing,")
    elif word.endswith("."):
        word = word.replace(".", "ing.")
    else:
        word = word + "ing"
    fin_text.append(word)
print(" ".join(fin_text))
