# MLOPS-DVC-Dataversion
This repor represent idea of Data versioning using DVC tool
# 📦 Data Versioning with DVC

Streamline your machine learning workflows by versioning data and models with DVC (Data Version Control). Keep your Git history lean, track large files seamlessly, and reproduce experiments end to end.

---

## 🚀 Overview

DVC brings Git-like versioning to data, models, and pipelines. With DVC you can:

- Version datasets and models without bloating your repo  
- Define reproducible pipelines (`dvc.yaml`)  
- Store artifacts on remote cloud storage (S3, GCS, Azure)  
- Track metrics, plots, and experiments  

---

## 🗂 Project Structure


---

## 🛠 Installation

1. Clone the repo  
   ```bash
   git clone [https://github.com/your-username/my-ml-project.git](https://github.com/Rksingh9883122/MLOPS-DVC-Dataversion.git)
   cd my-ml-project

pip install dvc

dvc init
git commit -m "Initialize DVC"

dvc add data/raw/dataset.csv
git add data/.gitignore data/raw/dataset.csv.dvc
git commit -m "Track raw dataset with DVC"

dvc remote add -d storage s3://my-bucket/dvc-storage
git commit -m "Configure DVC remote storage"
dvc push

dvc run -n preprocess \
  -d src/train.py -d data/raw/dataset.csv \
  -o data/processed/train.csv \
  "python src/train.py"
git add dvc.yaml dvc.lock params.yaml
git commit -m "Add preprocessing stage"

dvc repro


![alt text](image.png)

metrics:
  - metrics.json
  - plots:
    - confusion_matrix.png

dvc metrics diff
dvc plots diff
