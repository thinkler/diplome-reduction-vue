<template>
  <div>
    <h2>Results</h2>
    <button @click="onClick">Me</button>
  </div>
</template>

<script>
export default {
  methods: {
    onClick() {
      this.$router.go(-1);
    },
  },
};
</script>

<style>

</style>
