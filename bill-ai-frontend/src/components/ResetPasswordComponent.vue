<template>
    <div class="container">
        <div class="row">
            <div class="headshot col-md-3">
                <img alt="Vue logo" src="../assets/logo.png">
            </div>
            <div v-if="(!requestValidated) || resetInProgress" class="spinner-border" role="status">
                <span class="sr-only"></span>
            </div>
            <div v-if="!isValidRequest && requestValidated">
                <h1>Invalid Request</h1>
                <p>The password reset link you used is invalid. Please request a new password reset.</p>
            </div>
            <div v-if="isValidRequest && !resetInProgress" class="subscribe col-md-8">
                <div v-if="!resetSuccessful && !resetError">
                    <input type="password" class="form-control form-control-lg flex-grow-1 input" v-model="password"
                        placeholder="New Password" :class="{ invalid: !validatePassword() }" />
                    <p v-if="!validatePassword()">Password must be 8 characters or more.</p>
                    <button v-if="!savingAccount" class="btn btn-info ml-2" @click="submit"
                        :disabled="!validatePassword()">Submit</button>
                </div>
                <div v-if="resetSuccessful">
                    <h1>Success</h1>
                    <p>Your password has been updated! Please <router-link to="/login">Log In</router-link>.</p>
                </div>
                <div v-if="isError">
                    <h1>Error</h1>
                    <p>There was an issue updating your password. You can refresh the page and try again, or contact support at support@billtheai.com</p>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import axios from 'axios';
import { useRoute } from 'vue-router';
import crypto from 'crypto';

export default {
    name: 'ResetPasswordComponent',
    mounted() {
        let route = useRoute();
        this.resetToken = route.params.token;
        this.email = route.params.email;
        axios.post('/validate-password-reset', { token: this.resetToken, email: this.email })
            .then(() => {
                this.isValidRequest = true;
                this.requestValidated = true;
            })
            .catch(() => {
                this.isValidRequest = false;
                this.requestValidated = true;
            });
    },

    data() {
        return {
            userEmail: '',
            resetToken: '',
            isValidRequest: false,
            requestValidated: false,
            resetSuccessful: false,
            resetInProgress: false,
            password: '',
            resetError: false
        };
    },

    methods: {
        async submit() {
            this.resetInProgress = true;
            let passwordHash = crypto.createHash("md5");
            passwordHash.update(this.password);
            passwordHash = passwordHash.digest('hex');
            axios.post('/reset-password', { email: this.email, token: this.resetToken, password: passwordHash })
                .then(() => {
                    this.resetSuccessful = true;
                    this.resetInProgress = false;
                })
                .catch(() => {
                    this.resetError = true;
                    this.resetInProgress = false;
                });
        },

        validatePassword() {
            if (this.password.length > 7) {
                return true;
            }
            return false;
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