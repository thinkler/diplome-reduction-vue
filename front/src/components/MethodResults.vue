<template>
  <div>
    <b-container>
      <b-row>
        <scatter-chart title="Clustered Scatter Chart" :chartRows="res.data" xTitle="some" yTitle="stuff"></scatter-chart>
        <andrews-chart title="Andrews Colored Data Chart" :chartRows="res.data" xTitle="Pi" yTitle="Data"></andrews-chart>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import AndrewsChart from './AndrewsChart';
import ScatterChart from './ScatterChart';

export default {
  components: { AndrewsChart, ScatterChart },
  props: ['res'],
};
</script>

<style>

</style>
