import streamlit as st
import pandas as pd
import math
import matplotlib.pyplot as plt
from collections import namedtuple
import time

# Load data
df = pd.read_csv("dataFIX.csv")

# Define store data
Store = namedtuple('Store', ['name', 'type', 'floor', 'rating', 'x', 'y'])
stores = [
    Store(row['Store Names'], row['Store Type'], row['Location'], row['Rating'], row['Coordinate X'], row['Coordinate Y'])
    for _, row in df.iterrows()
]

# Define Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

# Greedy traversal
def greedy_traversal(stores, start):
    visited = [start]
    visited_types = {start.type}
    current = start

    while len(visited_types) < len(set(store.type for store in stores)):
        candidates = [s for s in stores if s.type not in visited_types and s != current]
        if not candidates:
            break
        next_store = min(candidates, key=lambda s: (euclidean_distance(current, s), -s.rating))
        visited.append(next_store)
        visited_types.add(next_store.type)
        current = next_store
    return visited

# Total cost
def total_cost(path):
    return sum(euclidean_distance(path[i], path[i + 1]) for i in range(len(path) - 1))

st.set_page_config(page_title="Mall Greedy Path Finder", page_icon="🛍️", layout="wide")
st.markdown(
    """
    <style>
    .stApp { background-color: #f4f6fb; }
    .stButton>button {
        background-color: #6c63ff;
        color: white !important;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #48409a;
        color: #fff !important;
    }
    /* Optional: Only sidebar button */
    /* div[data-testid="stSidebar"] .stButton>button { color: white !important; } */
    </style>
    """, unsafe_allow_html=True
)

st.title("🛍️ Mall Greedy Path Finder")
st.markdown("Find the optimal path to visit different store categories in the mall, minimizing your walking distance!")

with st.sidebar:
    st.header("Settings")
    selected_type = st.selectbox("Choose a Store Type to Start From", store_types)
    matching_stores = [s for s in stores if s.type == selected_type]
    store_names = [f"{i}: {s.name} (Floor {s.floor})" for i, s in enumerate(matching_stores)]
    selected_store = st.selectbox("Choose a Starting Store", store_names)
    run = st.button("🚀 Find Optimal Path")

if 'run' not in locals():
    run = False

if run:
    index = int(selected_store.split(":")[0])
    start_store = matching_stores[index]

    start_time = time.time()
    visited = greedy_traversal(stores, start_store)
    end_time = time.time()

    cost = total_cost(visited)

    st.success("✅ Path calculated!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Distance", f"{cost:.2f}")

        max_cost = 100 
        percent = min(int((cost / max_cost) * 100), 100)

        st.markdown(
            f"""
            <style>
            .progress {{
                background: #e0e0e0;
                border-radius: 8px;
                height: 22px;
                width: 100%;
                margin-top: 8px;
                margin-bottom: 12px;
                box-shadow: 0 2px 8px 0 rgba(44, 62, 80, 0.10);
            }}
            .progress-bar {{
                height: 100%;
                border-radius: 8px;
                background: linear-gradient(90deg, #6c63ff 0%, #ff4b4b 100%);
                width: {percent}%;
                color: white;
                text-align: center;
                font-weight: bold;
                line-height: 22px;
                transition: width 0.5s;
            }}
            </style>
            <div class="progress">
                <div class="progress-bar" role="progressbar" style="width: {percent}%;"
                     aria-valuenow="{percent}" aria-valuemin="0" aria-valuemax="100">{percent}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    col2.metric("Stores Visited", len(visited))
    col3.metric("Execution Time (s)", f"{end_time - start_time:.4f}")

    st.markdown("### 🗺️ Path Table")
    path_table = {
        "Store": [s.name for s in visited],
        "Floor": [s.floor for s in visited],
        "Category": [s.type for s in visited]
    }
    st.dataframe(pd.DataFrame(path_table), use_container_width=True)

    st.markdown("---")

    st.markdown("### 📍 Path Visualization")
    fig, ax = plt.subplots(figsize=(10, 4))
    x = [s.x for s in visited]
    y = [s.y for s in visited]
    names = [s.name for s in visited]
    ax.plot(x, y, marker='o', color='#ff4b4b', linewidth=2)
    for i, name in enumerate(names):
        ax.text(x[i], y[i], name, fontsize=9, ha='right', color='#333333')
    ax.set_title("Greedy Store Path", fontsize=14)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig)
