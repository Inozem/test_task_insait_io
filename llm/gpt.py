from dataclasses import dataclass

from openai import OpenAI

from configs import OPENAI_API_KEY


@dataclass
class AnswerBot:
    prompt: str = "Your task is to provide an answer to the user's question."
    llm_model: str = "gpt-3.5-turbo"

    def get_answer(self, question):
        messages = [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": question},
        ]
        return self.send_request(messages)
   
    def send_request(self, messages):
        client = OpenAI(
            api_key=OPENAI_API_KEY
        )
        completion = client.chat.completions.create(
            model=self.llm_model,
            messages=messages,
        )
        return completion.choices[0].message.content
