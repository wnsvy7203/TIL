<template>
  <div>
    <h1>{{ lunchMenu }} 먹고 Lotto 추첨</h1>
    <button @click="pickLottoNumbers">Pick Numbers</button>
    <div v-show="lottoNums">
      <p>{{ lottoNums }}</p>
      <button @click="goLunchPage">처음으로</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data () {
    return {
      lottoNums: null,
      lunchMenu: this.$route.params.lunchMenu,
    }
  },
  methods: {
    pickLottoNumbers () {
      const numbers = _.range(1, 46)
      this.lottoNums = _.sampleSize(numbers, 6)
    },

    goLunchPage () {
      this.$router.push({ name: 'lunch' })
    }
  }

}
</script>

<style>

</style>