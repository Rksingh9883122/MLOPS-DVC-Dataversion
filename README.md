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

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Key Features Comparison</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background-color: #f9f9f9;
    }
    h1 {
      text-align: center;
      color: #333;
    }
    table {
      width: 80%;
      margin: auto;
      border-collapse: collapse;
      background-color: #fff;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    th, td {
      padding: 12px 16px;
      border: 1px solid #ddd;
      text-align: center;
    }
    th {
      background-color: #4CAF50;
      color: white;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
    caption {
      caption-side: top;
      font-size: 1.2em;
      margin-bottom: 10px;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <h1>📊 Key Features Comparison</h1>

  <table>
    <caption>Git vs Git LFS vs DVC</caption>
    <thead>
      <tr>
        <th>Feature</th>
        <th>Git</th>
        <th>Git LFS</th>
        <th>DVC</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Large file tracking</td>
        <td>No</td>
        <td>Yes</td>
        <td>Yes</td>
      </tr>
      <tr>
        <td>Data pipelines</td>
        <td>No</td>
        <td>No</td>
        <td>Yes (dvc.yaml)</td>
      </tr>
      <tr>
        <td>Remote storage</td>
        <td>Limited to Git remotes</td>
        <td>Yes</td>
        <td>Yes (S3, GCS, Azure, SSH)</td>
      </tr>
      <tr>
        <td>Metrics & plots</td>
        <td>No</td>
        <td>No</td>
        <td>Yes (dvc metrics, plots)</td>
      </tr>
      <tr>
        <td>Reproducibility</td>
        <td>Partial</td>
        <td>No</td>
        <td>Full</td>
      </tr>
    </tbody>
  </table>

</body>
</html>


metrics:
  - metrics.json
  - plots:
    - confusion_matrix.png

dvc metrics diff
dvc plots diff
