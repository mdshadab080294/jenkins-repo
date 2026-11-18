"""A first Databricks Python script: create and display a tiny Spark DataFrame."""

print("Hello from Databricks!")

# Databricks provides the Spark session as `spark` when this file runs on compute.
people = [
    ("Asha", "Data analyst"),
    ("Ravi", "Data engineer"),
    ("Mina", "Data scientist"),
]

people_df = spark.createDataFrame(people, ["name", "role"])

print("People in the sample table:")
display(people_df)

print(f"Number of people: {people_df.count()}")
