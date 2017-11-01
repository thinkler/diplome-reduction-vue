<template>
  <div>
    <h2 class="page-title">Results</h2>
    <div>
        <b-tabs ref="tabs">
            <b-tab title="Raw Data">
              <method-results :res="rawData.data"></method-results>
              <data-table title="Colored Data Table" :data="rawData.data"></data-table>
            </b-tab>
            <b-tab v-for="(r, i) in results" :key="i" :title="r.title">
                <method-stats :res="r"></method-stats>
                <method-results :res="r.data"></method-results>
                <data-table :title="r.title + ' Colored Table'" :data="r.data"></data-table>
            </b-tab>
        </b-tabs>
    </div>
  </div>
</template>

<script>
import MethodResults from './MethodResults';
import MethodStats from './MethodStats';
import DataTable from './DataTable';

export default {
  components: { MethodResults, MethodStats, DataTable },
  computed: {
    rawData() {
      return this.$store.state.pure;
    },
    results() {
      const state = this.$store.state;
      return [state.pca, state.kmeans, state.mds, state.soma];
    },
  },
};
</script>

<style>
  .nav.nav-tabs {
    width: 90%;
    margin: auto;
    margin-bottom: 30px;
  }
  .tabs .card {
    width: 90%;
  }
</style>
