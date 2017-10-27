<template>
  <div class="card"> 
    <h3 class="card-title" @click="showChart = !showChart">{{title}}</h3>
    <div class="chart" v-show="showChart">
      <vue-chart v-if="pure" :chart-type="'ScatterChart'" :columns="pureColumns" :rows="rawData" :options="options"></vue-chart>
      <vue-chart v-if="!pure" :chart-type="'ScatterChart'" :columns="coloredColumns" :rows="coloredData" :options="options"></vue-chart>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'chartRows', 'chartCols', 'xTitle', 'yTitle', 'pure'],
  data() {
    return {
      showChart: true,
      pointsColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
      pureColumns: [{
        type: 'number',
        label: 'Column 1',
      }, {
        type: 'number',
        label: 'Column 2',
      }],
      coloredColumns: [{
        type: 'number',
        label: 'Column 1',
      }, {
        type: 'number',
        label: 'Column 2',
      }, {
        type: 'string',
        role: 'style',
      }],
      options: {
        hAxis: { title: this.xTitle },
        vAxis: { title: this.yTitle },
        height: 500,
        width: 1000,
        legend: { position: 'none' },
      },
    };
  },
  computed: {
    rawData() {
      const data = this.chartRows.slice(0);
      return data.map(el => el.slice(1, 3));
    },
    coloredData() {
      const data = this.chartRows.slice(0);
      return data.map((el) => {
        const row = el.slice(1, 3);
        row[2] = `point { fill-color: ${this.pointsColors[el[0]]}`;
        return row;
      });
    },
  },
};
</script>

<style>
  .card-title {
    cursor: pointer;
  }
</style>
