<template>
  <div>
    <h1>App</h1>
    <input
      type="text"
      v-model="appData"
    >
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <AppParent :app-data="appData" @parent-to-app="parentToApp" @child-to-app="childToApp"/>
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  data() {
    return {
      appData: null,
      parentData: null,
      childData: null
    }
  },
  components: {
    AppParent,
  },
  methods: {
    parentToApp: function(data) {
      this.parentData = data
    },
    childToApp: function(data) {
      this.childData = data
    }
  }
}
</script>

<style>

</style>
