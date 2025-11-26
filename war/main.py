import streamlit as st
from models import Athlete
from models.athlete import Athlete
from db.database import create_database, create_athlete_table, add_athlete, get_all_athletes
from PIL import Image
import io


create_database()
create_athlete_table()


id_number = st.number_input("Enter ID?")
profile = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])
name = st.text_input("Enter name")
martial_arts = st.multiselect("Martail arts", ["Judo", "Karate", "Jiu"])
current_weight = st.number_input("Current Weight in Kg", min_value=30.0, max_value=100.0)
category = st.selectbox("Competition weight category", ["Half LightwWight",
    "LightWeight",
    "Half MiddleWeight",
    "MiddleWeight",
    "Half HeavyWeight",
    "HeavyWeight"])
competition_per_month = st.slider("Number of Competitions this month", 0, 10)
private_coaching_hours = st.slider("Private Coaching Hours", 0, 5)

if st.button("Save & Computer"):
    profile_bytes = profile.read()
    athlete_record = Athlete(id_number, profile_bytes, name, martial_arts, current_weight, category, competition_per_month, private_coaching_hours)
    add_athlete(athlete_record)
    st.write("Total Fee charged:", athlete_record.total_fee())
    st.write("Coaching fee", athlete_record.coaching_fee())
    st.write("Weight Status", athlete_record.weight_status())
