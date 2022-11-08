// App.vue

<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 

  methods: {
    increase() {
      return this.$store.dispatch('increase')
    },
    decrease() {
      return this.$store.dispatch('decrease')
    },
  },
  computed: {
    counter() {
      return this.$store.state.counter
    },
    counterDouble() {
      return this.$store.getters.counterDouble
    },
  },
}
</script>

<style>
</style>
