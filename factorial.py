from flask import Flask

app = Flask(__name__)

class calculate:
    def __init__(self, numbr):
        self.numbr=numbr

    def factorial(self):
        # Initialize the factorial variable to 1
        result = 1

        # Calculate the factorial using a for loop
        for i in range(1, self.numbr + 1):
            result *= i
        #return factorial
        return f"factorial de {self.numbr} es {result}"

@app.route('/<int:numbr>')
def pay(numbr):
    factorial = calculate(numbr)
    return factorial.factorial()

if __name__ == "__main__":
    app.run(debug=True)