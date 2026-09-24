# SME Predictive Dashboard

A lightweight predictive analytics dashboard designed for Small and Medium Enterprises (SMEs). The system helps business owners forecast short-term product demand and detect unusual sales or inventory patterns that may indicate process issues or potential fraud.

## Project Overview

Many small businesses still rely on spreadsheets or manual methods for inventory planning. This often leads to stockouts, overstocking, or delayed detection of unusual patterns. 

This project aims to provide a simple, affordable, and easy-to-use software tool that:

- Forecasts 7-day and 30-day product demand
- Detects unusual patterns in sales and inventory data
- Provides clear risk scores with explanations
- Supports role-based access (Owner, Manager, Staff)
- Maintains an audit log of important actions

## Key Features

- CSV / Excel file upload
- Demand forecasting using ensemble machine learning models
- Anomaly detection with human override option
- Role-based access control
- Local data processing (privacy-focused)
- Simple web interface suitable for non-technical users

## Technology Stack

- **Language:** Python
- **Machine Learning:** scikit-learn (Random Forest, Gradient Boosting)
- **Data Processing:** pandas
- **Web Interface:** Streamlit or Flask
- **Version Control:** Git & GitHub

## Project Structure
sme-predictive-dashboard/
├── src/                # Source code
├── docs/               # Documentation and reports
├── design/             # Architecture diagrams and design files
└── README.md


## Current Status

This project is part of the **MSIT 5910 Capstone Project** at University of the People.

- Unit 1: Problem definition and literature review – Completed
- Unit 2: Project proposal and planning – Completed
- Unit 3: System architecture and detailed design – Completed
- Units 4–8: Implementation, testing, and final evaluation – Upcoming

## Author

**Rabin Panthi**  
MSIT Student, University of the People  

## License

This project is developed for academic purposes as part of the MSIT Capstone Project.