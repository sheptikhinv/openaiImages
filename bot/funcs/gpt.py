import openai

import config

client = openai.Client(api_key=config.get_openai_token())


def get_gpt_response(prompt: str, base64_image: str, description: str = None) -> str:
    messages = [{"role": "system", "content": prompt}, {"role": "user", "content": []}]
    if description:
        messages[1]["content"].append(
            {
                "type": "text",
                "text": description
            }
        )
    messages[1]["content"].append(
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        }
    )
    response = client.chat.completions.create(
       model="gpt-4-vision-preview",
       max_tokens=2000,
       messages=messages
    )
    return response.choices[0].message.content
