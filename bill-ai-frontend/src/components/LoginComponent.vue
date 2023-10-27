<template>
    <div class="container">
        <div class="row">
            <div class="headshot col-md-3">
                <img alt="Vue logo" src="../assets/logo.png">
            </div>
            <div class="subscribe col-md-8 form-group" v-if="!isSuccess">
                <h1>Log In</h1>
                <div v-if="isError">
                    <h3>Error</h3>
                    <p>Username or password is incorrect. Please check your credentials.</p>
                </div>
                <br />
                <div class="inputBox">
                    <input type="text" class="form-control form-control-lg flex-grow-1 input" v-model="userNameOrEmail"
                        :class="{ invalid: !validateUserNameOrEmail() }" placeholder="Username or Email" />
                    <input type="password" class="form-control form-control-lg flex-grow-1 input" v-model="password"
                        placeholder="Password" :class="{ invalid: !validatePassword() }" />
                    <button v-if="!loggingIn" class="btn btn-info ml-2" @click="submit"
                        :disabled="(!validateUserNameOrEmail()) || (!validatePassword())">Log In</button>
                    <div v-if="loggingIn" class="spinner-border" role="status">
                        <span class="sr-only"></span>
                    </div>
                </div>
            </div>
            <div class="subscribe col-md-8" v-if="isSuccess">
                <h1>Success</h1>
                <p>Redirecting.</p>
            </div>
        </div>
    </div>
</template>
    
<script>
export default {
    name: 'LoginComponent',

    data() {
        return {
            userNameOrEmail: '',
            password: '',
            isSuccess: false,
            isError: false,
            loggingIn: false,
            account: this.$root.$refs.Account,
        };
    },
    methods: {
        async submit() {
            this.loggingIn = true;
            this.isError = false;
            this.loadingQuery = true; 
            let success = await this.account.login(this.userNameOrEmail, this.password);
            if (success) {
                this.isSuccess = true;
                this.loggingIn = false;
                this.$root.$refs.HeaderComponent.isLoggedIn = true;
                this.$router.push('/')
            } else {
                this.isError = true;
                this.userNameOrEmail = '';
                this.password = '';
                this.loggingIn = false;
            }
        },

        validatePassword() {
            if (this.password.length > 7) {
                return true;
            }
            return false;
        },

        validateUserNameOrEmail() {
            if (this.userNameOrEmail.length > 7) {
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