<template>
  <div class="container header">
    <div class="row">
      <div class="headshot col-md-3">
        <img alt="Vue logo" src="../assets/logo.png">
      </div>
      <div class="intro col-md-9">
        <h1>Ask Bill a question about the Inflation Reduction Act</h1>
        <p>Bill is the AI that reads the laws that congress passes and explains them to you.
          He's only read the <a href="https://en.wikipedia.org/wiki/Inflation_Reduction_Act">Inflation Reduction Act</a>
          so far, but he's working on more.
          Read through some of the questions bellow, then ask Bill your own question.
          Here are some tips about how to ask Bill a good question:
        <ul>
          <li>Make your question specific for the best response, ask how the law effects a certain group of people, or a
            certain industry.</li>
          <li>Bill knows all the text of the Inflation Reduction Act, but doesn't always remember the name of the law. Ask
            questions in terms of "the bill" instead.</li>
          <li>Read existing questions before asking your own, Bill sends his developer an invoice every month for all the
            questions he answers.</li>
        </ul>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IntroComponent'
}
</script>
<style>
.header {
  display: inline-block;
}
.headshot {
  width: 30%;
}
.intro{
  text-align: left;
}
</style>