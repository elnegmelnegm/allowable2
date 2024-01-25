import streamlit as st

def calculate_allowed_change(original_value, relative_limit, absolute_limit):
    # Apply the relative limit below 10 if it is smaller than the absolute limit
    relative_limit = max(relative_limit, 10.0)
    
    # Calculate the allowable adjustment
    relative_adjustment = original_value * relative_limit / 100.0
    allowed_change = min(relative_adjustment, absolute_limit)
    return allowed_change

def main():
    st.title("Allowable Adjustments for Chromatography Parameters")

    #st.sidebar.header("Input Parameters")

    # pH Adjustment
    st.sidebar.subheader("Mobile Phase pH")
    original_ph = st.sidebar.number_input("Original pH", min_value=0.0, max_value=14.0, step=0.1, value=7.6)
    ph_relative_limit = original_ph+0.2
    ph_absolute_limit = 1.0

    # Concentration of Salts
    st.sidebar.subheader("Concentration of Salts in Buffer")
    original_concentration = st.sidebar.number_input("Original Concentration (mM)", min_value=0.0, max_value=100.0, step=1.0, value=20.0)
    concentration_relative_limit = 10.0
    concentration_absolute_limit = 2.0

    # Particle Size
    st.sidebar.subheader("Particle Size")
    original_particle_size = st.sidebar.number_input("Original Particle Size (µm)", min_value=0.0, max_value=100.0, step=1.0, value=10.0)
    particle_size_reduction_limit = 50.0

    # Column Length
    st.sidebar.subheader("Column Length")
    original_column_length = st.sidebar.number_input("Original Column Length (mm)", min_value=0.0, max_value=1000.0, step=1.0, value=150.0)
    column_length_relative_limit = 70.0

    # Column Inner Diameter
    st.sidebar.subheader("Column Inner Diameter")
    original_inner_diameter = st.sidebar.number_input("Original Column Inner Diameter (mm)", min_value=0.0, max_value=10.0, step=0.01, value=4.6)
    inner_diameter_relative_limit = 25.0

    # Column Temperature
    st.sidebar.subheader("Column Temperature")
    original_temperature = st.sidebar.number_input("Original Column Temperature (°C)", min_value=-100.0, max_value=100.0, step=0.1, value=25.0)
    temperature_absolute_limit = 10.0

    # Flow Rate
    st.sidebar.subheader("Flow Rate")
    original_flow_rate = st.sidebar.number_input("Original Flow Rate (mL/min)", min_value=0.0, max_value=100.0, step=0.1, value=1.0)
    flow_rate_relative_limit = 50.0

    # Calculate allowable adjustments
    allowed_ph_change = calculate_allowed_change(original_ph, ph_relative_limit, ph_absolute_limit)
    allowed_concentration_change = calculate_allowed_change(original_concentration, concentration_relative_limit, concentration_absolute_limit)
    allowed_particle_size_reduction = original_particle_size * particle_size_reduction_limit / 100.0
    allowed_column_length_change = original_column_length * column_length_relative_limit / 100.0
    allowed_inner_diameter_change = original_inner_diameter * inner_diameter_relative_limit / 100.0
    allowed_temperature_change = temperature_absolute_limit
    allowed_flow_rate_change = original_flow_rate * flow_rate_relative_limit / 100.0

    # Display results
    st.subheader("Results")

    st.write(f"1. Mobile Phase pH: Original pH: {original_ph}, Allowed Change: From {original_ph-0.2:.2f} to {original_ph+0.2:.2f}")
    st.write(f"2. Concentration of Salts in Buffer: Original Concentration: {original_concentration}mM, Allowed Change: From {original_concentration - allowed_concentration_change:.2f} to {original_concentration + allowed_concentration_change:.2f} mM")
    st.write(f"3. Particle Size: Original Particle Size: {original_particle_size}µm, Allowed Reduction: Up to {allowed_particle_size_reduction:.2f}µm")
    st.write(f"4. Column Length: Original Length: {original_column_length}mm, Allowed Change: From {original_column_length - allowed_column_length_change:.0f} to {original_column_length + allowed_column_length_change:.0f} mm")
    st.write(f"5. Column Inner Diameter: Original Diameter: {original_inner_diameter}mm, Allowed Change: From {original_inner_diameter - allowed_inner_diameter_change:.2f} to {original_inner_diameter + allowed_inner_diameter_change:.2f}")
    st.write(f"6. Column Temperature: Original Temperature: {original_temperature}°C, Allowed Change: From {original_temperature - allowed_temperature_change:.0f} to {original_temperature + allowed_temperature_change:.0f} °C")
    st.write(f"7. Flow Rate: Original Flow Rate: {original_flow_rate}mL/min, Allowed Change: From {original_flow_rate - allowed_flow_rate_change:.1f} to {original_flow_rate + allowed_flow_rate_change:.1f} mL/min")

if __name__ == "__main__":
    main()
