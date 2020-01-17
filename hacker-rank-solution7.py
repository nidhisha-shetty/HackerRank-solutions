# The first line contains the first name, and the second line contains the last name.

# The length of the first and last name ≤10. Print statement "Hello firstname lastname! You just delved into python."

f_n=input("Enter first name")
l_n=input("Enter last name")
len_f_n=len(f_n)
len_l_n=len(l_n)
if (len_f_n <=10) and (len_l_n <=10):
    print("Hello " + f_n + " " +l_n +"! You just delved into python.")
