# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:00:00 2020
@author: Nitesh Kumar Jain
"""
#importing the libraries
import pandas as pd
import webbrowser
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import plotly.graph_objects as go  
import plotly.express as px
from dash.exceptions import PreventUpdate

# Global variables
external_stylesheets = ['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def load_data():
  dataset_name = "global_terror.csv"

  global df, date_list, month_list, region_list, country_list, state_list, city_list, attack_type_list, year_list, year_dict
  df = pd.read_csv(dataset_name)
  
  #this line we use to hide some warnings which gives by pandas
  pd.options.mode.chained_assignment = None

  month = {
         "January":1,
         "February": 2,
         "March": 3,
         "April":4,
         "May":5,
         "June":6,
         "July": 7,
         "August":8,
         "September":9,
         "October":10,
         "November":11,
         "December":12
         }
  #Creating lists of data
  date_list = [x for x in range(1, 32)]
  month_list= [{"label":key, "value":values} for key,values in month.items()]
  region_list = [{"label": str(i), "value": str(i)}  for i in sorted( df['region_txt'].unique().tolist() ) ]  
  country_list = df.groupby("region_txt")["country_txt"].unique().apply(list).to_dict()
  state_list = df.groupby("country_txt")["provstate"].unique().apply(list).to_dict() 
  city_list  = df.groupby("provstate")["city"].unique().apply(list).to_dict()
  attack_type_list = [{"label": str(i), "value": str(i)}  for i in df['attacktype1_txt'].unique().tolist()]
  year_list = sorted ( df['iyear'].unique().tolist()  )
  year_dict = {str(year): str(year) for year in year_list}
  
  # Chart Variables
  global chart_dropdown_values, datas
  chart_dropdown_values = {"Terrorist Organisation":'gname', 
                             "Target Nationality":'natlty1_txt', 
                             "Target Type":'targtype1_txt', 
                             "Type of Attack":'attacktype1_txt', 
                             "Weapon Type":'weaptype1_txt', 
                             "Region":'region_txt',
                             "Country Attacked":'country_txt'
                          }
  chart_dropdown_values=[{'label':str(key),'value':str(value)} for key, value in chart_dropdown_values.items()]

def open_browser():
  # Open the default web browser
  webbrowser.open_new('http://127.0.0.1:8050/')


# Layout of your page
def create_app_ui():
  # Create the UI of the Webpage here
  main_layout = html.Div([
  html.H1(children='Terrorism Analysis with Insights', id='main_title', style={'textAlign':'center', 'background-color': '#0a61f7', 'color':'white'}), #Title to be shown in UI
  dcc.Tabs(id="Tabs", value="Map",children=[
      dcc.Tab(label="Map tool" ,id="Map tool",value="Map", children=[
          dcc.Tabs(id = "subtabs", value = "WorldMap",children = [
              dcc.Tab(label="World Map tool", id="World", value="WorldMap"),
              dcc.Tab(label="India Map tool", id="India", value="IndiaMap")
              ]),
                dcc.Dropdown(
                      id='region-dropdown', 
                      options=region_list,
                      placeholder='Select Region',
                      multi = True,
                      style = {'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}
                ),
                dcc.Dropdown(
                      id='country-dropdown', 
                      options=[{'label': 'All', 'value': 'All'}],
                      placeholder='Select Country',
                      multi = True,
                      style = {'width': '30vw', 'display': 'inline-block','margin-left':'10px', 'margin-right': '10px'}
                ),
                dcc.Dropdown(
                      id='state-dropdown', 
                      options=[{'label': 'All', 'value': 'All'}],
                      placeholder='Select State or Province',
                      multi = True,
                      style = {'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}
                ),
                dcc.Dropdown(
                      id='city-dropdown', 
                      options=[{'label': 'All', 'value': 'All'}],
                      placeholder='Select City',
                      multi = True,
                      style = {'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}
                ),
                dcc.Dropdown(
                      id='attacktype-dropdown', 
                      options=attack_type_list,
                      placeholder='Select Attack Type',
                      multi = True,
                      style = {'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}
                ),
                
                dcc.Dropdown(
                      id='month-dropdown', 
                      options=month_list,
                      placeholder='Select Month',
                      multi = True,
                      style = {'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}
                ),
                dcc.Dropdown(
                      id='date-dropdown', 
                      placeholder='Select Day',
                      multi = True,
                      style = {'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}
                ),
              
                html.H3('Select the Year', id='year_title'),
                dcc.RangeSlider(
                      id='year-slider',
                      min=min(year_list),
                      max=max(year_list),
                      value=[min(year_list),max(year_list)],
                      marks=year_dict,
                      step=None
                ),
          html.Br()
    ]),
      dcc.Tab(label = "Chart Tool", id="chart tool", value="Chart", children=[
          dcc.Tabs(id = "subtabs2", value = "WorldChart",children = [
              dcc.Tab(label="World Chart tool", id="WorldC", value="WorldChart"),
              dcc.Tab(label="India Chart tool", id="IndiaC", value="IndiaChart")
              ]),
                  html.Br(),
                  html.Hr(),
                  html.H3(children='Select Specific type to show Chart', style={'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}),
                  dcc.Dropdown(
                      id='chart_dropdown1', 
                      options=chart_dropdown_values,
                      value='region_txt',
                      style = {'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}
                ), 
                  html.Br(),
                  html.Hr(),
                  html.H3(children='Filter Search Results', id='filter_text', style={'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}),
                  dcc.Input(
                      id="search",
                      type="search",
                      placeholder="Search Filter",
                      style = {'width': '30vw', 'display': 'inline-block', 'margin-left':'10px', 'margin-right': '10px'}
                      ),
                  html.Hr(),
                  html.H3(children='Select Years', id='year_range_text'),
                  dcc.RangeSlider(
                    id='cyear_slider',
                    min=min(year_list),
                    max=max(year_list),
                    value=[min(year_list),max(year_list)],
                    marks=year_dict,
                    step=None
                      ),
                  html.Br()
              ]),
         ]),
  html.Div(id = "graph-object", children ="Graph will be shown here")
        ])
  return main_layout

# Callback of your page
@app.callback(
    Output('graph-object', 'children'),
    [
    Input('month-dropdown', 'value'),
    Input('date-dropdown', 'value'),
    Input('region-dropdown', 'value'),
    Input('country-dropdown', 'value'),
    Input('state-dropdown', 'value'),
    Input('city-dropdown', 'value'),
    Input('attacktype-dropdown', 'value'),
    Input('year-slider', 'value'),
    Input("Tabs", "value"),
    Input("search", "value"),
    Input("chart_dropdown1", "value"),
    Input("subtabs2", "value"),
    Input("cyear_slider", "value")
    ]
    )

def update_app_ui(month_value, date_value, region_value, country_value, state_value, city_value, attack_value, year_value, tab, search, chart_dp_value, subtabs2, chart_year_selector):
    fig = None

    # year_filter
    year_range = range(year_value[0], year_value[1]+1)
    new_df = df[df["iyear"].isin(year_range)]
    if tab == "Map":
    # month_filter
        if month_value==[] or month_value is None:
            pass
        else:
            if date_value==[] or date_value is None:
                new_df = new_df[new_df["imonth"].isin(month_value)]
            else:
                new_df = new_df[new_df["imonth"].isin(month_value)
                                & (new_df["iday"].isin(date_value))]
                  
        # region, country, state, city filter
        if region_value==[] or region_value is None:
            pass
        else:
            if country_value==[] or country_value is None :
                new_df = new_df[new_df["region_txt"].isin(region_value)]
            else:
                if state_value == [] or state_value is None:
                    new_df = new_df[(new_df["region_txt"].isin(region_value))&
                                    (new_df["country_txt"].isin(country_value))]
                else:
                    if city_value == [] or city_value is None:
                        new_df = new_df[(new_df["region_txt"].isin(region_value))&
                                    (new_df["country_txt"].isin(country_value)) &
                                    (new_df["provstate"].isin(state_value))]
                    else:
                        new_df = new_df[(new_df["region_txt"].isin(region_value))&
                                        (new_df["country_txt"].isin(country_value)) &
                                        (new_df["provstate"].isin(state_value))&
                                        (new_df["city"].isin(city_value))]
        
        if attack_value == [] or attack_value is None:
            pass
        else:
            new_df = new_df[new_df["attacktype1_txt"].isin(attack_value)]
    
        # You should always set the figure for blank, since this callback 
        # is called once when it is drawing for first time        
        figure = go.Figure()
        if new_df.shape[0]:
            pass
        else: 
            new_df = pd.DataFrame(columns = ['iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'provstate',
           'city', 'latitude', 'longitude', 'attacktype1_txt', 'nkill'])
            
            new_df.loc[0] = [0, 0 ,0, None, None, None, None, None, None, None, None]
    
        
        figure = px.scatter_mapbox(new_df,
                      lat="latitude", 
                      lon="longitude",
                      color="attacktype1_txt",
                      hover_name="city", 
                      hover_data=["region_txt", "country_txt", "provstate","city", "attacktype1_txt","nkill","iyear","imonth", "iday"],
                      zoom=1
                      )                       
        figure.update_layout(mapbox_style="open-street-map",
                  autosize=True,
                  margin=dict(l=0, r=0, t=25, b=20),
                  )
        fig = figure
  
    elif tab == "Chart":
        fig = None
        chart_df = None
        year_range_c = range(chart_year_selector[0], chart_year_selector[1]+1)
        chart_df = df[df["iyear"].isin(year_range_c)]
        if subtabs2 == "WorldChart":
            if chart_dp_value is not None:
                if search is not None: 
                    chart_df = chart_df.groupby("iyear")[chart_dp_value].value_counts().reset_index(name = "count")
                    chart_df  = chart_df[chart_df[chart_dp_value].str.contains(search, case = False)]
                else:
                    chart_df = chart_df.groupby("iyear")[chart_dp_value].value_counts().reset_index(name="count")
            else:
                raise PreventUpdate
                
        elif subtabs2 == "IndiaChart":
             if chart_dp_value is not None:
                chart_df = chart_df[(chart_df["region_txt"]=="South Asia") & (chart_df["country_txt"]=="India")]
                if search is not None:
                    chart_df = chart_df.groupby("iyear")[chart_dp_value].value_counts().reset_index(name="count")
                    chart_df  = chart_df[chart_df[chart_dp_value].str.contains(search, case = False)]
                else:
                    chart_df = chart_df.groupby("iyear")[chart_dp_value].value_counts().reset_index(name="count")
             else:
                raise PreventUpdate
                
        if chart_df.shape[0]:
                pass
        else: 
                chart_df = pd.DataFrame(columns = ['iyear', 'count', chart_dp_value])
                  
                chart_df.loc[0] = [0, 0,"No data"]
        fig = px.area(chart_df, x= "iyear", y ="count", color = chart_dp_value)
        
            
    return dcc.Graph(figure = fig)

@app.callback([Output("region-dropdown", "value"),
               Output("region-dropdown", "disabled"),
               Output("country-dropdown", "value"),
               Output("country-dropdown", "disabled")],
              [Input("subtabs", "value")])
def update_r(tab):
    region = None
    disabled_r = False
    country = None
    disabled_c = False
    if tab == "WorldMap":
        pass
    elif tab=="IndiaMap":
        region = ["South Asia"]
        disabled_r = True
        country = ["India"]
        disabled_c = True
    return region, disabled_r, country, disabled_c

@app.callback(
    Output('country-dropdown', 'options'),
    [Input('region-dropdown', 'value')])
def set_country_options(region_value):
    option = []
    # Making the country Dropdown data
    if region_value is  None:
        raise PreventUpdate()
    else:
        for var in region_value:
            if var in country_list.keys():
                option.extend(country_list[var])
    return [{'label':m , 'value':m} for m in option]

@app.callback(
    Output('state-dropdown', 'options'),
    [Input('country-dropdown', 'value')])
def set_state_options(country_value):
  # Making the state Dropdown data
    option = []
    if country_value is None :
        raise PreventUpdate()
    else:
        for var in country_value:
            if var in state_list.keys():
                option.extend(state_list[var])
    return [{'label':m , 'value':m} for m in option]


@app.callback(
    Output('city-dropdown', 'options'),
    [Input('state-dropdown', 'value')])
def set_city_options(state_value):
  # Making the city Dropdown data
    option = []
    if state_value is None:
        raise PreventUpdate()
    else:
        for var in state_value:
            if var in city_list.keys():
                option.extend(city_list[var])
    return [{'label':m , 'value':m} for m in option]

@app.callback(
    Output("date-dropdown", "options"),
    [Input("month-dropdown", "value")])
def update_date(month_value):
    options = []
    if month_value:
        options = [{"label":m, "value":m} for m in date_list]
    return options

# Flow of your Project
def main():
  load_data()
  open_browser()
  global app, df
  app.layout = create_app_ui()
  app.title = "Terrorism Analysis with Insights"
  # go to https://www.favicon.cc/ and download the ico file and store in assets directory 
  #from waitress import serve
  #serve(app, host="0.0.0.0", port=5003)
  app.run_server("0.0.0.0", 5003) # debug=True
  print("Closing...")
  
  # Deallocation of memory
  df = None
  app = None

if __name__ == '__main__':
    main()
