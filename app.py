import streamlit as st
from routes.home.home import home_page
from routes.quiz.quiz import quiz
from routes.about.about import about_us

# Define functions for different routes/pages --- will be changed later into separate route pages

def learning_paths_page():
    st.title("Learning Paths")
    # Add content for the learning paths page
    st.write("Discover personalized learning paths tailored to your interests and skill level.")

def quizzes_page():
    st.title("Quizzes")
    # Add content for the quizzes page
    st.write("Test your knowledge and understanding with interactive quizzes on various topics.")
    quiz()

def projects_page():
    st.title("Real-world Projects")
    # Add content for the real-world projects page
    st.write("Explore a collection of real-world project ideas to apply your skills.")

def profile_page():
    st.title("User Profile")
    # Add content for the user profile page
    st.write("View and manage your profile, track your learning progress, and set preferences.")

def community_page():
    st.title("Community Hub")
    # Add content for the community hub page
    st.write("Engage with the platform's community through forums, discussions, and collaborative projects.")

def recommendations_page():
    st.title("AI Recommendations")
    # Add content for the AI recommendations page
    st.write("Discover personalized recommendations generated by AI models based on your preferences.")

def settings_page():
    st.title("Settings")
    # Add content for the settings page
    st.write("Customize your experience, adjust notification preferences, and manage account settings.")

def about_page():
    about_us()

def help_page():
    st.title("Help and Support")
    # Add content for the help and support page
    st.write("Get assistance, access FAQs, and find resources for troubleshooting.")

# Define function to select page based on user input
def select_page():
    page = st.sidebar.selectbox(
        "Select Page",
        ["Home", "Quizzes", "User Profile", 
         "Community Hub", "AI Recommendations", "Settings", "About Us", "Help and Support"]
    )
    return page

# Main function to run the app
def main():
    st.sidebar.title("Navigation")
    selected_page = select_page()

    if selected_page == "Home":
        home_page()
    elif selected_page == "Quizzes":
        quizzes_page()
    elif selected_page == "User Profile":
        profile_page()
    # elif selected_page == "Community Hub":
    #     community_page()
    # elif selected_page == "AI Recommendations":
    #     recommendations_page()
    # elif selected_page == "Settings":
    #     settings_page()
    elif selected_page == "About Us":
        about_page()
    elif selected_page == "Help and Support":
        help_page()

# Run the app
if __name__ == "__main__":
    main()
