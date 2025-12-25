from services.auth_service import register_user,authenticate_user

def main():
    print("===Job Portal System===")
    print("1. Register")
    print("2. Login")

    choice = input("Select an option (1 or 2): ")

    if choice=='1':
        username=input("Enter username: ").strip().lower()
        email=input("Enter email: ").strip().lower()
        password=input("Enter password: ")
        role=input("Enter role (admin/employer/job_seeker): ").strip().lower()  

        try:
            user=register_user(username,email,password,role)
            print("Registration successful!")
            print(user.display_info())
        except ValueError as e:
            print(f"Error: {e}")

    elif choice=='2':
        username=input("Enter username:").strip().lower()
        password=input("Enter password:")
        user=authenticate_user(username,password)

        if user:
            print("Login successful!")
            print(user.display_info())
        else:
            print("Invalid username or password.")
    
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__=="__main__":
    main()