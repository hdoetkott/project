# Building and deploying a web application dashboard to a cloud service

## creating and managing python virtual environments, developing a web application, and deploying it to a cloud service and make it accessible to the public

This project show to do the following :

* create streamlit with render, add a streamlit configuration file to git repository at .streamlit/config.toml
* create account on render.com and create a new web service
* Create a new web service linked to Github repository
* Configure the new Render web service. At Build Command, add pip install streamlit & pip install -r requirements.txt 
* add Start Command, add: streamlit run app.py
* Deploy to Render,
* Verify that your application is accessible at the following URL: https://sprint4-1kgb.onrender.com/

# The minimal expected project structure
$ tree
.
├── streamlit
    └── config.toml 
├── notebooks
    └── eda4.ipynb    
├── README.md
├── app.py
├── requirements.txt
├── <vehicles_us>.csv

