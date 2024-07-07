from dataclasses import dataclass
from typing import Dict, List

from openai import OpenAI

from configs import MESSAGE_MAX_LEN, OPENAI_API_KEY


@dataclass
class AnswerBot:
    llm_model: str = "gpt-3.5-turbo"
    prompt: str = (
        "Your task is to provide an answer to the user's question. "
        "Your response should contain no more than "
        f"{MESSAGE_MAX_LEN} characters."
    )

    def get_answer(self, question: str) -> str:
        messages = [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": question},
        ]
        return self.send_request(messages)
   
    def send_request(self, messages: List[Dict[str, str]]) -> str:
        client = OpenAI(
            api_key=OPENAI_API_KEY
        )
        completion = client.chat.completions.create(
            model=self.llm_model,
            messages=messages,
        )
        return completion.choices[0].message.content
