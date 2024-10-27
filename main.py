import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Sample database of supermarket items and their aisles
# In a real app, this would come from a proper database
supermarket_items = {
    "milk": {"aisle": 2, "section": "Dairy"},
    "bread": {"aisle": 3, "section": "Bakery"},
    "apples": {"aisle": 1, "section": "Produce"},
    "pasta": {"aisle": 5, "section": "Dry Goods"},
    "chicken": {"aisle": 4, "section": "Meat"},
    # Add more items as needed
}

# Sample supermarket locations
# In a real app, this would come from a store locations API
supermarkets = {
    "SuperMart Downtown": {"lat": 40.7128, "lon": -74.0060},
    "SuperMart Uptown": {"lat": 40.7589, "lon": -73.9851},
}

st.title("🛒 Supermarket Item Finder")

# Get user's location
if st.button("📍 Use My Location"):
    # In a real app, you would use browser geolocation
    # For demo, we'll use a fixed location
    user_lat = 40.7128
    user_lon = -74.0060
    
    # Find nearest supermarket
    nearest_store = min(
        supermarkets.items(),
        key=lambda x: geodesic(
            (user_lat, user_lon),
            (x[1]["lat"], x[1]["lon"])
        ).miles
    )
    st.success(f"Nearest store: {nearest_store[0]}")

# Search for item
search_item = st.text_input("🔍 What are you looking for?").lower()

if search_item:
    if search_item in supermarket_items:
        item_info = supermarket_items[search_item]
        st.info(f"You can find {search_item} in:")
        st.write(f"🚶 Aisle: {item_info['aisle']}")
        st.write(f"📍 Section: {item_info['section']}")
    else:
        st.warning("Sorry, we couldn't find that item in our database.")

# Add some helpful information
st.sidebar.header("About")
st.sidebar.write("""
This app helps you locate items in the supermarket.
1. Allow location access to find your nearest store
2. Search for the item you're looking for
3. Get the exact aisle and section!
""")
