<template>
  <div class="header">
    <div class="headshot">
    <img alt="Vue logo" src="./assets/logo.png">
    </div>
    <div class="intro">
      
    <h1>Ask Bill a question about the Inflation Reduction Act</h1>
    <p>Bill is the AI that reads the laws that congress passes and explains them to you. 
      He's only read the Inflation Reduction Act so far, but he's working on more.
      Read through some of the questions bellow, then ask Bill your own question.
      Here are some tips about how to ask Bill a good question:
      <ul>
        <li>Make your question specific for the best response, ask how the law effects a certain group of people, or a certain industry.</li>
        <li>Bill knows all the text of the Inflation Reduction Act, but doesn't always remember the name of the law. Ask questions in terms of "the bill" instead.</li>
        <li>Read existing questions before asking your own, Bill sends his developer an invoice every month for all the questions he answers.</li>
      </ul>
    </p>
    </div>
  </div>
  <br/>
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
  background-color: #c1c1c1; 
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

.header {
  display: inline-block;

}

.headshot {
  float:left;
  
  width: 30%;
}
.intro{
  width: 60%;
  float:right;
  text-align: left;
}
</style>
