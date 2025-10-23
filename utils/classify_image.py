from openai import OpenAI
client = OpenAI()

def classify_image(image_path):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是一个图像分类助手，判断图片是食物、QR码、或萤养表。"},
            {"role": "user", "content": [{"type": "image_url", "image_url": image_path}]}
        ]
    )
    return response.choices[0].message.content.strip().lower()
