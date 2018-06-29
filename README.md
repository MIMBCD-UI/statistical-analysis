# Statistical Analysis

<img src="https://github.com/mida-project/meta/blob/master/banners/statistical-analysis.png?raw=true"/>

This repository aims to assemble a set of [`methods/`](methods/) for our statistical analysis. We use several statistical models (e.g.: [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance), [Kruskal-Wallis One-Way Analysis of Variance](https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_one-way_analysis_of_variance), [Mann-Whitney U test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test), etc...) to analyse our data and deeper understanding it. For instance, we used the [Kruskal-Wallis One-Way Analysis of Variance](https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_one-way_analysis_of_variance) for our [ISS'17](https://iss2017.acm.org/) Publications ([Paper](https://dl.acm.org/citation.cfm?id=3134111) & [Poster](https://iss2017.acm.org/program/posters/#iss43-ex)) for the **Results** analysis of our data. The hereby repository is dependent from the [sheet-reader](https://github.com/MIMBCD-UI/sheet-reader) repository, so please first of all clone that to your machine.

## Pre-Requisites

To run the various methods available on the `methods/` directory, it is needed:

- [Python 2.6](https://www.python.org/download/releases/2.6/) or [latest](https://www.python.org/downloads/);

- The [pip](https://pypi.org/project/pip/) package management tool;

## Instructions

The instructions are as follows. We assume that you already have knowledge over [Git](https://git-scm.com/) and [GitHub](https://github.com/). If not, please follow this [support](https://guides.github.com/activities/hello-world/) information. Any need for support, just open a [New issue](https://github.com/MIMBCD-UI/statistical_analysis/issues/new).

### Clone

To clone the hereby repository follow the guidelines. It is easy as that.

1.1. Please clone the repository by typing the command:

```
git clone https://github.com/MIMBCD-UI/statistical-analysis.git
```

1.2. Get inside of the repository directory:

```
cd statistical-analysis/
```

1.3. For the installation and running of the source code, follow the next steps;

### Install

The installation guidelines are as follows. Please, be sure that you follow it correctly.

2.1. Run the following command to install the [library](https://github.com/google/google-api-python-client) using [pip](https://pypi.org/project/pip/):

```
pip install --upgrade google-api-python-client
```

2.2. Follow the next step;

### Run

The running guidelines are as follows. Please, be sure that you follow it correctly.

3.1. Run the sample using the following command:

```
python3 src/main.py
```

3.2. Enjoy our source code!

### Notebooks

You can also run a Notebook to watch some of our `methods` chart plots. For this goal we are using the well known [Jupyter Notebook](http://jupyter.org/) web application. To run the [Jupyter Notebook](http://jupyter.org/) just follow the steps.

4.1. Get inside our project directory:

```
cd statistical-analysis/
```

4.2. Run [Jupyter Notebook](http://jupyter.org/) application by typing:

```
jupyter notebook
```

> If you have any question regarding the [Jupyter Notebook](http://jupyter.org/) just follow their [Documentation](http://jupyter.org/documentation). You can also ask for help close to the [Community](http://jupyter.org/community).

## Information

As far as we have to do several statictical analysis over our users, we need to address their results by calculating a set of measures. This measures will gave us a better understanding regarding how users are aiming to interact with our systems. Therefore it is of chief importance to scale this solution for a spreadsheet template-like where we can duplicate the same document and apply this group of source code to consume our data each time we need it.

### Acknowledgements

We would like to convey [Google](https://google.com) from their [Google Sheets API Documentation](https://developers.google.com/sheets/api/guides/concepts). This repository source code is based on [Google](https://google.com)'s [Python Quickstart](https://developers.google.com/sheets/api/quickstart/python) guide.

### Authors

- [Francisco Maria Calisto](http://www.franciscocalisto.me/) [[ResearchGate](https://www.researchgate.net/profile/Francisco_Maria_Calisto) | [GitHub](https://github.com/FMCalisto) | [Twitter](https://twitter.com/FMCalisto) | [LinkedIn](https://www.linkedin.com/in/fmcalisto/)]
