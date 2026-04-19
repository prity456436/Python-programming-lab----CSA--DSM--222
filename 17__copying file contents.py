# 17.  Copy contents of one file to another after removing digits.
with open("E:\\sample.txt", "r") as f1, open("E:\\output.txt", "w") as f2:
    for line in f1:
        new_line = ""
        for ch in line:
            if not ch.isdigit():   # skip digits
                new_line += ch
        f2.write(new_line)

print("File copied successfully without digits.")
