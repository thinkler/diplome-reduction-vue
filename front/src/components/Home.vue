<template>
  <div>
    <div v-show="loading" class="loading">
      <h3 class="loading-label">Processing...</h3>
    </div>
    <b-container>
      <b-row>
        <b-col cols="6">
          <h2 class="page-title">Method</h2>
          <b-form enctype="multipart/form-data" @submit.prevent="submitMethod">    
            <div class="card">
              <b-form-group label="Factors count:" label-for="factorsInput">
                <b-form-select v-model="selectedMethod" :options="options"></b-form-select>
              </b-form-group>
              <b-form-group label="Factors count:" label-for="factorsInput">
                <b-form-input id='factorsInput' type="number" v-model="factors" min=0 max=6 required placeholder="Factors Count"></b-form-input>
              </b-form-group>
              <b-form-group label="Table:" label-for="table">
                <b-form-file id="table" @change="onFileChange"></b-form-file>
              </b-form-group>
              <b-button type="submit" variant="defualt">Submit</b-button>
            </div>
          </b-form>
        </b-col>
        <b-col cols="6">
          <h2 class="page-title">Experiement</h2>
          <b-form enctype="multipart/form-data" @submit.prevent="submitExp">
            <div class="card">
              <b-form-group label="Table:" label-for="table">
                <b-form-file id="table" @change="onFileChange" v-model="table"></b-form-file>
              </b-form-group>
              <b-button type="submit" variant="defualt">Submit</b-button>
            </div>
          </b-form>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      table: '',
      factors: 2,
      options: ['mds', 'kmeans', 'pca', 'soma'],
      selectedMethod: 'pca',
      loading: false,
    };
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      const reader = new FileReader();
      const vm = this;

      reader.onload = () => { vm.table = reader.result; };
      reader.readAsText(file);
    },
    submitMethod() {
      const state = this.$store.state;
      this.loading = true;
      this.cutRowNames();
      const body = {
        table: this.table,
        factors: this.factors,
        method: this.selectedMethod,
      };
      axios.post('http://localhost:5000/method', body)
      .then((response) => {
        state.methodData = response.data;
        state.factors = this.factors;
        state.selectedMethod = this.selectedMethod;
        this.$router.push('method');
        this.loading = false;
      });
    },
    submitExp() {
      const state = this.$store.state;
      this.cutRowNames();
      this.loading = true;
      axios.post('http://localhost:5000/reduction', { table: this.table })
      .then((response) => {
        state.pure = response.data.pure;
        state.kmeans = response.data.kmeans;
        state.mds = response.data.mds;
        state.pca = response.data.pca;
        state.soma = response.data.soma;
        this.migrateToNewClusters(state.pure.data, state.pca.data);
        this.migrateToNewClusters(state.pure.data, state.kmeans.data);
        this.migrateToNewClusters(state.pure.data, state.mds.data);
        this.migrateToNewClusters(state.pure.data, state.soma.data);
        this.recalcStats(state.pure, state.pca);
        this.recalcStats(state.pure, state.kmeans);
        this.recalcStats(state.pure, state.mds);
        this.recalcStats(state.pure, state.soma);
        this.$router.push('data-before');
      })
      .catch((error) => {
        alert(error);
        this.loading = false;
      });
    },

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
      if (instructions) {
        return arr2.map((el) => {
          const fin = el;
          fin[0] = this.checkOf(el[0], [instructions]);
          return fin;
        });
      }
      return arr2;
    },
    recalcStats(pure, results) {
      results.clusters_sizes = {}; // eslint-disable-line
      results.clusters_sizes_error = {}; // eslint-disable-line
      results.match_error = 0; // eslint-disable-line
      results.data.forEach((res) => {
        if (results.clusters_sizes[res[0]]) {
          results.clusters_sizes[res[0]] += 1; // eslint-disable-line
        } else {
          results.clusters_sizes[res[0]] = 1;// eslint-disable-line
        }
      });
      Object.keys(pure.clusters_sizes).forEach((clust) => {
        results.clusters_sizes_error[clust] = Math.abs(pure.clusters_sizes[clust] - results.clusters_sizes[clust]); // eslint-disable-line
      });
      pure.data.forEach((el, ind) => {
        if (el[0] !== results.data[ind][0]) results.match_error += 1; // eslint-disable-line
      });
    },
    cutRowNames() {
      this.table = this.table.split('\n');
      const rowNames = this.table.shift().split(',');
      rowNames.shift();
      this.$store.state.rowNames = rowNames;
      this.table = this.table.join('\n');
    },
  },
};

</script>

<style>
  .loading {
    background-color: white;
    display: block;
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 9999;
  }

  .loading-label {
    position: absolute;
    top: 30%;
    left: 45%;
  }
</style>
