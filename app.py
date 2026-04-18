import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("teacher_model.pkl","rb") as f:
    model,le_subject,le_topic,ordered_topics,df = pickle.load(f)

st.title("AI Teacher Lesson Planner")

# Inputs
subject = st.selectbox(
    "Subject",
    sorted(df['subject'].unique())
)

grade = st.selectbox(
    "Grade",
    sorted(df['grade'].unique())
)

student_level = st.selectbox(
    "Student Level",
    ["Beginner","Intermediate","Advanced"]
)

topic = st.selectbox(
    "Select Topic",
    sorted(df['Topic'].unique())
)

# Button
if st.button("Generate Teaching Plan"):

    sub_enc = le_subject.transform([subject])[0]

    plan = []

    for t in ordered_topics:

        if t not in le_topic.classes_:
            continue

        topic_enc = le_topic.transform([t])[0]

        input_df = pd.DataFrame(
            [[sub_enc,topic_enc,grade]],
            columns=['subject_enc','topic_enc','grade']
        )

        pred_time = model.predict(input_df)[0]

        plan.append((t,round(pred_time)))

        # stop when selected topic reached
        if t == topic:
            break

    # OUTPUT
    st.subheader("Generated Teaching Plan")

    if len(plan) == 0:
        st.error("No teaching plan found for this topic.")
    else:
        for i,(t,time) in enumerate(plan):
            st.write(f"Week {i+1}: {t}  (Estimated Time: {time} hrs)")