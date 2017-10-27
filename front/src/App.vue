<template>
  <div id="app">
    <navigation></navigation>
    <router-view/>
  </div>
</template>

<script>
import Navigation from '@/components/Navigation';

export default {
  name: 'app',
  components: { Navigation },
};
</script>

<style>
  body {
    font-family: 'Quicksand', sans-serif;
  }
  .page-title {
    margin: 25px;
    text-align: center;
  }
  .card {
    background: #fff;
    border-radius: 3px;
    padding: 10px;
    box-shadow: 0 0px 14px 0px rgba(0, 0, 0, 0.3);
    margin: 0 auto 1.6%;
    position: relative;
    padding-bottom: 20px;
    margin-bottom: 30px;
  }
  .card-title {
    color: gray;
    text-align: center;
    margin-top: 15px;
  }
  .card-title:hover {
    color: black;
  }
</style>
