from flask import Flask, render_template, request, flash
import joblib
import logging

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the customer segmentation model
model = joblib.load('model/customer_segmentation_model.pkl')

# Define labels for the customer segments
segment_labels = {
    0: 'High-Spender',
    1: 'Frequent Buyer',
    2: 'Occasional Shopper',
    3: 'Low-Spender',
    4: 'Rare Visitor'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    segment = None
    if request.method == 'POST':
        try:
            # Get input values from form
            total_spend = request.form['total_spend']
            frequency = request.form['frequency']

            # Log the inputs for debugging
            app.logger.info(f"Received total_spend: {total_spend}, frequency: {frequency}")

            # Convert input values to float
            total_spend = float(total_spend)
            frequency = float(frequency)

            # Add input validation to handle various cases
            if total_spend < 0 or frequency < 0:
                flash("Negative values are not allowed.", 'error')
            elif total_spend == 0 and frequency == 0:
                flash("Both inputs cannot be zero.", 'error')
            elif total_spend == 0 and frequency > 0:
                flash("Zero spend with high frequency is not a high spender. Adjusting prediction.", 'info')
                segment = 'Low-Spender'  # Manually assign a logical segment
                flash(f'Predicted Segment: {segment}', 'success')
            elif total_spend > 0 and frequency == 0:
                flash("Spend without any frequency is unlikely. Adjusting prediction.", 'info')
                segment = 'Rare Visitor'  # Handle this case manually
                flash(f'Predicted Segment: {segment}', 'success')
            else:
                # Predict the customer segment using the model
                segment = model.predict([[total_spend, frequency]])[0]
                segment = segment_labels.get(segment, 'Unknown Segment')
                flash(f'Predicted Segment: {segment}', 'success')

        except ValueError:
            flash("Invalid input! Please enter valid numbers.", 'error')

    # Prepare segment distribution (example data)
    segment_distribution = [5, 10, 15, 10, 5]
    segment_labels_list = list(segment_labels.values())

    return render_template('index.html', segment=segment, 
                           segment_distribution=segment_distribution, 
                           segment_labels=segment_labels_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
