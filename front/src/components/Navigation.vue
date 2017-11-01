<template>
  <div>
    <b-navbar variant="light" toggleable>
      <b-nav-toggle target="nav_dropdown_collapse"></b-nav-toggle>
      <b-collapse is-nav id="nav_dropdown_collapse">
        <b-nav is-nav-bar>
          <router-link class="nav-link" to="/">Home</router-link>
          <router-link v-if="isDataUploded" class="nav-link" to="/data-before">Data Before</router-link>
          <router-link v-if="isDataUploded" class="nav-link" to="/results">Results</router-link>
          <router-link v-if="isDataUploded" class="nav-link" to="/comparing">Comparing</router-link>
          <router-link v-if="isDataUploded" class="nav-link" to="/stats">Statistics</router-link>
        </b-nav>
      </b-collapse>
    </b-navbar>
  </div>
  </div>
</template>

<script>
export default {
  computed: {
    isDataUploded() {
      return !!this.$store.state.pure.data;
    },
  },
};
</script>

<style>

</style>
