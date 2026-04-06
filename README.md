# Spark-WordCount
Assignment for CMPT 353 - Computational Data Science

This project implements a distributed WordCount application using PySpark. It reads text files from a directory, counts the occurrences of each word (ignoring case and punctuation), and outputs the results to a CSV file, sorted by descending frequency and alphabetically for ties.


## Table of Contents
1. [Navigation Guide](#1-navigation-guide)
2. [Installation](#install)
3. [Getting Started](#start)



<a name="navigation"></a>

## 1. Navigation Guide

```bash
repository
├── output/             ## store output CSV files
├── plots/              ## plots for blog post (dog-rates.ipynb)
├── wordcount-1/        ## input file for word count
├── Blog_Post.pdf       # Sample post for dog rates analysis
├── dog_rates_tweets.csv    ## input file for dog rates analysis
├── dog-rates.ipynb         ## code for dog rates analysis
├── wordcount.py            ## code for word count
```



<a name="install"></a>

## 2. Installation

This project requires using Python and the following Python libraries are used:
- pyspark

You can install the required libraries using the following command:
```bash
pip install pyspark
```


<a name="start"></a>

## 3. Getting Started

Suggestion: Use PyCharm to efficiently switch between algorithms.

#### 3.1. Clone and Navigate
```bash
# 1. Clone this repo to your local machine
git clone $THISREPO
# 2. Navigate into the repository directory
cd $THISREPO
```

#### 3.2. Run project
```bash
spark-submit wordcount.py <input_directory> <output_directory>
```
e.g. spark-submit wordcount.py wordcount-1 output

