import streamlit as st

# Define a function to determine skin type and solutions based on input
def determine_skin_type(experience, allergies, duration):
    # Simple logic for skin type determination
    if "dry" in experience:
        skin_type = "Dry Skin"
    elif "oily" in experience:
        skin_type = "Oily Skin"
    elif "sensitive" in experience:
        skin_type = "Sensitive Skin"
    else:
        skin_type = "Normal Skin"
    
    # Simple logic for determining number of solutions
    solutions = {
        "Dry Skin": ["Use a rich moisturizer", "Avoid hot water", "Use a gentle cleanser"],
        "Oily Skin": ["Use a matte moisturizer", "Use a salicylic acid cleanser", "Avoid heavy makeup"],
        "Sensitive Skin": ["Use fragrance-free products", "Avoid harsh exfoliants", "Use a soothing moisturizer"],
        "Normal Skin": ["Maintain a balanced skincare routine", "Use sunscreen", "Stay hydrated"]
    }
    
    return skin_type, solutions.get(skin_type, [])

# Streamlit app layout
st.title("Skin Type and Solution Finder")

# Collect user input
experience = st.text_input("What do you experience with your skin? (e.g., dry, oily, sensitive)")
allergies = st.text_input("Do you have any known allergies? (e.g., fragrance, certain ingredients)")
duration = st.text_input("How long have you been experiencing these issues? (e.g., weeks, months)")

# Determine skin type and provide solutions when the button is clicked
if st.button("Determine Skin Type and Solutions"):
    if not experience:
        st.error("Please provide your skin experience.")
    else:
        skin_type, solutions = determine_skin_type(experience.lower(), allergies.lower(), duration.lower())
        
        # Display the results
        st.write(f"**Your skin type is:** {skin_type}")
        st.write(f"**Number of solutions available:** {len(solutions)}")
        
        st.write("**Recommended Solutions:**")
        for solution in solutions:
            st.write(f"- {solution}")
