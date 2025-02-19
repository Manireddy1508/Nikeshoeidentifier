# Nike Sneaker Classification Model 🚀

---

### 🎯 ***Project Overview***
This project builds an ***AI-powered sneaker classification model*** to distinguish between ***Nike, Other brands, and Non-Shoe images***. The model leverages ***MobileNetV2*** as a feature extractor and is fine-tuned on a custom dataset.

---

### 🏗️ ***How It Works***
1. **Data Preprocessing**:
   - Images are resized to **224x224** pixels and normalized.
   - Applied **data augmentation** (rotation, zoom, brightness adjustments) for robustness.
2. **Model Architecture**:
   - Based on ***MobileNetV2*** with pre-trained **ImageNet** weights.
   - Added **Batch Normalization, Fully Connected Layers, and Dropout** for better generalization.
   - Uses **softmax activation** for multi-class classification.
3. **Training Strategy**:
   - **Fine-tuning** applied by gradually unfreezing layers.
   - Implemented **learning rate decay** and **early stopping** to optimize training.
   - **Categorical cross-entropy loss** with the **Adam optimizer**.

---

### 📂 ***Dataset***
The dataset consists of **Nike, Other brands, and Non-Shoe images**, containing over **39,000+ images** in total.

#### 🔽 ***How to Download***
The dataset is available on ***Google Drive***.

- 📥 [Google Drive Download](https://drive.google.com/drive/folders/1uJJg90lROdUhVUtHwYoLNDvcnlmB5Gmz?usp=drive_link)

To download and extract it, run:
```bash
pip install gdown
gdown --folder https://drive.google.com/drive/folders/1uJJg90lROdUhVUtHwYoLNDvcnlmB5Gmz
```

---

### 🌐 ***API Deployment***
The trained model is deployed as a **FastAPI web service on Google Cloud Run**.

#### 🚀 ***How to Use the API***
- Upload an image, and the API will return the predicted class (`Nike`, `Other`, or `Non-Shoe`).
- API is accessible via a public URL.

#### 🖥️ ***Run API Locally***
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```
- Open `http://127.0.0.1:8000/docs` to test via Swagger UI.

#### 📡 ***Cloud Deployed API***
- API is hosted on **Google Cloud Run** with a public endpoint.
- To test with an image:
```python
import requests
url = "https://your-cloud-run-url/predict/"
files = {"file": open("test_shoe.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
```
### 📜 ***How to Use the API***
** 1️⃣ ** Open Swagger UI for Interactive API Testing **
-Visit:
`https://nike-classifier-xxxxxx.a.run.app/docs`
Upload an image
Click "Execute"
View the classification result

 2️⃣ ** Test API Using cURL **

-Run the following command:

`curl -X POST -F "file=@/path/to/image.jpg" \
     https://nike-classifier-xxxxxx.a.run.app/predict`

** 3️⃣ ** Use the API in a Python Script **

`import requests
url = "https://nike-classifier-xxxxxx.a.run.app/predict"
files = {"file": open("/path/to/image.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())  # {'class': 'Nike', 'confidence': [[0.89, 0.07, 0.04]]}`

---

### 📊 ***Performance & Evaluation***
- **Train Accuracy:** ~97%  
- **Validation Accuracy:** ~95%  
- **Test Accuracy:** ~92.9%  
- **F1-Score:** 0.89 (Balanced across classes)

**Model Evaluation Tools:**
- **Confusion Matrix** to visualize classification results.
- **Precision, Recall, and F1-score** for performance insights.

---

### 📌 ***Next Steps***
✅ Improve classification between `Nike` and `Other` brands.
✅ Deploy API authentication using OAuth or API Keys.
✅ Integrate model into a mobile or web application.

---

🎉 **Developed by:** Mani 🚀


