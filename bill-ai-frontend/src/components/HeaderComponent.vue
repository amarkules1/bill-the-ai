<template>
  <div id="headerComponent">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark header">
        <div class="container">
            <a class="navbar-brand title" href="">Bill The AI</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                      <router-link class="nav-link" active-class="active" to="/home">Home</router-link>
                    </li>
                    <li class="nav-item">
                      <router-link class="nav-link" active-class="active" to="/signup">Get Updates</router-link>
                    </li>
                    <li class="nav-item">
                      <router-link class="nav-link" active-class="active" to="/feedback">Give Feedback</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
  </div>
</template>
  
<script>
export default {
    name: 'HeaderComponent'
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