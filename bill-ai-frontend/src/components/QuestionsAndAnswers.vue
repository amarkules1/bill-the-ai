<template>
  <div class="qaComponent"></div>
  <div class="container introComponent" v-if="!loadingSummary">
    <div class="row">
      <div class="headshot col-md-3">
        <img alt="Vue logo" src="../assets/logo.png">
      </div>
      <div class="intro col-md-8">
        <h1>Ask Bill a question about the {{ billSummary.bill_title }}</h1>
        <p>{{ billSummary.summary }}</p>
        <p><a v-bind:href="billSummary.wiki_link">Wikipedia Link</a> &nbsp;&nbsp; <a v-bind:href="billSummary.full_text_link">Full
            Text</a></p>
      </div>
    </div>
  </div>
  <br />
  <div>
    <div class="form-group d-flex queryBox">
      <input type="text" class="form-control form-control-lg flex-grow-1 queryInput" v-model="userQuery"
        :placeholder="'Ask Bill a question about the ' + billSummary.bill_title" @focus="checkLogin" />
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
        <QuestionComponent :q="item" />
      </div>
    </div>
    <div v-if="showModal">
      <LoginPromptModal @close="showModal = false" />
    </div>
  </div>
</template>

<script>
import { useRoute } from 'vue-router';
import QuestionComponent from './QuestionComponent.vue';
import LoginPromptModal from './LoginPromptModal.vue'
import Account from './account';

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
      billSummary: {},
      showModal: false
    };
  },
  async mounted() {
    let route = useRoute();
    this.bill_id = route.params.bill_id;
    this.fetchSummary();
    this.fetchQuestionsAndAnswers();
    this.$root.$refs.HeaderComponent = this;
    this.account = this.$root.$refs.Account;
    if (!this.account) {
      this.account = new Account();
      this.$root.$refs.Account = this.account;
    }
    let val = await this.account.isLoggedIn();
    this.isLoggedIn = val;
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
      this.queryResult.highlighted = true;
      this.questionsAndAnswers.unshift(this.queryResult);
      this.userQuery = '';
      this.loadingQuery = false;
    },
    async checkLogin() {
      if (!this.isLoggedIn)
        this.showModal = true
    }
  },
  components: { QuestionComponent, LoginPromptModal }
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
