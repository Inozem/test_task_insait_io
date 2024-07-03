from dataclasses import dataclass

from openai import OpenAI

from configs import OPENAI_API_KEY


@dataclass
class AnswerBot:
    prompt: str = "Your task is to provide an answer to the user's question."
    gpt_model: str

    def get_answer(self, question):
        messages = [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": question},
        ]
        return self.send_request("gpt-4o", messages)
   
    def send_request(self, messages):
        client = OpenAI(
            api_key=OPENAI_API_KEY
        )
        completion = client.chat.completions.create(
            model=self.gpt_model,
            messages=messages,
        )
        return completion.choices[0].message.content
