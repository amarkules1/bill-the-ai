<template>
    <div class="container">
        <div class="row">
            <div class="headshot col-md-3">
                <img alt="Vue logo" src="../assets/logo.png">
            </div>
            <div class="subscribe col-md-8 form-group" v-if="!isSuccess && !isError">
                <h1>Create an Account</h1>
                <br />
                <div class="inputBox">
                    <input type="email" class="form-control form-control-lg flex-grow-1 input" :class="{ invalid: !validateEmail() }"
                        v-model="userEmail" placeholder="Email" />
                    <p v-if="!validateEmail()">Please provide your real email address. You will be sent a confirmation email.</p>
                    <input type="text" class="form-control form-control-lg flex-grow-1 input" v-model="userName" :class="{ invalid: !validateUsername() }"
                        placeholder="Username" />
                    <p v-if="!validateUsername()">Username must be 8 characters or more, it can contain letters and numbers.</p>
                    <input type="password" class="form-control form-control-lg flex-grow-1 input" v-model="password"
                        placeholder="Password"  :class="{ invalid: !validatePassword() }"/>
                    <p v-if="!validatePassword()">Password must be 8 characters or more.</p>
                    <button v-if="!savingAccount" class="btn btn-info ml-2" @click="submit"
                        :disabled="(!validateEmail()) || (!validatePassword()) || (!validateUsername())">Submit</button>
                    <div v-if="savingAccount" class="spinner-border" role="status">
                        <span class="sr-only"></span>
                    </div>
                </div>
            </div>
            <div class="subscribe col-md-8" v-if="isSuccess">
                <h1>Success</h1>
                <p>You should receive a verification email from support@billtheai.com.
                    Once you verify your email, your account will be activated.</p>
            </div>
            <div class="subscribe col-md-8" v-if="isError">
                <h1>Error</h1>
                <p>There was an issue saving your account details, please try again later.</p>
            </div>
        </div>
    </div>
</template>
    
<script>
import axios from 'axios';
export default {
    name: 'SignupComponent',

    data() {
        return {
            userEmail: '',
            userName: '',
            password: '',
            isSuccess: false,
            isError: false,
            savingAccount: false,
            emailRegExp: new RegExp(/^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,6}$/),
            userRegExp: new RegExp(/^[a-zA-Z0-9]+$/),
        };
    },
    methods: {
        async submit() {
            this.savingAccount = true;
            this.loadingQuery = true; axios.post('/create-account', { email: this.userEmail, user_name: this.userName, password: this.password })
                .then(() => {
                    this.isSuccess = true;
                    this.savingAccount = false;
                })
                .catch(() => {
                    this.isError = true;
                    this.savingAccount = false;
                });
        },

        validateEmail() {
            if (this.userEmail.length > 1 && this.emailRegExp.test(this.userEmail)) {
                return true;
            }
            return false;
        },

        validateUsername() {
            if (this.userName.length > 7 && this.userRegExp.test(this.userName)) {
                return true;
            }
            return false;
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

.inputBox {
    width: 90%;
    display: block;
    margin: auto;
}

.input {
    margin-right: 10px;
    margin-bottom: 20px;
}

.input.invalid {
    border-color: red;
}
</style>