import streamlit as st
import math

# Function to calculate centripetal force
def calculate_centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

# Function to calculate normal force for a banked curve
def calculate_normal_force(mass, angle_deg, gravitational_acceleration=10):
    angle_rad = math.radians(angle_deg)
    return mass * gravitational_acceleration / math.cos(angle_rad)

# Function to calculate required friction force
def calculate_friction(μ_s, normal_force, centripetal_force_required):
    friction_max = μ_s * normal_force
    slipping = friction_max < centripetal_force_required
    friction = min(friction_max, centripetal_force_required)
    return friction, slipping

# Streamlit UI
st.title("Car on a Curve Problem Solver")
st.sidebar.header("Input Values")

# Dropdown to select the case
case_option = st.sidebar.selectbox(
    "Choose a scenario:",
    ["Banked without Friction (μ = 0, θ ≠ 0)", "Banked with Friction (μ ≠ 0, θ ≠ 0)", "Unbanked with Friction (μ ≠ 0, θ = 0)"]
)

# Input fields common to all cases
mass = st.sidebar.number_input("Mass of the car (kg)", min_value=0.1, value=1000.0)
radius = st.sidebar.number_input("Radius of the curve (m)", min_value=1.0, value=50.0)
velocity = st.sidebar.number_input("Velocity of the car (m/s)", min_value=1.0, value=30.0)

if "Banked" in case_option:
    angle = st.sidebar.number_input("Angle of the banked curve (degrees)", min_value=0.0, max_value=90.0, value=30.0)
if "Friction" in case_option:
    coefficient_of_friction = st.sidebar.number_input("Coefficient of Static Friction (μ_s)", min_value=0.0, value=0.5)

# Display results based on selected case
st.subheader(f"Results for: {case_option}")

if case_option == "Banked without Friction (μ = 0, θ ≠ 0)":
    st.write("**No friction assumed. Calculations based on centripetal and normal forces only.**")
    normal_force = calculate_normal_force(mass, angle)
    centripetal_force = calculate_centripetal_force(mass, velocity, radius)
    st.write(f"Normal Force: **{normal_force:.2f} N**")
    st.write(f"Centripetal Force: **{centripetal_force:.2f} N**")

elif case_option == "Banked with Friction (μ ≠ 0, θ ≠ 0)":
    st.write("**Friction is included in the calculations.**")
    normal_force = calculate_normal_force(mass, angle)
    centripetal_force = calculate_centripetal_force(mass, velocity, radius)
    friction, slipping = calculate_friction(coefficient_of_friction, normal_force, centripetal_force)
    st.write(f"Normal Force: **{normal_force:.2f} N**")
    st.write(f"Centripetal Force: **{centripetal_force:.2f} N**")
    st.write(f"Frictional Force: **{friction:.2f} N**")
    if slipping:
        st.write("**The car is slipping! Friction is insufficient.**")
    else:
        st.write("**No slipping. Friction is sufficient.**")

elif case_option == "Unbanked with Friction (μ ≠ 0, θ = 0)":
    st.write("**Flat curve with friction providing centripetal force.**")
    normal_force = mass * 10  # Since θ = 0, normal force equals weight
    centripetal_force = calculate_centripetal_force(mass, velocity, radius)
    friction, slipping = calculate_friction(coefficient_of_friction, normal_force, centripetal_force)
    st.write(f"Normal Force: **{normal_force:.2f} N**")
    st.write(f"Centripetal Force: **{centripetal_force:.2f} N**")
    st.write(f"Frictional Force: **{friction:.2f} N**")
    if slipping:
        st.write("**The car is slipping! Friction is insufficient.**")
    else:
        st.write("**No slipping. Friction is sufficient.**")
