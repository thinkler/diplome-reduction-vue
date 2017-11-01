<template>
  <div class="comparing-container">
    <h2 class="page-title">Custom Comparing</h2>
    <b-row>
      <b-col cols="6">
        <b-btn variant="outline-success" v-if="!showOptions1" @click="showOptions1 = !showOptions1">Select Results for Zone 1</b-btn>
        <div v-else >
          <b-btn variant="outline-success" @click="setZone1('pure')">Pure Data</b-btn>
          <b-btn variant="outline-success" @click="setZone1('kmeans')">K-Means</b-btn>
          <b-btn variant="outline-success" @click="setZone1('pca')">Principal component analysis</b-btn>
          <b-btn variant="outline-success" @click="setZone1('mds')">Multidimensinal Scaling</b-btn>
          <b-btn variant="outline-success" @click="setZone1('soma')">Self Organazing Map</b-btn>
        </div>
        <div v-if="dataZone1">
          <h3>{{dataZone1.title || 'Pure Data'}}</h3>
          <method-results :res="dataZone1.data"></method-results>
          <data-table :title="dataZone1.title + ' Colored Table'" :data="dataZone1.data"></data-table>
          <method-stats v-if="dataZone1.title" :res="dataZone1"></method-stats>
        </div>
      </b-col>
      <b-col cols="6">
        <b-btn variant="outline-success" v-if="!showOptions2" @click="showOptions2 = !showOptions2">Select Results for Zone 2</b-btn>
        <div v-else >
          <b-btn variant="outline-success" @click="setZone2('pure')">Pure Data</b-btn>
          <b-btn variant="outline-success" @click="setZone2('kmeans')">K-Means</b-btn>
          <b-btn variant="outline-success" @click="setZone2('pca')">Principal component analysis</b-btn>
          <b-btn variant="outline-success" @click="setZone2('mds')">Multidimensinal Scaling</b-btn>
          <b-btn variant="outline-success" @click="setZone2('soma')">Self Organazing Map</b-btn>
        </div>
        <div v-if="dataZone2">
          <h3>{{dataZone2.title || 'Pure Data'}}</h3>
          <method-results :res="dataZone2.data"></method-results>
          <data-table :title="dataZone2.title + ' Colored Table'" :data="dataZone2.data"></data-table>
          <method-stats v-if="dataZone2.title" :res="dataZone2"></method-stats>
        </div>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import MethodResults from './MethodResults';
import MethodStats from './MethodStats';
import DataTable from './DataTable';

export default {
  components: { MethodResults, MethodStats, DataTable },
  data() {
    return {
      showOptions1: false,
      showOptions2: false,
      dataZone1: '',
      dataZone2: '',
    };
  },
  methods: {
    setZone1(type) {
      this.showOptions1 = false;
      this.dataZone1 = this.$store.state[type];
    },
    setZone2(type) {
      this.showOptions2 = false;
      this.dataZone2 = this.$store.state[type];
    },
  },
};
</script>

<style>
.comparing-container {
  width: 97%;
  margin: auto;
}
</style>
