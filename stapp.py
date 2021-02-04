# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 00:05:46 2021

@author: pratap

"""

import streamlit as st
import pandas as pd
import sweetviz as sv
from pandas_profiling import ProfileReport
import streamlit.components.v1 as stc
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
import warnings
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot

warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)


def main():
    
    st.sidebar.info("Click on the X to Hide the Side bar")
    
    menu=['Home', "Pandas Profiling", 'Sweetviz','Graphs','About']
    
    #st.title("Simple EDA APP with Streamlit")
    
    choice= st.sidebar.selectbox("Menu",menu)
    
    st.sidebar.info("Please refresh the page when uploading New Dataset")
    st.sidebar.markdown(' Created by  **_Prathap_**. :sunglasses:')
    
    
    if choice=="Pandas Profiling":
        
        st.markdown("""
                    <style>
                   body {
                         color: #034F84;
                  background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
        
        st.subheader("EDA Using Pandas Profiling")
        
        data_file = st.file_uploader("Upload CSV File",type='CSV')
        
        if data_file is not None:
            df=pd.read_csv(data_file)
            st.subheader(" Head of Youre Dataset")
            st.write(df.head())
            profile=ProfileReport(df)
            if st.button(" Click Here To Generate The Detailed Report"):
                st.info("Please wait it may take some time if dataset is large")
         
                st.subheader("Scroll Down To See The Full Report")
                st_profile_report(profile)
                
            
            
      
    elif choice=='Sweetviz':
        
        st.markdown("""
                  <style>
                   body {
                     color: #034F84;
                     background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
                  
        st.subheader('EDA Using Sweetviz')
         
        data_file = st.file_uploader("Upload CSV File",type='CSV')
        
        if data_file is not None:
            df=pd.read_csv(data_file)
            st.subheader(" Head of Youre Dataset")
            st.write(df.head())
            report=sv.analyze(df)
            if st.button(" Click Here to Generate the Sweetviz Report"):
                st.info("Please wait it may take some time if dataset is large")
                report.show_html('sweet_report.html')
         
    elif   choice=="Graphs":
        st.subheader('Plotting Graphs')
        
        st.markdown("""
                    <style>
                   body {
                         color: #034F84;
                  background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
        
        
    
        data_file = st.file_uploader("Upload CSV File",type='csv')
        
        if data_file is not None:
            
            df=pd.read_csv(data_file)
            st.subheader(" Head of Youre Dataset")
            st.write(df.head())
            if st.button(' Click Here to Generate Pair Plot'):
               st.info("Please wait it may take some time if dataset is large")
               graph=sns.pairplot(df)
               sns.set(rc={'figure.figsize':(11.7,8.27)})
               st.pyplot(graph)
              
    elif choice=='About':
        
        st.markdown("""
                  <style>
                   body {
                     color: #034F84;
                     background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
        st.subheader('About Section')
        st.write("Hello. Prathap Here, a Motivated data scientist with 3+ years of experience as a Data Analyst. Passionate about building models that fix problems. Relevant skills include Machine learning, Deep learning, Computer vision, problem solving, programming, and creative thinking")
        st.write("Connect me through @ [LinkedIn](https://www.linkedin.com/in/pratap-reddy-2794b91b7/)")
        st.write("Check out The Code @ [Github](https://github.com/Pratap517)")
        st.subheader("Check out my Other tiny Projects below ")
        st.write(" Handy tool to Analyze Csv Files [Click Here](https://share.streamlit.io/pratap517/streamlitapp_dataanalysis/main/main_app.py)")
        st.write(" Simple loan Prediction App [Click Here](https://share.streamlit.io/pratap517/ml_deploy_using_streamlit/main/app.py)")
        st.write(" Simple Mask Detection App [Click Here](https://mask-detection-5a800.firebaseapp.com/)")
   
    else:
        st.subheader("Home")
        #stc.html("<p style = 'color: red;'>This is An Awesome App</p>")
        
        
        html_temp = """
		<div style="background-color:#F3F3F3;padding:10px;border-radius:10px">
		<h1 style="color:#85144b;text-align:center;">Simple EDA App with Python Streamlit</h1>
		</div>
		"""
        stc.html(html_temp)
        st.markdown("""
                  <style>
                   body {
                     color: #034F84;
                     background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
                  
        st.subheader("Please Select the Type of Report in the Side bar")
        
        stc.html("""
			<style>
			* {box-sizing: border-box}
			body {font-family: Verdana, sans-serif; margin:0}
			.mySlides {display: none}
			img {vertical-align: middle;}
			/* Slideshow container */
			.slideshow-container {
			  max-width: 1000px;
			  position: relative;
			  margin: auto;
			}
			/* Next & previous buttons */
			.prev, .next {
			  cursor: pointer;
			  position: absolute;
			  top: 50%;
			  width: auto;
			  padding: 16px;
			  margin-top: -22px;
			  color: white;
			  font-weight: bold;
			  font-size: 18px;
			  transition: 0.6s ease;
			  border-radius: 0 3px 3px 0;
			  user-select: none;
			}
			/* Position the "next button" to the right */
			.next {
			  right: 0;
			  border-radius: 3px 0 0 3px;
			}
			/* On hover, add a black background color with a little bit see-through */
			.prev:hover, .next:hover {
			  background-color: rgba(0,0,0,0.8);
			}
			/* Caption text */
			.text {
			  color: #f2f2f2;
			  font-size: 15px;
			  padding: 8px 12px;
			  position: absolute;
			  bottom: 8px;
			  width: 100%;
			  text-align: center;
			}
			/* Number text (1/3 etc) */
			.numbertext {
			  color: #f2f2f2;
			  font-size: 12px;
			  padding: 8px 12px;
			  position: absolute;
			  top: 0;
			}
			/* The dots/bullets/indicators */
			.dot {
			  cursor: pointer;
			  height: 15px;
			  width: 15px;
			  margin: 0 2px;
			  background-color: #bbb;
			  border-radius: 50%;
			  display: inline-block;
			  transition: background-color 0.6s ease;
			}
			.active, .dot:hover {
			  background-color: #717171;
			}
			/* Fading animation */
			.fade {
			  -webkit-animation-name: fade;
			  -webkit-animation-duration: 1.5s;
			  animation-name: fade;
			  animation-duration: 1.5s;
			}
			@-webkit-keyframes fade {
			  from {opacity: .4} 
			  to {opacity: 1}
			}
			@keyframes fade {
			  from {opacity: .4} 
			  to {opacity: 1}
			}
			/* On smaller screens, decrease text size */
			@media only screen and (max-width: 300px) {
			  .prev, .next,.text {font-size: 11px}
			}
			</style>
			</head>
			<body>
			<div class="slideshow-container">
			<div class="mySlides fade">
			  <div class="numbertext">1 / 3</div>
			  <img src="https://www.w3schools.com/howto/img_nature_wide.jpg" style="width:100%">
			  <div class="text">Caption Text</div>
			</div>
			<div class="mySlides fade">
			  <div class="numbertext">2 / 3</div>
			  <img src="https://www.w3schools.com/howto/img_snow_wide.jpg" style="width:100%">
			  <div class="text">Caption Two</div>
			</div>
			<div class="mySlides fade">
			  <div class="numbertext">3 / 3</div>
			  <img src="https://www.w3schools.com/howto/img_mountains_wide.jpg" style="width:100%">
			  <div class="text">Caption Three</div>
			</div>
			<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
			<a class="next" onclick="plusSlides(1)">&#10095;</a>
			</div>
			<br>
			<div style="text-align:center">
			  <span class="dot" onclick="currentSlide(1)"></span> 
			  <span class="dot" onclick="currentSlide(2)"></span> 
			  <span class="dot" onclick="currentSlide(3)"></span> 
			</div>
			<script>
			var slideIndex = 1;
			showSlides(slideIndex);
			function plusSlides(n) {
			  showSlides(slideIndex += n);
			}
			function currentSlide(n) {
			  showSlides(slideIndex = n);
			}
			function showSlides(n) {
			  var i;
			  var slides = document.getElementsByClassName("mySlides");
			  var dots = document.getElementsByClassName("dot");
			  if (n > slides.length) {slideIndex = 1}    
			  if (n < 1) {slideIndex = slides.length}
			  for (i = 0; i < slides.length; i++) {
			      slides[i].style.display = "none";  
			  }
			  for (i = 0; i < dots.length; i++) {
			      dots[i].className = dots[i].className.replace(" active", "");
			  }
			  slides[slideIndex-1].style.display = "block";  
			  dots[slideIndex-1].className += " active";
			}
			</script>
			""")
    
if __name__=="__main__":
    main()