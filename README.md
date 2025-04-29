
# Sales Data Visualizer

**Sales Data Visualizer** is an interactive, user-friendly Streamlit application that allows sales teams and business professionals to upload, explore, and visualize contact and call data directly from Excel files.

## Key Features

- **Easy Excel Upload**: Instantly upload `.xlsx` files containing your sales contacts and call records.
- **Insightful Metrics**: View total companies, total contacts, and connected calls at a glance.
- **Interactive Dashboards**: Explore dynamic charts for email, phone, and LinkedIn presence, call status distributions, and top companies by contact count.
- **Company-wise Call Analysis**: Drill down into call outcomes and engagement for each company.
- **Role and Status Insights**: Visualize top job titles and filter contacts by website status or call results.
- **Comprehensive Data Table**: Search and sort all company and contact details in one place.
- **Modern, Attractive Layout**: Clean, responsive design using interactive Plotly charts and Streamlit columns for a professional dashboard experience.

## Use Cases

- **Sales & Business Development**: Track outreach, analyze engagement, and prioritize follow-ups.
- **CRM Data Auditing**: Quickly spot missing or incomplete contact information.
- **Team Reporting**: Share visual summaries and detailed tables with stakeholders.

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/sales-data-visualizer.git
   cd sales-data-visualizer
   ```

2. **Install the required dependencies**:

   It's recommended to create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For macOS/Linux
   venv\Scriptsctivate      # For Windows
   ```

   Then install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:

   Launch the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. **Upload your Excel file**:

   - Click the "Upload File" button and select an `.xlsx` file containing your sales contacts and call data.
   - Explore the data and visualizations in the interactive dashboard.

## Technology Stack

- **Frontend**: Streamlit, Plotly
- **Backend**: Python
- **Libraries**: Pandas, NumPy

## Contribution

Feel free to fork the repo and submit a pull request if you'd like to contribute. Whether it's fixing a bug, improving the UI, or adding a new feature, contributions are welcome!

## License

This project is licensed under the MIT License.

---

Get started by uploading your sales contact Excel file and explore your data like never before! 🚀
