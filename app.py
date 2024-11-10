from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Function to calculate conical nanopore dimensions
def calculate_nanopore_dimensions(conductivity, conductance, tip_diameter, cone_angle):
    # Convert angle to radians for trigonometric functions
    angle_radians = math.radians(cone_angle)

    # Calculate length of the conical pore (L) using the cone angle and tip diameter
    length = tip_diameter / (2 * math.tan(angle_radians / 2))

    # Assuming conductance (G) = πσ/(4L) * (tip_diameter * base_diameter)
    base_diameter = (conductance * 4 * length / (math.pi * conductivity * tip_diameter)) ** 0.5

    return length, base_diameter

@app.route("/", methods=["GET", "POST"])
def nanopore_calculator():
    if request.method == "POST":
        # Retrieve form data
        conductivity = float(request.form["conductivity"])
        conductance = float(request.form["conductance"])
        tip_diameter = float(request.form["tip_diameter"])
        cone_angle = float(request.form["cone_angle"])

        # Perform calculation
        length, base_diameter = calculate_nanopore_dimensions(
            conductivity, conductance, tip_diameter, cone_angle
        )

        return render_template(
            "result.html", length=length, base_diameter=base_diameter
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
