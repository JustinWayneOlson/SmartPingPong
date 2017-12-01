import React, { Component } from 'react';
import Navbar from './components/navbar/navbar.js'
import Scoreboard from './components/scoreboard/scoreboard.js'
import Modal from './components/modal/modal.js'
import Stats from './components/stats/stats.js'
import Leaderboard from './components/leaderboard/leaderboard.js'
import Registration from './components/registration/registration.js'

import './App.css'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = { modalOpen: false, userRegistered: false}
  }
  componentDidMount(){
    fetch('https://localhost:8888/isUserRegistered/12',
    {
      method: "GET",
      header: {
        "Content-Type": "application/json",
        'Access-Control-Allow-Origin':'*'
      }
    }).then((res) => {
      res.json().then((response) => {
        this.setState((prevState, props) => {
          console.log(response)
          return {userRegistered: response.response}
        })
      }).catch((err) => {
        console.log(err)
      })
    })
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
          {
            this.state.userRegistered === "true" ? <Stats/> : <Registration/>
          }
        </div>
      </div>
    )
  }
}

export default App;
