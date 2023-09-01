<template>
    <div class="container">
        <div class="row">
            <div class="headshot col-md-3">
                <img alt="Vue logo" src="../assets/logo.png">
            </div>
                <div v-if="savingEmail" class="spinner-border" role="status">
                    <span class="sr-only"></span>
                </div>
                <div class="subscribe col-md-8" v-if="isSuccess">
                    <h1>Success</h1>
                    <p>Your email has been verified, we'll send you periodic updates about Bill the AI.
                        You can unsubscribe at any time <router-link to="/unsubscribe">here</router-link>.</p>
                </div>
                <div class="subscribe col-md-8" v-if="isError">
                    <h1>Error</h1>
                    <p>There was an issue verifying your email, please try again later.</p>
                </div>
        </div>
    </div>  
</template>
    
<script>
import axios from 'axios';
import { useRoute } from 'vue-router';

export default {
    name: 'EmailVerificationComponent',
    mounted() {
        let route = useRoute();
        let id = route.params.id;
        let email = route.params.email;
        axios.post('/verify-email', { id: id, email: email })
            .then(() => {
                this.isSuccess = true;
            })
            .catch(() => {
                this.isError = true;
            });
    },
  
    data() {
        return {
            userEmail: '',
            isSuccess: false,
            isError: false,
            savingEmail: false,
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