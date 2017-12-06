<template>
  <div>
    <h2 class="page-title">Upload file, select factors</h2>
    <b-form enctype="multipart/form-data" @submit.prevent="submitStaff">
      <b-container>
        <b-row>
          <b-col cols="4">
          </b-col>
          <b-col cols="4">
            <div class="card">
              <b-row>
                <b-col>
                  <b-form-group label="Factors count:" label-for="factorsInput">
                    <b-form-input id='factorsInput' type="number" v-model="factors" required placeholder="Factors Count"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Table:" label-for="table">
                      <b-form-file id="table" @change="onFileChange"></b-form-file>
                  </b-form-group>
                  <b-button type="submit" variant="defualt">Submit</b-button>
                </b-col>
              </b-row>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      table: '',
      factors: 2,
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
    submitStaff() {
      const state = this.$store.state;
      this.cutRowNames();
      axios.post('http://localhost:5000/reduction', { table: this.table, factors: this.factors })
      .then((response) => {
        state.pure = response.data.pure;
        state.kmeans = response.data.kmeans;
        state.mds = response.data.mds;
        state.pca = response.data.pca;
        state.soma = response.data.soma;
        console.log('PCA');
        this.migrateToNewClusters(state.pure.data, state.pca.data);
        console.log('Kmeans');
        this.migrateToNewClusters(state.pure.data, state.kmeans.data);
        console.log('MDS');
        this.migrateToNewClusters(state.pure.data, state.mds.data);
        console.log('Soma');
        this.migrateToNewClusters(state.pure.data, state.soma.data);
        this.recalcStats(state.pure, state.pca);
        this.recalcStats(state.pure, state.kmeans);
        this.recalcStats(state.pure, state.mds);
        this.recalcStats(state.pure, state.soma);
        this.$router.push('data-before');
      })
      .catch(() => {});
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
      console.log(counts);
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
        // console.log(results.clusters_sizes[res[0]]);
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
</style>
