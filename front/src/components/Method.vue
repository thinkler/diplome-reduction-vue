<template>
  <b-container>
    <h2 class="page-title">{{method}} Results</h2>
    <div class="card pure-statistics">
      <h3 class="card-title">General Statistics</h3>
      <b-row>
        <b-col><strong>Clusters Count: </strong> {{totalClusters}}</b-col>
        <b-col><strong>Elements Count: </strong> {{table.data.length}}</b-col>
      </b-row>
      <b-row>
        <b-col><strong>Time Spent:</strong>{{table.time.toPrecision(5)}}</b-col>
        <b-col><strong>Memory Spent:</strong>{{table.memory}}</b-col>
      </b-row>
    </div>
     <div>
        <method-results :res="table.data"></method-results>
        <data-table title="Colored Data Table" :data="table.data"></data-table>
    </div>
  </b-container>
</template>

<script>
import DataTable from './DataTable';
import MethodResults from './MethodResults';

export default {
  data() {
    return {
      table: this.$store.state.methodData,
      totalClusters: this.$store.state.factors,
      method: this.$store.state.selectedMethod,
    };
  },
  components: { MethodResults, DataTable },
};
</script>

<style>

</style>
