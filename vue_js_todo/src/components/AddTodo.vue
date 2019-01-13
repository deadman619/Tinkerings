<template>
	<div>
		<form @submit="addTodo">                   <!-- At submit run addTodo -->
			<input type="text" v-model="title" name="title" placeholder="Add Todo...">
			<input type="submit" value="Submit" class="btn">
		</form>
	</div>
</template>

<script>
//import uuid from 'uuid';                    // npm install uuid, generates random ids, using jsonplaceholder so we don't need it now
export default {
	name: "AddTodo",
	data() {
		return {
			title: ''
		}
	},
	methods: {
		addTodo(e) {
			e.preventDefault();						// Prevent form from submitting
			const newTodo = {
				//id: uuid.v4(),                       // Different versions of uuid exist, calling version 4 here, using jsonplaceholder which creates the ID automatically so we don't need this now
				title: this.title,					// v-model title has the title from data() bound to it, so we can access it with this.title
				completed: false
			}
			this.$emit('add-todo', newTodo);        // Gotta send the newTodo back to App.vue after constructing it, so we have to use an $emit 
			this.title = '';						// Reset the input
		}
	}
}
</script>

<style scoped>
form {
	display: flex;
}
input[type='text'] {
	flex: 10;
	padding: 5px;
}
input[type='submit'] {
	flex: 2;
}
</style>