import streamlit as st
import math

# Function to calculate the centripetal force given mass, radius, and velocity
def calculate_centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

# Function to calculate the normal force
def calculate_normal_force(mass, angle_deg, gravitational_acceleration=10):
    """
    Calculate the normal force on a frictionless banked curve.

    Parameters:
    mass (float): Mass of the car (kg)
    angle_deg (float): Banking angle of the curve (degrees)
    gravitational_acceleration (float): Gravitational acceleration (default is 10 m/s^2)

    Returns:
    float: Normal force (N)
    """
    angle_rad = math.radians(angle_deg)
    normal_force = mass * gravitational_acceleration / math.cos(angle_rad)
    return normal_force

# Function to calculate the velocity given the centripetal force
def calculate_velocity(centripetal_force, mass, radius):
    return math.sqrt(centripetal_force * radius / mass)

# Function to calculate the angle for the car's motion on the banked curve
def calculate_angle(centripetal_force, mass, radius):
    g = 10  # Acceleration due to gravity
    angle = math.atan(centripetal_force / (mass * g))
    return angle

# Function to calculate the frictional force and check if slipping occurs
def calculate_friction(μ_s, normal_force, centripetal_force_required):
    friction_max = μ_s * normal_force
    if friction_max >= centripetal_force_required:
        slipping = False
        friction = centripetal_force_required  # Friction needed to provide centripetal force
    else:
        slipping = True
        friction = friction_max  # Maximum friction available
    return friction, slipping

# Streamlit UI
st.title("Car on Banked Curve Problem Solver with Friction")

st.sidebar.header("Input Values")

mass = st.sidebar.number_input("Mass of the car (kg)", min_value=0.1, value=1000.0)
radius = st.sidebar.number_input("Radius of the curve (m)", min_value=1.0, value=50.0)
velocity = st.sidebar.number_input("Velocity of the car (m/s)", min_value=1.0, value=30.0)
centripetal_force = st.sidebar.number_input("Centripetal Force (N)", min_value=1.0, value=5000.0)
angle = st.sidebar.number_input("Angle of the banked curve (degrees)", min_value=0.0, max_value=90.0, value=30.0)
coefficient_of_friction = st.sidebar.number_input("Coefficient of Static Friction (μ_s)", min_value=0.0, value=0.5)

# Checkbox to toggle friction input
use_friction = st.sidebar.checkbox("Include Friction in Calculations", value=False)

# Convert angle from degrees to radians for calculation
angle_rad = math.radians(angle)

st.sidebar.header("Select What to Calculate:")
calculation_option = st.sidebar.selectbox(
    "What would you like to calculate?", ["Centripetal Force", "Normal Force", "Velocity", "Angle", "Friction"]
)

if calculation_option == "Centripetal Force":
    if st.button("Calculate Centripetal Force"):
        result = calculate_centripetal_force(mass, velocity, radius)
        st.write(f"The centripetal force is: {result:.2f} N")

elif calculation_option == "Normal Force":
    if st.button("Calculate Normal Force"):
        gravitational_force = mass * 10  # Assume g = 10 m/s^2
        result = calculate_normal_force(mass, angle, gravitational_acceleration=10)
        st.write(f"The normal force is: {result:.2f} N")

elif calculation_option == "Velocity":
    if st.button("Calculate Velocity"):
        result = calculate_velocity(centripetal_force, mass, radius)
        st.write(f"The velocity of the car is: {result:.2f} m/s")

elif calculation_option == "Angle":
    if st.button("Calculate Angle"):
        result = calculate_angle(centripetal_force, mass, radius)
        st.write(f"The angle of the banked curve is: {math.degrees(result):.2f} degrees")

elif calculation_option == "Friction":
    if use_friction:
        if st.button("Calculate Friction and Check for Slipping"):
            normal_force = calculate_normal_force(mass, angle_rad, mass * 10, centripetal_force)
            centripetal_force_required = calculate_centripetal_force(mass, velocity, radius)
            friction, slipping = calculate_friction(coefficient_of_friction, normal_force, centripetal_force_required)
            
            st.write(f"Frictional Force: {friction:.2f} N")
            if slipping:
                st.write("The car is slipping! The frictional force is not enough to provide the required centripetal force.")
            else:
                st.write("No slipping. The frictional force is enough to provide the required centripetal force.")
    else:
        st.write("Friction is not included in the calculations.")

# Display diagram when friction is not included
if not use_friction:
    st.subheader("Banked Curve with No Friction")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwr--617E15yi1wU_dCDJuvw-JrEnbg2GFmA&s", caption="Banked Curve Diagram", width=400)

# Display different diagram when friction is included
if use_friction:
    st.subheader("Banked Curve with Friction")
    st.image("https://i.ytimg.com/vi/35KcguGfIEY/maxresdefault.jpg", caption="Banked Curve with Friction", width=400)
