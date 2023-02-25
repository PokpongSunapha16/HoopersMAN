from PIL import Image
import pandas as pd
from streamlit.elements.media import *
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Define your options as a dictionary
options = ["HOME","NBA_PLAYERS","PRACTICE"]
selected_option = st.sidebar.selectbox("LIBRARY", options)
if selected_option == "HOME":
    P1 = st.sidebar
    if P1:
        st.markdown(
            "<h1 style='color: orange; -webkit-text-stroke: 1px black; text-align: center;'>𝑯𝑶𝑶𝑷𝑬𝑹𝑺 𝑴𝑨𝑵 🏀</h1>",
            unsafe_allow_html=True)
        st.text('\n')
        st.markdown(
            "<h4 style='color: white; text-align: left;'>เว็ปไซต์ที่รวบรวมเทคนิค และ สาระที่เกี่ยวข้องกับบาสเกตบอล</h4>",
            unsafe_allow_html=True)
        st.markdown("<h4 style='color: white;'>(By Pokpong Sunapha)</h4>",
                    unsafe_allow_html=True)
        st.text('\n')
        st.markdown(
            f"""
                   <style>
                   .stApp {{
                       background-image: url("https://images.squarespace-cdn.com/content/v1/57d4b0456a49635bed4dae6c/1621179897307-KU7RQBRQE2BQD40B41ZY/HOF_Kobe_v2.gif?format=1500w");
                       background-attachment: fixed;
                       background-size: cover;
                       /* opacity: 0.3; */
                   }}
                   </style>
                   """,
            unsafe_allow_html=True)


        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://toppng.com/public/uploads/thumbnail/basketball-dunk-11545691635ziel7u9w0o.png", width=230)
        with col2:
            st.markdown(
                "<iframe width='400' height='233' src='https://www.youtube.com/embed/Tjn3cgS8XQw' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
                unsafe_allow_html=True)



if selected_option == "NBA_PLAYERS":
    P2 = st.sidebar
    if P2:
        st.markdown(
            f"""
                           <style>
                           .stApp {{
                               background-image: url("https://images.squarespace-cdn.com/content/v1/57d4b0456a49635bed4dae6c/1588008936026-R8QA0JCY4JSQW6NGK1Y4/lastdance.gif?format=1000w");
                               background-attachment: fixed;
                               background-size: cover;
                               /* opacity: 0.3; */
                           }}
                           </style>
                           """,
            unsafe_allow_html=True)

# Font Changer : >>> Anton = Font Name
        st.markdown(
            """
            <link href='https://fonts.googleapis.com/css?family=Anton' rel='stylesheet'>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            "<h1 style='color: Yellow; font-family: Anton, sans-serif; -webkit-text-stroke: 1px black; text-align: center;'>NBA PLAYERS SIGNATURES MOVE</h1>",
            unsafe_allow_html=True)
        st.text('\n')


        st.markdown(
            "<h4 style='color: white;'>นักกีฬาบาสเกตบอลทุกคน มักจะต้องมีท่าไม้ตายที่ตัวเองใช้บ่อยอยู่เสมอ และมีประสิทธิภาพ</h4>",
            unsafe_allow_html=True)
        st.text('\n')


        st.write("<h1 style='color: white; text-align: center; -webkit-text-stroke: 1px black;'>Michael Jordan</h1>",
                 unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col1.image("https://image.cnbcfm.com/api/v1/image/106498863-1587478459689michaeljordan.jpg?v=1587478546",
                   width=350)
        col2.markdown(
            "<iframe width='400' height='233' src='https://www.youtube.com/embed/Ztb3KhRsBQc' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
            unsafe_allow_html=True)
        st.markdown(
                '<p style="text-align: left; color: white; -webkit-text-stroke: 0.32px black; font-size: 18px;">The Fadeaway Moves : ท่าไม้ตายตอกฝาโรงตัวประกบ โดยใช้การเคาะบอล และ ใช้ร่างกายดันคู่ต่อสู้(Post)เพื่อหาจังหวะที่เหมาะสม แล้วค่อยพลิกตัวไปอีกฝั่งของขาข้างที่ตัวเองถนัด กระโดดให้สูง พร้อมกับ</p>',
                unsafe_allow_html=True)

        st.text('\n')
        st.write("<h1 style='color: white; text-align: center; -webkit-text-stroke: 1px black;'>Kobe Bryant</h1>",
                 unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col1.image("https://www.indiewire.com/wp-content/uploads/2022/09/GettyImages-93243663.jpg?w=780",
                   width=350)
        col2.markdown(
            "<iframe width='400' height='233' src='https://www.youtube.com/embed/AsAHFzqxs0o' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
            unsafe_allow_html=True)
        st.markdown(
            '<p style="text-align: left; color: white; -webkit-text-stroke: 0.32px black; font-size: 18px;">The Fadeaway Moves : ท่าไม้ตายตอกฝาโรงตัวประกบ โดยใช้การเคาะบอล และ ใช้ร่างกายดันคู่ต่อสู้(Post)เพื่อหาจังหวะที่เหมาะสม แล้วค่อยพลิกตัวไปอีกฝั่งของขาข้างที่ตัวเองถนัด กระโดดให้สูง พร้อมกับ</p>',
            unsafe_allow_html=True)

        st.text('\n')
        st.write("<h1 style='color: white; text-align: center; -webkit-text-stroke: 1px black;'>LeBron James</h1>",
                 unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col1.image("https://compote.slate.com/images/32deaf1b-cab7-4feb-9591-c1f79d53976a.jpeg?crop=4625%2C3083%2Cx0%2Cy0",
                   width=350)
        col2.markdown(
            "<iframe width='400' height='233' src='https://www.youtube.com/embed/6R-vo91Tcu8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
            unsafe_allow_html=True)
        st.markdown(
            '<p style="text-align: left; color: white; -webkit-text-stroke: 0.32px black; font-size: 18px;">The Tomahawk Dunk : ท่าไม้ตายที่ใช้พละกำลังมหาศาลในการจบสกอร์ จะสามารถใช้ได้ในจังหวะเล่นเกมเร็ว(Fast Break) และ วิ่งตัดเข้าวงในเพื่อทำสกอร์ โดยการที่ผู้เล่นจะพุ่งตัวเข้าหาห่วง กระโดดให้สุดตัวพร้อมค้างตัวกลางอากาศ ในขณะเดียวกันถือลูกบาสแค่มือเดียว และยัดมันลงห่วงเหมือนดั่งเอาขวานสับลงไป</p>',
            unsafe_allow_html=True)

        st.text('\n')
        st.write("<h1 style='color: white; text-align: center; -webkit-text-stroke: 1px black;'>Stephen Curry</h1>",
                 unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col1.image(
            "https://people.com/thmb/0LxNo0FsX0Z3KzVdbIwi9z9Msjo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(999x0:1001x2)/Stephen-Curry-a250a7b0a1a14109a476f9454e2d9fed.jpg",
            width=350)
        col2.markdown(
            "<iframe width='400' height='233' src='https://www.youtube.com/embed/BRz9Y_fmUS8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
            unsafe_allow_html=True)
        st.markdown(
            '<p style="text-align: left; color: white; -webkit-text-stroke: 0.32px black; font-size: 18px;">The Pull-up Threes : ท่าไม้ตายจบสกอร์ 3 แต้ม โดยให้เพื่อนร่วมทีมเซ็ทสกรีนให้ เพื่อที่จะได้วิ่งเลี้ยงหลบตัวประกบ และไปหยุดที่ระยะ 3 คะแนน ต้องรักษาสมดุล(Balance)ไว้ได้ดีจวบจนวินาทีที่หยุดยิง เพื่อให้มีประสิทธิภาพในการทำแต้ม เพราะมันจะช่วยเพิ่มโอกาศที่ลูกบาสจะทำวิถีโค้ง และ หยอดลงห่วงได้แบบ Smooth!!</p>',
            unsafe_allow_html=True)




if selected_option == "PRACTICE":
    P3 = st.sidebar
    if P3:
        st.markdown(
            f"""
                                   <style>
                                   .stApp {{
                                       background-image: url("https://i.pinimg.com/originals/74/21/f8/7421f81c83e23ec29508f1088db49ce0.gif");
                                       background-attachment: fixed;
                                       background-size: cover;
                                       /* opacity: 0.3; */
                                   }}
                                   </style>
                                   """,
            unsafe_allow_html=True)
        st.markdown(
            """
            <link href='https://fonts.googleapis.com/css?family=Tilt+Warp' rel='stylesheet'>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            "<h1 style='color: Cyan; font-family: Anton, sans-serif; -webkit-text-stroke: 1px black; text-align: center;'>PRACTICE PROGRAMS</h1>",
            unsafe_allow_html=True)
        st.markdown(
            "<h2 style='color: Gold; font-family: Anton, sans-serif; -webkit-text-stroke: 1px black; text-align: center;'>BALL COUNTER</h2>",
            unsafe_allow_html=True)
        st.text('\n')

        st.image('https://i.ytimg.com/vi/EURxaOytO5M/maxresdefault.jpg')
        st.markdown(
            "<h4 style='color: red; -webkit-text-stroke: 0.35px black; text-align: center;'>[ถ้าหากเราอยากที่จะมีพัฒนาการมากจากเดิม เราก็ต้องทุ่มเทกับการฝึกซ้อม ให้มากขึ้น และ ทำมันอย่างถูกต้อง]</h4>",
            unsafe_allow_html=True)
        st.text('\n')
        st.image('https://i.pinimg.com/originals/29/0f/c5/290fc566ed83486e6f50979f535fb25e.png')
        st.text('\n')
        st.markdown(
            "<h5 style='color: Gray; -webkit-text-stroke: 0.4px black; text-align: center;'>*RECOMMEND* การที่เราฝึกชู้ตบาสลงห่วงได้วันละ 100 ลูก โดยไม่จำเป็นต้องยิงซ้ำที่เดิมก็ได้ มันจะช่วยให้เรามีพัฒนาการในด้านการจดจำของกล้ามเนื้อ(Muscle Memory)มากยิ่งขึ้น</h5>",
            unsafe_allow_html=True)
        st.text('\n')



    # Machine Learning Zone : Config and Run
        # Load basketball data from .xlsx file
        def load_basketball():
            return pd.read_excel('hoopers.xlsx')


        # Save data to .xlsx file
        def save_data(data_df):
            data_df.to_excel("hoopers.xlsx", index=False)
            st.success("Data saved to hoopers.xlsx")


        # Load data from .xlsx file
        def load_data():
            df = load_basketball()
            st.write("Data loaded from hoopers.xlsx")
            return df


        # Create an empty list to data
        data = []

        # Get user input for the date and amount
        date = st.date_input("Date : ")
        goal = st.number_input("Goal : ")
        ball = st.number_input("Ball Count : ")
        amount = st.write(goal - ball)

        # Add the expense to the list when the user clicks the "Add data" button
        if st.button("Add Data"):
            data.append((date, goal, ball))
            st.success("Data added!")

        # Display the list of data
        if data:
            data_df = pd.DataFrame(data, columns=["date", "goal", "ball"])
            st.write("Your Data:")
            st.write(data_df)
            save_data(data_df)
        else:
            data_df = load_data()
            if not data_df.empty:
                st.write("Your Data:")
                st.write(data_df)
            else:
                st.write("No Data added.")

        # Plot scatter plot of data
        if not data_df.empty:
            if st.button("PLOT DATA"):
                fig, ax = plt.subplots()
                ax.scatter(data_df["goal"], data_df["ball"])
                plt.xlabel("goal")
                plt.ylabel("ball")
                st.pyplot(fig)

        # Train model to predict
        if not data_df.empty:
            if st.button('TRAIN MODEL'):
                # Train model on data
                model = LinearRegression()
                model.fit(data_df['ball'].values.reshape(-1, 1), data_df.index)

                # Save model to disk
                joblib.dump(model, 'model.joblib')
                st.success("Model trained and saved to model.joblib")

        # Load model and predict amount
        if st.button('PREDICT BALL'):
            # Load model from disk
            model = joblib.load('model.joblib')

            # Get user input for date
            predict_date = st.date_input("Enter the date to predict the ball:")

            # Convert date to number of days since a reference date
            reference_date = pd.to_datetime('2022-01-01')
            days_since_reference = (pd.to_datetime(predict_date) - reference_date).days

            # Predict amount using loaded model and user input
            predicted_ball = model.predict(np.array(days_since_reference).reshape(1, -1))[0]
            st.success(f"วันที่ {predict_date} คุณยังต้องยิ่งเพิ่มอีก {goal - ball} สู้ๆนะครับ 🏀✌️")
        st.text('\n')
        uploaded_file = st.file_uploader("สามารถอัพโหลดรูปสวยๆ เท่ห์ๆ ในขณะที่กำลังฝึกได้น๊าาาา 📷🏀", type=["jpg", "jpeg", "png"])
        # Display the uploaded image
        if uploaded_file is not None:
            # Open the image using PIL
            image = Image.open(uploaded_file)
            # Display the image using Streamlit
            st.image(image, caption='รูปภาพของคุณ', use_column_width=True)
            st.text(f'สู้ต่อไปนะ อย่ายอมแพ้นะ !!! 🏀❤️‍🔥')
        else:
            st.write("[ยังไม่ได้อัพโหลดรูป]")


