import streamlit as st
import pandas as pd
import plotly.express as px
table=pd.DataFrame({"column1":[1,2,3,4,5,6,7],"column2":[22,45,90,78,85,78,100]})
st.title("Hi streamlit is powerful for web application")
st.write(table)
st.text("streamlit is used by datascientist to visualize output for datascience.")

## add vistualization to streamlit
heatmap_fig=px.imshow(table.values,x=table.columns,y=table.index,color_continuous_scale="viridis")
st.plotly_chart(heatmap_fig,use_consider_width=True)

#pie chart
pie_chart_fig=px.pie(table,values="column2",names="column1",title="pie chart")
st.plotly_chart(pie_chart_fig,use_container_width=True)

## bar plot 
bar_plot_fig=px.bar(table,x="column1",y="column2",title="bar plot")
st.plotly_chart(bar_plot_fig,use_container_width=True)

## Treemap
treemap_data=pd.DataFrame({
    "category":["Bola","Ahmad","take","shola","adamu","grace","blessing"],
    "subcategory":["biologist","engineer","full stact","medical doctor","nurse","datascience","app developer"],
    "value":[10,20,30,40,50,60,70]})
treemap_fig=px.treemap(treemap_data,path=["category","subcategory"],values="value") 
st.plotly_chart(treemap_fig,use_container_width=True)                        

# map
choropleth_data=pd.DataFrame({
    "country":["Nigeria","ghana","togo","benin","senegal","cameroon","nigeria"],
    "value":[10,20,30,40,50,60,70]})
st.title("Choropleth map for country") 
st.write(choropleth_data)  
st.text("Choropleth maps vistualize geographical data.")
choropleth_fig=px.choropleth(choropleth_data,locations="country",locationmode="country names",color="value",  
                            title="Choropleth map",color_continuous_scale="deep")
st.plotly_chart(choropleth_fig,use_contianer_width=True)