# Nike Sneaker Classification Model 🚀

---

### 🎯 ***Project Overview***
This project focuses on building a ***deep learning model*** to classify sneakers as ***Nike or Other brands***.  
The model is based on ***MobileNetV2*** and trained using a custom dataset containing various sneaker images.  

---

### 🏗️ ***How It Works***
1. **Data Preprocessing**: Images are loaded, resized, and augmented for better generalization.
2. **Model Architecture**:
   - Utilizes ***MobileNetV2*** as the feature extractor.
   - Added ***fully connected layers*** with dropout for regularization.
   - Fine-tuned the model by unfreezing selected layers.
3. **Training Strategy**:
   - Implemented ***learning rate scheduling*** and ***early stopping*** to optimize training.
   - Used ***data augmentation*** to make the model robust.
   - Trained with ***binary cross-entropy loss*** and ***Adam optimizer***.

---

### 📂 ***Dataset***
The full dataset contains ***26,000+ images***, making it too large for GitHub.  

#### 🔽 ***How to Download***
The dataset is hosted on ***Google Drive*** and ***Kaggle***.

- 📥 [Google Drive Download](https://drive.google.com/drive/folders/1uJJg90lROdUhVUtHwYoLNDvcnlmB5Gmz?usp=drive_link)
- 📥 [Kaggle Dataset](YOUR_KAGGLE_LINK)

To download and extract it, run:
```bash
wget -O dataset.zip "YOUR_DOWNLOAD_LINK"
unzip dataset.zip -d data/
