# Nov 16, 2024 - Starting Documentation
I statred documenting the process of creating this project.  
What I have done so far? 
- make this project general rag app not the the math solver, IEEE papers rag app.
- managed to addd the mongodb database image and get up and running 
- amde the code in the CVM approch.  for now I only made  controllers , and models. and some helpers 
- requirments.txt file if up to the current state of the app  
- .gitignore ignores the docker file database, It saved in ./assets/docker/mongodb
- installed the WSL, windows subsystem ubunto and development in this system.
- using uvicorn python web server  
- made .env, compose.yml 
- made the routes:
    - uplaod: to uplaod the pdf file and save it to in the project folder 
    - post: to process the file and it chunks  
- controllers  
    - base controller: a base model for other ineretnce
    - project controller: handles project folders
    - data controlelr: it handels the writing process 
    - process controller:  to chunk the file 
- made some schemse 