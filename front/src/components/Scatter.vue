<template>
  <div class="card"> 
    <h3 class="card-title" @click="showChart = !showChart">{{title}}</h3>
    <div class="chart" v-show="showChart">
      <b-row>
        <b-col cols='4'><b-form-select v-model="secondRow" :options="rows"></b-form-select></b-form-select></b-col>
        <b-col cols='4'><b-form-select v-model="firstRow" :options="rows"></b-form-select></b-col>
      </b-row>
      <br>
      <scatter-chart :data="data" :xtitle="firstRow" :ytitle="secondRow"></scatter-chart>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'chartRows', 'pure'],
  data() {
    return {
      showChart: true,
      firstRow: this.$store.state.rowNames[0],
      secondRow: this.$store.state.rowNames[1],
      pointsColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
      rows: this.$store.state.rowNames,
    };
  },
  computed: {
    rowNames() {
      return this.$store.state.rowNames;
    },
    pureData() {
      return this.chartData || this.chartRows.map(el => el.slice(1, el.length));
    },
    coloredData() {
      return this.chartData || this.processColors(this.chartRows);
    },
    data() {
      const firstIndex = this.rows.indexOf(this.firstRow);
      const secondIndex = this.rows.indexOf(this.secondRow);
      const newArr = this.pure ? [firstIndex, secondIndex] : [0, firstIndex + 1, secondIndex + 1];

      if (this.pure) {
        const data = this.chartRows.map(el => el.slice(1, el.length));
        return data.map(el => newArr.map(it => el[it]));
      }
      const data = this.chartRows;
      const toProcess = data.map(el => newArr.map(it => el[it]));
      return this.processColors(toProcess);
    },
  },
  methods: {
    processColors(data) {
      const groups = {};
      data.forEach((el) => {
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
