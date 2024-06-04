# Import libraries
from flask import Flask, request, url_for, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions = transactions)

# Create operation : Display add transaction form
@app.route("/add", methods =['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
       # Create a new transaction object using form field values
       transaction = {
        "id": len(transactions)+1
        "date": request.form['date']
        'amount': float(request.form['amount'])
       }
        # Append the new transaction to the list
        transactions.append(transaction)
        
        # Redirect to the transactions list page
        return redirect(url_for(get_transactions))
    
    # Render the form template to display the add transaction form
    return render_template('form.html')

# Update operation : Dsiplat edit transaction form
@app.route('/edit/<int:transaction_id>', methods = ['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']
        amount = float(request.form['amount'])

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction.id:
                transaction["date"] = date
                transaction['amount'] = amount
                break
        
        # Redirect to the transaction list page
        return redirect(url_for('get_transactions'))
    
    # Find the transaction with the mathcing ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction.id:
            return render_template('edit.html', transaction = transactions)


# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id
        transaction.remove(transaction)
        break
    
    # Redirect to the transactions list page
    return redirect(url_for('get_transactions'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug = True)
