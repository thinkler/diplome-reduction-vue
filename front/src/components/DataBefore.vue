<template>
  <div>
    <b-container v-if="isShow">
      <h2 class="page-title">Data Before</h2>
      <b-row>
        <b-col>
          <b-row>
            <b-col cols="8">
              <div class="card pure-statistics">
                <h3 class="card-title">General Statistics</h3>
                <b-row>
                  <b-col><strong>Clusters Count:</strong> {{totalClusters}}</b-col>
                  <b-col><strong>Elements Count:</strong> {{totalElements}}</b-col>
                </b-row>
                <b-row>
                  <b-col cols="4"><strong>Elements Count:</strong></b-col>
                  <b-col v-for="(count, index) in pureData.clusters_sizes" :key="index"><span :style="{ color: pointsColors[index] }">{{pointsColors[index]}}</span> - {{count}}</b-col>
                </b-row>
              </div>
            </b-col>
            <b-col>
              <div class="card">
                <h3 class="card-title">Scroll To:</h3>
                <ul>
                  <li><a href="#data-chart">Raw Data Chart</a></li>
                  <li><a href="#clusterd-chart">Clustered Data Chart</a></li>
                  <li><a href="#andrews-chart">Andrews Colored Data Chart</a></li>
                  <li><a href="#data-table">Data Table</a></li>
                </ul>
              </div>
            </b-col>
          </b-row>
          <chart-card id="data-chart" title="Raw Data Chart" :chartRows="rawData" :chartCols="pureColumns" xTitle="some" yTitle="stuff"></chart-card>
          <chart-card id="clusterd-chart" title="Clustered Data Chart" :chartRows="coloredData" :chartCols="coloredColumns" xTitle="some" yTitle="stuff"></chart-card>
          <chart-card id="andrews-chart" title="Andrews Colored Data Chart" :chartRows="pureData.data" :andrews='true' xTitle="Pi" yTitle="Data"></chart-card>
          <div id="data-table" class="card">
            <h3 class="card-title" @click="showTable = !showTable">Data Table</h3>
            <b-table v-show="showTable" hover small :items='tableData' :fields='tableFields'></b-table>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import ChartCard from './ChartCard';

export default {
  data() {
    return {
      pureData: {},
      showTable: true,
      tableFields: ['col1', 'col2', 'col3', 'col4'],
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
        height: 500,
        legend: 'none',
      },
    };
  },
  components: { ChartCard },
  computed: {
    totalElements() {
      let sum = 0;
      Object.keys(this.pureData.clusters_sizes).forEach((el) => {
        sum += this.pureData.clusters_sizes[el];
      });
      return sum;
    },
    totalClusters() {
      return Object.keys(this.pureData.clusters_sizes).length;
    },
    rawData() {
      const data = this.pureData.data;
      return data.map(el => el.slice(1, 3));
    },
    coloredData() {
      const data = this.pureData.data;
      return data.map((el) => {
        const row = el.slice(0);
        row[3] = `point { fill-color: ${this.pointsColors[row[0]]}`;
        return row.slice(1, 4);
      });
    },
    tableData() {
      const data = this.pureData.data.slice(0);
      return data.map((el) => {
        const elementObject = {};
        el.forEach((e, i) => {
          elementObject[`col${i}`] = e;
        });
        elementObject._rowVariant = `color-${el[0] + 1}`; // eslint-disable-line 
        return elementObject;
      });
    },
    classColor(index) {
      return `span-color-${this.pointsColors[index]}`;
    },
  },
  created() {
    if (this.$store.state.pure) {
      this.pureData = this.$store.state.pure;
      this.isShow = true;
    }
  },
};
</script>
  
<style>
  .page-title {
    margin: 25px;
    text-align: center;
  }
  .card-title {
    color: gray;
    text-align: center;
    margin-top: 15px;
  }
  .card-title:hover {
    color: black;
  }
  .pure-statistics {
    text-align: center;
    font-size: 25px;
    padding-bottom: 20px !important;
  }
  tr.table-color-1 { background-color: hsla(0, 100%, 50%, 0.2) }
  tr.table-color-2 { background-color: rgba(0, 128, 0, 0.2)}
  tr.table-color-3 { background-color: rgba(0, 0, 255, 0.2) }
  tr.table-color-4 { background-color: rgba(0, 0, 0, 0.2) }
  tr.table-color-5 { background-color: rgba(255, 255, 0, 0.2) }
  tr.table-color-6 { background-color: rgba(128, 0, 128, 0.2)}

  .span-color-color-1 { color: hsla(0, 100%, 50%, 0.2) }
  .span-color-color-2 { color: rgba(0, 128, 0, 0.2)}
  .span-color-color-3 { color: rgba(0, 0, 255, 0.2) }
  .span-color-color-4 { color: rgba(0, 0, 0, 0.2) }
  .span-color-color-5 { color: rgba(255, 255, 0, 0.2) }
  .span-color-color-6 { color: rgba(128, 0, 128, 0.2)}
  .card {
    background: #fff;
    border-radius: 3px;
    padding: 10px;
    box-shadow: 0 0px 14px 0px rgba(0, 0, 0, 0.3);
    margin: 0 auto 1.6%;
    position: relative;
    margin-bottom: 30px;
  }
</style>
