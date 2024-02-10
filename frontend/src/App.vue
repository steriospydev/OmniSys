<template>
  <nav class="dnav">
    <router-link to="/">Home</router-link> |    
    <router-link to="login/">Login</router-link> | 
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.dnav {
  padding: 30px;
}

.dnav a {
  font-weight: bold;
  color: #2c3e50;
}

.dnav a.router-link-exact-active {
  color: #42b983;
}
</style>
