
priority_colors = {"High": "red", "Medium": "yellow", "Low": "blue"}

def card(item, col, pos, modal):
    color = priority_colors[item["Priority"]]
    with col:
        col.markdown(
            f"""
            <div style='background-color: #2E2E2E; padding: 20px; border-radius: 10px; margin-bottom: 20px; position: relative;'>
                <div style='width: 20px; height: 20px; background-color: {color}; border-radius: 50%; position: absolute; top: 10px; right: 10px;'></div>
                <h3>{item["Title"]}</h3>
                <p>{item["Message"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if col.button(f"See more details", key=f"btn_{pos}"):
            modal.open()
