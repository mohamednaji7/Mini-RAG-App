# IEEE-Papers-QA
## Description
IEEE-Papers-QA is a Retrieval-Augmented Generation (RAG) system built to query and extract answers from PDF documents, specifically focusing on IEEE technical papers. Leveraging a Large Language Model (LLM) for intelligent question answering, this tool is designed for researchers and engineers seeking quick insights from complex documents. Built in Python, it runs seamlessly in Google Colab, with clear step-by-step instructions for setup and usage. This repository includes explanations of the code and a demo to guide users through creating a powerful question-answering assistant.

## Environment
- conda  
- python 3.8 or later 

### Set-up
1) use this [doc](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for download and installation 
2) Create a new isolated conda environment 
    ```bash
    $ conda creat -n ieee-papers-qa-env python=3.8 
    ```
3) activate the environment
    ```bash
    $ source activate base 
    $ conda activate ieee-papers-qa-env
    ```
4) install requirements
    ```bash
    $ pip install -r requirements.txt
    ```

