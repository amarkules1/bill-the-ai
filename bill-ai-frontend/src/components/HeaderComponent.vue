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
  float: right;
  padding-top: 10px
}

.btn {
  text-decoration: none;
  color: white;
  border: 1px solid #555;
  padding: 10px;
  margin-right: 10px;
  background-color: #555;
  transition: background-color 0.3s;
  font-weight: 400;
}

.btn.active {
  background-color: white;
  font-weight: 400;
  color: #555;
}

.btn:hover {
  background-color: grey;
}

.title {
  color: white;
  font-size: 44px;
  font-weight: 600;
  float:left;
}
</style>