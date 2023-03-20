# MOL3022


## Installation

### Anaconda

All commands for installing and running the program need to be executed in an Anaconda terminal

Install Anaconda by following the instructions on the following webpage https://docs.anaconda.com/anaconda/install/index.html . Use the installation guide fitted to your operating system

To open an Anaconda terminal, search for Anaconda in your operating system

### Node.js

To be able to run the client application, Node.js must be installed. Open https://nodejs.org/en/download and follow the instructions for downloading on your operating system

### Download project dependecies

Open an Anaconda terminal

```
conda create -n mol3022 python=3.9
conda activate mol3022
conda install -c conda-forge jupyterlab
pip install -r req.txt
```

## Running the program

### Starting the server

Before you are able to test the program, you need to start the server who manages the model predicting the secondary structures. The server must be up and running before the client application is stared

Start by opening an Anaconda terminal. Make sure the mol3022 environment is activated. If it is activated, the command line will have ```(mol3022)``` written at the start of the line. If ```(base)``` is written, activate the environment by endering the following command

```
conda activate mol3022
```

 After the correct terminal is opened, nagivate to the project folder. This is done using the command ```cd path```. The path is the folders that must be entered to get to the project files. Make sure you also enter the project folder. If you need to exit a folder, use ```cd ..``` to enter a higher level in the hierarchy

Heres an example
```bash
cd ../user/downloads/MOL3022
```

When you have reached the project foler, run the following command:

```bash
uvicorn main:app --reload
```

The server should now be running on ```http://127.0.0.1:8000```

If you get the error 
```bash 
Error loading ASGI app. Could not import module "main".
```
you have not managed to navigate to the correct folder

If you want to see the documentation of the server endpoint, go to the following URL: ```http://127.0.0.1:8000/docs```

The documentation is interactable and you are able to test the endpoint youself by clicking the ```Try it out``` button.

To stop the server, simply press ```Ctrl + c``` in the same terminal as the server is running

### Training the neural network

The neural network has already been trained and is located in the ```model_1.torch``` file. However, you are able to retrain the model yourself. Note that this may take some time

To train the model yourself, open a new Anaconda terminal, activate the mol3022 environment and maneuver to the project folder. This is the same folder as the server was stared in. Write the command

```bash
jupyter notebook
```

This will start a jupyter notebook at a local URL. The URL can be found in the terminal

When you have opened the URL, open the ```lstm.ipynb``` file. In the menu located at the top, click the ```kerkel tab``` and then ```Restart & Run All```

When all code blocks have a run number next to it, the model has finished training (the code blocks will have a * if it is still working on it). If the server already is up and running, it will automatically restart and use the newly trained model

To stop jupyter notebook, press ```Ctrl + c``` in the terminal

### Starting the client

To start the client application, open a new Anaconda terminal, activate the mol3022 environment, maneuver to the project folder and then into the ```frontend``` folder.

For example
```bash
cd ../user/downloads/MOL3022/frontend
```

Install the Node.js dependencies by entering
```bash
npm install
```

The application is then started with the following command
```bash
npm start
```

The client can be reacted at a local URL found in the terminal

To stop client application, press ```Ctrl + c``` in the terminal