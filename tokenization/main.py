# pip freeze > requirements.txt is command that create a file requirements.txt which shows what packages are installed

import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! My name is Aditya"
print(text)
tokens = encoder.encode(text)

print(tokens)
print(len(tokens))

detoken = encoder.decode(tokens)

print(detoken)