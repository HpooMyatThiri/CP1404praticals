'''
get username
display """(H)ello
(G)oodbye
(Q)uit"""
get choice
while choice != Q
   if choice == H
       display "hello" username
   else if choice == G
       display "goodbye" username
   else
       display invalid choice
   display """(H)ello
(G)oodbye
(Q)uit"""
get choice
   get choice
display finished message
'''



username = input("Enter name: ")
print("""(H)ello
(G)oodbye
(Q)uit""")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {username}")
    elif choice == "G":
        print(f"Goodbye {username}")
    else:
        print("Invalid choice")
    print("""(H)ello
(G)oodbye
(Q)uit""")
    choice = input(">>> ").upper()
print("Thank you for using!")


