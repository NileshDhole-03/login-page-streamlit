import streamlit as st
# import passcheck as cp  # Import the checkpass module

def main():
    st.title("Simple Login and Registration Page")

    menu = ["Home", "Login", "Register","premCHUTIya"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to the Home Page")
        st.write("Please use the sidebar to navigate to the login or registration page.")

    elif choice == "Login":
        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            st.info(f"Attempted login with username: {username} and password: {password}")
            # Display message for now (replace with actual authentication logic)
            st.success(f"Welcome {username}!")  # Simulate a successful login
    # elif choice=="premCHUTIya":
    #     if st.button("i am gay"):
    #         st.text("the prem who is the founder of the gay club which is present in the jspm college and his community name is LGBTQ++")

    elif choice == "Register":
        st.subheader("Create a New Account")

        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')

        if st.button("Register"):
            st.info(f"Attempted registration with username: {new_username} and password: {new_password}")

            # if cp.checkpwd(password):
            #     # Display message for now (replace with actual registration logic)
            #     st.success("Account created successfully!")
            #     st.info("Go to the Login page to log in")
            # else:
            #     st.error("Password must be at least 8 characters long, contain at least one special character, and one number.")

if __name__ == '__main__':
    main()
