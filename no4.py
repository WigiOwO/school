import matplotlib.pyplot as plt

years = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
highs = [40.85, 40.85, 40.85, 48.00, 64.75, 51.75, 72.00, 81.65, 80.15, 75.35, 98.35, 99.00]
lows  = [30.90, 30.00, 29.25, 34.00, 32.00, 39.65, 45.75, 63.25, 63.50, 60.25, 67.75, 70.00]

plt.figure(figsize=(10, 5))
plt.plot(years, highs, marker='o', linewidth=2, color='#A32D2D', markersize=6, label='High')
plt.plot(years, lows,  marker='o', linewidth=2, color='#185FA5', markersize=6, label='Low')
plt.fill_between(years, highs, lows, alpha=0.08, color='gray')
plt.title('Figure 3. High and Low Common Stock Prices of "XXX" Corporation, 2007–2018', fontsize=13)
plt.xlabel('Year', fontsize=11)
plt.ylabel('Stock Price (₱)', fontsize=11)
plt.xticks(years, rotation=0)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('stock_high_low.png', dpi=150)
plt.show()