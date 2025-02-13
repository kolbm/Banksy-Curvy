import streamlit as st
import math

# Function to calculate centripetal force
def calculate_centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

# Function to calculate normal force
def calculate_normal_force(mass, angle_deg, gravitational_acceleration=10):
    angle_rad = math.radians(angle_deg)
    return mass * gravitational_acceleration / math.cos(angle_rad)

# Function to calculate velocity
def calculate_velocity(centripetal_force, mass, radius):
    return math.sqrt(centripetal_force * radius / mass)

# Function to calculate angle
def calculate_angle(centripetal_force, mass, radius):
    g = 10  # Gravitational acceleration
    return math.atan(centripetal_force / (mass * g))

# Function to calculate friction and check for slipping
def calculate_friction(μ_s, normal_force, centripetal_force_required):
    friction_max = μ_s * normal_force
    slipping = friction_max < centripetal_force_required
    friction = min(friction_max, centripetal_force_required)
    return friction, slipping

# Streamlit UI
st.title("Car on a Banked Curve Problem Solver with Friction Option")

st.sidebar.header("Input Values")
mass = st.sidebar.number_input("Mass of the car (kg)", min_value=0.1, value=1000.0)
radius = st.sidebar.number_input("Radius of the curve (m)", min_value=1.0, value=50.0)
velocity = st.sidebar.number_input("Velocity of the car (m/s)", min_value=1.0, value=30.0)
angle = st.sidebar.number_input("Angle of the banked curve (degrees)", min_value=0.0, max_value=90.0, value=30.0)
coefficient_of_friction = st.sidebar.number_input("Coefficient of Static Friction (μ_s)", min_value=0.0, value=0.5)

# Dropdown to include or exclude friction
friction_option = st.sidebar.selectbox("Include Friction in Calculations?", ["No", "Yes"])

# Select calculation
st.sidebar.header("Select What to Calculate:")
calculation_option = st.sidebar.selectbox(
    "What would you like to calculate?",
    ["Centripetal Force", "Normal Force", "Velocity", "Angle", "Friction"]
)

# Display calculation and result
if calculation_option == "Centripetal Force":
    st.subheader("Centripetal Force Calculation")
    st.latex(r"F_c = \frac{m v^2}{r}")
    result = calculate_centripetal_force(mass, velocity, radius)
    st.write(f"The centripetal force is: **{result:.2f} N**")

elif calculation_option == "Normal Force":
    st.subheader("Normal Force Calculation")
    st.latex(r"F_N = \frac{m g}{\cos(\theta)}")
    result = calculate_normal_force(mass, angle)
    st.write(f"The normal force is: **{result:.2f} N**")

elif calculation_option == "Velocity":
    st.subheader("Velocity Calculation")
    st.latex(r"v = \sqrt{\frac{F_c \cdot r}{m}}")
    result = calculate_velocity(calculate_centripetal_force(mass, velocity, radius), mass, radius)
    st.write(f"The velocity of the car is: **{result:.2f} m/s**")

elif calculation_option == "Angle":
    st.subheader("Angle Calculation")
    st.latex(r"\theta = \tan^{-1}\left(\frac{F_c}{m g}\right)")
    result = math.degrees(calculate_angle(calculate_centripetal_force(mass, velocity, radius), mass, radius))
    st.write(f"The angle of the banked curve is: **{result:.2f} degrees**")

elif calculation_option == "Friction":
    st.subheader("Friction Calculation")
    if friction_option == "Yes":
        st.latex(r"F_f = \mu_s \cdot F_N")
        st.latex(r"F_f \geq F_c \quad (\text{No Slipping Condition})")
        normal_force = calculate_normal_force(mass, angle)
        centripetal_force_required = calculate_centripetal_force(mass, velocity, radius)
        friction, slipping = calculate_friction(coefficient_of_friction, normal_force, centripetal_force_required)
        
        st.write(f"Frictional Force: **{friction:.2f} N**")
        if slipping:
            st.write("**The car is slipping!** The frictional force is not enough to provide the required centripetal force.")
        else:
            st.write("**No slipping.** The frictional force is sufficient to provide the required centripetal force.")
    else:
        st.latex(r"\text{No friction included in calculations.}")
        st.write("This is a frictionless scenario. Calculations assume no frictional forces acting on the car.")

