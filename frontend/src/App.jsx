import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";
import TodoItem from "./component/TodoItem";

function App() {
  const [todoList, setTodoList] = useState([{}]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/todo")
      .then((res) => setTodoList(res.data));
  });

  const addTodoHandler = () => {
    axios
      .post("http://localhost:8000/api/todo/", {
        title: title,
        description: description,
      })
      .then((res) => console.log(res));

    setTitle("");
    setDescription("");
  };

  return (
    <>
      <h1>Todo App</h1>
      <input
        type="text"
        placeholder="title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <input
        type="text"
        placeholder="description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button onClick={addTodoHandler}>Add Todo</button>
      {todoList.map((todo) => (
        <div>
          <TodoItem item={todo} />
        </div>
      ))}
    </>
  );
}

export default App;
