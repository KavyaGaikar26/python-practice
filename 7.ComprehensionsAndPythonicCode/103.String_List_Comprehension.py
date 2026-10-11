sentence = "Python makes programming interesting and enjoyable"

string = [word for word in sentence.split() if len(word) > 5]

print(string)
