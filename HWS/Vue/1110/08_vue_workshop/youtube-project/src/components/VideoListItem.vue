<template>
  <div @click="selectedVideo">
    <img :src="youtubeImgSrc" alt="#">
    <h3>{{ unescape }}</h3>
    <p>{{ videoDesc }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    youtubeImgSrc() {
      return this.video.snippet.thumbnails.default.url
    },
    videoDesc() {
      return this.video.snippet.description
    },
    unescape() {
      return _.unescape(this.video.snippet.title)
    }
  },
  methods: {
    selectedVideo() {
      this.$emit('selected-video', this.video)
    }
  }
}
</script>

<style>

</style>