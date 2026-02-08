# Global AI Content Impact Dataset Analysis & Dashboard

## Project Overview
This project provides comprehensive analysis and visualization tools for the Global AI Content Impact Dataset, which contains information about AI adoption rates, economic impacts, social effects, and regulatory environments across different countries, industries, and years.

## Files Included

### Note about existing files
The following files may be present in your directory but were not created as part of this project:
- ai_impact_analysis.pdf: A PDF export of the basic Jupyter notebook (if created separately)

### Files created as part of this project:

### 1. ai_impact_analysis.ipynb
A Jupyter Notebook that performs exploratory data analysis on the Global AI Content Impact Dataset.

#### Features:
- Loads and inspects the dataset
- Provides summary statistics
- Creates visualizations for:
  - Distribution of records by country, year, and industry
  - AI adoption rates by country and industry
  - Correlation matrix of numerical variables
  - Relationships between key metrics (adoption vs revenue, adoption vs job loss)
  - Popularity of AI tools
  - Distribution of regulation statuses
  - Consumer trust by country
  - Market share of AI companies by country
  - Average metrics by country and industry
  - Trends over time for key metrics
- Generates a summary of key findings

#### Libraries Used:
- pandas: For data manipulation and analysis
- numpy: For numerical computations
- matplotlib: For plotting
- seaborn: For statistical data visualization

### 2. ai_impact_dashboard.py
A Streamlit application that provides an interactive dashboard for exploring the dataset.

#### Features:
- Interactive filters for countries, industries, and years
- Multiple tabs for different aspects of the data:
  - Overview: Basic metrics and distribution charts
  - AI Adoption: Analysis of AI adoption rates by country and industry
  - Economic Impact: Revenue increases, job losses, and market shares
  - Social Impact: Consumer trust and human-AI collaboration
  - Tools & Regulations: AI tools popularity and regulation status
- Scatter plots showing relationships between key variables
- Bar charts for comparisons across countries and industries
- Download functionality for filtered data
- Responsive design for different screen sizes

#### Libraries Used:
- streamlit: For creating the web application
- pandas: For data manipulation
- numpy: For numerical computations
- plotly: For interactive visualizations

### 3. requirements.txt
A file listing all required Python packages for the project.

### 4. setup_and_run.sh
A bash script to set up the virtual environment and run the analysis tools on Linux/macOS.

### 5. setup_and_run.bat
A batch script to set up the virtual environment and run the analysis tools on Windows.

## How to Use

### Prerequisites
1. Make sure you have Python 3.7+ installed
2. Place the `Global_AI_Content_Impact_Dataset.csv` file in the same directory as the scripts

### Using Setup Scripts (Recommended)
1. Run the appropriate setup script for your OS:
   - On Linux/macOS: `./setup_and_run.sh`
   - On Windows: `setup_and_run.bat`
2. Follow the instructions in the script output

### Manual Setup
1. Create a virtual environment:
   ```bash
   python -m venv ai_impact_env
   source ai_impact_env/bin/activate  # On Windows: ai_impact_env\Scripts\activate
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### For Jupyter Notebook Analysis:
1. Run the analysis notebook:
   ```bash
   jupyter notebook ai_impact_analysis.ipynb
   ```
2. Execute the cells to see the analysis and visualizations

### For Streamlit Dashboard:
1. Run the dashboard with:
   ```bash
   streamlit run ai_impact_dashboard.py
   ```
2. The dashboard will open in your browser where you can interact with the filters and visualizations

## Dataset Description
The Global AI Content Impact Dataset contains the following columns:
- Country: The country where the data was collected
- Year: The year of data collection
- Industry: The industry sector
- AI Adoption Rate (%): Percentage of AI adoption in the sector
- AI-Generated Content Volume (TBs per year): Volume of AI-generated content
- Job Loss Due to AI (%): Percentage of jobs lost due to AI
- Revenue Increase Due to AI (%): Percentage increase in revenue due to AI
- Human-AI Collaboration Rate (%): Rate of collaboration between humans and AI
- Top AI Tools Used: Most commonly used AI tools in the sector
- Regulation Status: Regulatory environment (Strict/Moderate/Lenient)
- Consumer Trust in AI (%): Level of consumer trust in AI
- Market Share of AI Companies (%): Market share held by AI companies

## Key Insights Explored
- How AI adoption varies across countries and industries
- The relationship between AI adoption and economic outcomes
- The impact of AI on employment in different sectors
- Consumer trust levels in different regions
- Regulatory approaches to AI across countries
- The most popular AI tools in different sectors
- Trends over time in AI adoption and impact