from ids import ids

text = input("Enter text: ")

output = []

i = 0
while i < len(text):
    # handle multi-character symbols if needed
    if text[i:i+6] in ids:          # e.g. {{1.}}
        output.append(str(ids[text[i:i+6]]))
        i += 6
    else:
        char = text[i]
        if char in ids:
            output.append(str(ids[char]))
        else:
            output.append("????")   # unknown character
        i += 1

print(" ".join(output))
