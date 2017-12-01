import React, { Component } from 'react';

import './leaderboard.css';

class Leaderboard extends Component {
  constructor(props) {
    super(props)
    this.state = {selectedTab:"Singles"}
  }

  selectTab(tab) {
    if(tab==="Singles") {
      this.setState({selectedTab:"Singles"})
    }
    if(tab==="Doubles") {
      this.setState({selectedTab:"Doubles"})
    }
  }

  render() {
    const isActiveTab = (selectedTab) => {
      if (selectedTab === this.state.selectedTab) {
        return 'active'
      } else {
        return ''
      }
    }
    return (
      <div className="Leaderboard">
        <div className="singles-or-doubles">
          <div className={`singles tab ${isActiveTab("Singles")}`} onClick={()=>{this.selectTab("Singles")}}>
            {"Singles"}
          </div>
          <div className={`doubles tab ${isActiveTab("Doubles")}`}  onClick={()=>{this.selectTab("Doubles")}}>
            {"Doubles"}
          </div>
        </div>
        {
          this.state.selectedTab === "Singles" ? (
            <div className="singles leaderboard-tab">
              <div>
                {"Name"}
              </div>
              <div className="avatar">
              </div>
              <div>
                {"W/L"}
              </div>
            </div>
          ) : (
            <div className="doubles leaderboard-tab">
              <div>
                {"Name & Name"}
              </div>
              <div className="team-avatars">
                <div className="avatar">
                </div>
                <div className="avatar">
                </div>
              </div>
              <div>
                {"W/L"}
              </div>
            </div>
          )
        }
      </div>
    );
  }
}

export default Leaderboard;
