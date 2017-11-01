<template>
  <div>
    <scatter title="Clustered Scatter" :chartRows="res" xTitle="some" yTitle="stuff"></scatter>
    <andrews-chart title="Andrews Colored Data Chart" :chartRows="res" xTitle="Pi" yTitle="Data"></andrews-chart>
  </div>
</template>

<script>
import AndrewsChart from './AndrewsChart';
import Scatter from './Scatter';

export default {
  components: { AndrewsChart, Scatter },
  props: ['res'],
};
</script>

<style>

</style>
