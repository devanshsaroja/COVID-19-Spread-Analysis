# 🌍 COVID-19 Global Spread Analysis Dashboard

![Dashboard Screenshot](covid.png)  
*Interactive dashboard showing COVID-19 statistics and geographical distribution*

## 📊 Key Features
- **Interactive World Map**
  - Proportional circles visualize case severity
  - Hover/click interactions for detailed case numbers
- **Top Countries Ranking**
  - Auto-generated top 15 affected nations
  - Real-time data processing with Pandas
- **Clean Visualization**
  - Color-coded for intuitive understanding
  - Responsive design works on all devices

## 🛠️ Technical Stack
| Component       | Technology Used |
|----------------|----------------|
| Backend        | Python Flask   |
| Data Processing| Pandas         |
| Visualization  | Folium         |
| Frontend       | HTML5/CSS3     |
| Map Tiles      | CartoDB        |

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/covid-19-spread-analysis.git
   cd covid-19-spread-analysis
2. Install dependencies:
   ```bash
   pip install flask folium pandas
3. Add your dataset:
 - Place covid-19-dataset-1.csv in project root
 - Ensure it contains columns: Lat, Long_, Confirmed, Country_Region   
 - pip install flask folium pandas
### Running the Application
    python app.py
- Access dashboard at: http://localhost:5000

### 📈 Understanding the Dashboard
- **Top Countries Table**
- ![Dashboard Screenshot](country%20table.png) 
  - Displays ranked list of most affected countries with:
  - Country name
  - Total confirmed cases
- **Interactive World Map**
- ![Dashboard Screenshot](map.png) 
  - Map Section
  - Circle Size: Proportional to case numbers
  - Color Coding: Red intensity indicates severity
- **Interactions**
  - Hover: See location name
  - Click: View detailed case count
 
- **📂 Project Structure**
- ```bash
  ├── app.py                # Main application
  ├── requirements.txt      # Dependencies
  ├── covid-19-dataset-1.csv # Dataset
  ├── templates/
  │   └── home.html         # Dashboard UI
  │   └── base.html         # Base template
  └── static/               
      └── style.css         # Custom styling
- **📃 License**
- This project is licensed under the MIT License. 
