<template>
  <div>
    <b-container v-if="isShow">
      <h2 class="page-title">Data Before</h2>
      <b-row>
        <b-col cols="9" class="chart">
          <div class="card">
            <h3 class="card-title">Raw Data Chart</h3>
            <vue-chart :chart-type="'ScatterChart'" :columns="pureColumns" :rows="rawData" :options="options"></vue-chart>
          </div>
        </b-col>
        <b-col>
          <div class="card">
            <table>
              <tr>
                <td><strong>Clusters Count:</strong></td>
                <td>{{totalClusters}}</td>
              </tr>
              <tr>
                <td><strong>Elements Count:</strong></td>
                <td>{{totalElements}}</td>
              </tr>
              <tr>
                <td><strong>Elements in clusters:</strong></td>
                <td>
                </td>
              </tr>
              <ol>
                <li v-for="(count, index) in pureData.clusters_sizes" :key="index">{{count}}</li>
              </ol>
            </table>
          </div>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <div class="card">
            <h3 class="card-title">Clustered Data Chart</h3>
            <vue-chart :chart-type="'ScatterChart'" :columns="coloredColumns" :rows="coloredData" :options="options"></vue-chart>
          </div>
          <div class="card">
            <h3 class="card-title">Andrews Raw Data Chart</h3>
          </div>
          <div class="card">
            <h3 class="card-title">Andrews Colored Data Chart</h3>
          </div>
          <div class="card">
            <h3 class="card-title">Data Table</h3>
            <b-table hover small :items='tableData' :fields='tableFields'></b-table>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pureData: {},
      isShow: false,
      tableFields: ['col1', 'col2', 'col3', 'col4'],
      pointsColors: ['red', 'green', 'blue', 'black', 'yellow', 'purple'],
      pureColumns: [{
        type: 'number',
        label: 'Column 1',
      }, {
        type: 'number',
        label: 'Column 2',
      }],
      coloredColumns: [{
        type: 'number',
        label: 'Column 1',
      }, {
        type: 'number',
        label: 'Column 2',
      }, {
        type: 'string',
        role: 'style',
      }],
      options: {
        height: 500,
        legend: 'none',
      },
    };
  },
  computed: {
    totalElements() {
      let sum = 0;
      Object.keys(this.pureData.clusters_sizes).forEach((el) => {
        sum += this.pureData.clusters_sizes[el];
      });
      return sum;
    },
    totalClusters() {
      return Object.keys(this.pureData.clusters_sizes).length;
    },
    rawData() {
      const data = this.pureData.data;
      return data.map(el => el.slice(1, 3));
    },
    coloredData() {
      const data = this.pureData.data;
      return data.map((el) => {
        const row = el.slice(0);
        row[3] = `point { fill-color: ${this.pointsColors[row[0]]}`;
        return row.slice(1, 4);
      });
    },
    tableData() {
      const data = this.pureData.data.slice(0);
      return data.map((el) => {
        const elementObject = {};
        el.forEach((e, i) => {
          elementObject[`col${i}`] = e;
        });
        elementObject._rowVariant = `color-${el[0] + 1}`; // eslint-disable-line
        return elementObject;
      });
    },
  },
  created() {
    if (this.$store.state.pure) {
      this.pureData = this.$store.state.pure;
      this.isShow = true;
    }
  },
};
</script>
  
<style>
  .container {
    margin-top: 20px;
    font-family: 'Quicksand', sans-serif;
  }
  .page-title {
    margin: 25px;
    text-align: center;
  }
  .card-title {
    text-align: center;
    margin-top: 15px;
  }
  tr.table-color-1 { background-color: hsla(0, 100%, 50%, 0.2) }
  tr.table-color-2 { background-color: rgba(0, 128, 0, 0.2)}
  tr.table-color-3 { background-color: rgba(0, 0, 255, 0.2) }
  tr.table-color-4 { background-color: rgba(0, 0, 0, 0.2) }
  tr.table-color-5 { background-color: rgba(255, 255, 0, 0.2) }
  tr.table-color-6 { background-color: rgba(128, 0, 128, 0.2)}
  .card {
    background: #fff;
    border-radius: 3px;
    padding: 10px;
    box-shadow: 0 0px 14px 0px rgba(0, 0, 0, 0.3);
    margin: 0 auto 1.6%;
    position: relative;
    margin-bottom: 30px;
  }
</style>
