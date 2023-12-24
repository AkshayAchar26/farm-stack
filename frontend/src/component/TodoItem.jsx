import axios from "axios";
import React from "react";

function TodoItem(item) {
  console.log(item);
  const deletTodoHandler = (title) => {
    console.log(title);
    axios
      .delete(`http://localhost:8000/api/todo/${title}`)
      .then((res) => console.log(res.data));
  };

  return (
    <div>
      <p>
        <span> {item.item.title} :</span>
        {item.item.description}
        <button onClick={() => deletTodoHandler(item.item.title)}>X</button>
      </p>
    </div>
  );
}

export default TodoItem;
