# testrepo

it is a markdown file in the repository

# SpaceX Falcon 9 First Stage Landing Prediction

This repository contains the complete capstone project for the **IBM Data Science Professional Certificate**. The goal of this project is to predict whether the first stage of the Falcon 9 rocket will land successfully. Since the first stage represents a significant portion of the launch cost, predicting its landing success allows us to estimate the overall cost of a launch, helping SpaceX's competitors bid against them effectively.

---

## 🚀 Project Overview

SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore, determining whether the first stage will land successfully allows us to predict the price of a launch.

This project covers the entire data science workflow:
1. **Data Collection** (using SpaceX API & Web Scraping)
2. **Data Wrangling** (cleaning and preprocessing)
3. **Exploratory Data Analysis (EDA)** (using SQL and visualization libraries like Seaborn/Matplotlib)
4. **Interactive Map Visualizations** (using Folium)
5. **Interactive Dashboard** (using Plotly Dash)
6. **Predictive Analysis** (Machine Learning Classification)

---

## 📁 Repository Structure

Here is a breakdown of the completed notebooks and files included in this repository:

| File Name | Description |
| :--- | :--- |
| `1_Data_Collection_API.ipynb` | Collecting SpaceX launch data using requests and API calls. |
| `2_Data_Collection_Webscraping.ipynb` | Scraping Falcon 9 launch records from Wikipedia using BeautifulSoup. |
| `wrap.ipynb` / `3_Data_Wrangling.ipynb` | Cleaning, preprocessing, and creating binary landing outcome labels (`Class 0` or `Class 1`). |
| `4_EDA_with_SQL.ipynb` | Querying the SQLite database to discover key insights from the dataset. |
| `5_EDA_with_Visualization.ipynb` | Creating visual plots (scatter plots, bar charts) to identify patterns in features like Launch Sites, Flight Numbers, and Orbit types. |
| `6_Interactive_Map_Folium.ipynb` | Building interactive map visualizations to mark launch sites and calculate distances to proximities (coastlines, highways, railways). |
| `7_Plotly_Dash_App.py` | Python script for the interactive dashboard containing payload range sliders and launch site dropdown selections. |
| `8_Machine_Learning_Prediction.ipynb` | Training and tuning 4 classification models (Logistic Regression, SVM, Decision Tree, KNN) using `GridSearchCV`. |

---

## 📊 Key Findings & Results

* **Success Rate Improvements (Learning Curve):** Early flights had a higher failure rate, but SpaceX's landing success rates dramatically improved as the flight numbers increased (proven by EDA).
* **Launch Site Performance:** **KSC LC 39A** demonstrated the highest success rate among all launch sites.
* **Proximity Insight:** Launch sites are strategically placed near coastlines to ensure failed landings occur over water, and close to railways/highways for easy transportation of rocket stages.
* **Machine Learning Performance:**
  * All four models (Logistic Regression, SVM, Decision Tree, and KNN) achieved an identical test set accuracy of **83.33%**.
  * The main challenge observed in the confusion matrix was **False Positives** (unsuccessful landings predicted as successful), which was primarily caused by class imbalance in the small test dataset.

---

## 🛠️ How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/hans1202/testrepo.git](https://github.com/hans1202/testrepo.git)
   cd testrepo
