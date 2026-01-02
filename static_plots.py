import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import us




#ADD THIS TO EVERYTHING AND MAKE IT OUTPUT PNGS
#fig.write_image("assets/plot_name.png")

#THEN THEY GO TO THE ASSETS FOLDER AND THEN DASH CAN ACCESS THEM WITH THIS:
#html.Img(src="/assets/plot_name.png", style={"width": "80%"})

#Not yet sure how to make a link/page to access all of the graphs. That will be a work in progress.



############################################################
# DATA LOADING AND TRANSFORMATION
############################################################

# Path to the folder containing THIS script (static_graphs.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one folder, then into Datasets
# Puts the strings together with / between
DATA_PATH = os.path.join(BASE_DIR, "..", "Datasets", "cleaned","cleaned_tobacco_data.csv")
DATA_PREVALENCE_PATH = os.path.join(BASE_DIR, "..", "Datasets", "cleaned", "prevalence_tobacco_data.csv")

# Load the CSVs
df = pd.read_csv(DATA_PATH)
df_prevalence = pd.read_csv(DATA_PREVALENCE_PATH) #just prevalence data across demographic groups, states, years








##########################################
#Graph XXXXXXXXXXX:

'''print("TEST GRAPH:")


# Take average disparity across focus groups and sort them
df_top_disparity = df.groupby(["demographic", "focus_group"], as_index=False)['disparity_value'].mean().sort_values(['disparity_value'],ascending=False)

#Show top 5 avg disparities
print(df_top_disparity.head(5))

# Get groups with 5 highest avg disparities as their own data:
df_top5 = df_top_disparity.head(5)

# Get groups with 5 lowest avg disparities as their own data:
df_bottom5 = df_top_disparity.tail(5)




time.sleep(1) # Wait 1 second before continuing
print("END TEST GRAPH.")'''
##########################################







##########################################
#Graph 1a:
#Line plot for cig use prevalence over time for by age level
#Aggregate mean disparity per year for the selected group
##########################################

df['focus_prevalence'] = (
    df['focus_prevalence']
        .astype(str)
        .str.strip()
        .str.replace('%', '', regex=False)
)
df['focus_prevalence'] = pd.to_numeric(
    df['focus_prevalence'],
    errors='coerce'
)

#df['focus_prevalence'].dtype


df_age = df[df['demographic'] == "Age"]
df_plot = (
    df_age.groupby(['focus_group', 'year'], as_index=False)['focus_prevalence']
            .mean()
            .sort_values(['focus_group', 'year'])
)
#df_plot.head()
#df_plot.columns

import plotly.express as px

fig_1a=px.line(
    df_plot,
    x="year",
    y="focus_prevalence",
    color="focus_group",
    title="Average Cigarette Use Prevalence Over Time by Age Group",
    markers=True
)

fig_1a.update_layout(
    xaxis_title="Year",
    yaxis_title="Avg Cigarette Use Prevalence (%) ",
    template="plotly_white",
    title_x=0.5,
    legend_title="Age Group"
)

#fig_1a.show()
fig_1a.write_html("Plots/LinePlotAge.html")
#time.sleep(1) # Wait 1 second before continuing







##########################################
#Graph 1b:
#Line plot for cig use prevalence over time for income levels
#Aggregate mean disparity per year for the selected group
##########################################

df['focus_prevalence'] = (
    df['focus_prevalence']
        .astype(str)
        .str.strip()
        .str.replace('%', '', regex=False)
)
df['focus_prevalence'] = pd.to_numeric(
    df['focus_prevalence'],
    errors='coerce'
)

#df['focus_prevalence'].dtype

#
df['focus_group'] = (
    df['focus_group']
        .astype(str)
        .str.replace('$', '\\$', regex=False)
)

df_income = df[df['demographic'] == "Income"]
df_plot = (
    df_income.groupby(['focus_group', 'year'], as_index=False)['focus_prevalence']
            .mean()
            .sort_values(['focus_group', 'year'])
)
#df_plot.head()
#df_plot.columns


fig_1b=px.line(
    df_plot,
    x="year",
    y="focus_prevalence",
    color="focus_group",
    title="Average Cigarette Use Prevalence Over Time by Income Level",
    markers=True
)

fig_1b.update_layout(
    xaxis_title="Year",
    yaxis_title="Avg Cigarette Use Prevalence (%) ",
    template="plotly_white",
    title_x=0.5,
    legend_title="Income Level"
)

#fig_1b.show()
fig_1b.write_html("Plots/LinePlotIncome.html")
#time.sleep(1) # Wait 1 second before continuing







##########################################
#Graph 1c:
#Line plot for cig use prevalence over time for by mental health status
#Aggregate mean disparity per year for the selected group
##########################################

df_mh = df[df['demographic'] == "Mental Health"]
df_plot_mh = (
    df_mh.groupby(['focus_group', 'year'], as_index=False)['focus_prevalence']
            .mean()
            .sort_values(['focus_group', 'year'])
)
#df_plot.head()
#df_plot.columns

import plotly.express as px

fig_1c=px.line(
    df_plot_mh,
    x="year",
    y="focus_prevalence",
    color="focus_group",
    title="Average Cigarette Use Prevalence Over Time by Mental Health Status",
    markers=True
)

fig_1c.update_layout(
    xaxis_title="Year",
    yaxis_title="Avg Cigarette Use Prevalence (%) ",
    template="plotly_white",
    title_x=0.5,
    legend_title="Mental Health Status"
)

#fig_1c.show()
fig_1c.write_html("Plots/LinePlotMentalHealth.html")
#time.sleep(1) # Wait 1 second before continuing







##########################################
#Graph 1d:
#Line plot for cig use prevalence over time for by employment status
#Aggregate mean disparity per year for the selected group
##########################################

df_employ = df[df['demographic'] == "Employment"]
df_plot_employ = (
    df_employ.groupby(['focus_group', 'year'], as_index=False)['focus_prevalence']
            .mean()
            .sort_values(['focus_group', 'year'])
)
#df_plot.head()
#df_plot.columns

import plotly.express as px

fig_1d=px.line(
    df_plot_employ,
    x="year",
    y="focus_prevalence",
    color="focus_group",
    title="Average Cigarette Use Prevalence Over Time by Employment Status",
    markers=True
)

fig_1d.update_layout(
    xaxis_title="Year",
    yaxis_title="Avg Cigarette Use Prevalence (%) ",
    template="plotly_white",
    title_x=0.5,
    legend_title="Employment Status"
)

#fig_1d.show()
fig_1d.write_html("Plots/LinePlotEmployment.html")
#time.sleep(1) # Wait 1 second before continuing







##########################################
#Graph 1e:
#Line plot for cig use prevalence over time for by race/ethnicity
#Aggregate mean disparity per year for the selected group
##########################################

df_re = df[df['demographic'] == "Race and Ethnicity"]
df_plot_re = (
    df_re.groupby(['focus_group', 'year'], as_index=False)['focus_prevalence']
            .mean()
            .sort_values(['focus_group', 'year'])
)
#df_plot.head()
#df_plot.columns

import plotly.express as px

fig_1e=px.line(
    df_plot_re,
    x="year",
    y="focus_prevalence",
    color="focus_group",
    title="Average Cigarette Use Prevalence Over Time by Race and Ethnicity",
    markers=True
)

fig_1e.update_layout(
    xaxis_title="Year",
    yaxis_title="Avg Cigarette Use Prevalence (%) ",
    template="plotly_white",
    title_x=0.5,
    legend_title="Racial/Ethnic Group"
)

#fig_1e.show()
fig_1e.write_html("Plots/LinePlotRaceEthnicity.html")
#time.sleep(1) # Wait 1 second before continuing







##########################################
#Graph 2:
#Multi-box plot for smoking prevalence across ethnic groups
#
##########################################

# Filter for Race and Ethnicity
df_race = df_prevalence[df_prevalence['demographic'] == "Race and Ethnicity"]

# Select needed columns (no grouping!)
df_plot = df_race[['focus_group', 'year', 'focus_prevalence']]

# Create box plot
fig = px.box(
    df_plot,
    x="focus_group",
    y="focus_prevalence",
    #points="all",  # show each year's value as dots next to the box plot
    title="Distribution of Smoking Prevalence Across Years by Race/Ethnicity",
    color = 'focus_group',
)

fig.update_layout(
    xaxis_title="Race/Ethnicity Group",
    yaxis_title="Cigarette Use Prevalence (%)",
    template="plotly_white",
    title_x=0.5
)

fig.show()
#time.sleep(1) # Wait 1 second before continuing





##########################################
#Graph 3: Combined bar plot and disparity value
#
##########################################

# Take average disparity across focus groups and sort them
df_top_disparity = df.groupby(["demographic", "focus_group"], as_index=False)['disparity_value'].mean().sort_values(['disparity_value'],ascending=False)

#Show top 5 avg disparities
print(df_top_disparity.head(5))

# Get groups with 5 highest avg disparities as their own data:
df_top5 = df_top_disparity.head(5)

# Get groups with 5 lowest avg disparities as their own data:
#df_bottom5 = df_top_disparity.tail(5)


#Bar + Line Graph
import pandas as pd


# 1. Data Aggregation (Two Metrics in One Frame)

# Calculate the mean disparity and the mean prevalence for every demographic/focus group.
df_combined = df.groupby(["demographic", "focus_group"], as_index=False).agg(
    avg_disparity=('disparity_value', 'mean'),
    avg_prevalence=('focus_prevalence', 'mean')
)

# Sort by disparity and select the top 5 groups
df_top5_combined = df_combined.sort_values('avg_disparity', ascending=False).head(5).reset_index(drop=True)

# Create a combined label for the X-axis (e.g., "Income: Less than $20,000")
df_top5_combined['group_label'] = df_top5_combined['demographic'] + ": " + df_top5_combined['focus_group']


# Create the Plotly Figure with both axes

# Initialize a Plotly Subplot with a secondary Y-axis
fig_bar_line = make_subplots(specs=[[{"secondary_y": True}]])

# Add the Bar Trace (Average Disparity) - Primary Y-axis
fig_bar_line.add_trace(
    go.Bar(
        x=df_top5_combined['group_label'],
        y=df_top5_combined['avg_disparity'],
        name='Avg Disparity Value (Left Axis)',
        marker_color='mediumaquamarine'
    ),
    secondary_y=False,
)

# Add the Line Trace (Average Prevalence) - Secondary Y-axis
fig_bar_line.add_trace(
    go.Scatter(
        x=df_top5_combined['group_label'],
        y=df_top5_combined['avg_prevalence'],
        name='Avg Prevalence (%) (Right Axis)',
        mode='lines+markers',
        marker=dict(color='darkorange', size=10)
    ),
    secondary_y=True,
)

# Update Layout and Labels
fig_bar_line.update_layout(
    title_text="Top 5 Focus Groups by Disparity: Disparity vs. Prevalence",
    template='plotly_white',
    title_x=0.5,
    legend=dict(y=1.1, x=0.5, xanchor='center', orientation="h")
)

# Set X-axis title
fig_bar_line.update_xaxes(title_text="Demographic Category and Focus Group", tickangle=-15)

# Set Y-axis titles
fig_bar_line.update_yaxes(
    title_text="<b>Average Disparity Value</b>",
    secondary_y=False,
    range=[0, df_top5_combined['avg_disparity'].max() * 1.1] # Ensure bars fit
)

fig_bar_line.update_yaxes(
    title_text="<b>Average Prevalence (%)</b>",
    secondary_y=True,
    range=[0, df_top5_combined['avg_prevalence'].max() * 1.1], # Ensure line fits
    gridcolor='lightgray'
)




##########################################
#Graph 8:
#Scatter plot for focus prevalence vs disparity
#MAY BE A GOOD IDEA TO TURN INTO A FACET PLOT AND SPLIT BY GROUP
##########################################

# Drop rows where we don't have both prevalence + disparity
df_scatter = df.dropna(subset=["focus_prevalence", "disparity_value"]).copy()

fig8 = px.scatter(
    df_scatter,
    x="focus_prevalence",
    y="disparity_value",
    color="demographic",
    title="Relationship Between Smoking Prevalence and Disparity",
    opacity=0.6,
)

fig8.update_layout(
    xaxis_title="Focus-Group Smoking Prevalence (%)",
    yaxis_title="Disparity Value",
    template="plotly_white",
    title_x=0.5,
    legend_title="Demographic Type",
)

fig8.show()
print("The plot shows a general positive correlation. As the smoking prevalence in the focus group increases (moving right along the X-axis), the disparity value tends to increase (moving up along the Y-axis). Most points cluster in the lower prevalence (below 20%) and lower disparity (below 2) areas. Focus groups with higher smoking rates tend to exhibit a larger disparity relative to their reference groups.")







#######################################
#Graph 9:
#5x line plot showing average disparity over time for age, employment, and income
#
##########################################


demo_subset = ["Age", "Income", "Race and Ethnicity", "Mental Health", "Employment"]
df_demo = df[df["demographic"].isin(demo_subset)].copy()

df_demo_line = (
    df_demo.groupby(["demographic", "year"], as_index=False)["disparity_value"]
           .mean()
)

fig9 = px.line(
    df_demo_line,
    x="year",
    y="disparity_value",
    color="demographic",
    facet_col="demographic",
    facet_col_wrap=3,
    title="Average Smoking Disparity Over Time by Demographic Category",
)

fig9.update_layout(
    template="plotly_white",
    title_x=0.5,
)

fig9.for_each_xaxis(lambda ax: ax.update(title="Year"))
fig9.for_each_yaxis(lambda ax: ax.update(title="Avg Disparity"))

fig9.show()
print("Age Disparity: Decreased from around 1.25 in 2012 to a low point around 2016 before slightly increasing again .")
print("Employment Disparity: Shows a slight upward trend or general stability, fluctuating around 1.40-1.45 .")
print("The factors driving disparity (Age, Income, Race, Mental Health, Employment) have distinct trends. For instance, the age-related disparity has generally lessened, while the employment-related disparity appears to be stable or increasing slightly.")
