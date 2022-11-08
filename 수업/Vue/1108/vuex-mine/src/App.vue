<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <EditForm/>
  </div>
</template>

<script>
import EditForm from '@/components/EditForm'

export default {
  name: 'App',
  components: {
    EditForm,
  },
  computed: {
    message() {
      return this.$store.state.message
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
