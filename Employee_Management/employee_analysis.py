from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Database connection
engine = create_engine("mysql+pymysql://root:1234@localhost/EMPP")

query = "SELECT * FROM employees"
df = pd.read_sql(query, engine)

print(df)

print("\nAverage Salary:", df['salary'].mean())

print("\nHighest Salary:")
print(df.loc[df['salary'].idxmax()])

print("\nLowest Salary:")
print(df.loc[df['salary'].idxmin()])

print("\nTotal Employees:", df.shape[0])

# Average Salary by Position
df.groupby("position")["salary"].mean().plot(kind="bar")
plt.title("Average Salary by Position")
plt.show()

# Salary Distribution
df["salary"].plot(kind="hist")
plt.title("Salary Distribution")
plt.show()

# Employee Distribution by Role
df["position"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Employee Distribution by Role")
plt.ylabel("")
plt.show()
