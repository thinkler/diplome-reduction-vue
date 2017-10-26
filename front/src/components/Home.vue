<template>
  <div>
    <h2 class="page-title">Upload file, select factors</h2>
    <b-form enctype="multipart/form-data" @submit.prevent="submitStaff">
      <b-container>
        <b-row>
          <b-col cols="4"></b-col>
          <b-col cols="4">
            <div class="card">
              <b-row>
                <b-col>
                  <b-form-group label="Factors count:" label-for="factorsInput">
                    <b-form-input id='factorsInput' type="number" v-model="factors" required placeholder="Factors Count"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Table:" label-for="table">
                      <b-form-file id="table" @change="onFileChange"></b-form-file>
                  </b-form-group>
                  <b-button type="submit" variant="defualt">Submit</b-button>
                </b-col>
              </b-row>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      table: '',
      factors: 3,
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
  .page-title {
    margin: 25px;
    text-align: center;
  }
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
