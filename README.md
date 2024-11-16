# Mini RAG Web App (In Progress) 
## Description 

building a mini RAG app to be a base app for my future apps. 
- Math solver app with RAG and LLM 
- CV raking per job posting 
- IEEE papers questions and answer app


## Environment
python 3.8 or later  
- download and install
    - mongodb   
        - docker         
    - [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)        

### Set-up
0) clone this repo in your system
    ```bash
    git clone https://github.com/mohamednaji7/Mini-RAG-App.git 
    ```
    or click Code > Download ZIP > extract it 
1) change the current directory
    ```bash
    cd Mini-RAG-App/src
    ```
2) Create a new isolated conda environment 
    ```bash
    conda create -n mini-rag-env python=3.8 
    ```
3) activate the environment
    ```bash
    source activate base 
    conda activate mini-rag-env
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
