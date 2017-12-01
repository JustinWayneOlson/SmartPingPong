import React, { Component } from 'react';
import Navbar from './components/navbar/navbar.js'
import Scoreboard from './components/scoreboard/scoreboard.js'

import './App.css'

class App extends Component {
  render() {
    return(
      <div className="App">
        <Navbar/>
        <Scoreboard/>
        <h1> Hello World </h1>
      </div>
    )
  }
}

export default App;
