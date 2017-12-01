import React, { Component } from 'react';

import './scoreboard.css';

class Scoreboard extends Component {
  render() {
    return (
      <div className="Scoreboard">
        <div className="team-container">
          <div className="left-team lesser-team-container">
            <div className="name-container">
              <div className="player-container">
                <div className="player-avatar"/>
                {"Name 1"}
              </div>
              <br/>
              <div className="player-container">
                <div className="player-avatar"/>
                {"Name 2"}
              </div>
            </div>
            <div className="score-container">
              {"1"}
            </div>
          </div>
          <div className="right-team lesser-team-container">
            <div className="score-container">
              {"2"}
            </div>
            <div className="name-container">
              <div className="player-container">
                <div className="player-avatar"/>
                {"Name 3"}
              </div>
              <br/>
              <div className="player-container">
                <div className="player-avatar"/>
                {"Name 4"}
              </div>
            </div>
          </div>
        </div>
        <div className="game-container">
          <div className="match-container">
            {"1"}
          </div>
          <div className="lesser-game-container">
            {"Game 3"}
          </div>
          <div className="match-container">
            {"1"}
          </div>
        </div>
      </div>
    );
  }
}

export default Scoreboard;
