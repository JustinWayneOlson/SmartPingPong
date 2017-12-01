import React, { Component } from 'react';
import Navbar from './components/navbar/navbar.js'
import Scoreboard from './components/scoreboard/scoreboard.js'
import Modal from './components/modal/modal.js'
import Stats from './components/stats/stats.js'
import Leaderboard from './components/leaderboard/leaderboard.js'

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
        <div className="leaderboard-and-stats">
          <Leaderboard/>
          <Stats/>
        </div>
      </div>
    )
  }
}

export default App;
