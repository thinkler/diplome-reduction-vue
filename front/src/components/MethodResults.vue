<template>
  <div>
    <b-container>
      <b-row>
        <chart-card title="Andrews Colored Data Chart" :chartRows="res.data" :andrews='true' xTitle="Pi" yTitle="Data"></chart-card>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import ChartCard from './ChartCard';

export default {
  components: { ChartCard },
  props: ['res'],
};
</script>

<style>

</style>
