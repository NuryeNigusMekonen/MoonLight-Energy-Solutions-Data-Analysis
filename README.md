
 EDA pipeline to **Benin**, **Sierra Leone**, and **Togo**,

* Summarizes the project and objective
* Explains your process and structure
* Shows how to run the analysis
* Highlights insights and findings

---



````markdown
#  Cross-Country Solar Data Analysis – Week 0 Challenge

This project is part of the 10 Academy Week 0 AI Mastery Challenge. It focuses on exploring and analyzing solar farm sensor data from **Benin**, **Sierra Leone**, and **Togo** to identify high-potential regions for solar investment.

---

##  Project Objective

As an analytics engineer at **MoonLight Energy Solutions**, my goal is to:
- Clean and explore environmental sensor data
- Detect anomalies, trends, and correlations
- Compare performance across the three countries
- Recommend optimal regions for solar installation based on data

---

## Project Structure

```bash
MoonLight-Energy-Solutions-Data-Analysis/
├-- notebooks/
     benin.ipynb
     sierraleone.ipynb
     togo.ipynb
├-- scripts/
     ()
|-- Data/
|-- cleaned_data/
|-- graphs/
          benin/benin_bubble_chart.png
          windorose_plote.png

├-- requirements.txt
├-- .gitignore
└-- README.md
````

---

## Analysis Highlights

Each country’s EDA notebook includes:

* Summary statistics & missing value report
* Outlier detection and cleaning (Z-score method)
* Time-series plots (daily & hourly GHI, Tamb)
* Boxplots, histograms, and heatmaps
* Wind rose plots and scatter plots
* Bubble charts (GHI vs Tamb with RH as size)
* Impact analysis of manual cleaning on panel performance

> All datasets were cleaned and saved locally, but are **excluded from the repo** per `.gitignore` rules.

---

##  How to insall

1. **Clone the repository**

```bash
git clone https://github.com/NuryeNigusMekonen/MoonLight-Energy-Solutions-Data-Analysis.git
cd solar-challenge-week1
```

2. **Create and activate a virtual environment**

```bash
python -m venv week_0_venv
source week_0_venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run notebooks**
   Use Jupyter or VSCode to open and run the notebooks under the `notebooks/` directory.

---

## Key Insights

Benin--showed strong midday irradiance and moderate wind stability. Cleaning events slightly improved panel output.
Sierra Leone-- experienced more cloud cover and humidity, reducing direct irradiance (DNI).
Togo-- had balanced environmental conditions and fewer outliers, making it a promising candidate for stable output.

---

##  Tools Used

* Python, Pandas, NumPy
* Matplotlib, Seaborn, Plotly
* Jupyter Notebooks
* Git & GitHub
* Windrose library (for wind direction plots)

---

##  Files Not Included

* Raw and cleaned `.csv` files are located in `data/` and `cleaned_data/`, which are ignored via `.gitignore` for best practices.
* You must add the raw datasets locally to run the notebooks.

---
##  Sample EDA Results


###  GHI vs Ambient Temperature (Bubble Size = RH)
This bubble chart shows that GHI generally increases with ambient temperature, with bubble size representing relative humidity. Larger bubbles (higher RH) are often associated with lower GHI, suggesting a cloud impact.
![Bubble Chart](graphs/benin_bubble_chart.png)

---

###  windorose plote

to visulaize wind direction and speed this requires a special plot type
![GHI Trend](graphs/windorose_plote.png)

---

## Author & Credits

👤 Author
Nurye Nigus
Electrical & Software Engineer
📧 Email :    nurye.nigus.me@gmail.com
🌐 LinkedIn   (https://www.linkedin.com/in/nryngs/)
🐙 GitHub:    @NuryeNigusMekonen
📞 Phone :    +251929404324

---


