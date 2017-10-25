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
      axios.post('http://localhost:5000/reduction', { table: this.table, factors: this.factors })
      .then((response) => {
        // Write response body to main state
        console.log(response);
        // this.$router.push('Results');
      })
      .catch((error) => {
        console.log(error);
      });
    },
  },
};

</script>

<style>

</style>
