import streamlit as st
import math

# Function to calculate the centripetal force given mass, radius, and velocity
def calculate_centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

# Function to calculate the normal force
def calculate_normal_force(mass, angle, gravitational_force, centripetal_force):
    normal_force = mass * 10 * math.cos(angle) + centripetal_force
    return normal_force

# Function to calculate the velocity given the centripetal force
def calculate_velocity(centripetal_force, mass, radius):
    return math.sqrt(centripetal_force * radius / mass)

# Function to calculate the angle for the car's motion on the banked curve
def calculate_angle(centripetal_force, mass, radius):
    g = 10  # Acceleration due to gravity
    angle = math.atan(centripetal_force / (mass * g))
    return angle

# Streamlit UI
st.title("Car on Banked Curve Problem Solver")

st.sidebar.header("Input Values")

mass = st.sidebar.number_input("Mass of the car (kg)", min_value=0.1, value=1000.0)
radius = st.sidebar.number_input("Radius of the curve (m)", min_value=1.0, value=50.0)
velocity = st.sidebar.number_input("Velocity of the car (m/s)", min_value=1.0, value=30.0)
centripetal_force = st.sidebar.number_input("Centripetal Force (N)", min_value=1.0, value=5000.0)
angle = st.sidebar.number_input("Angle of the banked curve (degrees)", min_value=0.0, max_value=90.0, value=30.0)

# Convert angle from degrees to radians for calculation
angle_rad = math.radians(angle)

st.sidebar.header("Select What to Calculate:")
calculation_option = st.sidebar.selectbox(
    "What would you like to calculate?", ["Centripetal Force", "Normal Force", "Velocity", "Angle"]
)

if calculation_option == "Centripetal Force":
    if st.button("Calculate Centripetal Force"):
        result = calculate_centripetal_force(mass, velocity, radius)
        st.write(f"The centripetal force is: {result:.2f} N")

elif calculation_option == "Normal Force":
    if st.button("Calculate Normal Force"):
        gravitational_force = mass * 10  # Assume g = 10 m/s^2
        result = calculate_normal_force(mass, angle_rad, gravitational_force, centripetal_force)
        st.write(f"The normal force is: {result:.2f} N")

elif calculation_option == "Velocity":
    if st.button("Calculate Velocity"):
        result = calculate_velocity(centripetal_force, mass, radius)
        st.write(f"The velocity of the car is: {result:.2f} m/s")

elif calculation_option == "Angle":
    if st.button("Calculate Angle"):
        result = calculate_angle(centripetal_force, mass, radius)
        st.write(f"The angle of the banked curve is: {math.degrees(result):.2f} degrees")

