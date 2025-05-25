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

# Streamlit UI
st.title("Mall Greedy Path Finder 🛍️")

store_types = sorted(set(store.type for store in stores))
selected_type = st.selectbox("Choose a Store Type to Start From", store_types)

matching_stores = [s for s in stores if s.type == selected_type]
store_names = [f"{i}: {s.name} (Floor {s.floor})" for i, s in enumerate(matching_stores)]
selected_store = st.selectbox("Choose a Starting Store", store_names)

if st.button("Find Optimal Path"):
    index = int(selected_store.split(":")[0])
    start_store = matching_stores[index]

    start_time = time.time()
    visited = greedy_traversal(stores, start_store)
    end_time = time.time()

    cost = total_cost(visited)

    # Show summary
    st.success("Path calculated!")
    # st.write(f"**Total Cost:** {cost:.2f}")
    # st.write(f"**Execution Time:** {end_time - start_time:.4f} seconds")

    # Build and display table
    path_table = {
        "Store": [s.name for s in visited],
        "Floor": [s.floor for s in visited],
        "Category": [s.type for s in visited]
    }
    st.table(pd.DataFrame(path_table))

    # Optional: Plot the path
    fig, ax = plt.subplots()
    x = [s.x for s in visited]
    y = [s.y for s in visited]
    names = [s.name for s in visited]
