import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# Calculate z-scores
def calculate_z_score(x: float, mean: float, std_dev: float) -> float:
    """Calculate the z-score for a value x given mean and standard deviation."""
    return (x - mean) / std_dev


# Calculate area under the curve (cumulative probability)
def area_under_curve(z_score: float) -> float:
    """Calculate area under the normal curve up to z-score."""
    return stats.norm.cdf(z_score)


# Example usage
mean = 5
std_dev = 1
value = 6

# Calculate z-score
z = calculate_z_score(value, mean, std_dev)
print(f"Z-score for {value} with mean={mean}, std_dev={std_dev}: {z:.4f}")

# Calculate probability (area under curve)
area = area_under_curve(z)
print(f"Area under curve for z={z:.4f}: {area:.4f}")
print(
    f"This means there's a {area*100:.2f}% chance of getting a value less than {value}"
)

# Visualize
x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)
y = stats.norm.pdf(x, mean, std_dev)

plt.figure(figsize=(10, 6))
plt.plot(x, y, "b-", label="Normal Distribution")
plt.fill_between(
    x[x <= value], y[x <= value], color="skyblue", alpha=0.5, label=f"Area = {area:.4f}"
)
plt.axvline(value, color="red", linestyle="--", label=f"x = {value}")
plt.axvline(mean, color="green", linestyle="-", label=f"mean = {mean}")
plt.title("Normal Distribution Curve")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
