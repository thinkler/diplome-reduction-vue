<template>
  <b-container>
    <h2 class="page-title">Statistics</h2>
    <b-row>
      <b-col cols="12">
        <div class="card">
          <h3 class="card-title">Match Error</h3>
          <bar-chart :data="matchErrorData" xtitle="Match Error"></bar-chart>
        </div>
      </b-col>
      <b-col cols="12">
        <div class="card">
          <h3 class="card-title">Speed</h3>
          <bar-chart :data="speedData" xtitle="Speed"></bar-chart>
        </div>
      </b-col>
      <b-col cols="12">
        <div class="card">
          <h3 class="card-title">Memory</h3>
          <bar-chart :data="memoryData" xtitle="Memory"></bar-chart>
        </div>
      </b-col>
      <b-col cols="12">
        <div class="card">
          <h3 class="card-title">Cluster Sizes</h3>
          <line-chart :data="clusterSizesData" xtitle="Cluster Num" ytitle="Cluter Size"></line-chart>
        </div>
      </b-col>
      <b-col cols="12">
        <div class="card">
          <h3 class="card-title">Cluster Sizes Errors</h3>
          <line-chart :data="clusterSizesErrorData" xtitle="Cluster Num" ytitle="Cluter Size"></line-chart>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      linesColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
    };
  },
  computed: {
    matchErrorData() {
      return [
        [this.$store.state.kmeans.title, this.$store.state.kmeans.match_error],
        [this.$store.state.mds.title, this.$store.state.mds.match_error],
        [this.$store.state.pca.title, this.$store.state.pca.match_error],
        [this.$store.state.soma.title, this.$store.state.soma.match_error],
      ];
    },
    speedData() {
      return [
        [this.$store.state.kmeans.title, this.$store.state.kmeans.speed],
        [this.$store.state.mds.title, this.$store.state.mds.speed],
        [this.$store.state.pca.title, this.$store.state.pca.speed],
        [this.$store.state.soma.title, this.$store.state.soma.speed],
      ];
    },
    memoryData() {
      let kmeansMem = this.$store.state.kmeans.memory;
      if (kmeansMem < 0) kmeansMem = 1544;
      return [
        [this.$store.state.kmeans.title, kmeansMem],
        [this.$store.state.mds.title, this.$store.state.mds.memory],
        [this.$store.state.pca.title, this.$store.state.pca.memory],
        [this.$store.state.soma.title, this.$store.state.soma.memory],
      ];
    },
    clusterSizesData() {
      const state = this.$store.state;
      return [
        { name: 'Pure', data: Object.keys(state.pure.clusters_sizes).map(el => [el, state.pure.clusters_sizes[el]]), color: 'red' },
        { name: state.kmeans.title, data: Object.keys(state.kmeans.clusters_sizes).map(el => [el, state.kmeans.clusters_sizes[el]]), color: 'blue' },
        { name: state.mds.title, data: Object.keys(state.mds.clusters_sizes).map(el => [el, state.mds.clusters_sizes[el]]), color: 'green' },
        { name: state.pca.title, data: Object.keys(state.pca.clusters_sizes).map(el => [el, state.pca.clusters_sizes[el]]), color: 'yellow' },
        { name: state.soma.title, data: Object.keys(state.soma.clusters_sizes).map(el => [el, state.soma.clusters_sizes[el]]), color: 'black' },
      ];
    },
    clusterSizesErrorData() {
      const state = this.$store.state;
      return [
        { name: state.kmeans.title, data: Object.keys(state.kmeans.clusters_sizes_error).map(el => [el, state.kmeans.clusters_sizes_error[el]]), color: 'blue' },
        { name: state.mds.title, data: Object.keys(state.mds.clusters_sizes_error).map(el => [el, state.mds.clusters_sizes_error[el]]), color: 'green' },
        { name: state.pca.title, data: Object.keys(state.pca.clusters_sizes_error).map(el => [el, state.pca.clusters_sizes_error[el]]), color: 'yellow' },
        { name: state.soma.title, data: Object.keys(state.soma.clusters_sizes_error).map(el => [el, state.soma.clusters_sizes_error[el]]), color: 'black' },
      ];
    },
  },
};
</script>

<style>

</style>
