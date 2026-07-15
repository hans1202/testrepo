# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown',
                                    options=[
                                        {'label': 'All Sites', 'value': 'ALL'},
                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                        {'label': 'CCAFS SLC-40', 'value': 'KSC LC-39A'},
                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                    ],
                                    value='ALL',
                                    placeholder="place holder here",
                                    searchable=True
                                ),

                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider',
                                    min=0, 
                                    max=10000, 
                                    step=1000,
                                    marks={
                                        0: '0', 
                                        2500: '2500', 
                                        5000: '5000', 
                                        7500: '7500', 
                                        10000: '10000'
                                    },                    # 2. 修正刻度，讓它符合 0 到 10000 的範圍
                                    value=[0, 10000]      # 3. 直接給定預設初始範圍（包含最大與最小）
                                ),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        all_success_df = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(all_success_df, values='class', 
        names='Launch Site', 
        title='Total Success Launches By All Sites')
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        
        # 2. 計算該發射場中 0 (失敗) 與 1 (成功) 的數量
        # 我們可以使用 values='class' 的 count（或是直接讓 Plotly 幫我們計算 class 的分布）
        df_site = filtered_df.groupby(['class']).size().reset_index(name='class count')
        
        # 3. 繪製圓餅圖
        fig = px.pie(
            df_site, 
            values='class count', 
            names='class', 
            title=f'Total Success Launches for site {entered_site}'
        )
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
# ==============================================================================
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs,
# `success-payload-scatter-chart` as output
# ==============================================================================
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value') # 接收拉桿的 [最小值, 最大值] 陣列
    ]
)
def get_scatter_chart(entered_site, payload_range):
    # 1. 先根據滑動拉桿選擇的 [低限, 高限] 來過濾載荷範圍
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]
    
    # 2. 判斷使用者選擇的是「所有發射場」還是「特定發射場」
    if entered_site == 'ALL':
        # 繪製所有發射場符合該載荷範圍的散點圖
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category', # 以火箭子型號區分顏色
            title='Correlation between Payload and Success for all Sites'
        )
        return fig
    else:
        # 額外過濾出使用者指定的發射場數據
        site_filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        
        # 繪製特定發射場的散點圖
        fig = px.scatter(
            site_filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category', # 同樣以火箭子型號區分顏色
            title=f'Correlation between Payload and Success for site {entered_site}'
        )
        return fig

# Run the app
if __name__ == '__main__':
    app.run()
