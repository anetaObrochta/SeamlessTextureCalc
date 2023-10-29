from flask import Flask, render_template, request, redirect, url_for, flash
import math

app = Flask(__name__)
app.secret_key = "secret_key"  # Required for flash messages


@app.route('/', methods=['GET', 'POST'])
def index():
    pattern_width = ""
    image_width = ""
    final_width = ""
    if request.method == 'POST':
        pattern_width = request.form['pattern_width']
        image_width = request.form['image_width']
        try:
            pattern_width = float(request.form.get('pattern_width'))
            image_width = float(request.form.get('image_width'))
            rounding_method = request.form.get('rounding_method')

            if pattern_width <= 0 or image_width <= 0 or image_width > pattern_width:
                flash("Invalid input. Please check the values and try again.")
                return redirect(url_for('index'))

            result = pattern_width / image_width

            if rounding_method == "up":
                rounded_result = math.ceil(result)
            elif rounding_method == "down":
                rounded_result = math.floor(result)
            else:
                flash("Invalid choice for rounding. Please choose 'up' or 'down'.")
                return redirect(url_for('index'))

            final_width = float(format(pattern_width / rounded_result, ".6f"))

        except ValueError:
            flash("Invalid input. Please check the values and try again.")
            return redirect(url_for('index'))

    return render_template('index.html',
                           pattern_width=pattern_width, image_width=image_width, final_width=final_width)


if __name__ == '__main__':
    app.run(debug=True)
