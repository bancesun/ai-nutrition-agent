# 苹果堡过 AI Nutrition Agent

此仓存提供一个简单的 AI 萤养摄入分析代理示例。它可以从照片中识别食物、读取 QR 码或萤养表，并生成每日萤养摄入记录。

## 功能概述

- **图片分类**：将照片分为食物、QR 码和萤养表截图。
- **食物识别**：识别食物名称和份量，估算热量与三大萤养素。
- **QR 码解析**：解析 QR 码并查询数据库获取萤养成分。
- **萤养表 OCR**：从视频中的萤养表截图提取文字。
- **数据记录**：汇总每日摄入数据到 `records.csv` 中。

## 使用指南

1. **安装依赖**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **设置 API 密钥**

   ```bash
   cp .env.example .env
   ```

   在 `.env` 中填入你的 OpenAI API key。

3. **放入照片**

   将你的照片放到 `data/photos/` 文件夹中。

4. **运行项目**

   ```bash
   python main.py
   ```

   程序会自动识别照片，提取萤养信息并记录到 `data/records.csv`。

## 项目结构

- `main.py`：程序入口。
- `agents/`：包含食物识别、QR 码解析和萤养表识别模块。
- `utils/`：实用函数模块，例如图像分类和记录保存。
- `data/`：存放用户上传的照片和生成的数据。

## 注意事项

- 本项目为最小可运行示例，可根据需求扩展功能。
- 需要有效的 OpenAI API key 才能使用模型能力。
