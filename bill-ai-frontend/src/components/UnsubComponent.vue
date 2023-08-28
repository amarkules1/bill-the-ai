<template>
    <div class="container">
        <div class="row">
            <div class="headshot col-md-3">
                <img alt="Vue logo" src="../assets/logo.png">
            </div>
            <div class="subscribe col-md-8 form-group" v-if="!isSuccess && !isError">
                <h2>If you would like to unsubscribe, enter your email below.</h2>
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
            <div class="subscribe col-md-8" v-if="isSuccess">
                <h1>Success</h1>
                <p>You've been unsubscribed from updates about Bill. You can sign back up <router-link
                        to="/signup">here</router-link>.</p>
            </div>
            <div class="subscribe col-md-8" v-if="isError">
                <h1>Error</h1>
                <p>There was an issue removing your email, please try again later or reach out to bill.the.ai.guy@gmail.com
                    for support.</p>
            </div>
        </div>
    </div>
</template>
    
<script>
import axios from 'axios';
export default {
    name: 'UnsubComponent',

    data() {
        return {
            userEmail: '',
            isSuccess: false,
            isError: false,
            savingEmail: false
        };
    },
    methods: {
        async submitEmail() {
            this.savingEmail = true;
            this.loadingQuery = true; axios.post('/unsubscribe', { email: this.userEmail })
                .then(() => {
                    this.isSuccess = true;
                    this.savingEmail = false;
                })
                .catch(() => {
                    this.isError = true;
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
}</style>