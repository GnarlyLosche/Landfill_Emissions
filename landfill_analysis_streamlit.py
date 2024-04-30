import streamlit as st
import pandas as pd
import base64

# Set page to wide mode
st.set_page_config(layout="wide")

def main():
    # Title of the application
    st.title('Landfill Methane Emission Analysis Dashboard')

    # Visualizing the top 10 methane emitting landfills image
    st.header('Top 10 Methane Emitting Landfills')
    st.image('top_10_Methane_emitting_landfills.png', use_column_width=True)

    # Displaying high emitters CSV
    st.header('Top 15 High Methane Emitting Landfills')
    high_emitters = pd.read_csv('high_emitters.csv')
    st.dataframe(high_emitters.head(15))

    # Displaying top operators by emissions CSV
    st.header('Top 10 Operators by Total Methane Emissions')
    top_operators_by_emissions = pd.read_csv('top_operators_by_emissions.csv')
    st.dataframe(top_operators_by_emissions.head(10))

    # Visualizing LFG collection efficiency
    st.header('Landfill Gas Collection Efficiency')
    st.image('lfg_collection_efficiency.png', use_column_width=True)

    # Visualizing top states by methane emissions
    st.header('Top States by Methane Emissions from Landfills')
    st.image('top_states_by_methane_emissions.png', use_column_width=True)

    # Displaying methane emissions heatmap
    st.header('Methane Emissions Heatmap')
    HtmlFile = open('methane_emissions_heatmap.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    st.components.v1.html(source_code, height=600)

    # Displaying collection efficiency map
    st.header('Collection Efficiency Map')
    HtmlFile = open('collection_efficiency_map.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    st.components.v1.html(source_code, height=600)

    # Displaying sunburst for largest emitters
    st.header('Sunburst Chart of Largest Emitters by Operator')
    HtmlFile = open('operators_Landfills_largest_emitters_sunburst_image.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    st.components.v1.html(source_code, height=600)

    # Displaying sunburst for most inefficient landfills
    st.header('Sunburst Chart of Most Inefficient Landfills by Operator')
    HtmlFile = open('operators_Landfills_inefficient_sunburst_image.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    st.components.v1.html(source_code, height=600)

    # Displaying timeline of landfill openings and closures
    st.header('Timeline of Landfill Openings and Closures')
    HtmlFile = open('open_close_timeline_image.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    st.components.v1.html(source_code, height=600)

if __name__ == "__main__":
    main()
