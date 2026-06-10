import matplotlib.pyplot as plt

years = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
debt  = [124, 2025, 1841, 619, 915, 469, 126, 59, 1706, 2888, 3456, 3500]

plt.figure(figsize=(10, 5))
plt.plot(years, debt, marker='o', linewidth=2, color='#185FA5', markersize=6)
plt.title('Figure 2. Short-term Debt of "XXX" Corporation, 2007–2018', fontsize=13)
plt.xlabel('Year', fontsize=11)
plt.ylabel('Short-term Debt (₱ Millions)', fontsize=11)
plt.xticks(years, rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('short_term_debt.png', dpi=150)
plt.show()