<template>
  <div>
    <h2 class="page-title">Results</h2>
    <div>
        <b-tabs ref="tabs">
            <b-tab v-for="(r, i) in results" :key="i" :title="r.title" active>
                <method-stats :res="r"></method-stats>
                <method-results :res="r"></method-results>
            </b-tab>
        </b-tabs>
    </div>
  </div>
</template>

<script>
import MethodResults from './MethodResults';
import MethodStats from './MethodStats';

export default {
  components: { MethodResults, MethodStats },
  data() {
    return {
      results: [],
    };
  },
  created() {
    const state = this.$store.state;
    this.results.push(state.pca);
    this.results.push(state.kmeans);
    this.results.push(state.mds);
    this.results.push(state.soma);
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
