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
                    <router-link to="/comparing"><b-button class="next-button" variant='success'>Comparing</b-button></router-link>
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
          <data-table title="Data Table" :data="pureData.data" :pure='true'></data-table>
          <scatter id="data-chart" title="Raw Data Chart" :chartRows="pureData.data" :pure='true'></scatter>
          <scatter id="clusterd-chart" title="Clustered Data Chart" :chartRows="pureData.data"></scatter>
          <andrews-chart id="pure-andrews-chart" title="Andrews Raw Data Chart" :chartRows="pureData.data" :pure='true'></andrews-chart>
          <andrews-chart id="andrews-chart" title="Andrews Colored Data Chart" :chartRows="pureData.data"></andrews-chart>
          <data-table title="Colored Data Table" :data="pureData.data"></data-table>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Scatter from './Scatter';
import AndrewsChart from './AndrewsChart';
import DataTable from './DataTable';

export default {
  data() {
    return {
      pureData: {},
      showTable: true,
      pointsColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
    };
  },
  components: { Scatter, AndrewsChart, DataTable },
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
  },
  methods: {
    getClustersCombiations(arr, arr2) {
      const counts = {};
      arr.forEach((el) => {
        counts[el[0]] = {};
      });
      arr.forEach((el, ind) => {
        if (counts[el[0]][arr2[ind][0]]) {
          counts[el[0]][arr2[ind][0]] += 1;
        } else {
          counts[el[0]][arr2[ind][0]] = 1;
        }
      });

      return counts;
    },
    getMigrationInstructions(arr, arr2) {
      const counts = this.getClustersCombiations(arr, arr2);
      let sMax = 0;
      let res;
      Object.keys(counts).forEach((el) => {
        const clust = counts[el];
        const max = Math.max(...Object.values(clust));
        const newClust = Object.keys(clust)
                               .find(key => clust[key] === max);
        if (max > sMax && newClust !== el) {
          sMax = max;
          res = [newClust, el];
        }
      });
      return res;
    },
    checkOf(item, inst) {
      let res = item;
      inst.forEach((i) => {
        if (item == i[0]) res = i[1]; // eslint-disable-line
        if (item == i[1]) res = i[0]; // eslint-disable-line
      });
      return parseInt(res); // eslint-disable-line
    },
    migrateToNewClusters(arr, arr2) {
      const instructions = this.getMigrationInstructions(arr, arr2);

      return arr2.map((el) => {
        const fin = el;
        if (instructions) fin[0] = this.checkOf(el[0], [instructions]);
        return fin;
      });
    },
    recalcStats(pure, results) {
      results.clusters_sizes = {}; // eslint-disable-line
      results.clusters_sizes_error = {}; // eslint-disable-line
      results.match_error = 0; // eslint-disable-line
      results.data.forEach((res) => {
        if (results.clusters_sizes[res[0]]) {
          results.clusters_sizes[res[0]] += 1; // eslint-disable-line
        } else {
          results.clusters_sizes[res[0]] = 1; // eslint-disable-line
        }
      });
      Object.keys(pure.clusters_sizes).forEach((clust) => {
        results.clusters_sizes_error[clust] = Math.abs(pure.clusters_sizes[clust] - results.clusters_sizes[clust]); // eslint-disable-line
      });
      pure.data.forEach((el, ind) => {
        if (el[0] !== results.data[ind][0]) results.match_error += 1; // eslint-disable-line
      });
    },
  },
  created() {
    if (this.$store.state.pure) {
      const state = this.$store.state;
      this.pureData = state.pure;
      // this.migrateToNewClusters(state.pure.data, state.kmeans.data);
      // this.recalcStats(state.pure, state.kmeans);
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
  .span-color-color-1 { color: hsla(0, 100%, 50%, 0.2) }
  .span-color-color-2 { color: rgba(0, 128, 0, 0.2)}
  .span-color-color-3 { color: rgba(0, 0, 255, 0.2) }
  .span-color-color-4 { color: rgba(0, 0, 0, 0.2) }
  .span-color-color-5 { color: rgba(255, 255, 0, 0.2) }
  .span-color-color-6 { color: rgba(128, 0, 128, 0.2)}
</style>
