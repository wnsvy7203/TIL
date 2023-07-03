<template>
  <div>
    <h1>{{ lunchMenu }} 먹고 로또</h1>
    <button @click="getLottoNums">Get Lucky Numbers</button>
    <br>
    {{ lottoNums }}
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data() {
    return {
      lottoNums: null,
    }
  },
  props: {
    lunchMenu: String,
  },
  methods: {
    getLottoNums: function () {
      const nums = _.range(1, 46)
      this.lottoNums = _.sampleSize(nums, 6)
    }
  },
}
</script>

<style>

</style>