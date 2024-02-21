<template>
  <div>
    <h1>Log in</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username">
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password">
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="error" style="color: red;">{{ error }}</p>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      error: ''
    };
  },
  methods: {
    login() {
      const formData = {
        username: this.username,
        password: this.password
      };

      fetch('http://127.0.0.1:8000/auth/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      })
      .then(response => {
        if (response.ok) {
          return response.json();
        } else if (response.status === 401) {
          throw new Error('Invalid username or password');
        } else {
          throw new Error('Error logging in');
        }
      })
      .then(data => {
        localStorage.setItem('token', data.token);
        this.$router.push('/home');
      })
      .catch(error => {
        this.error = error.message;
      });
    }
  }
};
</script>
