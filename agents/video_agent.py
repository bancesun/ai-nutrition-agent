import cv2
import pytesseract

def extract_text_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    texts = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        text = pytesseract.image_to_string(frame)
        if "kcal" in text or "protein" in text.lower():
            texts.append(text)
    cap.release()
    return "\n".join(texts[-3:])  # 取最后几帧
