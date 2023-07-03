<template>
  <div v-if="videoList.length">
    <VideoListItem
      v-for="video in extraVideos"
      :video=video
      :key="video.id.videoId"
      @selected-video="selectedVideo"
    />
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videoList: Array,
  },
  computed: {
    extraVideos() {
      return this.videos.slice(1)
    }
  },
  methods: {
    selectedVideo(video) {
      this.$emit('selected-video', video)
    }
  }
}
</script>

<style>

</style>