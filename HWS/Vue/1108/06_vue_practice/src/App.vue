<template>
  <div id="app">
    <button @click="getCatImage"></button>
    <br>
    <img v-if="imgSrc" :src="imgSrc" alt="#" class="cat">
    <br>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      imgSrc: null,
    }
  },
  methods: {
    getCatImage() {
      const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'

      axios({
        methods: 'get',
        url: catImageSearchURL,
      })
        .then((response) => {
          const message = response.data[0].url
          this.imgSrc = message
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getCatImage()
  },
  mounted() {
    const btn = document.querySelector('button')
    btn.innerText = 'GIVE ME THE CAT'
  },
  updated() {
    console.log('이미지 리소스가 업데이트 되었습니다.')
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

.cat {
  height: 560px;
  width: 700px;
}
</style>
