# Company Revenue Analyzer

A Python tool that automatically fetches and visualizes company financial performance over time using `yfinance`, `pandas`, and `matplotlib`.

---

## 🚀 Features

- 🗂️ Retrieves **Revenue** and **Net Income** for any public company via dynamic ticker input.
- 📈 Processes data using `pandas` and produces **trend visualizations** (Revenue vs. Net Income) with `matplotlib`.
- 💾 Saves analysis results:
  - Growth metrics calculation (e.g. YoY%)
  - Exported as CSV for further analysis
  - Charts saved as PNG images

---

## 🧰 Technologies

- **Python** (3.7+)
- [`yfinance`](https://pypi.org/project/yfinance/) — Fetches financial statements :contentReference[oaicite:1]{index=1}  
- `pandas` — Data processing  
- `matplotlib` — Visualizations  

---

## 📥 Installation

```bash
git clone https://github.com/mddaniyaal/Company-Revenue-Analyzer.git
cd Company-Revenue-Analyzer
pip install -r requirements.txt
````

---

## ⚙️ Usage

Run the script from the terminal:

```bash
python main.py --ticker AAPL --start 2015-01-01 --end 2025-01-01
```

This generates:

* `AAPL_revenue_net_income.csv` (processed data)
* `AAPL_growth_metrics.csv` (growth percentages)
* `AAPL_financial_trends.png` (Revenue vs Net Income chart)

Example script snippet:

```python
data = fetch_financials(ticker, start, end)
metrics = calculate_growth(data)
export_csv(data, metrics, ticker)
plot_trends(data, ticker)
```

---

## 📊 Example Output

*(Include a sample PNG or CSV snippet here for better context)*

---

## 🛠️ Project Structure

```
.
├── main.py               # Core script logic
├── financials.py         # yfinance API wrappers
├── analysis.py           # Metrics & calculations
├── plotter.py            # Visualization functions
├── requirements.txt
└── README.md
```

---

## 🌟 Why This Project?

Inspired by modern financial analysis workflows that use Python for fetching and visualizing company performance data ([everhour.com][1]), this tool simplifies trend analysis for analysts, investors, and students.

---

## 📚 References

* Using `yfinance` for financial statement retrieval&#x20;
* Financial trend visualization with `pandas` & `matplotlib` ([github.com][2])

---

## 📝 License

MIT License — See [LICENSE](LICENSE) for details.

---

## 🗣️ Contributing

Contributions welcome! Feel free to open issues or pull requests.

---

## 🙋‍♂️ Author

Developed by **mddaniyaal**.
GitHub: [@mddaniyaal](https://github.com/mddaniyaal)

```

---

### 🧭 Notes

- The structure follows common README patterns and improves readability :contentReference[oaicite:18]{index=18}.  
- Always include an example output to clarify the project's functionality.  
- Add badges (build status, license, PyPI) once configured to enhance presentation.

Let me know if you'd like help adding CI workflows, badges, or expanding examples!
::contentReference[oaicite:19]{index=19}
```

[1]: https://everhour.com/blog/github-readme-template/?utm_source=chatgpt.com "How to Write a Github README.md That Developers Actually Read"
[2]: https://github.com/dotpep/stock-analyze?utm_source=chatgpt.com "Lab. Analyze/Visualize stock data of Tesla and GameStop ... - GitHub"
