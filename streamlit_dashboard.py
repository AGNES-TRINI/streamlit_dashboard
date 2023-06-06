import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
#import hydralit_components as hc
from streamlit_option_menu import option_menu


import toml
print (toml.load(r"C:\Users\agnes\dash_plotly\[theme].toml"))

st.set_page_config(page_title="AP DASHBOARD",
                   page_icon="favicon",
                   layout="wide"  
                   
)

st.markdown("<h1 style='text-align:center;'>AP DASHBOARD</h1>",unsafe_allow_html=True)
st.markdown("---")

with open(r"C:\Users\agnes\dash_plotly\style.css") as source_design:
    st.markdown(f"<style>{source_design.read()}</style>",unsafe_allow_html=True)

#import data

df_overall=pd.read_excel(r"C:\Users\agnes\Downloads\AP Dashboard (1).xlsx",sheet_name="Overall")

df_ae=pd.read_excel(r"C:\Users\agnes\Downloads\AP Dashboard (1).xlsx",sheet_name="AE")



#navigation bar for home,analysis,data summary
selected=option_menu(menu_title=None,
                     options=["Home","Analysis","Data summary"],
                     menu_icon="cast",
                     default_index=0,
                     orientation="horizontal",
                     styles={
                "container": {"padding": "0!important", "background-color": "#010101"},
                "icon": {"color": "#3669ED", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#474747",
                },
                "nav-link-selected": {"background-color": "#071B4F"},
            },
        )
        


# if selected=="Data summary":
# with st.expander("Show the Dataframe"):
#         st.table(df_overall.head(st.session_state['number_of_rows']))

#selectbox for district and ac name

dist = df_overall['District_Name'].unique()
dist_choice = st.selectbox('Select District',dist)
df_overall = df_overall[(df_overall["District_Name"] == dist_choice)]

AC = df_overall['AC_Name']
AC_choice = st.selectbox('Select AC',AC)
df_overall = df_overall[(df_overall["AC_Name"] == AC_choice)]


total_pop=int(df_overall["Total_Population"].sum())
male_pop=int(df_overall["Male"].sum())
female_pop=int(df_overall["Female"].sum())
total_rural=int(df_overall["Rural"].sum())
total_urban=int(df_overall["Urban"].sum())
total_hindu=int(df_overall["Hindu"].sum())
total_muslim=int(df_overall["Muslim"].sum())
total_other=int(df_overall["Other"].sum())

# st.markdown("---")

#total population,male,female


kpi1,kpi2,kpi3=st.columns(3)

kpi1.metric(label="Total Population",
           value=int(df_overall.Total_Population.values[0]),
           )
kpi2.metric(label="Male",
            value=int(df_overall.Male.values[0]))
kpi3.metric(label="Female",
            value=int(df_overall.Female.values[0]))

#rural and urban

kpi4,kpi5=st.columns(2)
kpi4.metric(label="Total rural",
           value=int(df_overall.Rural.values[0]),
           )
kpi5.metric(label="urban",
            value=int(df_overall.Urban.values[0]))

#hindu,muslim,others

kpi6,kpi7,kpi8=st.columns(3)
kpi6.metric(label="Hindu",
            value=int(df_overall.Hindu.values[0]))
kpi7.metric(label="Muslim",
            value=int(df_overall.Muslim.values[0]))
kpi8.metric(label="Other",
            value=int(df_overall.Other.values[0]))
#OC,BC,SC,ST

kpi9,kpi10,kpi11,kpi12=st.columns(4)
kpi9.metric(label="OC",
            value=int(df_overall.OC.values[0]))
kpi10.metric(label="BC",
            value=int(df_overall.BC.values[0]))
kpi11.metric(label="SC",
            value=int(df_overall.SC.values[0]))
kpi12.metric(label="ST",
            value=int(df_overall.ST.values[0]))

st.markdown("---")

# left_column,male_column,female_column,rural_column,urban_column,hindu_column,muslim_column,other_column=st.columns(8)
# with left_column:
#     st.success("Total Population")
#     st.success(f"{total_pop:,}")

# with male_column:
#     st.success("Male Population")
#     st.success(f"{male_pop:,}")

# with female_column:
#     st.success("Female Population")
#     st.success( f"{female_pop:,}" )

# with rural_column:
#     st.success("Rural Population")
#     st.success(f"{total_rural:,}")

# with urban_column:
#     st.success("Urban Population")
#     st.success(f"{total_urban:,}")

# with hindu_column:
#     st.success("Hindu Population")
#     st.success(f"{total_hindu:,}")

# with muslim_column:
#     st.success("Muslim Population")
#     st.success(f"{total_muslim:,}")

# with other_column:
#     st.success("Others Population")
#     st.success(f"{total_other:,}")
st.markdown("---")




if 'number_of_rows' not in st.session_state:
    st.session_state['number_of_rows']=5
    st.session_state['type']='Categorical'

df_overall=pd.read_excel(r"C:\Users\agnes\Downloads\AP Dashboard (1).xlsx",sheet_name="Overall")



with st.expander("Show the Dataframe"):

    st.table(df_overall.head(st.session_state['number_of_rows']))

st.markdown("---")

#by district name plot

total_by_district=(df_overall.groupby(by=['District_Name']).sum()[['Total_Population']].sort_values(by="Total_Population"))

fig_total_ac=px.bar(total_by_district,
                    x="Total_Population",
                    y=total_by_district.index,
                    orientation="h",
                    title="<b> Total by District <b>",
                    color_discrete_sequence=["#0083B8"] * len(total_by_district),
                    template="plotly_white",
                    )

fig_total_ac.update_layout(

    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_total_ac)




#ae data selectbox for year 

year = df_ae['Year'].unique()
year_choice = st.selectbox('Select year',year)
df_ae = df_ae[(df_ae["Year"] == year_choice)]

total_votes=int(df_ae["Total_Votes_Secured"].sum()) 
votes_polled=int(df_ae["Votes_polled_AC"].sum())
electors=int(df_ae["Electors_in_AC"].sum())
vote_share=int(df_ae["Vote_share"].mean())

kpi13,kpi14,kpi15=st.columns(3)

kpi13.metric(label="Total Votes",
           value=df_ae.Total_Votes_Secured.values[0],
           )
kpi14.metric(label="Votes Polled",
            value=df_ae.Votes_polled_AC.values[0])
kpi15.metric(label="Electors",
            value=df_ae.Electors_in_AC.values[0])






# column_1,column_2,column_3,column_4=st.columns(4)
# with column_1:
#     st.success("Total Votes")
#     st.success(f"{total_votes:,}")

# with column_2:
#     st.success("Votes Polled")
#     st.success(f"{votes_polled:,}")

# with column_3:
#     st.success("Electors")
#     st.success(f"{electors:,}")

# with column_4:
#     st.success("Vote Share")
#     st.success(f"{vote_share:.1%}")
st.markdown("---")

with st.expander("Show the Dataframe"):

    st.table(df_ae.head(st.session_state['number_of_rows']))

st.markdown("---")


types={'Categorical':['District_Name','AC_Name','AC_No'],'Numerical':['Total_Population','Male','Female']}
column =st.selectbox('Select a column',types[st.session_state['type']])

def handle_click(new_type):
    st.session_state.type=new_type

def handle_click_wo_button():
    if st.session_state.kind_of_column:
        st.session_state.type=st.session_state.kind_of_column

type_of_column=st.radio("what kind of analysis",['Categorical','Numerical'],on_change=handle_click_wo_button,key='kind_of_column')

# type_of_column=st.radio("what kind of analysis",['Categorical','Numerical'])
# change=st.button('Change',on_click=handle_click,args=[type_of_column])

#st.session_state['type']=st.radio("what kind of analysis",['Categorical','Numerical'])

if st.session_state['type']=='Categorical':
    distr=pd.DataFrame(df_overall[column].value_counts()).head(50)
    st.bar_chart(distr)
else:
    st.table(df_overall[column].describe())

st.markdown("---")


