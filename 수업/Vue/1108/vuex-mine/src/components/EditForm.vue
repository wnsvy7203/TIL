<template>
  <div>
    <input
      type="text"
      :value="message"
      @keyup.enter="doUpdate"
    >
  </div>
</template>

<script>
export default {
  name: 'EditForm',
  computed: {
    message() {
      return this.$store.getters.message
    }
  },
  methods: {
    doUpdate(event) {
      this.$store.dispatch('changeMessage', event.target.value)
    }
  }
}
</script>

<style>

</style>