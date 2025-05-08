from preswald import text, plotly, connect, get_df, table, query, sidebar
import pandas as pd
import plotly.express as px

# sidebar
sidebar()

text("# Welcome to Preswald!")
text("This is your first app. 🎉")

# Load the CSV
connect()
df = get_df("sample_csv")

# Create a scatter plot
fig = px.scatter(
    df,
    x="quantity",
    y="value",
    text="item",
    title="Quantity vs. Value",
    labels={"quantity": "Quantity", "value": "Value"},
)

# Add labels for each point
fig.update_traces(textposition="top center", marker=dict(size=12, color="lightblue"))

# Style the plot
fig.update_layout(template="plotly_white")

# Show the plot
plotly(fig)

# Show the data
table(df)

# Query the data
sql = "SELECT * FROM sample_csv WHERE value > 50"
filtered_df = query(sql, "sample_csv")

# Interactive UI
text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

# Visualisation
fig = px.scatter(df, x="quantity", y="value", color="item", title="Quantity vs Value")
plotly(fig)
