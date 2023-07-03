<template>
  <div id="app">
    <h1>VueTube Project</h1>
    <header>
      <TheSearchBar
        @search-result="showList"
      />
    </header>
    <section>
      <VideoDetail
        :video="selectedVideo"
      />
      <VideoList
        :videoList="videoList"
        @selected-video="selectedVideo"
      />      
    </section>
  </div>
</template>

<script>
import axios from 'axios'

import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      inputValue: null,
      videoList: [],
      video: null
    }
  },
  methods: {
    showList(inputText) {
      this.inputValue = inputText

      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.inputValue
        },
      })
        .then((response) => {
          this.videoList = response.data.items
        })
        .catch((error) => {
          console.log(error)
        })
    },
    selectedVideo(video) {
      this.video = video
    }
  },
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
</style>
