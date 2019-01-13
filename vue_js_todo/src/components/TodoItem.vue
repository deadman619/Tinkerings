<template>
	<div class='todo-item' v-bind:class="{'is-complete':todo.completed}">  <!-- Conditional, if true then get class --> 
		<p>
			<input type="checkbox" v-on:change="markComplete">     <!-- On change execute function -->
			{{todo.title}}				<!-- Using the todo object imported from Todos.vue -->
			<button @click="$emit('del-todo', todo.id)" class='del'>x</button>     <!-- @ and v-on does the same thing (probably not, but it does here :^) ), $emit sends the event to the component that imports this component, so Todos.vue in this case  -->
		</p>       				
	</div>
</template>

<script>
export default {
	name: "TodoItem",
	props: ['todo'],
	methods: {								// Function/method definitions
		markComplete() {
			this.todo.completed = !this.todo.completed;
		}
	}
}
</script>

<style scoped>
.todo-item {
	background-color: #f4f4f4;
	padding: 10px;
	border-bottom: 1px #ccc dotted;
}
.is-complete {
	text-decoration: line-through;
}
.del {
	background: #ff0000;
	color: #fff;
	border: none;
	padding: 5px 9px;
	border-radius: 8px;
	cursor: pointer;
	float: right;
}
</style>