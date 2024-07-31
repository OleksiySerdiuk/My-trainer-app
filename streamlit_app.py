import streamlit as st

st.title("🎈 My trainer app")
st.write("This how to works st.write command")
st.markdown("# Це заголовок першого рівня")
st.markdown("## Це заголовок другого рівня")
st.markdown("### Це заголовок третього рівня")
st.markdown("Це **жирний текст** і це *курсивний текст*.")
st.markdown("""
- Перший елемент списку
- Другий елемент списку
  - Вкладений елемент списку
""")

st.markdown("""
1. Перший елемент нумерованого списку
2. Другий елемент нумерованого списку
""")
st.markdown("[Перейти на Google](https://www.google.com)")
st.markdown("```python\nprint('Привіт, світ!')\n```")
st.markdown("---")
st.header("Це також заголовок")
st.subheader("А це підзаголовок")
