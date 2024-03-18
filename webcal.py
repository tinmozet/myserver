
from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Calculator</title>
</head>
<body>
    <h1>Web Calculator</h1>
    <form method="post">
        <input type="text" name="expression" value="{{ expression }}" placeholder="Enter an expression">
        <button type="submit">Calculate</button>
    </form>
    <h2>Result: {{ result }}</h2>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    expression = ''
    result = ''

    if request.method == 'POST':
        try:
            expression = request.form['expression']
            result = str(eval(expression))
        except:
            result = 'Invalid expression'

    return render_template_string(html_template, expression=expression, result=result)

if __name__ == '__main__':
    app.run(debug=True)


