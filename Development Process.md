# Nov 16, 2024 - Starting Documentation
I started documenting the process of creating this project.  
What I have done so far? 
- make this project general rag app not the the math solver, IEEE papers rag app.
- managed to add the mongodb database image and get up and running 
- made the code in the CVM approach.  for now I only made  controllers , and models. and some helpers 
- requirements.txt file if up to the current state of the app  
- .gitignore ignores the docker file database, It saved in ./assets/docker/mongodb
- installed the WSL, windows subsystem Ubuntu and development in this system.
- using uvicorn python web server  
- made .env, compose.yml 
- made the routes:
    - uplaod: to uplaod the pdf file and save it to in the project folder 
    - post: to process the file and it chunks  
- controllers  
    - base controller: a base model for other inheritance
    - project controller: handles project folders
    - data controller: it handles the writing process 
    - process controller:  to chunk the file 
- made some scheme 