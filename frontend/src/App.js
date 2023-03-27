import './App.css';
import { useState, useRef } from 'react';

/* This is the main client application file */


function App() {

  /* Variables that hold the sequences */
  const structureInputRef = useRef();
  const [structure, setStructure] = useState("");
  const [resultStructure, setResultStructure] = useState("");

  /* The function that runs once a user clicks the submit button */
  async function submitHandler(event) {
    event.preventDefault();
    const enteredStructure = structureInputRef.current.value;
    const structureData = {
      sequence: enteredStructure
    }
    /* A post request that sends the written sequence to backend, where it uses
    the calculations there and recieves a response*/
    const response =  await fetch(' http://127.0.0.1:8000/sequence', {
                            method: 'POST',                                
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify(structureData),
                        }).then(async (res) => {
                            const data = await res.json()
                            console.log(data)
                            setResultStructure(data.structure)
                        })

  }


  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={submitHandler}>
          <label>Enter your structure:
            <input 
              type="text" 
              ref={structureInputRef}
              onChange={(e) => setStructure(e.target.value)}
            />
          </label>
          <input type="submit" />
        </form>
        <h2>Result: </h2>
        <h4>{resultStructure}</h4>
      </header>
    </div>
  );
}

export default App;

