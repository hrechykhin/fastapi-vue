<template>
  <div class="container">
    <h2>Todo List</h2>
    <form @submit.prevent="addTodo">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="title" class="form-control">
      </div>
      <div class="form-group">
        <label for="description">Description:</label>
        <input type="text" id="description" v-model="description" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Add Todo</button>
    </form>
    <ul class="list-group mt-4">
      <li v-for="todo in todos" :key="todo.id"
          class="list-group-item d-flex justify-content-between align-items-center">
          <span>
            <strong>{{ todo.title }}</strong>: {{ todo.description }}
          </span>
        <button @click="deleteTodo(todo.id)" class="btn btn-danger btn-sm">✖</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

const API_BASE = process.env.VUE_APP_API_BASE;

export default {
  name: 'TodoList',
  data() {
    return {
      title: '',
      description: '',
      todos: []
    };
  },
  async mounted() {
    await this.fetchTodos();
  },
  methods: {
    async fetchTodos() {
      try {
        const response = await axios.get(`${API_BASE}/todos`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        });
        this.todos = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addTodo() {
      try {
        const response = await axios.post(`${API_BASE}/todos`, {
          title: this.title,
          description: this.description
        }, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        });
        this.todos.push(response.data);
        this.title = '';
        this.description = '';
      } catch (error) {
        console.error(error);
      }
    },
    async deleteTodo(todoId) {
      console.log(1, todoId)
      try {
        await axios.delete(`${API_BASE}/todos/${todoId}`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        });
        this.todos = this.todos.filter(todo => todo.id !== todoId);
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style>
/* Add any global styles here if needed */
</style>
  