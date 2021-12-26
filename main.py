import streamlit as st
import time

st.title('streamlit 入門')
st.write('プログレスバーの表示')

'Start'
latest_iteration = st.empty()
bar = st.progress(0)