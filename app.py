import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate centripetal force
def calculate_centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

# Function to calculate the normal force
def calculate_normal_force(mass, angle_deg, gravitational_acceleration=10):
    angle_rad = math.radians(angle_deg)
    normal_force = mass * gravitational_acceleration / math.cos(angle_rad)
    return normal_force

# Function to calculate velocity given the centripetal force
def calculate_velocity(centripetal_force, mass, radius):
    return math.sqrt(centripetal_force * radius / mass)

# Function to calculate the angle for the car's motion on the banked curve
def calculate_angle(centripetal_force, mass, radius):
    g = 10  # Acceleration due to gravity
    angle = math.atan(centripetal_force / (mass * g))
    return angle

# Streamlit UI
st.title("Car on a Banked Curve Problem Solver with Graphs and Equations")

st.sidebar.header("Input Values")
mass = st.sidebar.number_input("Mass of the car (kg)", min_value=0.1, value=1000.0)
radius = st.sidebar.number_input("Radius of the curve (m)", min_value=1.0, value=50.0)
velocity = st.sidebar.number_input("Velocity of the car (m/s)", min_value=1.0, value=30.0)
angle = st.sidebar.number_input("Angle of the banked curve (degrees)", min_value=0.0, max_value=90.0, value=30.0)
coefficient_of_friction = st.sidebar.number_input("Coefficient of Static Friction (μ_s)", min_value=0.0, value=0.5)

# Convert angle from degrees to radians
angle_rad = math.radians(angle)

st.sidebar.header("Select What to Calculate:")
calculation_option = st.sidebar.selectbox(
    "What would you like to calculate?",
    ["Centripetal Force", "Normal Force", "Velocity", "Angle"]
)

# Display selected equation in LaTeX
if calculation_option == "Centripetal Force":
    st.latex(r"F_c = \frac{m v^2}{r}")
    result = calculate_centripetal_force(mass, velocity, radius)
    st.write(f"The centripetal force is: **{result:.2f} N**")

elif calculation_option == "Normal Force":
    st.latex(r"F_N = \frac{m g}{\cos(\theta)}")
    result = calculate_normal_force(mass, angle)
    st.write(f"The normal force is: **{result:.2f} N**")

elif calculation_option == "Velocity":
    st.latex(r"v = \sqrt{\frac{F_c \cdot r}{m}}")
    centripetal_force = calculate_centripetal_force(mass, velocity, radius)
    result = calculate_velocity(centripetal_force, mass, radius)
    st.write(f"The velocity of the car is: **{result:.2f} m/s**")

elif calculation_option == "Angle":
    st.latex(r"\theta = \tan^{-1}\left(\frac{F_c}{m g}\right)")
    centripetal_force = calculate_centripetal_force(mass, velocity, radius)
    result = math.degrees(calculate_angle(centripetal_force, mass, radius))
    st.write(f"The angle of the banked curve is: **{result:.2f} degrees**")

# Dynamic Graphs
st.subheader("Graph: How the Selected Quantity Changes with Velocity")
velocities = np.linspace(1, 100, 100)

if calculation_option == "Centripetal Force":
    forces = [calculate_centripetal_force(mass, v, radius) for v in velocities]
    plt.plot(velocities, forces, label="Centripetal Force (N)")
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Centripetal Force (N)")
    plt.title("Centripetal Force vs Velocity")

elif calculation_option == "Normal Force":
    normal_forces = [calculate_normal_force(mass, angle) for v in velocities]
    plt.plot(velocities, normal_forces, label="Normal Force (N)")
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Normal Force (N)")
    plt.title("Normal Force vs Velocity")

elif calculation_option == "Velocity":
    calculated_velocities = [calculate_velocity(calculate_centripetal_force(mass, v, radius), mass, radius) for v in velocities]
    plt.plot(velocities, calculated_velocities, label="Calculated Velocity (m/s)")
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Calculated Velocity (m/s)")
    plt.title("Calculated Velocity vs Velocity Input")

elif calculation_option == "Angle":
    angles = [math.degrees(calculate_angle(calculate_centripetal_force(mass, v, radius), mass, radius)) for v in velocities]
    plt.plot(velocities, angles, label="Angle (degrees)")
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Angle (degrees)")
    plt.title("Angle vs Velocity")

plt.legend()
st.pyplot(plt)
