{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    │
    ├── {{cookiecutter.project_name}}       <- Source code for use in this project.
    │   ├── __init__.py    <- Makes project a Python module
    │   │
    │   ├── data           <- Scripts to data pre-processex (ploration and cleaning)
    │   │   ├── __init__.py    
    │   │   ├── load.py
    │   │   ├── cleaning.py
    │   │   ├── exploration.py
    │   │   └── util.py
    │   │
    │   ├── features       <- Scripts to feature selection and engineering
    │   │   ├── __init__.py    
    │   │   ├── selection.py
    │   │   ├── exploration.py
    │   │   ├── dataset.py
    │   │   └── util.py
    │   │
    │   ├── models         <- Scripts to model training and predictions
    │   │   ├── __init__.py    
    │   │   ├── model_component     <- Model backbone and loss function 
    │   │   │   └── __init__.py
    │   │   ├── optim_component     <- The optimizer for training
    │   │   │   └── __init__.py
    │   │   ├── metric_component    <- Metrics for evaluation  
    │   │   │   └── __init__.py
    │   │   ├── modeling.py
    │   │   ├── tuning.py
    │   │   ├── optimizer.py
    │   │   ├── evalution.py
    │   │   ├── train_model.py
    │   │   ├── predict_model.py
    │   │   └── util.py
    │   │
    │   └── dashboard       <- Scripts to create exploratory and results oriented visualizations
    │       ├── __init__.py  
    │       └── visualize.py
    │
    │
    ├── tests               <- Tests for `{{ cookiecutter.repo_name }}` package
    │   ├── conftest.py 
    │   ├── test_data
    │   ├── test_feature
    │   ├── test_model
    │   └── test_dashboard
    │
    ├── pytest.ini         <- To provide a consistent and customizable test execution environment
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://github.com/Hanyifan1019/cookiecutter-data-science/">cookiecutter data science project template</a>. #ibswufe-dea</small></p>
