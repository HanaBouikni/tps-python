string=str(input("type in a string: "))

frame_width = 30

padding =(frame_width-len(string))//2

print("*" * frame_width)
print("*" + " " * padding + string + " " * padding + "*")
print("*" * frame_width)
