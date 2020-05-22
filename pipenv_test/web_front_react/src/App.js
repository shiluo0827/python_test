import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Button} from 'antd';
import axios from 'axios';

class Data extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      getdata: '无数据',
      btntext: '获取数据'
    };
    this.btnclick = this.btnclick.bind(this);
  }

  btnclick() {
    let  url="https://xllsib-8000-moqyoi.access.myide.io/";
    axios.get(url)
      .then((response)=>{
        let data = response.data;
        this.setState({getdata: data, btntext: '已获取'})
      })
      .catch(function (error) {
        console.log(error);
      });
  }
 
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <div>{this.state.getdata}</div>
        <Button type="danger" onClick={this.btnclick}>{this.state.btntext}</Button>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Data />
      </header>
    </div>
  );
}

export default App;
