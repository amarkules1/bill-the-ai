<template>
    <div>
        <div v-if="isLoaded">
            <p>Username: {{ userName }}</p>
            <p>Email: {{ email }}</p>
        </div>
        <div v-if="!isLoaded" class="spinner-border" role="status">
            <span class="sr-only"></span>
        </div>
    </div>
</template>
<script>
import Account from './account';


export default {
    name: 'AccountComponent',
    data() {
        return {
            account: {},
            userName: '',
            email: '',
            isLoaded: '',
        };
    },

    async mounted() {
        this.account = this.$root.$refs.Account;
        if (!this.account) {
            this.account = new Account();
            this.$root.$refs.Account = this.account;
        }
        if (!await this.account.isLoggedIn()) {
            this.$router.push('/login');
        }
        this.userName = this.account.username;
        this.email = this.account.email;
        this.isLoaded = true;
    },
}
</script>