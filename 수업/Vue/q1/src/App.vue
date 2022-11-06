<template>
  <div id="app">
    <header class="title">
      <h1>버튼 박스 제작</h1>
    </header>
    <section class="wrap">
      <div class="time-wrap">
        <h2>예약 페이지</h2>
        <h3>시간 선택</h3>
        <div class="timebox">
          <span class="timebtn" :class="{'selected-timebtn': isSelected(time)}" v-for="(time, index) in times" :key="index" @click="selectTime(time)">{{ time }}</span>
        </div>
        <div class="divider"></div>
        <div>
          <h3 v-if="!selectedTimes.length">시간을 선택해 주세요.</h3>
          <h3 v-else>선택 시간 : <span class="eachtime" v-for="(time, index) in selectedTimes" :key="index">{{ time }}</span></h3>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectedTimes: [],
    }
  },
  methods: {
    selectTime(time) {
      if (this.selectedTimes.includes(time)){
        const time_idx = this.selectedTimes.indexOf(time);
        this.selectedTimes.splice(time_idx, 1);
      } else {
        if (this.selectedTimes.length === 5) {
          alert('5타임까지만 신청할 수 있습니다.')
          return
        }
        this.selectedTimes.push(time)
      }
    },
    isSelected(time) {
      if (this.selectedTimes.includes(time)) {
        return true
      } else {
        return false
      }
    },
  }
}
</script>

<style>
  * {
    font-family: 'Noto Sans KR', sans-serif;
    color: #424242;
  }

  #app {
    min-width: 900px;
  }

  .title {
    text-align: center;
  }

  .wrap {
    display: flex;
    box-shadow : rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
    width: 520px;
    margin: 0 auto;
  }

  .time-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .timebox {
    width: 530px;
    display: flex;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }

  .timebtn {
    background-color: transparent;
    border: transparent;
    color: #84898C;
    font-size: 16px;
    margin-top: 2px;
    margin-bottom: 2px;
    width: 65px;
    text-align: center;
    cursor: pointer;
  }

  .selected-timebtn {
    background-color: #658dc63d;
    border: transparent;
    color: #0F4C81;
    font-size: 16px;
    margin-top: 2px;
    margin-bottom: 2px;
    width: 65px;  
  }

  .divider {
    border-top: 1px solid #0F4C81;
    width: 80%;
    margin-top: 20px;
  }

  .eachtime {
    display: inline-block;
    margin: 0 5px;
  }
</style>
