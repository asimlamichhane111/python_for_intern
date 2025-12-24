from models.user import User
def main():
    user1=User("asim","asim@example.com","Admin")
    user1.set_password("asdfghjkl")
    print(user1.display_info())

    print("Password correct?",user1.check_password("asdfghjkl"))
    print("Password correct?",user1.check_password("wrongpass"))

if __name__=="__main__":
    main()