import torch
from torchvision import transforms
from PIL import Image
from fastapi import UploadFile

MODEL_PATH = "models/disease_model/tiny_cnn.pt"
model = torch.load(MODEL_PATH, map_location="cpu")
model.eval()

classes = ["Healthy", "Disease1", "Disease2"]  # adjust as needed
transform = transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor()
])

def predict_disease(file: UploadFile):
    image = Image.open(file.file).convert("RGB")
    img_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)
    return {"disease": classes[predicted.item()]}
