from streamlit_tensorboard import st_tensorboard
import streamlit as st
st.set_page_config(layout="wide")

logdir=st.text_input("Path to Logs",value="/logs")
if logdir: st_tensorboard(logdir=logdir, port=6006)