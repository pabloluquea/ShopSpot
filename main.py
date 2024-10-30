import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import geocoder
from pprint import pprint  # Import the function, not the module

from data.stores import supermarkets
from data.inventory import supermarket_items


st.title("🛒 ShopSpot")

# Get user's location automatically on app load
try:
    g = geocoder.ip('me')
    if g.ok:
        user_lat = g.lat
        user_lon = g.lng
        st.write(f"📍 Your Location: {user_lat:.4f}, {user_lon:.4f}")
        
        # Calculate distances for all stores
        stores_with_distances = [
            (
                store_name,
                store_data,
                geodesic(
                    (user_lat, user_lon),
                    (store_data["lat"], store_data["lon"])
                ).miles
            )
            for store_name, store_data in supermarkets.items()
        ]
        print(f"Stores with distances: {stores_with_distances}")

        
        # Sort by distance and get top 5
        closest_stores = sorted(stores_with_distances, key=lambda x: x[2])[:5]
        
        # Create radio buttons for store selection
        store_options = {
            f"{store[0]} ({store[2]:.2f} miles away)": store[0] 
            for store in closest_stores
        }
        
        selected_store = st.radio(
            "📍 Select your store:",
            options=store_options.keys(),
            index=0  # Default to closest store
        )
        
        # Get the actual store name from the selection
        selected_store_name = store_options[selected_store]
        st.success(f"You selected: {selected_store_name}")
        
    else:
        raise Exception("Could not get location")
        
except Exception as e:
    st.error(f"Error getting location: {str(e)}")
    # Fallback to default NYC coordinates
    user_lat = 40.7128
    user_lon = -74.0060
    st.info("Using default location (New York City)")

# Search for item
search_item = st.text_input("🔍 What are you looking for?").lower()

if search_item:
    if selected_store_name in supermarket_items:
        store_inventory = supermarket_items[selected_store_name]
        if search_item in store_inventory:
            item_info = store_inventory[search_item]
            st.info(f"You can find {search_item} in {selected_store_name}:")
            st.write(f"🚶 Aisle: {item_info['aisle']}")
            st.write(f"📍 Section: {item_info['section']}")
        else:
            st.warning(f"Sorry, we couldn't find {search_item} in {selected_store_name}.")
    else:
        st.error("Please select a store first!")

# Add some helpful information
st.sidebar.header("About")
st.sidebar.write("""
This app helps you locate items in the supermarket.
1. Allow location access to find your nearest store
2. Search for the item you're looking for
3. Get the exact aisle and section!
""")

# Debug logs
print(f"Selected store: {selected_store_name}")
print("Available items in", selected_store_name)
pprint(supermarket_items.get(selected_store_name, {}))
