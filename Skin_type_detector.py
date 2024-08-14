import streamlit as st

# Define skin types and corresponding solutions
skin_types = {
    'Normal': 'Your skin is well-balanced. Use a gentle cleanser and a lightweight moisturizer.',
    'Oily': 'Your skin produces excess oil. Use a foaming cleanser and an oil-free moisturizer.',
    'Dry': 'Your skin lacks moisture. Use a hydrating cleanser and a rich moisturizer.',
    'Combination': 'Your skin has both oily and dry areas. Use a balanced cleanser and a combination moisturizer.',
    'Sensitive': 'Your skin is prone to irritation. Use a hypoallergenic cleanser and a soothing moisturizer.'
}

def detect_skin_type(dryness, oiliness, sensitivity):
    if dryness and oiliness:
        return 'Combination'
    elif oiliness:
        return 'Oily'
    elif dryness:
        return 'Dry'
    elif sensitivity:
        return 'Sensitive'
    else:
        return 'Normal'

def main():
    st.title("Skin Type Detector")

    st.header("Step 1: Assess Your Skin")

    # Collect user input
    dryness = st.checkbox('I have dry skin')
    oiliness = st.checkbox('I have oily skin')
    sensitivity = st.checkbox('I have sensitive skin')

    if st.button('Detect Skin Type'):
        skin_type = detect_skin_type(dryness, oiliness, sensitivity)
        st.write(f"Your skin type is: **{skin_type}**")
        st.write(skin_types[skin_type])
    else:
        st.write("Select your skin characteristics and press 'Detect Skin Type'")

if __name__ == "__main__":
    main()
