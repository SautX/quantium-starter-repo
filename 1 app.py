import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("data/formatted_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "fontFamily": "Arial"
        }
    ),

    html.Div([
        html.Label("Select Region:",
                   style={"fontWeight": "bold", "fontSize": "18px"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            labelStyle={"display": "inline-block", "margin-right": "20px"}
        ),
    ],
    style={"textAlign": "center", "margin-bottom": "30px"}),

    dcc.Graph(id="sales-chart")

],
style={
    "width": "80%",
    "margin": "auto",
    "backgroundColor": "#f5f5f5",
    "padding": "20px",
    "borderRadius": "10px"
})


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    grouped = filtered_df.groupby("Date")["Sales"].sum().reset_index()

    fig = px.line(
        grouped,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        labels={"Sales": "Total Sales", "Date": "Date"}
    )

    fig.update_layout(
        plot_bgcolor="white",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)