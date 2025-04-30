

import hashlib
import streamlit as st

# Initialize an empty school report card ledger (a dictionary where keys are student names)
school_report_ledger = {}

# Function to generate a hash for a student's report card record
def generate_hash(student_name, subject, marks, date_of_exam):
    # Combine all exam details into one string
    report_data = student_name + subject + str(marks) + date_of_exam
    # Generate the SHA-256 hash of the report data
    report_hash = hashlib.sha256(report_data.encode()).hexdigest()
    return report_hash

# Streamlit UI to input student exam details
def add_student_report():
    st.title("School Report Card System")

    # Get student details from the user through Streamlit forms
    student_name = st.text_input("Enter the student's name:")
    subject = st.text_input("Enter the subject name:")
    marks = st.number_input("Enter the marks obtained:", min_value=0, max_value=100)
    date_of_exam = st.date_input("Enter the date of exam:")

    # If user clicks on the 'Submit' button, process the data
    if st.button("Submit"):
        # Generate a hash for this report card
        report_hash = generate_hash(student_name, subject, marks, str(date_of_exam))

        # Create a dictionary for the report card with the hash
        report = {
            "student_name": student_name,
            "subject": subject,
            "marks": marks,
            "date_of_exam": str(date_of_exam),
            "report_hash": report_hash  # Store the hash to verify data integrity
        }

        # Add the report to the student's list of reports
        if student_name not in school_report_ledger:
            school_report_ledger[student_name] = []

        school_report_ledger[student_name].append(report)

        # Display a success message with the hash
        st.success(f"Report added for {student_name} on {date_of_exam} for {subject} with {marks} marks.")
        st.write(f"Report Hash: {report_hash}")

# Display the report ledger for all students
def display_school_report_ledger():
    st.subheader("School Report Card Ledger")

    if not school_report_ledger:
        st.warning("No reports have been added yet.")
    else:
        for student, reports in school_report_ledger.items():
            st.write(f"### Student: {student}")
            for report in reports:
                st.write(f"  **Subject**: {report['subject']}, **Marks**: {report['marks']}, **Date of Exam**: {report['date_of_exam']}, **Hash**: {report['report_hash']}")

# Call the functions to add and display student reports
add_student_report()
display_school_report_ledger()
