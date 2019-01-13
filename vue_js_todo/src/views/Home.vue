<template>
  <div id="app">
    <AddTodo v-on:add-todo="addTodo" />                   <!-- Catching the emit from AddTodo.vue -->
    <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo"/>   <!-- Using imported components as a tag, exporting todos data to Todos.vue, catches the del-todo that started in TodoItem and runs the delete function-->
  </div>
</template>

<script>
import AddTodo from '../components/AddTodo'
import Todos from '../components/Todos';                  // Importing components
import axios from 'axios';                              // Axios is a library for get requests, etc.

export default {
  name: 'Home',
  components: {                                         // Declaring which imported components to use
    Todos,
    AddTodo
  },
  data() {                                              // Function for defining data
    return {
      todos: []
    }
  },
  methods: {
    deleteTodo(id) {
      axios.delete(`https://jsonplaceholder.typicode.com/todos/${id}`)
      .then(res => this.todos = this.todos.filter(todo => todo.id !== id))    // Changes the todos with filter, only keeping the ones that don't have the id that called the function
      .catch(err => console.log(err));
    },
    addTodo(newTodo) {
      const {title, completed} = newTodo;               //jsonplaceholder creates the ID automatically so we only need title and completion status
      axios.post('https://jsonplaceholder.typicode.com/todos', {
        title,
        completed
      })
      .then(res => this.todos = [...this.todos, res.data])
      .catch(err => console.log(err));
    }
  },
  created() {                                             // Created means it runs as soon as the app loads 
    axios.get('https://jsonplaceholder.typicode.com/todos?_limit=10')
    .then(res => this.todos = res.data)                   // Gets the response from axios, then sets the todos to the gotten data
    .catch(err => console.log(err))                      // If there's an error, it console logs it
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.4;
}
.btn {
  display: inline-block;
  border: none;
  background: #555;
  color: #fff;
  padding: 7px 20px;
  cursor: pointer;
}
.btn:hover {
  background: #666;
}
</style>
