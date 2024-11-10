# IEEE-Papers-QA
## Description
IEEE-Papers-QA is a Retrieval-Augmented Generation (RAG) system built to query and extract answers from PDF documents, specifically focusing on IEEE technical papers. Leveraging a Large Language Model (LLM) for intelligent question answering, this tool is designed for researchers and engineers seeking quick insights from complex documents. Built in Python, it runs seamlessly in Google Colab, with clear step-by-step instructions for setup and usage. This repository includes explanations of the code and a demo to guide users through creating a powerful question-answering assistant.

## Environment
python 3.8 or later  
- download and install
    - mongodb   
        - docker         
    - [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)        

### Set-up
0) clone this repo in your system
    ```bash
    git clone https://github.com/mohamednaji7/IEEE-Papers-QA.git 
    ```
    or click Code > Download ZIP > extraxt it 
1) chnage current directory
    ```bash
    cd IEEE-Papers-QA/src
    ```
2) Create a new isolated conda environment 
    ```bash
    conda creat -n ieee-papers-qa-env python=3.8 
    ```
3) activate the environment
    ```bash
    source activate base 
    conda activate ieee-papers-qa-env
    ```
4) install requirements
    ```bash
    pip install -r requirements.txt
    ```

5) setting the mongodb docker image
    ```bash
    docker compose up -d
    ```
6) setting the mongodb database 
    ```bash
    docker exec -it mongodb mongosh
    use rag-database
    show dbs
    exit
    ```
7) run the server
    ```bash
    uvicorn main:app --reload
    ```
    the `--reload` is to force reload the server when the base code is edited
