<template>
  <div class="qaComponent"></div>
  <div class="container introComponent" v-if="!loadingSummary">
    <div class="row">
      <div class="headshot col-md-3">
        <img alt="Vue logo" src="../assets/logo.png">
      </div>
      <div class="intro col-md-8">
        <h1>Ask Bill a question about the {{billSummary.bill_title}}</h1>
        <p>{{ billSummary.summary }}</p>
        <p><a href={{billSummary.wiki_link}}>Wikipedia Link</a> &nbsp;&nbsp; <a href={{billSummary.full_text_link}}>Full Text</a></p>
      </div>
    </div>
  </div>
  <br />
  <div>
    <div class="form-group d-flex queryBox">
      <input type="text" class="form-control form-control-lg flex-grow-1 queryInput" v-model="userQuery"
        :placeholder="'Ask Bill a question about the '+ billSummary.bill_title" />
      <button v-if="!loadingQuery" class="btn btn-info ml-2" @click="submitQuery"
        :disabled="userQuery.length < 20">Submit</button>
      <div v-if="loadingQuery" class="spinner-border" role="status">
        <span class="sr-only"></span>
      </div>
    </div>
    <div v-if="loadingQuestions" class="spinner-border" role="status">
      <span class="sr-only"></span>
    </div>
    <div v-if="!loadingQuestions" class="qnaContainer">
      <div v-for="item in questionsAndAnswers" :key="item.question"
        :class="{ 'selected': item.highlighted, 'card': true, 'mb-3': true }">
        <div class="card-body">
          <p><strong>Question:</strong> {{ item.question }}</p>
          <p><strong>Answer:</strong> {{ item.answer }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRoute } from 'vue-router';

export default {
  name: 'QuestionsAndAnswers',

  data() {
    return {
      userQuery: '',
      queryResult: null,
      questionsAndAnswers: [],
      loadingQuery: false,
      loadingQuestions: true,
      loadingSummary: true,
      bill_id: '',
      billSummary: {}
    };
  },
  mounted() {
    let route = useRoute();
    this.bill_id = route.params.bill_id;
    this.fetchSummary()
    this.fetchQuestionsAndAnswers();
  },
  methods: {
    async fetchQuestionsAndAnswers() {
      const response = await fetch(`/${this.bill_id}-q-and-a`);
      this.questionsAndAnswers = await response.json();
      this.loadingQuestions = false;
    },
    async fetchSummary() {
      const response = await fetch(`/bill-summary?bill_id=${this.bill_id}`);
      this.billSummary = await response.json();
      this.loadingSummary = false;
    },
    async submitQuery() {
      this.loadingQuery = true;
      const response = await fetch(`/${this.bill_id}-query?query=${this.userQuery}`);
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
  width: 90%;
  display: inline-flex;
  margin-left: auto;
  margin-right: auto;
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

.queryInput {
  margin-right: 10px;
}

.qnaContainer {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}
</style>
