<template>
  <b-container>
    <div class="card">
      <h3 class="card-title">{{res.title}} Statistics</h3>
      <b-row>
        <b-col>
          <strong>Match Error:</strong> {{res.match_error}}
        </b-col>
        <b-col>
          <strong>Time Spent:</strong> {{methodSpeed}}
        </b-col>
        <b-col>
          <strong>Memory Spent:</strong> {{res.memory}}
        </b-col>
      </b-row>
      <b-row>
        <b-col><strong>Cluster Sizes:</strong></b-col>
        <b-col v-for="(count, index) in res.clusters_sizes" :key="index"><span :style="{ color: pointsColors[index] }">{{pointsColors[index]}}</span> - {{count}}</b-col>
      </b-row>
      <b-row>
        <b-col><strong>Cluster Sizes Errors:</strong></b-col>
        <b-col v-for="(count, index) in res.clusters_sizes_error" :key="index"><span :style="{ color: pointsColors[index] }">{{pointsColors[index]}}</span> - {{Math.abs(count)}}</b-col>
      </b-row>
    </div>
  </b-container>
</template>

<script>
export default {
  props: ['res'],
  data() {
    return {
      pointsColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
    };
  },
  computed: {
    methodSpeed() {
      return Math.abs(this.res.speed);
    },
  },
};
</script>

<style>

</style>
