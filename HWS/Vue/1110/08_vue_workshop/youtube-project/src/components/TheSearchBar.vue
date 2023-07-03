<template>
  <div>
    <input
      type="text"
      @keyup.enter="searchResult"
    >
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  methods: {
    searchResult(event) {
      this.$emit('search-result', event.target.value)
    }
  },
}
</script>

<style>

</style>