import streamlit as st


st.title('Python 不同的库实现图像读入成 numpy 数组')
tab1, tab2, tab3 = st.tabs(['opencv', 'pillow', 'imageio'])

with tab1:
    '''
    ```python
    import cv2
    image = cv2.imread('image.png')
    ```
    '''

with tab2:
    '''
    ```python
    from PIL import Image
    image = Image.open('image.png')
    ```
    '''

with tab3:
    '''
    ```python
    import imageio
    image = imageio.imread('image.png')
    ```
    '''
