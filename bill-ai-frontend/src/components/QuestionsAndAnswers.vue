<template>
  <div class="qaComponent"></div>
  <IntroComponent/>
  <br/>
  <div>
    <div class="form-group d-flex queryBox">
      <input type="text" class="form-control form-control-lg flex-grow-1" v-model="userQuery"
        placeholder="Ask Bill a question about the Inflation Reduction Act" />
      <button v-if="!loadingQuery" class="btn btn-info ml-2" @click="submitQuery" :disabled="userQuery.length < 20">Submit</button>
      <div v-if="loadingQuery" class="spinner-border" role="status">
        <span class="sr-only"></span>
      </div>
    </div>
    <div v-if="loadingQuestions" class="spinner-border" role="status">
      <span class="sr-only"></span>
    </div>
    <div v-if="!loadingQuestions">
      <div v-for="item in questionsAndAnswers" :key="item.question" :class="{ 'selected': item.highlighted, 'card': true, 'mb-3': true}">
        <div class="card-body">
          <p><strong>Question:</strong> {{ item.question }}</p>
          <p><strong>Answer:</strong> {{ item.answer }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import IntroComponent from './IntroComponent.vue';

export default {
  name: 'QuestionsAndAnswers',
  components: {
    IntroComponent
  },

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
      this.queryResult.highlighted = true
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
.qaComponent {
  margin-top: 60px;
  margin-right: auto;
  margin-left: auto;
  width: 90%;
}
.selected {
  border: 5px solid #777;
    border-radius: 8px;
}
</style>
