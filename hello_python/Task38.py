# Напишите программу, удаляющую из текста все слова содержащие "абв".


text = "Я знаю, что ничеабвго не знаю. "

text = list(filter(lambda x: "абв" not in x, text.split()))
text = " ".join(text)

print(text)