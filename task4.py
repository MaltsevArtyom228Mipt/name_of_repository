import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')

pairs = [
    ('SepalWidthCm', 'SepalLengthCm'),
    ('PetalLengthCm', 'SepalLengthCm'),
    ('PetalWidthCm', 'SepalLengthCm'),
    ('PetalLengthCm', 'SepalWidthCm'),
    ('PetalWidthCm', 'SepalWidthCm'),
    ('PetalWidthCm', 'PetalLengthCm')
]

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
axes = axes.flatten()

for i, (x_col, y_col) in enumerate(pairs):
    x = df[x_col]
    y = df[y_col]

    x_mean = x.mean()
    y_mean = y.mean()

    numerator = ((x - x_mean) * (y - y_mean)).sum()
    denominator = ((x - x_mean) ** 2).sum()

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    y_pred = slope * x + intercept
    residuals = y - y_pred
    ss_res = (residuals ** 2).sum()
    ss_tot = ((y - y_mean) ** 2).sum()
    r2 = 1 - (ss_res / ss_tot)

    axes[i].scatter(x, y, alpha=0.6, label=f'{y_col} vs {x_col}')
    axes[i].plot([x.min(), x.max()],
                 [slope*x.min()+intercept, slope*x.max()+intercept],
                 color='red', linewidth=2,
                 label=f'y = {slope:.2f}x + {intercept:.2f} (R²={r2:.2f})')
    axes[i].set_title(f'{y_col} vs {x_col}', fontsize=10)
    axes[i].legend(prop={'size': 8})

plt.tight_layout()
plt.suptitle('Комбинации длин и ширин лепестков с прямой МНК', fontsize=16, y=1.02)
plt.show()