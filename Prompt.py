class prompt:
    def __init__(self,subtopic):
        # self.concept=concept
          self.subtopic=subtopic

    def generate_prompt(self):
        prompt=f"Provide a structured overview of {self.subtopic}, including sections for Introduction, History, Use Cases, Demand, Industry Usage, Challenges, and Technologies Usage."
        print(prompt)
        return prompt
