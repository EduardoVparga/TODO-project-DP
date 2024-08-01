import streamlit as st
def modal(idx, item, image, modal):
    if modal.is_open():
        with modal.container():
            st.write(f"### Some details:")
            st.write(f'**When:** {item["Datetime"]}')
            st.write(f'**Where:** {item["Location"]}')
            st.write(f'**Have guests:** {item["Guess"]}')
            if item["Alarm"] != 'None':
                st.write(f'**Alarm:** {item["Alarm"]}')
        
            st.image(image.show_animal_image())
            