<template>
  <div class="container introComponent">
    <div class="row">
      <div class="headshot col-md-3">
        <img alt="Vue logo" src="../assets/logo.png">
      </div>
      <div class="intro col-md-8">
        <h1>Ask Bill questions about various bills!</h1>
        <p>Bill is the AI that reads the laws that congress passes and explains them to you.
          He's only read a few recent bills so far, but he's working on more.
          Select a bill from the menu, read through some of the questions, then ask Bill your own question.
          Here are some tips about how to ask Bill a good question:
        <ul>
          <li>Make your question specific for the best response, ask how the law effects a certain group of people, or a
            certain industry.</li>
          <li>Bill knows all the text of the bills, but doesn't always remember the name of the law. Ask
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
  name: 'IntroComponent',
  data() {
    return {
      showModal: false
    };
  }
}
</script>
<style>
.introComponent {
  display: inline-block;
}

.headshot {
  width: 30%;
}

.intro {
  text-align: left;
}
</style>