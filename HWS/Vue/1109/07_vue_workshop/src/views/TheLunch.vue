<template>
  <div>
    <h1>Lunch</h1>
    <button @click="pickLunchMenu">Pick Lunch</button>
    <div v-show="menu">
      <p>{{ menu }}</p>
      <button @click="goLottoPage">Lotto 뽑으러가기</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data () {
    return {
      menus: ['짜장면', '짬뽕', '라면', '냉면', '비빔냉면', '국수'],
      menu: null,
    }
  },
  methods: {
    pickLunchMenu () {
      this.menu = _.sample(this.menus)
    },
    goLottoPage () {
      this.$router.push({ 
        name: 'lotto', 
        params: {
          lunchMenu: this.menu,
        }
      })
    }
  }
}
</script>

<style>

</style>