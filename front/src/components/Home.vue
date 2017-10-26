<template>
  <div>
    <h2>Upload file, select factors</h2>
    <form enctype="multipart/form-data" @submit.prevent="submitStaff">
      <input type="number" v-model="factors">
      <input type="file" @change='onFileChange' class="input-file">
      <input type="submit" value="Submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      table: '',
      factors: 0,
    };
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      const reader = new FileReader();
      const vm = this;

      reader.onload = () => { vm.table = reader.result; };
      reader.readAsText(file);
    },
    submitStaff() {
      const state = this.$store.state;
      axios.post('http://localhost:5000/reduction', { table: this.table, factors: this.factors })
      .then((response) => {
        state.pure = response.data.pure;
        state.kmeans = response.data.kmeans;
        state.mds = response.data.mds;
        state.pca = response.data.pca;
        state.soma = response.data.soma;
        this.$router.push('data-before');
      })
      .catch(() => {});
    },
  },
};

</script>

<style>

</style>
