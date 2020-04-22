<template>
  <div class="app" :class="{'app--login': !loggedIn}">
    <navigation-bar :hidden="!loggedIn"></navigation-bar>
    <router-view class="app__view" @logged-in="login" @logged-out="logout"></router-view>
  </div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue';

export default {
  components: {
    NavigationBar,
  },
  data() {
    return {
      loggedIn: true,
    }
  },
  methods: {
    login() {
      this.loggedIn = true;
    },
    logout() {
      this.loggedIn = false;
    }
  }
}
</script>

<style>
.app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100vh;
  padding: 0 10vw;
  height: 100%;
  background-image: url("~@/assets/rectangle.png");
  background-repeat: no-repeat;
  background-size: cover;
}

.app--login {
  padding: 0 37vw;
}

.app--login .app__view {
  min-height: 35vh;
}

.app__view {
  margin-top: 30px;
  border-radius: 25px;
  background-color: #ffffff;
  min-height: 45vh;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 30px;
}

body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}
</style>
