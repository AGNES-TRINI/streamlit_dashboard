import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
from streamlit_option_menu import option_menu
import annotated_text as ant
from annotated_text import annotation
import altair as alt


# import toml
# print (toml.load(r"C:\Users\agnes\dash_plotly\[theme].toml"))

st.set_page_config(page_title="AP DASHBOARD",
                   page_icon="favicon",
                   layout="wide"  
                   
)


# st.markdown("---")

with open("style.css") as source_design:
    st.markdown(f"<style>{source_design.read()}</style>",unsafe_allow_html=True)

#import data

df_overall=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="Overall")

df_ae=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="AE")

df_ge=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="GE")

df_caste=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="caste")

df_elector=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="Elector")


with st.sidebar:
    choose = option_menu("Main Menu", ["Main Page","Visualization", "Data Summary"],
                         icons=['file-slides','app-indicator','person lines fill'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#969696"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#4070ee"},
        "nav-link-selected": {"background-color": "#071B4F"},
    }
    )

if choose=="Main Page":
    st.markdown("<h1 style='text-align:center;'>AP DASHBOARD</h1>",unsafe_allow_html=True)
    total_ac=int(df_overall["AC_Name"].count())
    total_dist=int(df_overall["District_Name"].count())
    total_Mandals=int(df_overall["Mandals"].sum())
    total_gp=int(df_overall["Gram_Panchayats"].sum())
    total_vil=int(df_overall["Villages"].sum())
    total_pop=int(df_caste["Population"].sum())
    column1,column2,column3,column4,column5,column6=st.columns(6)
    with column1:
         st.success("Total AC")
         st.success(f"{total_ac:,}")
         
    with column2:
         st.success("Total Districts")
         st.success(f"{26}")
    with column3:
         st.success("Total Mandals")
         st.success(f"{total_Mandals:,}")
    with column4:
         st.success("Total Panchayats ")
         st.success(f"{total_gp:,}")
    with column5:
         st.success("Total Villages")
         st.success(f"{total_vil:,}")
    with column6:
         st.success("Total Population")
         st.success(f"{total_pop:,}")

    ant.annotated_text(
    annotation("Overall Data", border='3px groove yellow'))

    dist = df_overall['District_Name'].unique()
    dist_choice = st.selectbox('Select District',dist)
    df_overall = df_overall[(df_overall["District_Name"] == dist_choice)]

    AC = df_overall['AC_Name']
    AC_choice = st.selectbox('Select AC',AC)
    df_overall = df_overall[(df_overall["AC_Name"] == AC_choice)]
    kpi1,kpi2,kpi3=st.columns(3)
    with kpi1:
         st.metric(label="Total Population",
           value=int(df_overall.Total_Population.values[0]),)
    with kpi2:
         st.metric(label="Male",
            value=int(df_overall.Male.values[0]))
    with kpi3:
         st.metric(label="Female",
            value=int(df_overall.Female.values[0]))
    kpi4,kpi5=st.columns(2)
    with kpi4:
        st.metric(label="Total rural",
           value=int(df_overall.Rural.values[0]),)
    with kpi5:
        st.metric(label="urban",
            value=int(df_overall.Urban.values[0]))
    kpi6,kpi7,kpi8=st.columns(3)
    with kpi6:
        st.metric(label="Hindu",
            value=int(df_overall.Hindu.values[0]))
    with kpi7:
        st.metric(label="Muslim",
            value=int(df_overall.Muslim.values[0]))
    with kpi8:
        st.metric(label="Other",
            value=int(df_overall.Other.values[0]))  
    kpi9,kpi10,kpi11,kpi12=st.columns(4)  
    with kpi9:
        st.metric(label="OC",
            value=int(df_overall.OC.values[0]))
    with kpi10:
        st.metric(label="BC",
            value=int(df_overall.BC.values[0]))
    with kpi11:
        st.metric(label="SC",
            value=int(df_overall.SC.values[0]))
    with kpi12:
        st.metric(label="ST",
            value=int(df_overall.ST.values[0]))
        st.markdown("---") 
     
    ant.annotated_text(
    annotation("AE Data", border='3px groove yellow'))

    year = df_ae['Year'].unique()
    year_choice = st.selectbox('Select year',year)
    df_ae = df_ae[(df_ae["Year"] == year_choice)]
    total_votes=int(df_ae["Total_Votes_Secured"].sum()) 
    votes_polled=int(df_ae["Votes_polled_AC"].sum())
    electors=int(df_ae["Electors_in_AC"].sum())
    vote_share=int(df_ae["Vote_share"].mean())

    kpi13,kpi14,kpi15=st.columns(3)
    with kpi13:
        st.metric(label="Total Votes",
           value=df_ae.Total_Votes_Secured.values[0],)
    with kpi14:
        st.metric(label="Votes Polled",
            value=df_ae.Votes_polled_AC.values[0])
    with kpi15:
        st.metric(label="Electors",
            value=df_ae.Electors_in_AC.values[0])
    #GE data
    ant.annotated_text(
    annotation("GE Data", border='3px groove yellow'))

    year_ge = df_ge['Year'].unique()
    year_choice_ge = st.selectbox('Select year as',year_ge)
    df_ge = df_ge[(df_ge["Year"] == year_choice_ge)]

    total_votes_ge=int(df_ge["Total_Votes_Secured"].sum()) 
    votes_polled_ge=int(df_ge["Votes_polled_AC"].sum())
    electors_ge=int(df_ge["Electors_in_AC"].sum())
    vote_share_ge=int(df_ge["Vote_share"].mean())

    kpi16,kpi17,kpi18=st.columns(3)
    with kpi16:
        st.metric(label="Total Votes",
           value=df_ge.Total_Votes_Secured.values[0],)
    with kpi17:
        st.metric(label="Votes Polled",
            value=df_ge.Votes_polled_AC.values[0])
    with kpi18:
        st.metric(label="Electors",
            value=df_ge.Electors_in_AC.values[0])
    ant.annotated_text(
    annotation("Caste Data", border='3px groove yellow'))

    caste = df_caste['Caste'].unique()
    caste_choice = st.selectbox('Select caste',caste)
    df_caste_1 = df_caste[(df_caste["Caste"] == caste_choice)]

    total_caste=int(df_caste_1["Population"].sum())
    tot_popu=int(df_caste["Population"].sum())
    kpi19,kpi20=st.columns(2)
    with kpi19:
        st.metric(label="caste wise population",value=total_caste)
    with kpi20:
        st.metric(label="Total Population", value=tot_popu)

if choose =="Visualization":
    st.markdown("<h1 style='text-align:center;'>Visualizations</h1>",unsafe_allow_html=True)
#     if 'number_of_rows' not in st.session_state:
#          st.session_state['number_of_rows']=5
#          st.session_state['type']='Categorical'
   
#     df_ae=pd.read_excel(r"C:\Users\agnes\Downloads\AP Dashboard (1).xlsx",sheet_name="AE")
#     types={'Categorical':['AC_Name','Party'],'Numerical':['Total_Votes_Secured']}
#     column =st.selectbox('Select a column',types[st.session_state['type']])
#     def handle_click(new_type):
#        st.session_state.type=new_type
#     # def handle_click_wo_button():
#     #   if st.session_state.kind_of_column:
#     #     st.session_state.type=st.session_state.kind_of_column
#     #     type_of_column=st.radio("what kind of analysis",['Categorical','Numerical'],on_change=handle_click_wo_button,key='kind_of_column')
#     #     type_of_column=st.radio("what kind of analysis",['Categorical','Numerical'])
#     #     change=st.button('Change',on_click=handle_click,args=[type_of_column])
#     #     st.session_state['type']=st.radio("what kind of analysis",['Categorical','Numerical'])
#     #     return handle_click()
#        if st.session_state['type']=='Categorical':
#            distr=pd.DataFrame(df_ae[column].value_counts()).head(50)
#            st.bar_chart(distr)
    
# if __name__ =="__main__":
#     handle_click()
    years_1 = df_ae['Year'].unique()
    selected_year_1 = st.selectbox("Select Year for", years_1)
    filtered_df = df_ae[df_ae['Year'] == selected_year_1]

# data_container = st.container()
    filtered_df=filtered_df.drop_duplicates(subset=['Electors_in_AC'])
    sum=filtered_df['Electors_in_AC'].sum()
    df3=filtered_df.groupby('Party')['Total_Votes_Secured'].sum().reset_index(name="Count")
    df3['vote_share'] = (df3['Count']/sum)*100
    df4=df3.sort_values(by="vote_share",ascending=False).head(5)
    df5=df4.drop(['Count'], axis=1)
    st.bar_chart(df5, x="Party", y="vote_share")

    # seats_won=filtered_df.groupby('Party')['Rank'].count().reset_index(name="seats_won")
    # st.bar_chart(data=seats_won,x='Party', y='seats_won', width=0, height=0, use_container_width=True)
    # with data_container:
#     table, plot = st.columns(2)
# with table:
#     st.markdown("vote_share")
#     st.write(df5)

# with plot:
#      chart = (alt.Chart(df5).mark_bar().encode(alt.X("Party"),alt.Y("vote_share"),alt.Color("Party"),alt.Tooltip(["Party", "vote_share"]),).interactive())
#      st.altair_chart(chart)
    ant.annotated_text(
    # annotation("GeeksforGeeks", color='#f5f6fa'),
    annotation("Gender wise votes", border='3px groove yellow'))
    male_sum = df_elector['Male'].sum()
    female_sum = df_elector['Female'].sum()
    other_sum= df_elector['Other'].sum()
    total_sum = male_sum + female_sum+other_sum

    male_percentage = (male_sum / total_sum) * 100
    female_percentage = (female_sum / total_sum) * 100
    other_percentage = (other_sum / total_sum) * 100
    # Create a bar plot
    labels = ['Male', 'Female','Other']
    values = [male_sum, female_sum,other_sum]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title='Gender wise votes')
    st.plotly_chart(fig)
    
    years = df_ae['Year'].unique()
    selected_year = st.selectbox("Select Year", years)
    filtered_df = df_ae[df_ae['Year'] == selected_year]

    fig = go.Figure(data=[go.Bar(x=filtered_df['Party'], y=filtered_df['Total_Votes_Secured'])])
    fig.update_layout(title=f'Party Votes for Year: {selected_year}')
    st.plotly_chart(fig)
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


# st.bar_chart(df_ae, x="Party", y="Total_Votes_Secured")
    st.markdown("---")
    st.bar_chart(df_caste, x="Caste", y="Population")

if choose =="Data Summary":
  
  st.markdown("<h1 style='text-align:center;'>Data Summary</h1>",unsafe_allow_html=True)
  selected_database = st.selectbox("Select a Database", ["Overall Data","Assembly Data" ,"General Data","Caste Data", "Electoral Data"])
  if selected_database:
    # Load data based on the selected database
    if selected_database == "Overall Data":
        data=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="Overall")
    elif selected_database == "Assembly Data":
        data=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="AE")
    elif selected_database == "General Data":
        data=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="GE")
    elif selected_database == "Caste Data":
        data=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="caste")
    elif selected_database == "Electoral Data":
        data=pd.read_excel("AP Dashboard (1).xlsx",sheet_name="Elector")

    st.write(data)
    st.write("Summary Statistics:", data.describe())

   


# ant.annotated_text(
    
#     annotation("Overall Data", border='3px groove yellow')
    
# )

#OC,BC,SC,ST





# with st.expander("Show the Dataframe"):

#     st.table(df_overall.head(st.session_state['number_of_rows']))

# st.markdown("---")




#ae data selectbox for year 

#Caste data

# with st.expander("Show the Dataframe"):

#     st.table(df_ae.head(st.session_state['number_of_rows']))

# st.markdown("---")




# st.markdown("---")


