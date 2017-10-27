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
                <b-row>
                  <b-col>
                    <router-link to="/results"><b-button class="next-button" variant='success'>Results</b-button></router-link>
                  </b-col>
                </b-row>
              </div>
            </b-col>
            <b-col>
              <div class="card">
                <h3 class="card-title">Scroll To:</h3>
                <ul>
                  <li><a href="#data-chart">Raw Data Chart</a></li>
                  <li><a href="#clusterd-chart">Clustered Data Chart</a></li>
                  <li><a href="#pure-andrews-chart">Andrews Raw Data Chart</a></li>
                  <li><a href="#andrews-chart">Andrews Colored Data Chart</a></li>
                  <li><a href="#data-table">Data Table</a></li>
                </ul>
              </div>
            </b-col>
          </b-row>
          <scatter-chart id="data-chart" title="Raw Data Chart" :chartRows="pureData.data" :pure='true' xTitle="some" yTitle="stuff"></scatter-chart>
          <scatter-chart id="clusterd-chart" title="Clustered Data Chart" :chartRows="pureData.data" xTitle="some" yTitle="stuff"></scatter-chart>
          <andrews-chart id="pure-andrews-chart" title="Andrews Raw Data Chart" :chartRows="pureData.data" :pure='true' xTitle="Pi" yTitle="Data"></andrews-chart> -->
          <andrews-chart id="andrews-chart" title="Andrews Colored Data Chart" :chartRows="pureData.data" xTitle="Pi" yTitle="Data"></andrews-chart>
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
import ScatterChart from './ScatterChart';
import AndrewsChart from './AndrewsChart';

export default {
  data() {
    return {
      pureData: {},
      showTable: true,
      tableFields: ['col1', 'col2', 'col3', 'col4'],
      pointsColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
    };
  },
  components: { ScatterChart, AndrewsChart },
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
  .next-button {
    margin-top: 20px;
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
</style>
