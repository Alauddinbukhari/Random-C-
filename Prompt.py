class prompt:
    def __init__(self,subtopic):
        # self.concept=concept
        self.subtopic=subtopic
    def generate_prompt(self):
        prompt=f"OVERVIEW: {self.subtopic} | HISTORY | {self.concept} Technology | Use Cases | Challenges | The Future | Provide information in between 1500 and 2000 words."
        return prompt
