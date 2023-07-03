<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="pickLunchMenu">Pick One</button>
    <br>
    <p>{{ pickMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data() {
    return {
      lunchList: ['햄버거', '짜장면', '국밥'],
      pickMenu: null,
    }
  },
  methods: {
    pickLunchMenu: function () {
      this.pickMenu = _.sample(this.lunchList)
      this.$emit('get-menu', this.pickMenu)
    }
  }
}
</script>

<style>

</style>