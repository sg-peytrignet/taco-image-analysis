
<div align="center">
  <div class="column">
    <img src="https://raw.githubusercontent.com/wiki/pedropro/TACO/images/1.png" width="17%" hspace="3">
    <img src="https://raw.githubusercontent.com/wiki/pedropro/TACO/images/2.png" width="17%" hspace="3">
    <img src="https://raw.githubusercontent.com/wiki/pedropro/TACO/images/3.png" width="17%" hspace="3">
    <img src="https://raw.githubusercontent.com/wiki/pedropro/TACO/images/4.png" width="17%" hspace="3">
    <img src="https://raw.githubusercontent.com/wiki/pedropro/TACO/images/5.png" width="17%" hspace="3">
  </div>
</div>
<p align="center">
    <h1 align="center">♻️ TRASH-IMAGES-ANALYSIS ♻️</h1>
</p>

<p align="center">
	<img src="https://img.shields.io/github/license/sg-peytrignet/trash-images-analysis?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/sg-peytrignet/trash-images-analysis?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/sg-peytrignet/trash-images-analysis?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/sg-peytrignet/trash-images-analysis?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/TensorFlow-FF6F00.svg?style=flat&logo=TensorFlow&logoColor=white" alt="TensorFlow">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/PyTorch-EE4C2C.svg?style=flat&logo=PyTorch&logoColor=white" alt="PyTorch">
	<img src="https://img.shields.io/badge/Keras-D00000.svg?style=flat&logo=Keras&logoColor=white" alt="Keras">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<br>
	<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat&logo=SciPy&logoColor=white" alt="SciPy">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Kaggle-20BEFF.svg?style=flat&logo=Kaggle&logoColor=white" alt="Kaggle">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running trash-images-analysis](#-running-trash-images-analysis)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#acknowledgments)

---

##  Overview

HTTP error 429 for prompt `overview`

---

##  Notebooks

HTTP error 429 for prompt `features`

---

##  Repository Structure

```sh
└── trash-images-analysis/
    ├── LICENSE
    ├── README.md
    ├── data
    │   ├── TACO
    │   │   └── data
    │   │	├──batch_1/
    │   │	├──batch_2/
    │   │	├──batch_3/
    │   │	├──batch_.../
    │   │	├──batch_15/
    │   │       └── annotations.json
    │   ├── features
    │   │   └── classification-labels.npz
    │   └── kaggle.json
    ├── environment.yml
    ├── helpers.py
    ├── notebooks
    │   ├── 01_download_data.ipynb
    │   ├── 02_exploratory_data_analysis.ipynb
    │   ├── 03_image_processing_for_ML_models.ipynb
    │   ├── 04_classifying_objects.ipynb
    │   └── 05_segmenting_images.ipynb
    └── saved_models
        └── widen_param_0.05
            └── segm_model.h5
```

---

##  Modules

<details closed><summary>helper functions and virtual environment setup</summary>

| File                                                                                                  | Summary                                     |
| ---                                                                                                   | ---                                         |
| [helpers.py](https://github.com/sg-peytrignet/trash-images-analysis/blob/master/helpers.py)           | `helpers.py`      |
| [environment.yml](https://github.com/sg-peytrignet/trash-images-analysis/blob/master/environment.yml) | `environment.yml` |

</details>

<details closed><summary>analysis notebooks</summary>

| File                                                                                                                                                            | Summary                                                                       |
| ---                                                                                                                                                             | ---                                                                           |
| [01_download_data.ipynb](https://github.com/sg-peytrignet/trash-images-analysis/blob/master/notebooks/01_download_data.ipynb)                                   | `notebooks/01_download_data.ipynb`                  |
| [05_segmenting_images.ipynb](https://github.com/sg-peytrignet/trash-images-analysis/blob/master/notebooks/05_segmenting_images.ipynb)                           | `notebooks/05_segmenting_images.ipynb`              |
| [04_classifying_objects.ipynb](https://github.com/sg-peytrignet/trash-images-analysis/blob/master/notebooks/04_classifying_objects.ipynb)                       | `notebooks/04_classifying_objects.ipynb`            |
| [02_exploratory_data_analysis.ipynb](https://github.com/sg-peytrignet/trash-images-analysis/blob/master/notebooks/02_exploratory_data_analysis.ipynb)           | `notebooks/02_exploratory_data_analysis.ipynb`      |
| [03_image_processing_for_ML_models.ipynb](https://github.com/sg-peytrignet/trash-images-analysis/blob/master/notebooks/03_image_processing_for_ML_models.ipynb) | `notebooks/03_image_processing_for_ML_models.ipynb` |

</details>

---

##  Getting Started

***Requirements***

Ensure you have conda installed on your system before creating the environment. You can refer to the official conda documentation for [installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/).

Ensure you have the following dependencies installed on your system:

* **JupyterNotebook**: `version v7.1.3 `

###  Installation

1. Clone the trash-images-analysis repository:

```sh
git clone https://github.com/sg-peytrignet/trash-images-analysis
```

2. Change to the project directory:

```sh
cd trash-images-analysis
```

3. Install the dependencies with conda:

```sh
# We recommend installing the libmamba solver, which is faster
conda install -n base conda-libmamba-solver

# Create new environment called 'taco-env' with the required packages 
conda env create -n taco-env -f environment.yml --solver mamba

# Activate the new environment
conda activate taco-env
```

###  Running trash-images-analysis

Run each notebook in the IDE of your choice, such as JupyterLab or Visual Studio.

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/sg-peytrignet/trash-images-analysis/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/sg-peytrignet/trash-images-analysis/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/sg-peytrignet/trash-images-analysis/issues)**: Submit bugs found or log feature requests for Trash-images-analysis.

---

##  License

This project is protected under the [MIT]([https://choosealicense.com/licenses](https://github.com/sg-peytrignet/trash-images-analysis/blob/main/LICENSE)) License.

---

##  Acknowledgments

- Thank you to the resources published by [Dr. Sreenivas Bhattiprolu](https://github.com/bnsreenu/python_for_microscopists/blob/master/335%20-%20Converting%20COCO%20JSON%20annotations%20to%20labeled%20mask%20images/335d-convert_coco_to_labeled_masks.py), which were useful to pre-process image data and annotations in the COCO-Json format.
- And thank you to my supervisors at the Ecole Polytechnique Federale de Lausanne for their guidance on carrying out this project.

[**Return**](#-quick-links)

---
