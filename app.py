import streamlit as st
import matplotlib.pyplot as plt
import math
import numpy as np

# Function to calculate centripetal force
def calculate_centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

# Function to calculate the normal force
def calculate_normal_force(mass, angle_deg, gravitational_acceleration=10):
    angle_rad = math.radians(angle_deg)
    return mass * gravitational_acceleration / math.cos(angle_rad)

# Function to calculate velocity given the centripetal force
def calculate_velocity(centripetal_force, mass, radius):
    return math.sqrt(centripetal_force * radius / mass)

# Streamlit UI
st.title("Car on a Banked Curve Problem Solver with Dynamic Graphs")

st.sidebar.header("Input Values")
mass = st.sidebar.number_input("Mass of the car (kg)", min_value=0.1, value=1000.0)
radius = st.sidebar.number_input("Radius of the curve (m)", min_value=1.0, value=50.0)
velocity = st.sidebar.number_input("Velocity of the car (m/s)", min_value=1.0, value=30.0)
angle = st.sidebar.number_input("Angle of the banked curve (degrees)", min_value=0.0, max_value=90.0, value=30.0)

# Equation Display
st.subheader("Centripetal Force Equation")
st.latex(r"F_c = \frac{m v^2}{r}")

# Calculation and Result Display
centripetal_force = calculate_centripetal_force(mass, velocity, radius)
st.write(f"The calculated centripetal force is: **{centripetal_force:.2f} N**")

# Generate Dynamic Graph
st.subheader("Graph: Centripetal Force vs Velocity")

velocities = np.linspace(1, 100, 100)
forces = [calculate_centripetal_force(mass, v, radius) for v in velocities]

fig, ax = plt.subplots()
ax.plot(velocities, forces, label="Centripetal Force (N)", color="blue")
ax.set_xlabel("Velocity (m/s)")
ax.set_ylabel("Centripetal Force (N)")
ax.set_title("Centripetal Force vs Velocity")
ax.legend()
ax.grid(True)

# Display the plot using Streamlit's built-in function
st.pyplot(fig)
