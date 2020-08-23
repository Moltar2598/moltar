def emoji_convertor(message):
    emoji = {
        ':)': "😊",
        ':(':'😢'
        
    }
    sentence = message.split(" ")
    output = ""
    for ch in sentence:
        output += emoji.get(ch,ch) + ' '
    return output

message = input(">")
output = emoji_convertor(message)
print(output)