# KPI-Dashboard

## Overview

This project involves the automation of a Key Performance Indicator (KPI) dashboard using a given sales dataset. The dashboard includes calculations and visualizations of key metrics to analyze sales performance.

## Project Structure

- **`kpi_dashboard.py`**: Python script that performs data processing, KPI calculations, and generates the dashboard.
- **`kpi_data.csv`**: Sample dataset used for KPI calculations.
- **`kpi_dashboard.pdf`**: Generated PDF report of the KPI dashboard.
- **`total_sales.png`**: Bar chart visualizing total sales by category.
- **`avg_order_value.png`**: Bar chart visualizing average order value by category.
- **`README.md`**: This file, providing an overview and instructions for the project.

## Requirements

- Python 3.11 or later
- `pandas`
- `matplotlib`
- `plotly`
- `fpdf`
- `reportlab`
- `xlrd` (for reading `.xls` files)

Install the required libraries using the following command:

```bash
pip install pandas matplotlib plotly fpdf reportlab xlrd
```

## Usage

1. **Prepare the Data:**
   Ensure that `kpi_data.csv` is in the same directory as the script.

2. **Run the Script:**
   Execute the script to generate the KPI dashboard:

   ```bash
   python kpi_dashboard.py
   ```

   This will create `kpi_dashboard.pdf` with visualizations of total sales and average order values.

3. **Automate the Script:**
   To run the script at regular intervals, you can set up a task scheduler:
   
   - **On Windows:** Use Task Scheduler to run `python kpi_dashboard.py` periodically.
   - **On macOS/Linux:** Use `cron` jobs to automate the script execution.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the open-source community for providing the tools used in this project.
