<template>
  <div class="card"> 
    <h3 class="card-title" @click="showChart = !showChart">{{title}}</h3>
    <div class="chart" v-show="showChart">
      <scatter-chart v-if="pure" :data="pureData" :xtitle="rowNames[0]" :ytitle="rowNames[1]"></scatter-chart>
      <scatter-chart v-if="!pure" :data="coloredData" :xtitle="rowNames[0]" :ytitle="rowNames[1]"></scatter-chart>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'chartRows', 'pure'],
  data() {
    return {
      showChart: true,
      pointsColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
    };
  },
  computed: {
    rowNames() {
      return this.$store.state.rowNames;
    },
    pureData() {
      return this.chartRows.map(el => el.slice(1, el.length));
    },
    coloredData() {
      const groups = {};
      this.chartRows.forEach((el) => {
        if (groups[el[0]]) {
          groups[el[0]].push(el.slice(1, el.length));
        } else {
          groups[el[0]] = [el.slice(1, el.length)];
        }
      });
      return Object.keys(groups).map((key, ind) => ({ name: `Cluster ${key}`, data: groups[key], color: this.pointsColors[ind] }));
    },
  },
};
</script>

<style>
  .card-title {
    cursor: pointer;
  }
</style>
