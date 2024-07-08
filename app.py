# app.py
from flask import Flask, render_template, request
import pandas as pd
from Issuer import IssuerModule
from Buyer import BuyerModule
from Buyer_Industry import BuyerIndustryModule
from Supplier import SupplierModule
from Supplier_Industry import SupplierIndustryModule

app = Flask(__name__)

# Load data
df = pd.read_excel("Input.xlsx")

# Initialize modules
issuer_module = IssuerModule(df)
buyer_module = BuyerModule(df)
buyer_industry_module = BuyerIndustryModule(df)
supplier_module = SupplierModule(df)
supplier_industry_module = SupplierIndustryModule(df)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/issuer', methods=['GET', 'POST'])
def issuer():
    if request.method == 'POST':
        issuer_name = request.form['issuer_name']
        top_n = int(request.form.get('top_n', 5))  # Default to 5 if not specified
        stats = {
            'issuer_name': issuer_name,
            'issuer_position': issuer_module.get_issuer_position(issuer_name),
            'number_of_buyers': issuer_module.get_number_of_buyers(issuer_name),
            'top_buyers': issuer_module.get_top_and_bottom_buyers(issuer_name, top_n)[0],
            'bottom_buyers': issuer_module.get_top_and_bottom_buyers(issuer_name, top_n)[1],
            'top_buyer_industry': issuer_module.get_top_buyer_industry(issuer_name, top_n)[0],
            'bottom_buyer_industry': issuer_module.get_top_buyer_industry(issuer_name, top_n)[1],
            'top_suppliers': issuer_module.get_top_and_bottom_suppliers(issuer_name, top_n)[0],
            'bottom_suppliers': issuer_module.get_top_and_bottom_suppliers(issuer_name, top_n)[1],
            'top_supplier_industry': issuer_module.get_top_supplier_industry(issuer_name, top_n)[0],
            'bottom_supplier_industry': issuer_module.get_top_supplier_industry(issuer_name, top_n)[1]
        }
        return render_template('issuer.html', stats=stats)
    return render_template('issuer.html')

@app.route('/buyer', methods=['GET', 'POST'])
def buyer():
    if request.method == 'POST':
        buyer_name = request.form['buyer_name']
        stats = {
            'buyer_position': buyer_module.get_buyer_position(buyer_name),
            'no of issuer' : buyer_module.get_number_of_issuers(buyer_name)
        }
        return render_template('buyer.html', stats=stats)
    return render_template('buyer.html')

@app.route('/buyer_industry', methods=['GET', 'POST'])
def buyer_industry():
    if request.method == 'POST':
        buyer_industry_name = request.form['buyer_industry_name']
        stats = {
            'buyer_industry_position': buyer_industry_module.get_buyer_industry_position(buyer_industry_name)
        }
        return render_template('buyer_industry.html', stats=stats)
    return render_template('buyer_industry.html')

@app.route('/supplier', methods=['GET', 'POST'])
def supplier():
    if request.method == 'POST':
        supplier_name = request.form['supplier_name']
        stats = {
            'supplier_position': supplier_module.get_supplier_position(supplier_name)
        }
        return render_template('supplier.html', stats=stats)
    return render_template('supplier.html')

@app.route('/supplier_industry', methods=['GET', 'POST'])
def supplier_industry():
    if request.method == 'POST':
        supplier_industry_name = request.form['supplier_industry_name']
        stats = {
            'supplier_industry_position': supplier_industry_module.get_supplier_industry_position(supplier_industry_name)
        }
        return render_template('supplier_industry.html', stats=stats)
    return render_template('supplier_industry.html')

if __name__ == '__main__':
    app.run(debug=True)
