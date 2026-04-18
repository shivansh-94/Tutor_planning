# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import random

# st.title("AI Tutor Planner")

# # -----------------------------
# # Subject → Topics → Subtopics
# # -----------------------------

# topic_data = {

#     "Physics": {

#         "Electrostatics": [
#             "Electric Charge",
#             "Coulomb's Law",
#             "Electric Field",
#             "Electric Potential",
#             "Capacitance",
#             "Dielectrics"
#         ],

#         "Thermodynamics": [
#             "Temperature",
#             "Heat Transfer",
#             "First Law of Thermodynamics",
#             "Second Law of Thermodynamics",
#             "Entropy",
#             "Applications"
#         ],

#         "Magnetism": [
#             "Magnetic Field",
#             "Magnetic Force",
#             "Magnetic Materials",
#             "Electromagnetic Induction",
#             "Applications"
#         ]
#     },

#     "Chemistry": {

#         "Chemical Bonding": [
#             "Ionic Bonding",
#             "Covalent Bonding",
#             "Metallic Bonding",
#             "Bond Polarity",
#             "Molecular Geometry",
#             "Intermolecular Forces"
#         ],

#         "Periodic Table": [
#             "Periodic Trends",
#             "Atomic Radius",
#             "Ionization Energy",
#             "Electron Affinity",
#             "Electronegativity"
#         ],

#         "Organic Chemistry": [
#             "Hydrocarbons",
#             "Functional Groups",
#             "Isomerism",
#             "Reaction Mechanisms",
#             "Applications"
#         ]
#     },

#     "Biology": {

#         "Photosynthesis": [
#             "Chloroplast Structure",
#             "Light Reaction",
#             "Calvin Cycle",
#             "Factors Affecting Photosynthesis",
#             "Applications"
#         ],

#         "Cell Biology": [
#             "Cell Structure",
#             "Cell Membrane",
#             "Organelles",
#             "Cell Division",
#             "Cell Communication"
#         ],

#         "Genetics": [
#             "DNA Structure",
#             "Gene Expression",
#             "Mendelian Genetics",
#             "Mutation",
#             "Genetic Disorders"
#         ]
#     }
# }

# # -----------------------------
# # Inputs
# # -----------------------------

# subject = st.selectbox("Select Subject", list(topic_data.keys()))

# grade = st.selectbox("Grade", [10,11,12])

# student_level = st.selectbox(
#     "Student Level",
#     ["Beginner","Intermediate","Advanced"]
# )

# # Dynamic topic selection based on subject
# topics = list(topic_data[subject].keys())

# topic = st.selectbox("Select Topic", topics)

# # -----------------------------
# # Generate Plan
# # -----------------------------

# if st.button("Generate Teaching Plan"):

#     subtopics = topic_data[subject][topic]

#     # Dynamic time values
#     times = [random.randint(1,5) for _ in subtopics]

#     df = pd.DataFrame({
#         "Topic": subtopics,
#         "Time (hrs)": times
#     })

#     st.subheader("Generated Teaching Plan")

#     for i,row in df.iterrows():

#         st.write(
#             f"Step {i+1}: {row['Topic']} (Estimated Time: {row['Time (hrs)']} hrs)"
#         )

#     # ---------------- Bar Chart ----------------

#     st.subheader("Time Distribution")

#     fig1, ax1 = plt.subplots()

#     ax1.bar(df["Topic"], df["Time (hrs)"])

#     plt.xticks(rotation=30)

#     st.pyplot(fig1)

#     # ---------------- Line Chart ----------------

#     st.subheader("Learning Progression")

#     fig2, ax2 = plt.subplots()

#     ax2.plot(df["Topic"], df["Time (hrs)"], marker="o")

#     plt.xticks(rotation=30)

#     st.pyplot(fig2)

#     # ---------------- Pie Chart ----------------

#     st.subheader("Topic Percentage Distribution")

#     fig3, ax3 = plt.subplots()

#     ax3.pie(df["Time (hrs)"], labels=df["Topic"], autopct="%1.1f%%")

#     st.pyplot(fig3)

#     # ---------------- Teaching Flow ----------------

#     st.subheader("Teaching Flow")

#     flow_text = " → ".join(subtopics)

#     st.success(flow_text)

































import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="AI Tutor Planner", layout="wide")

st.title("AI Tutor Planner")

# ---------------------------------------------------
# Dataset
# ---------------------------------------------------

topic_data = {

"Physics":{

"Electrostatics":["Electric Charge","Coulomb's Law","Electric Field","Electric Potential","Capacitance","Dielectrics"],
"Thermodynamics":["Temperature","Heat Transfer","First Law","Second Law","Entropy","Applications"],
"Magnetism":["Magnetic Field","Magnetic Force","Magnetic Materials","Electromagnetic Induction","Magnetic Flux","Applications"],
"Optics":["Reflection","Refraction","Snell Law","Lenses","Optical Instruments","Applications"],
"Waves":["Wave Motion","Wave Properties","Sound Waves","Doppler Effect","Interference","Applications"],
"Modern Physics":["Photoelectric Effect","Atomic Models","Quantum Theory","Nuclear Physics","Radioactivity","Applications"],
"Motion":["Speed","Velocity","Acceleration","Equations of Motion","Graphical Analysis","Applications"],
"Work Energy":["Work","Kinetic Energy","Potential Energy","Power","Energy Conservation","Applications"],
"Gravitation":["Newton Law","Gravitational Field","Potential","Escape Velocity","Orbital Motion","Applications"],
"Electric Current":["Ohm's Law","Resistance","Electric Circuits","Power","Kirchhoff Laws","Applications"]

},

"Chemistry":{

"Chemical Bonding":["Ionic Bonding","Covalent Bonding","Metallic Bonding","Bond Polarity","Molecular Geometry","Intermolecular Forces"],
"Periodic Table":["Periodic Trends","Atomic Radius","Ionization Energy","Electron Affinity","Electronegativity","Applications"],
"Organic Chemistry":["Hydrocarbons","Functional Groups","Isomerism","Reaction Mechanisms","Polymers","Applications"],
"Thermochemistry":["Heat of Reaction","Enthalpy","Calorimetry","Hess Law","Energy Changes","Applications"],
"Electrochemistry":["Redox Reactions","Electrochemical Cells","Electrolysis","Nernst Equation","Batteries","Applications"],
"Chemical Kinetics":["Rate of Reaction","Order","Activation Energy","Catalysis","Rate Laws","Applications"],
"Solutions":["Solubility","Concentration","Colligative Properties","Osmosis","Raoult Law","Applications"],
"Acids Bases":["pH Scale","Strong vs Weak","Neutralization","Buffer Solutions","Indicators","Applications"],
"Coordination":["Ligands","Coordination Number","Isomerism","Chelation","Crystal Field Theory","Applications"],
"Biochemistry":["Proteins","Carbohydrates","Lipids","Enzymes","Metabolism","Applications"]

},

"Biology":{

"Cell Biology":["Cell Structure","Cell Membrane","Organelles","Cell Division","Cell Communication","Applications"],
"Genetics":["DNA Structure","Gene Expression","Mendel Laws","Mutation","Genetic Disorders","Applications"],
"Photosynthesis":["Chloroplast","Light Reaction","Calvin Cycle","Factors","Energy Conversion","Applications"],
"Human Digestive System":["Digestion","Enzymes","Absorption","Metabolism","Nutrition","Applications"],
"Respiration":["Aerobic Respiration","Anaerobic Respiration","ATP Production","Glycolysis","Energy Release","Applications"],
"Nervous System":["Neurons","Brain","Spinal Cord","Reflex Action","Signal Transmission","Applications"],
"Circulatory System":["Heart","Blood","Blood Vessels","Oxygen Transport","Regulation","Applications"],
"Ecology":["Ecosystems","Food Chains","Energy Flow","Biodiversity","Conservation","Applications"],
"Evolution":["Natural Selection","Darwin Theory","Adaptation","Speciation","Evidence","Applications"],
"Immunity":["Immune Cells","Antibodies","Vaccines","Pathogens","Defense Mechanisms","Applications"]

},

"Maths":{

"Algebra":["Linear Equations","Quadratic Equations","Polynomials","Factorization","Functions","Applications"],
"Trigonometry":["Trigonometric Ratios","Identities","Angles","Graphs","Inverse Trigonometry","Applications"],
"Calculus":["Limits","Derivatives","Integration","Differential Equations","Applications"],
"Probability":["Random Events","Sample Space","Probability Rules","Conditional Probability","Bayes Theorem","Applications"],
"Statistics":["Mean","Median","Mode","Variance","Standard Deviation","Applications"],
"Matrices":["Matrix Operations","Determinants","Inverse","Linear Systems","Applications"],
"Coordinate Geometry":["Straight Line","Circle","Parabola","Ellipse","Hyperbola","Applications"],
"Vectors":["Vector Addition","Dot Product","Cross Product","Direction Cosines","Applications"],
"Sequences":["Arithmetic Progression","Geometric Progression","Series","Summation","Applications"],
"Number Theory":["Divisibility","Prime Numbers","Modular Arithmetic","GCD","Applications"]

}

}

# ---------------------------------------------------
# Inputs
# ---------------------------------------------------

col1,col2,col3 = st.columns(3)

with col1:
    subject = st.selectbox("Subject", list(topic_data.keys()))

with col2:
    grade = st.selectbox("Grade",[9,10,11,12])

with col3:
    student_level = st.selectbox("Student Level",["Beginner","Intermediate","Advanced"])

topics = list(topic_data[subject].keys())

topic = st.selectbox("Select Topic", topics)

# ---------------------------------------------------
# Generate Plan
# ---------------------------------------------------

if st.button("Generate Teaching Plan"):

    subtopics = topic_data[subject][topic]

    times = [random.randint(1,5) for _ in subtopics]

    df = pd.DataFrame({
        "Subtopic":subtopics,
        "Time":times
    })

    st.subheader("Generated Teaching Plan")

    for i,row in df.iterrows():
        st.write(f"Step {i+1}: {row['Subtopic']} (Estimated Time: {row['Time']} hrs)")

    # ---------------- Graphs in Two Columns ----------------

    col1, col2 = st.columns(2)

    # Bar Chart
    with col1:
        st.subheader("Time Distribution")

        fig1, ax1 = plt.subplots(figsize=(4,3))
        ax1.bar(df["Subtopic"],df["Time"])
        plt.xticks(rotation=30)
        st.pyplot(fig1)

    # Pie Chart
    with col2:
        st.subheader("Topic Percentage")

        fig2, ax2 = plt.subplots(figsize=(4,3))
        ax2.pie(df["Time"],labels=df["Subtopic"],autopct="%1.1f%%")
        st.pyplot(fig2)

    # Teaching Flow
    st.subheader("Teaching Flow")

    flow = " → ".join(subtopics)
    st.success(flow)

    