import streamlit as st
import Modules.functions


ToDos = Modules.functions.get_ToDos()

def addTodo():
    ToDo = st.session_state["newTodo"] + "\n" #session_state es un objeto que me permite tener acceso al valor almacenado en un text_input por ejemplo
    ToDos.append(ToDo)
    Modules.functions.post_ToDos(ToDos)
    st.session_state["newTodo"] = ""


st.title("My Todo App")
st.subheader("esta es una app con tu lista de pendientes")
st.write("acá podrás almacenar todo lo que tenga pendiente por realizar")

for index,ToDo in enumerate(ToDos):
    checkBox = st.checkbox(ToDo, key=ToDo)
    if checkBox:
        ToDos.pop(index)
        Modules.functions.post_ToDos(ToDos)
        del st.session_state[ToDo]
        st.experimental_rerun()


st.text_input(label="Ingresa aqui tus pendientes",
              placeholder="Nuevo pendiente",
              on_change=addTodo,
              key="newTodo") #el método on_change requiere un call back function

#st.session_state