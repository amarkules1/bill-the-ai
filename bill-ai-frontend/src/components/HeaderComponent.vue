<template>
    <div id="headerComponent">
        <nav class="header">
            <div class="title">Bill the AI</div>
            <div class="nav-buttons">
                <router-link class="btn" active-class="active" to="/home">Home</router-link>
                <router-link class="btn" active-class="active" to="/signup">Sign Up</router-link>
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  background-color: #555;
}

.nav-buttons {
  display: flex;
}

.btn {
  text-decoration: none;
  color: #555;
  border: 1px solid white;
  padding: 10px;
  margin-right: 10px;
  background-color: white;
  transition: background-color 0.3s;
  font-weight: 400;
}

.btn.active {
  background-color: #555;
  font-weight: 400;
  color: white;
}

.btn:hover {
  background-color: grey;
}

.title {
  color: white;
  font-size: 20px;
}
</style>