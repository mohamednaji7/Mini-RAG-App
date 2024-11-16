# AI Math Problems Solver Web App
## Description
- (In Progress)  

Building a web application to solve challenging math problems that standard Large Language Model (LLM) prompting cannot handle accurately. By integrating a Retrieval-Augmented Generation (RAG) system, this app enhances LLM capabilities by querying relevant mathematical resources and leveraging retrieved context to produce correct solutions.

This approach is based on my work in  the [AI Mathematical Olympiad](https://aimoprize.com/) particularly my participation in the [Progress Prize 2 competition](https://www.kaggle.com/competitions/ai-mathematical-olympiad-progress-prize-2/) on  Kaggle

Building with Python, the app focuses on providing accurate and detailed answers for advanced mathematical diffcult probelms.

This repository meant to features detailed code explanations, deployment instructions, and a live demo showcasing the tool's potential for researchers, students, and educators seeking a robust math-solving assistant.

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
