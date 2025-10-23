from openai import OpenAI
client = OpenAI()

def estimate_food_calories(image_path):
    prompt = """
    请识别图片中的食物名称和份量，并输出：
    食物: 名称
    份量: 数值+单位
    热量(kcal):
    碼汁/蛋白质/脂肪(g):
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "你是萤养师AI"},
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": image_path}
            ]}
        ]
    )
    return response.choices[0].message.content
