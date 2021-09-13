# A Simple Demo Application
This web application is developed using a Svelte client framework, deployed using Axios. The user interface communicates with a Python script using FastAPI and is deployed with Uvicorn.

## Backend Deployment
Plans are in place to implement a relational database of some sort.  But for a working case, the data is currently stored a json formatted file.

### Requirements
* [Python 3](https://www.python.org/)  
    Install according to your OS. You may want to install py `pip install py`  
* [FastAPI](https://fastapi.tiangolo.com/)  
    ```
    pip install fastapi
    ```
* [Uvicorn](https://www.uvicorn.org/)  
    ```
    pip install uvicorn[standard]
    ```

Once the requirements are installed run `python ./main.py` from the commandline in the project's API directory to start the API service. Visit `http://127.0.0.1:5000/docs` to view the available endpoints and to test the API.

## Frontend Deployment
Right now, the UI only demonstrates a simple `[GET]` call to the API, returning a list of recordsets. As development progresses, a full CRUD stack will be implemented.  If you are forking this project, you should be able to `npm install` within the `ui` directory without further configuration. 

### Requirements
* [Node](https://nodejs.org/)  
    Install according to your OS
* [Svelte](https://svelte.dev/)  
    ```
    npm install svelte
    ```
* [degit](https://www.npmjs.com/package/degit)  
    ```
    npx degit sveltejs/template my-svelte-project
    npm install
    ```
* [Axios](https://axios-http.com)  
    ```
    npm install axios
    ```    

Once all the pacakages are installed, start the service using `npm run dev`. The default deployment location is `http://127.0.0.1:5000`.  

### Additional notes
## Rollup Config
The default `rollup.config.js` presented issues using a vanilla install of Axios. `Line 7` and `Line 11` were added in the document to prevent the JSON errors.

## .gitignore
GitHub has a great resource for `.gitignore` templates.  If you plan on further expanding to other environments, it is recommended to look through them. This project implements the [Node.gitignore](https://github.com/github/gitignore) template.