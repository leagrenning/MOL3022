# MOL3022


## Installation
```
conda create -n mol3022 python=3.9
conda activate mol3022
conda install -c conda-forge jupyterlab
pip install -r req.txt
```

## Running the program

### Starting the server

Before you are able to test the program, you need to start the server which communicates with the model predicting the secondary structures.

Start by opening a command window and nagivate to the project folder. This is done using the command ```cd path```. The path is the folders that must be entered to get to the project files. Make sure you also enter the project folder. 

Heres an example
```bash
cd user/downloads/MOL3022
```

When you have reached the project foler, run the following command:

```bash
uvicorn main:app --reload
```

The server should now be running on ```http://127.0.0.1:8000```. 

If you get the error 
```bash 
Error loading ASGI app. Could not import module "main".
```
you have not managet to navigate to the correct folder.

If you want to see the documentation of the server endpoint, go to the following URL ```http://127.0.0.1:8000/docs```

The documentation is interactable and you are able to test the endpoint youself by clicking the ```Try it out``` button.

To stop the server, simply press ```Ctrl + c``` in the command window where the server is running.