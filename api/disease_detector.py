import torch
from torchvision import transforms
from PIL import Image

# Load model
model = torch.load('models/tiny_disease_model.pt', map_location='cpu')
model.eval()

# Dummy inference function
def predict_disease(image_path):
    image = Image.open(image_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize((128,128)),
        transforms.ToTensor()
    ])
    img_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)
    classes = ['Healthy', 'Disease1', 'Disease2']  # example
    return classes[predicted.item()]

# Test
print(predict_disease('sample_leaf.jpg'))
