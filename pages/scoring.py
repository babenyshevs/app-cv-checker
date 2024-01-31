import streamlit as st

class ResumeParserApp:
    TEXT_AREA_HEIGHTS = {
        "description": 150,
        "responsibilities": 150,
        "requirements": 150,
        "resume": 500,
        "profile": 120,
        "experience": 60,
        "education": 60,
        "skills": 60,
    }

    def __init__(self):
        self.description = ""
        self.responsibilities = ""
        self.requirements = ""
        self.resume_text = ""
        self.profile = ""
        self.experience = ""
        self.education = ""
        self.skills = ""

    def render_job_description_column(self, form):
        form.text("Job Description")
        self.description = form.text_area("Description", placeholder="Enter job description", key="description", 
                                         height=self.TEXT_AREA_HEIGHTS["description"], label_visibility="hidden")
        self.responsibilities = form.text_area("Responsibilities", placeholder="Enter responsibilities", key="responsibilities",
                                              height=self.TEXT_AREA_HEIGHTS["responsibilities"], label_visibility="hidden")
        self.requirements = form.text_area("Requirements", placeholder="Enter requirements", key="requirements",
                                         height=self.TEXT_AREA_HEIGHTS["requirements"], label_visibility="hidden")

    def render_resume_column(self, form):
        form.text("Resume")
        self.resume_text = form.text_area("Resume", placeholder="Enter your resume", key="resume",
                                         height=self.TEXT_AREA_HEIGHTS["resume"], label_visibility="hidden")

    def render_parsed_resume_column(self, form):
        form.text("Parsed Resume")
        self.profile = form.text_area("Profile", placeholder="Enter profile", key="profile",
                                      height=self.TEXT_AREA_HEIGHTS["profile"], label_visibility="hidden")
        self.experience = form.text_area("Experience", placeholder="Enter experience", key="experience",
                                         height=self.TEXT_AREA_HEIGHTS["experience"], label_visibility="hidden")
        self.education = form.text_area("Education", placeholder="Enter education", key="education",
                                        height=self.TEXT_AREA_HEIGHTS["education"], label_visibility="hidden")
        self.skills = form.text_area("Skills", placeholder="Enter skills", key="skills",
                                     height=self.TEXT_AREA_HEIGHTS["skills"], label_visibility="hidden")

    def calculate(self):
        # Perform parsing or any other calculation here
        # Update the parsed resume text based on the input job description and resume text
        self.profile, self.experience, self.education, self.skills = self.parse_resume()

    def parse_resume(self):
        # Implement your resume parsing logic here
        # This is a placeholder function, replace it with your actual parsing code
        profile = "Parsed Profile based on job description and resume"
        experience = "Parsed Experience based on job description and resume"
        education = "Parsed Education based on job description and resume"
        skills = "Parsed Skills based on job description and resume"
        return profile, experience, education, skills

    def run(self):
        st.set_page_config(layout="wide")  # Set page layout to wide
        st.title("Scoring")

        # Create a container with three columns
        col1, col2, col3 = st.columns(3)

        # Left column - Job description
        self.render_job_description_column(col1)

        # Middle column - Resume
        self.render_resume_column(col2)

        # Right column - Parsed resume
        self.render_parsed_resume_column(col3)

        # Calculate button in the sidebar
        if st.sidebar.button("Calculate"):
            self.calculate()


if __name__ == "__main__":
    app = ResumeParserApp()
    app.run()