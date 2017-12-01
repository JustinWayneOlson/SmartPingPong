import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import './modal.css';

class Modal extends Component {
  render() {
    return ReactDOM.createPortal(
      (
        <div className="Backdrop" onClick={this.props.onClose}>
          <div className="Modal">
            <div className="current-queue-container">
              {"Current Queue:"}
              <div className="current-queue-list">
                {"Name 1 vs Name 2"}
              </div>
            </div>
            <div className="add-to-queue-container">
              <div className="type-of-game-container">
                {"Singles"}
                <input type="radio"/>
                {"Doubles"}
                <input type="radio"/>
              </div>
              <div className="who-to-add-queue">
                <div className="player">
                  {"Name 1"}
                </div>
                <div className="vs">
                  {"vs."}
                </div>
                <div className="player">
                  <input type="text"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      ),
      document.getElementById('modal-container')
    )
  }
}

export default Modal;
