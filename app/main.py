import streamlit as st
from streamlit_modal import Modal

from app.components.modal import modal
from app.utils import (
    show_cards_in_rows,
)
N_ROWS = 3

def app(db, data, image):
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    data.sort(key=lambda x: priority_order[x["Priority"]])

    # Create a modal for each card
    modals = [Modal(title= f"{card["Title"]}", key=f"modal_{card["Id"]}") for card in data]

    # Function to display the cards in rows of three
    show_cards_in_rows(data, modals, N_ROWS)

    # Display the details in the corresponding modal
    for idx, item in enumerate(data):
        modal(idx, item, image, modals[idx])


