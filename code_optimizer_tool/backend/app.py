# Importing necessary libraries
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='D:\AI_Tool\code_optimizer_tool\frontend\template')  # Specify the path if needed

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
# Your existing route and app code...
# from flask import Flask, request, jsonify, render_template
# app = Flask(__name__)

# Sample function to simulate code analysis (replace with your actual analysis logic)
def analyze_code(code_snippet):
    # Here you can add your code analysis logic.
    # For now, we will just return a simple result.
    return f"Analyzed code: {code_snippet}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the code snippet from the form
        code_snippet = request.form['code_snippet']
        
        # Call the function to analyze the code
        result = analyze_code(code_snippet)
        
        # Render the result in a different template (or you can return the same page with the result)
        return render_template('result.html', result=result)
    
    # Default page when the user accesses the page via GET
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    

