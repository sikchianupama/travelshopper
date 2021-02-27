import React from 'react'
import TodoList from './TodoList'
import Styling from './Styling'
class TodoList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};
  
}

render(){
  return(
<>
<Styling/>


</>

  );
}
}


export default TodoList;
