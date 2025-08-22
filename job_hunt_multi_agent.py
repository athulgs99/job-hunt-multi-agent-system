from groq import Groq


client = Groq(api_key="")

class job_hunt_agent:
    def __init__(self, company, role):
        self.company = company
        self.role = role
    
    def fetch_company_info(self):x
        # Dummy example; will replace with API calls in next commit
        info = {
            "job_desc": f"{self.role} at {self.company}, requires Python and Java skills.",
            "reviews": "Overall rating 4.2/5. Good culture."
        }
        return info
    
    def generate_questions(self):
        prompt = (
            f"Generate 5 likely interview questions for the role of {self.role} at {self.company}, "
            "including both coding and behavioral questions."
        )
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.split("\n")
    
    def mock_interview(self, answers):
        # ask LLM for feedback
        feedback_text = ""
        for q, ans in answers.items():
            prompt = f"Q: {q}\nA: {ans}\nGive detailed feedback and improvements for this answer."
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}]
            )
            feedback_text += response.choices[0].message.content + "\n\n"
        return feedback_text
    
    def run(self):
        info = self.fetch_company_info()
        questions = self.generate_questions()
        
        print("=== Company Info ===")
        print(info)
        print("\n=== Interview Questions ===")
        for q in questions:
            print("-", q)
        
        # Simulate your answers
        answers = {q: "Sample answer" for q in questions}
        print("\n=== Mock Interview Feedback ===")
        print(self.mock_interview(answers))


agent = JobHuntAgent(company="Meta", role="SWE")
agent.run()
