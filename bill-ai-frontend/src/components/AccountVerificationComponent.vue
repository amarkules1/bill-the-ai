<template>
    <div class="container">
        <div class="row">
            <div class="headshot col-md-3">
                <img alt="Vue logo" src="../assets/logo.png">
            </div>
                <div v-if="verifyingAccount" class="spinner-border" role="status">
                    <span class="sr-only"></span>
                </div>
                <div class="subscribe col-md-8" v-if="isSuccess">
                    <h1>Success</h1>
                    <p>Your account has been verified!</p>
                </div>
                <div class="subscribe col-md-8" v-if="isError">
                    <h1>Error</h1>
                    <p>There was an issue verifying your account, please try again later.</p>
                </div>
        </div>
    </div>  
</template>
    
<script>
import axios from 'axios';
import { useRoute } from 'vue-router';

export default {
    name: 'AccountVerificationComponent',
    mounted() {
        let route = useRoute();
        let token = route.params.token;
        let email = route.params.email;
        axios.post('/verify-account', { token: token, email: email })
            .then(() => {
                this.isSuccess = true;
                this.verifyingAccount = false;
            })
            .catch(() => {
                this.isError = true;
                this.verifyingAccount = false;
            });
    },
  
    data() {
        return {
            userEmail: '',
            isSuccess: false,
            isError: false,
            verifyingAccount: true,
            errorMessage: ''
        };
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