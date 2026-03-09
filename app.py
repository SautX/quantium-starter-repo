import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load formatted sales data
df = pd.read_csv("data/formatted_sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Group sales by date
df = df.groupby("Date")["Sales"].sum().reset_index()

# Sort by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )

])

if __name__ == "__main__":
    app.run(debug=True)