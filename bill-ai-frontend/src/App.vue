<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <QuestionsAndAnswers/>
</template>

<script>
import QuestionsAndAnswers from './components/QuestionsAndAnswers.vue'

export default {
  name: 'App',
  components: {
    QuestionsAndAnswers
  }
}
</script>

<style>
html, body {
  background-color: #CCC; 
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin-right: auto;
  margin-left: auto;
  width: 90%;
}
</style>
