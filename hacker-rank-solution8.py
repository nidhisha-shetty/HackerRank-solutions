# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def splitjoin(string):
    return "-".join(string.split(" "))

string=input("Enter a line")
final_string= splitjoin(string)
print(final_string)
