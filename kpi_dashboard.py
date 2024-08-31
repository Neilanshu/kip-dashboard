import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# File path to the Excel file
file_path = '/Users/nilanshubhandare/Documents/kpi_dashboard/Sales Data.xls'

# Load the Excel file
data = pd.read_excel(file_path)

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Extract year from 'Date' column
data['Year'] = data['Date'].dt.year

# Calculate KPIs
kpi_data = data.groupby(['Year', 'Category']).agg(
    TotalSales=pd.NamedAgg(column='TotalSales', aggfunc='sum'),
    QuantitySold=pd.NamedAgg(column='QuantitySold', aggfunc='sum')
).reset_index()

# Calculate Average Order Value (AOV)
kpi_data['AOV'] = kpi_data['TotalSales'] / kpi_data['QuantitySold']

# Sample Marketing Spend for ROI calculation
# (Replace with actual data if available)
kpi_data['MarketingSpend'] = 1000  # Example constant, adjust accordingly
kpi_data['ROMS'] = kpi_data['TotalSales'] / kpi_data['MarketingSpend']

# Save KPIs to CSV for review
kpi_data.to_csv('kpi_data.csv', index=False)

# Create visualizations
# Total Sales per Category
fig1 = px.bar(kpi_data, x='Category', y='TotalSales', color='Year', title='Total Sales per Category')
fig1.write_image('total_sales.png')

# Average Order Value per Category
fig2 = px.line(kpi_data, x='Year', y='AOV', color='Category', title='Average Order Value per Category')
fig2.write_image('avg_order_value.png')

# Create a PDF with visualizations
def create_pdf():
    c = canvas.Canvas("kpi_dashboard.pdf", pagesize=letter)
    width, height = letter

    c.drawString(100, height - 100, 'KPI Dashboard')

    c.drawImage('total_sales.png', 100, height - 500, width=400)
    c.drawString(100, height - 520, 'Total Sales per Category')

    c.drawImage('avg_order_value.png', 100, height - 800, width=400)
    c.drawString(100, height - 820, 'Average Order Value per Category')

    c.save()

create_pdf()