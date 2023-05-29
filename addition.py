from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def add():
    return "Welcome to the Addition API!"

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    if "numbers" in data:
        numbers = data["numbers"]
        if isinstance(numbers, list) and all(isinstance(num, (int, float)) for num in numbers):
            result = sum(numbers)
            return f"The result of the addition is: {result}"
    return "Invalid input. Please provide a list of numbers."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
