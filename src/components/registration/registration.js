import React, { Component } from 'react';

import './registration.css';

class Registration extends Component {
  render() {
    return (
      <div className="Registration">
        <h2> Register: </h2>
        {"Name:"}
        <input type="text"/>
        <br/>
        {"Employee #:"}
        <input type="text"/>
        <br/>
        {"Avatar:"}
        <input type="file"/>
      </div>
    );
  }
}

export default Registration;
