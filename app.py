import streamlit as st
import math

# Function to calculate centripetal force
def calculate_centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

# Function to calculate centripetal acceleration
def calculate_centripetal_acceleration(velocity, radius):
    return velocity**2 / radius

# Function to calculate normal force for a banked curve
def calculate_normal_force(mass, angle_deg, gravitational_acceleration=10):
    angle_rad = math.radians(angle_deg)
    return mass * gravitational_acceleration / math.cos(angle_rad)

# Function to calculate gravitational force
def calculate_gravitational_force(mass, gravitational_acceleration=10):
    return mass * gravitational_acceleration

# Streamlit UI
st.title("Car on a Curve Problem Solver with LaTeX Equations")
st.sidebar.header("Input Values")

# Dropdown to select the case
case_option = st.sidebar.selectbox(
    "Choose a scenario:",
    ["Banked without Friction (μ = 0, θ ≠ 0)", "Banked with Friction (μ ≠ 0, θ ≠ 0)", "Unbanked with Friction (μ ≠ 0, θ = 0)"]
)

# Common inputs for all cases
mass = st.sidebar.number_input("Mass of the car (kg)", min_value=0.1, value=1000.0)
radius = st.sidebar.number_input("Radius of the curve (m)", min_value=1.0, value=50.0)
velocity = st.sidebar.number_input("Velocity of the car (m/s)", min_value=1.0, value=30.0)

# Inputs based on selected case
if case_option == "Banked without Friction (μ = 0, θ ≠ 0)":
    angle = st.sidebar.number_input("Angle of the banked curve (degrees)", min_value=0.0, max_value=90.0, value=30.0)

elif case_option == "Banked with Friction (μ ≠ 0, θ ≠ 0)":
    angle = st.sidebar.number_input("Angle of the banked curve (degrees)", min_value=0.0, max_value=90.0, value=30.0)
    coefficient_of_friction = st.sidebar.number_input("Coefficient of Static Friction (μ_s)", min_value=0.0, value=0.5)

elif case_option == "Unbanked with Friction (μ ≠ 0, θ = 0)":
    coefficient_of_friction = st.sidebar.number_input("Coefficient of Static Friction (μ_s)", min_value=0.0, value=0.5)

# Dropdown to select what to calculate
calculation_option = st.sidebar.selectbox(
    "Select What to Calculate:",
    ["Centripetal Force", "Centripetal Acceleration", "Gravitational Force", "Normal Force"]
)

# Display results with LaTeX equations and answers
st.subheader(f"Results for: {case_option} - {calculation_option}")

if calculation_option == "Centripetal Force":
    st.latex(r"F_c = \frac{m v^2}{r}")
    centripetal_force = calculate_centripetal_force(mass, velocity, radius)
    st.write(f"Centripetal Force: **{centripetal_force:.2f} N**")

elif calculation_option == "Centripetal Acceleration":
    st.latex(r"a_c = \frac{v^2}{r}")
    centripetal_acceleration = calculate_centripetal_acceleration(velocity, radius)
    st.write(f"Centripetal Acceleration: **{centripetal_acceleration:.2f} m/s²**")

elif calculation_option == "Gravitational Force":
    st.latex(r"F_g = m \cdot g")
    gravitational_force = calculate_gravitational_force(mass)
    st.write(f"Gravitational Force: **{gravitational_force:.2f} N**")

elif calculation_option == "Normal Force":
    if "Banked" in case_option:
        st.latex(r"F_N = \frac{m \cdot g}{\cos(\theta)}")
        normal_force = calculate_normal_force(mass, angle)
    else:
        st.latex(r"F_N = m \cdot g")
        normal_force = calculate_gravitational_force(mass)  # Normal force equals weight for unbanked
    st.write(f"Normal Force: **{normal_force:.2f} N**")

# Additional explanation for each case
if case_option == "Banked without Friction (μ = 0, θ ≠ 0)":
    st.write("**Note:** No friction is considered in this case. Calculations are based only on centripetal and normal forces.")

elif case_option == "Banked with Friction (μ ≠ 0, θ ≠ 0)":
    st.write("**Note:** Friction is included in calculations to check for slipping conditions.")

elif case_option == "Unbanked with Friction (μ ≠ 0, θ = 0)":
    st.write("**Note:** This is a flat curve where friction provides the centripetal force.")
