<template>
  <div class="card"> 
    <h3 class="card-title" @click="showChart = !showChart">{{title}}</h3>
    <div class="chart" v-show="showChart">
      <line-chart v-if="!pure" :data="coloredData" :legend="false" height="500px" xtitle="Pi" ytitle="Data"></line-chart>
      <line-chart v-if="pure" :data="pureData" :legend="false" height="500px" xtitle="Pi" ytitle="Data"></line-chart>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'chartRows', 'pure'],
  data() {
    return {
      showChart: true,
      linesColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
    };
  },
  computed: {
    andrewsRows() {
      let result = [];
      const data = this.chartRows.slice(0);
      const theta = this.linspace(-3.14, 3.14, 10);
      result = data.map(elem => theta.map((th) => {
        let sum = 0;
        elem.forEach((el, index) => {
          if (index === 0) sum += el / Math.sqrt(2);
          if (index === 1) sum += el * Math.sin(th);
          if (index === 2) sum += el * Math.cos(th);
          if (index === 3) sum += el * Math.sin(2 * th);
          if (index === 4) sum += el * Math.cos(2 * th);
          if (index === 5) sum += el * Math.sin(3 * th);
          if (index === 6) sum += el * Math.cos(3 * th);
          if (index === 7) sum += el * Math.sin(4 * th);
          if (index === 8) sum += el * Math.cos(4 * th);
          if (index === 9) sum += el * Math.sin(5 * th);
          if (index === 12) sum += el * Math.cos(5 * th);
        });
        return sum;
      }));
      result.unshift(theta);
      result = result[0].map((col, i) => result.map(row => row[i]));
      return result;
    },
    pureData() {
      const clusters = this.chartRows;
      const formatted = clusters.map((el, ind) => this.andrewsRows.map(e => [e[0], e[ind]]));
      return formatted.map(data => ({ data, color: 'blue' }));
    },
    coloredData() {
      const clusters = this.chartRows;
      const formatted = clusters.map((el, ind) => this.andrewsRows.map(e => [e[0], e[ind]]));
      return formatted.map((data, ind) =>
        ({ data, color: this.linesColors[clusters[ind][0]] }));
    },
  },
  methods: {
    linspace(a, b, n) {
      if (typeof n === 'undefined') n = Math.max(Math.round(b - a) + 1, 1); // eslint-disable-line
      if (n < 2) { return n === 1 ? [a] : []; }
      let i;
      const ret = Array(n);
      n--; // eslint-disable-line
      for (i = n; i >= 0; i--) { ret[i] = (i * b + (n - i) * a) / n; } // eslint-disable-line
      return ret;
    },
  },
};
</script>

<style>
  .card-title {
    cursor: pointer;
  }
</style>
