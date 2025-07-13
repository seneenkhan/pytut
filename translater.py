def translate(phrase):
    translated_text = ""
    for letter in phrase:
        if letter  in "AEIOUaeiou":
            translated_text = translated_text + "r"
        else:
            translated_text = translated_text + letter
    return translated_text

print(translate(input("Enter a text: ")))