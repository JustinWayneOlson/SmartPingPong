import React, { Component } from 'react';
import Navbar from './components/navbar/navbar.js'
import Scoreboard from './components/scoreboard/scoreboard.js'
import Modal from './components/modal/modal.js'

import './App.css'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {modalOpen:false}
  }
  render() {
    return(
      <div className="App">
        <Navbar/>
        <Scoreboard/>
        <button className="Queue-button" onClick={() => {
          this.setState({modalOpen:true})
        }}> Queue </button>
        {
          this.state.modalOpen === true ? <Modal onClose={() => {
            this.setState({ modalOpen: false })
          }}/> : null
        }
        <h1> Hello World </h1>
      </div>
    )
  }
}

export default App;
