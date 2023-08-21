<template>
  <div>
    <div class="form-group d-flex queryBox">
      <input type="text" class="form-control form-control-lg flex-grow-1" v-model="userQuery"
        placeholder="Ask Bill a question about the Inflation Reduction Act" />
      <button v-if="!loadingQuery" class="btn btn-primary ml-2" @click="submitQuery" :disabled="userQuery.length < 20">Submit</button>
      <div v-if="loadingQuery" class="spinner-border" role="status">
        <span class="sr-only"></span>
      </div>
    </div>
    <div v-if="loadingQuestions" class="spinner-border" role="status">
      <span class="sr-only"></span>
    </div>
    <div v-if="!loadingQuestions">
      <div v-for="item in questionsAndAnswers" :key="item.question" class="card mb-3">
        <div class="card-body">
          <p><strong>Question:</strong> {{ item.question }}</p>
          <p><strong>Answer:</strong> {{ item.answer }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuestionsAndAnswers',

  data() {
    return {
      userQuery: '',
      queryResult: null,
      questionsAndAnswers: [],
      loadingQuery: false,
      loadingQuestions: true
    };
  },
  mounted() {
    this.fetchQuestionsAndAnswers();
  },
  methods: {
    async fetchQuestionsAndAnswers() {
      const response = await fetch('/ira-q-and-a');
      this.questionsAndAnswers = await response.json();
      this.loadingQuestions = false;
    },
    async submitQuery() {
      this.loadingQuery = true;
      const response = await fetch(`/ira-query?query=${this.userQuery}`);
      this.queryResult = await response.json();
      this.questionsAndAnswers.unshift(this.queryResult);
      this.userQuery = '';
      this.loadingQuery = false;
    }
  }
};
</script>

<style>
.queryBox {
  margin-bottom: 20px;
}
</style>
