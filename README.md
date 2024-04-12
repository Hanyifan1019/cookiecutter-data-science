# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 3.6+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter git@github.com:Hanyifan1019/cookiecutter-data-science.git



### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
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
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://github.com/Hanyifan1019/cookiecutter-data-science).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
