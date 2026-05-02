print("What do you want to calculate?")
print("1. Pressure (P = F/A)")
print("2. Density (ρ = m/V)")
print("3. Speed (v = d/t)")
print("4. Force (F = m*a)")
print("5. Kinetic Energy (KE = 0.5*m*v²)")

while True:
    cal = int(input("Enter your choice (1-5): "))
    if cal >= 1 and cal <= 5:
        break
    print("Invalid choice. Please choose 1-5.")

if cal == 1:
    f = float(input("Enter the force (N): "))
    a = float(input("Enter the area (m²): "))
    p = round(f / a, 3)
    print(f"The pressure is {p} Pa")

elif cal == 2:
    m = float(input("Enter the mass (kg): "))
    v = float(input("Enter the volume (m³): "))
    d = round(m / v, 3)
    print(f"The density is {d} kg/m³")

elif cal == 3:
    d = float(input("Enter the distance (m): "))
    t = float(input("Enter the time (s): "))
    s = round(d/t, 3)
    print(f"The speed is {s} m/s")

elif cal == 4:
    m = float(input("Enter the mass (kg): "))
    a = float(input("Enter the acceleration (m/s²): "))
    f = round(m * a, 3)
    print(f"The force is {f} N")

elif cal == 5:
    m = float(input("Enter the mass (kg): "))
    v = float(input("Enter the velocity (m/s): "))
    ke = round(0.5 * m * (v ** 2), 3)
    print(f"The kinetic energy is {ke} J")