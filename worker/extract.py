import pdfplumber

class TextExtractor:
    def __init__(self, request, client):
        self.mailBox = request.mailBox
        self.messageId = request.messageId
        self.text=request.data
        self.client = client


    def extract_fields_with_open_ai(self, prompt):
        response = self.client.chat.completions.create(
        model="gpt-4",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content":  prompt + "\n\n" + self.text}
                # {"role": "user", "content":  prompt }
            ],
        # max_tokens=200   
        )
        print(response.usage)
        return response.choices[0].message.content

