from gingerit.gingerit import GingerIt

text = input("Enter your text ")

corrected_text = GingerIt().parse(text)

print(corrected_text["result"])

