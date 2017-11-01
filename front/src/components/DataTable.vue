<template>
  <div id="data-table" class="card">
    <h3 class="card-title" @click="showTable = !showTable">{{title}}</h3>
    <b-table v-if="pure" v-show="showTable" hover small :items='rawData' :fields='tableFields'></b-table>
    <b-table v-if="!pure" v-show="showTable" hover small :items='tableData' :fields='tableFields'></b-table>
  </div>
</template>

<script>
export default {
  props: ['title', 'data', 'pure'],
  data() {
    return {
      showTable: true,
      tableFields: this.$store.state.rowNames,
    };
  },
  computed: {
    rawData() {
      return this.data.map((el) => {
        const elementObject = {};
        el.forEach((e, i) => {
          elementObject[this.tableFields[i]] = el[i + 1];
        });
        return elementObject;
      });
    },
    tableData() {
      return this.data.map((el) => {
        const elementObject = {};
        el.forEach((e, i) => {
          elementObject[this.tableFields[i]] = el[i + 1];
        });
        elementObject._rowVariant = `color-${el[0] + 1}`; // eslint-disable-line 
        return elementObject;
      });
    },
  },
};
</script>

<style>
  tr.table-color-1 { background-color: hsla(0, 100%, 50%, 0.2) }
  tr.table-color-2 { background-color: rgba(0, 128, 0, 0.2)}
  tr.table-color-3 { background-color: rgba(0, 0, 255, 0.2) }
  tr.table-color-4 { background-color: rgba(0, 0, 0, 0.2) }
  tr.table-color-5 { background-color: rgba(255, 255, 0, 0.2) }
  tr.table-color-6 { background-color: rgba(128, 0, 128, 0.2)}
</style>
