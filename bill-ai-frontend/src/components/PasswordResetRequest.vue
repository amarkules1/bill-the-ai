<template>
    <div class="container">
      <div class="row">
        <div class="headshot col-md-3">
          <img alt="Vue logo" src="../assets/logo.png">
        </div>
        <div class="subscribe col-md-8 form-group" v-if="!isSubmitted">
          <h1>Reset Password</h1>
          <p>Enter the email associated with your account.</p>
          <br />
          <div class="emailBox">
            <input type="email" v-validate="'email'"  class="form-control form-control-lg flex-grow-1 emailInput" v-model="userEmail"
              placeholder="Email" />
            <button v-if="!savingEmail" class="btn btn-info ml-2" @click="submitEmail"
              :disabled="userEmail.length < 1">Submit</button>
            <div v-if="savingEmail" class="spinner-border" role="status">
              <span class="sr-only"></span>
            </div>
          </div>
        </div>
        <div class="subscribe col-md-8" v-if="isSubmitted">
          <h1>Success</h1>
          <p>If there is an account associated with the email you entered, you'll receive an email with a link to reset your password.
            Please use the link within 24 hours, or you'll need to request another password reset.
          </p>
        </div>
      </div>
    </div>
  </template>
    
  <script>
  import axios from 'axios';
  export default {
    name: 'PasswordResetRequest',
  
    data() {
      return {
        userEmail: '',
        isSubmitted: false,
        savingEmail: false
      };
    },
    methods: {
      async submitEmail() {
        this.savingEmail = true;
        this.loadingQuery = true; axios.post('/send-password-reset', { email: this.userEmail })
          .then(() => {
            this.isSubmitted = true;
            this.savingEmail = false;
          })
          .catch(() => {
            this.isSubmitted = true;
            this.savingEmail = false;
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
  
  .emailBox {
    width: 90%;
    display: inline-flex;
    margin: auto;
  }
  
  .emailInput {
    margin-right: 10px;
  }
  </style>