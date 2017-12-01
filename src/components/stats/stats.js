import React, { Component } from 'react';

import './stats.css';

class Stats extends Component {
  render() {
    return (
      <div className="Stats">
        <br/>
        {"Your Stats:"}
        <br/>
        <br/>
        {"Singles"} {"W/L"}
        <br/>
        <br/>
        {"Doubles"} {"W/L"}
        <br/>
        <br/>
        {"Best Partner"} {"Super Human Name"}
        <br/>
        <br/>
        {"Last Game"} {"Singles/Doubles"} {"Partner Name"} {"Score"}
        <br/>
        <br/>
      </div>
    );
  }
}

export default Stats;
