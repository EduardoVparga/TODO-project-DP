import streamlit as st
from app.components.card import card

# Función para mostrar las tarjetas en filas de tres
def show_cards_in_rows(data, modals, n_rows):
    for i in range(0, len(data), n_rows):
        cols = st.columns(n_rows)
        for j, col in enumerate(cols):
            if i + j < len(data):
                item = data[i + j]
                pos = i + j
                card(item, col, pos, modals[pos])