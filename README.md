# WhatsApp Chat Analyzer 📊💬

An end-to-end conversational analytics web dashboard that transforms raw, unformatted WhatsApp chat exports (`.txt` files) into rich data visualizations. This application exposes hidden behavioral patterns, temporal trends, and linguistic insights across entire group ecosystems or for standalone individual profiles.


## ✨ Features Breakdown

### 1. High-Level KPI Statistics
* **Total Messages:** Total conversational transaction volume across the selected scope.
* **Total Words:** Total vocabulary footprint extracted from message arrays.
* **Links Shared:** Total count of unique URLs scraped via `urlextract`.

### 2. Temporal & Trend Analysis
* **Monthly Timeline:** A continuous line chart tracking long-term communication momentum across months and years.
* **Daily Timeline:** A highly granular timeline tracking precise daily transaction spikes.
* **Activity Maps:** Standalone bar charts mapping relative activity weights by **Day of the Week** and **Month of the Year**.
* **Weekly Activity Heatmap:** An interactive Seaborn grid mapping out peak communication windows (Hours of the Day vs. Days of the Week).

### 3. Linguistics & Advanced Text Mining
* **WordCloud Generation:** A visual cluster displaying high-frequency vocabulary scaled by occurrence density.
* **Most Common Words:** A clean, horizontal ranking chart displaying the top 20 structural words used.
* *Note: Both text features utilize a custom Hinglish/English stop-words mask (`stop_hinglish.txt`) to automatically eliminate conversational filler words.*

### 4. Emoji Distribution
* **Emoji Frequency Mapping:** Complete parsing of unique Unicode characters utilizing `emoji.EMOJI_DATA`.
* **Proportional Breakdown:** Top-performing emotional expressions mapped cleanly using Matplotlib pie charts.

---

## 🛠️ Built With

* **Frontend UI Framework:** [Streamlit](https://streamlit.io/)
* **Data Wrangling & Processing:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
* **Data Visualization Engines:** [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), [WordCloud](https://github.com/amueller/word_cloud)
* **Text & Data Mining Utilities:** [URLExtract](https://github.com/ndexter/urlextract), [Emoji (v2.0.0+)](https://github.com/carpedm20/emoji/)

---
