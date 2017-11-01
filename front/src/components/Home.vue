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
      factors: 3,
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
        this.migrateToNewClusters(state.pure.data, state.pca.data);
        this.migrateToNewClusters(state.pure.data, state.kmeans.data);
        this.migrateToNewClusters(state.pure.data, state.mds.data);
        this.migrateToNewClusters(state.pure.data, state.soma.data);
        this.$router.push('data-before');
      })
      .catch(() => {});
    },
    getClustersCombiations(arr, arr2) {
      const countsSt = {};
      arr.forEach((el) => {
        countsSt[el[0]] = {};
      });
      arr.forEach((el, ind) => {
        if (countsSt[el[0]][arr2[ind][0]]) {
          countsSt[el[0]][arr2[ind][0]] += 1;
        } else {
          countsSt[el[0]][arr2[ind][0]] = 1;
        }
      });
      return countsSt;
    },
    getMigrationInstructions(arr, arr2) {
      const counts = this.getClustersCombiations(arr, arr2);
      console.log(counts);
      const instructions = Object.keys(counts).map((el) => {
        const clust = counts[el];
        const newClust = Object.keys(clust)
                               .find(key => clust[key] === Math.max(...Object.values(clust)));
        return [newClust, el];
      });
      return instructions.filter(i => i[0] !== i[1]);
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
      const instructions = [this.getMigrationInstructions(arr, arr2)[0]];
      console.log(instructions);
      return arr2.map((el) => {
        const fin = el;
        fin[0] = this.checkOf(el[0], instructions.slice(0, 1));
        return fin;
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
