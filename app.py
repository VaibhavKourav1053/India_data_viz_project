import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
###################################################
### import dataset
df = pd.read_csv("India.csv")
### for selectbox list
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

###################################################
st.set_page_config(layout = "wide")
st .sidebar.title("India ka data Vizualization")

selected_state = st.sidebar.selectbox("select State",list_of_states)

primary = st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[5:]))


plot = st.sidebar.button("Plot Graph")
#######################################

############################################
# 2 cases # over all india # or # particular state
if plot:
    st.text("Size represent Primary Parameter")
    st.text("Color represents Secondary Parameter")
    if selected_state == 'Overall India' :
        ## plotting for india
        fig = px.scatter_map(df, lat="Latitude", lon="Longitude",
                             size = primary,
                             color= secondary,
                             size_max=35,
                             zoom=4,
                             map_style="carto-positron",
                             width=1000, height=600,
                             hover_name="District"
                             )
        # Display in Streamlit
        st.plotly_chart(fig, use_container_width=True)  # This makes the plot responsive

    else :
        ## plot for state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude",
                             size=primary,
                             color=secondary,
                             size_max=35,
                             zoom=5,
                             map_style="carto-positron",
                             width=1200, height=700,
                             hover_name="District"
                             )
        # Display in Streamlit
        st.plotly_chart(fig, use_container_width=True)  # This makes the plot responsive