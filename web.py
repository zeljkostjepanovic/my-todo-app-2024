import streamlit as st
from modules import functions


st.set_page_config(layout="wide")

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""
    

st.title("My todo app")
st.subheader("This is my todo app")
st.write("This is a simple todo app to improve your productivity.")
st.write("I'm experimenting with streamlit and python, following udemy course.")

st.write("---")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()
       

st.text_input(label="Add a new todo", 
              placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")
