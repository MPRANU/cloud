from flask import Flask

app = Flask(__name__)
@app.route("/")
class Employee:
    def __init__(self, name, productivity, teamwork, punctuality):
        self.name = name
        self.productivity = productivity
        self.teamwork = teamwork
        self.punctuality = punctuality

def evaluate_performance(employee):
    performance_score = 0

    # Evaluate productivity
    if employee.productivity >= 8:
        performance_score += 3
    elif employee.productivity >= 6:
        performance_score += 2
    elif employee.productivity >= 4:
        performance_score += 1

    # Evaluate teamwork
    if employee.teamwork >= 8:
        performance_score += 3
    elif employee.teamwork >= 6:
        performance_score += 2
    elif employee.teamwork >= 4:
        performance_score += 1

    # Evaluate punctuality
    if employee.punctuality >= 8:
        performance_score += 3
    elif employee.punctuality >= 6:
        performance_score += 2
    elif employee.punctuality >= 4:
        performance_score += 1

    # Assign performance rating based on the total score
    if performance_score >= 8:
        rating = "Outstanding"
    elif performance_score >= 6:
        rating = "Good"
    elif performance_score >= 4:
        rating = "Average"
    else:
        rating = "Below Average"

    return rating

# Take input from the user
name = input("Enter employee name: ")
productivity = int(input("Enter productivity score (1-10): "))
teamwork = int(input("Enter teamwork score (1-10): "))
punctuality = int(input("Enter punctuality score (1-10): "))

# Create an Employee object with user input
employee = Employee(name, productivity, teamwork, punctuality)

# Evaluate the performance
rating = evaluate_performance(employee)

# Print the result
print(f"{employee.name}: {rating}")

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
