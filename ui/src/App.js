import React from 'react'
import queryString from 'query-string';
import Styling from './Styling'
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};
    this.state = {userId: ''};
    this.state = {reports: ''};
    this.handleChange = this.handleChange.bind(this);
    
    //this.handleChangeUserId=this.handleChangeUserId.bind(this)
}
handleChange(event) {
  this.setState({value: event.target.value});
}
handleChangeUserId(event) {
  this.setState({userId: event.target.value});
}


handleSubmit() {
  
     if(this.state.value !== ""){ 

      var url='http://127.0.0.1:5000/recommendations?userId='+this.state.userId+'&city='+this.state.value;
     
        fetch('http://127.0.0.1:5000/recommendations?userId='+this.state.userId+'&city='+this.state.value,{
          
            method: "GET",
            dataType: "JSON",
            headers: {
              "Content-Type": "application/json; charset=utf-8",
            }
        })
        .then(response => response.json())
        .then(data => { 
            //console.log(JSON.stringify(data));
            <div>
              hello
            </div>
            //this.props.history.push(TodoList);
            this.setState({ reports: JSON.stringify(data)})

        });
      }

}
render(){
 

  var url= window.location.href;
  const parsed = queryString.parse(url);
  this.state.value=parsed.city;
  this.state.userId=parsed.userId;
  this.handleSubmit()
  // let url = this.props.location.search;
  // let params = queryString.parse(url);
  // console.log(params);
  let x="";
  if(this.state.reports!==""){

  var resonseFromTrawalmart=JSON.parse(this.state.reports);
  var list=resonseFromTrawalmart.items;
  var result = "<table border=1>";
  const items = list.map((val) =>{
    result += "<tr>";
    var itemDetail=val.split("::");
    var image=itemDetail[0];
    var desc=itemDetail[1];
    var url=itemDetail[2];
    result += "<td>"+"<img src="+ image+" width=\"100\" height=\"100\"></img></td>";
    result += "<td>"+desc+"</td>";
    result += "<td>"+"<a href=\""+url+"\">"+url+"</a>+</td>";
    result += "</tr>";

  });
  result += "</table>";

 
    
    x=<>
      <h1>Things you might need on your travel</h1>
     <div className="Container" dangerouslySetInnerHTML={{__html: result}}></div>
    </>
  }



 
return x;
}
}


export default App;
