
with open("artifacts01.txt", "r") as f:
    text = f.read()


with open("artifacts02.txt", "w") as f:
    text = f.write(text + "added lines")

print("end of stage 03")