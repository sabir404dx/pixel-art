import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Initialize 5x5 grid
if 'grid' not in st.session_state:
    st.session_state.grid = np.ones((5, 5, 3))

# Paint function
def paint(row_col, color):
    r, c = map(int, row_col.strip("()").split(","))
    st.session_state.grid[r, c] = plt.cm.colors.to_rgb(color)

# Basic UI
st.title("Pixel Art")
pixel = st.text_input("Pixel (e.g., (1,1))", "(1,1)")
color = st.text_input("Color (e.g., red)", "red")

# Buttons
col1, col2, col3 = st.columns(3)
if col1.button("Paint"):
    paint(pixel, color)
if col2.button("Fill"):
    st.session_state.grid[:] = plt.cm.colors.to_rgb(color)
if col3.button("Clear"):
    st.session_state.grid[:] = np.ones((5, 5, 3))

# Display grid
fig, ax = plt.subplots(figsize=(3, 3))
ax.imshow(st.session_state.grid)
ax.set_xticks(range(5))
ax.set_yticks(range(5))
ax.grid(color='grey', linestyle='-', linewidth=0.5)
st.pyplot(fig)
