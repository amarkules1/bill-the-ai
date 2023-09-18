<template>
    <div class="container">
      <div class="row">
        <div class="headshot col-md-3">
          <img alt="Vue logo" src="../assets/logo.png">
        </div>
        <div class="subscribe col-md-8 form-group" v-if="!isSuccess && !isError">
          <h1>Give Feedback</h1>
          <p>Do you find Bill helpful? Something not working right? New feature request? You can submit it here.</p>
          <br />
          <div class="inputBox">
            <input type="email" v-validate="'email'"  class="form-control form-control-lg flex-grow-1 emailInput" v-model="userEmail"
              placeholder="Email (optional)" />
            <br/>
            <textarea v-model="feedback" autosize placeholder="Feedback" class="form-control form-control-lg flex-grow-1"></textarea>
            <br/>
            <button v-if="!savingFeedback" class="btn btn-info ml-2" @click="submitFeedback"
              :disabled="feedback.length < 1">Submit</button>
            <div v-if="savingFeedback" class="spinner-border" role="status">
              <span class="sr-only"></span>
            </div>
          </div>
        </div>
        <div class="subscribe col-md-8" v-if="isSuccess">
          <h1>Success</h1>
          <p>Thanks for your feedback!</p>
        </div>
        <div class="subscribe col-md-8" v-if="isError">
          <h1>Error</h1>
          <p>There was an issue saving your feedback, please try again later.</p>
        </div>
      </div>
    </div>
  </template>
    
  <script>
  import axios from 'axios';
  export default {
    name: 'FeedbackComponent',
  
    data() {
      return {
        userEmail: '',
        feedback: '',
        isSuccess: false,
        isError: false,
        savingFeedback: false
      };
    },
    methods: {
      async submitFeedback() {
        this.savingFeedback = true;
        this.loadingQuery = true; axios.post('/feedback', { email: this.userEmail, feedback: this.feedback })
          .then(() => {
            this.isSuccess = true;
            this.savingFeedback = false;
          })
          .catch(() => {
            this.isError = true;
            this.savingFeedback = false;
          });
      }
    }
  }
  </script>
  <style>
  .header {
    display: inline-block;
  }
  
  .headshot {
    width: 30%;
  }
  
  .intro {
    text-align: left;
  }
  
  .inputBox {
    width: 90%;
    margin: auto;
  }
  
  .emailInput {
    margin-right: 10px;
  }
  </style>