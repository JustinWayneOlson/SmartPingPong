import React, { Component } from 'react';

import './registration.css';

class Registration extends Component {
  render() {
    return (
      <div className="Registration">
        <h2> Register: </h2>
        {"Office:"}
        <input type="text"/>
        <br/>
        {"Name:"}
        <input type="text"/>
        <br/>
        {"Avatar:"}
        <input type="file"/>
      </div>
    );
  }
}

export default Registration;
