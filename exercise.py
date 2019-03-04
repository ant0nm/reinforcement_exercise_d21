digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
rus = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'cемь', 'восемь', 'девять']

# creating a dictionary that maps the digits to different languages
languages = {"french": fr, "english": en, "russian": rus}
num_to_lang = {}
for digit in digits:
    num = int(digit)
    index = num - 1
    l = {}
    for key, value in languages.items():
        l[key] = languages[key][index]
    num_to_lang[digit] = l

print("Here's the RAW resulting digit-to-language dictionary:")
print(num_to_lang)

print()
print("Same dictionary, but printed nicely:")
for n, l in num_to_lang.items():
    print('*', '{} - {}'.format(n, l))
