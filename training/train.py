import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models
import os

# ==========================
# 1️⃣ Configuration
# ==========================
DATA_DIR = "training/data"  # folder with subfolders per class
MODEL_SAVE_PATH = "models/tiny_cnn.pt"
BATCH_SIZE = 32
EPOCHS = 10
LR = 0.001
IMG_SIZE = 128
NUM_CLASSES = 3  # e.g., Healthy, Disease1, Disease2

# ==========================
# 2️⃣ Transformations
# ==========================
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
])

# ==========================
# 3️⃣ Dataset and Loader
# ==========================
train_dataset = datasets.ImageFolder(os.path.join(DATA_DIR, "train"), transform=transform)
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

val_dataset = datasets.ImageFolder(os.path.join(DATA_DIR, "val"), transform=transform)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)

# ==========================
# 4️⃣ Tiny CNN Model
# ==========================
class TinyCNN(nn.Module):
    def __init__(self, num_classes=NUM_CLASSES):
        super(TinyCNN, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * (IMG_SIZE // 8) * (IMG_SIZE // 8), 128),
            nn.ReLU(),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

# ==========================
# 5️⃣ Training Setup
# ==========================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = TinyCNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

# ==========================
# 6️⃣ Training Loop
# ==========================
for epoch in range(EPOCHS):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    train_acc = 100 * correct / total
    print(f"Epoch [{epoch+1}/{EPOCHS}] Loss: {running_loss/len(train_loader):.4f} Train Acc: {train_acc:.2f}%")

# ==========================
# 7️⃣ Save Model
# ==========================
os.makedirs("models", exist_ok=True)
torch.save(model, MODEL_SAVE_PATH)
print(f"Model saved to {MODEL_SAVE_PATH}")
