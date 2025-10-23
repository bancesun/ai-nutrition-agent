import os
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from agents.food_agent import estimate_food_calories
from agents.qr_agent import get_qr_text, lookup_nutrition_from_qr
from utils.classify_image import classify_image
from utils.save_record import save_record

llm = ChatOpenAI(model="gpt-4o")

tools = [
    Tool(name="ClassifyImage", func=classify_image, description="识别图片类型"),
    Tool(name="EstimateFood", func=estimate_food_calories, description="分析食物营养"),
    Tool(name="QRLookup", func=lookup_nutrition_from_qr, description="根据QR码查食物信息")
]

agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")

folder = "data/photos"
for f in os.listdir(folder):
    path = f"{folder}/{f}"
    if not os.path.isfile(path):
        continue
    result = agent.run(f"分析这张图片: {path}")
    print(f"\n📷 {f}:\n{result}\n")
