<template>
  <div id="app">
    <Header/>
    <section>
      <router-view/>
    </section>
  </div>
</template>

<script>

import Header from './components/Layout/Header.vue'


export default {
  name: 'App',
  components: {
    Header
  }
}
</script>

<style>
html{
  background: #f5f5f5;
  height:100%;

}
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  color: #2c3e50;
  background: #f5f5f5;
}
</style>
