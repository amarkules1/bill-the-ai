<template>
  <div id="headerComponent">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark header">
      <div class="container">
        <a class="navbar-brand title" href="">Bill The AI</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02"
          aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="nav-link" active-class="active" to="/home">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" active-class="active" to="/q_and_a/ira">Inflation Reduction Act</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" active-class="active" to="/q_and_a/fra">Fiscal Responsibility
                Act</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" active-class="active" to="/q_and_a/chips">CHIPS and Science Act</router-link>
            </li>
            <li class="nav-item" v-if="!isLoggedIn">
              <router-link class="nav-link" active-class="active" to="/signup">Sign Up</router-link>
            </li>
            <li class="nav-item" v-if="!isLoggedIn">
              <router-link class="nav-link" active-class="active" to="/login">Log In</router-link>
            </li>
            <li class="nav-item" v-if="isLoggedIn">
              <a class="nav-link" @click="logout">Log Out</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>
  
<script>
import Account from './account';

export default {
  name: 'HeaderComponent',

  data() {
    return {
      account: {},
      isLoggedIn: false
    };
  },

  async mounted() {
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
    async logout() {
      await this.account.logout();
      this.isLoggedIn = false;
      this.$router.push('/home');
    }
  }
}
</script>
<style>
.header {
  padding: 10px;
  width: 100%;
  background-color: #555 !important;
}

.title {
  font-size: 30px;
  font-weight: 500;
}
</style>