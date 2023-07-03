<template>
  <div>
    <h1>AppParent</h1>
    <input
      type="text"
      v-model="parentData"
      @input="parentToApp"
    >
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <AppChild :app-data="appData" :parent-data="parentData" @child-to-parent="childToApp"/>
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  data() {
    return {
      parentData: null,
      childData: null,
    }
  },
  components: {
    AppChild
  },
  props: {
    appData: String
  },
  methods: {
    parentToApp: function() {
      this.$emit('parent-to-app', this.parentData)
    },
    childToApp: function(data) {
      this.childData = data
      this.$emit('child-to-app', data)
    }
  }
}
</script>

<style>

</style>
