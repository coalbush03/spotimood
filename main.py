#load all the data from apis
#use spotipy

import spotipy
import spotipy.oauth2 as oauth2
import streamlit as st
import pandas as pd
import os

CLIENT_ID = os.environ.get('CLIENT_ID')