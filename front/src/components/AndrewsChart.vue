<template>
  <div class="card"> 
    <h3 class="card-title" @click="showChart = !showChart">{{title}}</h3>
    <div class="chart" v-show="showChart">
      <vue-chart v-if="!pure" :chart-type="'LineChart'" :columns="andrewsCols" :rows="andrewsRows" :options="coloredAndrewsOptions"></vue-chart>
      <vue-chart v-if="pure" :chart-type="'LineChart'" :columns="andrewsCols" :rows="andrewsRows" :options="pureAndrewsOptions"></vue-chart>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'chartRows', 'xTitle', 'yTitle', 'andrews', 'pure'],
  data() {
    return {
      showChart: true,
      linesColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
      pureAndrewsOptions: {
        colors: ['blue'],
        hAxis: { title: this.xTitle },
        vAxis: { title: this.yTitle },
        height: 500,
        legend: { position: 'none' },
      },
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
    andrewsCols() {
      return this.andrewsRows[0].map(() => ({ type: 'number', label: 'data' }));
    },
    coloredAndrewsOptions() {
      const options = {
        hAxis: { title: this.xTitle },
        vAxis: { title: this.yTitle },
        legend: { position: 'none' },
        height: 500,
        width: 1000,
        series: {},
      };
      this.chartRows.forEach((el, i) => {
        options.series[i] = { color: this.linesColors[el[0]] };
      });
      return options;
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
