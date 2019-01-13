<!-- Each component is a seperate file in the components folder with its own script and styling -->
<template>                            
	<div>
		<div v-bind:key="todo.id" v-for='todo in todos'>   <!-- foreach loop, key is optional -->
			<TodoItem v-bind:todo='todo' v-on:del-todo="$emit('del-todo', todo.id)" />      		   <!-- v-bind - Exporting the todo object to TodoItem, 
			v-on:del-todo - Continues the chain started on TodoItem.vue, sending the del-todo and todo.id further on back to App.vue -->
		</div>
	</div>
</template>

<script>
import TodoItem from './TodoItem.vue';

export default {
	name: "Todos",
	components: {
		TodoItem						// Using the imported TodoItem in Todos
	},
	props: ["todos"]                   // Importing todos from App.vue
}
</script>

<style scoped>
	
</style>