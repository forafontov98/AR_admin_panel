<template>
  <div class="login-view">
    <h2>Авторизация</h2>
    <form class="login-view__form">
        <input
            type="text"
            placeholder="Логин"
            class="login-view__input"
            v-model="username"
        >
        <input 
            type="password"
            placeholder="Пароль"
            class="login-view__input"
            v-model="password"
        >
    </form>
    <base-button class="login-view__button" @click="login">Войти</base-button>
  </div>
</template>

<script>
import BaseButton from "@/components/BaseButton";
import API from "@/api";

export default {
    components: {BaseButton},
    mounted() {
        this.$emit('logged-out');
    },
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        async login() {
            await API.login(this.username, this.password);

            if (localStorage.getItem('token')) {
                this.$emit('logged-in');
                this.$router.push('objects');
            }

        }
    }
}
</script>

<style>
.login-view {
    align-items: center;
    justify-content: space-between;
}

.login-view__input {
    width: 90%;
    height: 35px;
}

.login-view__input + .login-view__input {
    margin-top: 15px;
}

.login-view__button {
    width: 100%;
}
</style>