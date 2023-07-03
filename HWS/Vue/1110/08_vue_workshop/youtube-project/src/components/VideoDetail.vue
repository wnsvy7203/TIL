<template>
  <div v-if="video">
    <iframe :src="videoURI" frameborder="0"></iframe>
    <h2>{{ video.snippet.title | unescape }}</h2>
    <p>{{ video.snippet.description | unescape }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: Object,
  },
  computed: {
    videoURI() {
      return `https://www.youtube.com/embed/${ this.video.id.videoId }`
    }
  },
  filters: {
    unescape(rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>

</style>